#!/usr/bin/env python3
"""Build the word-locked Eleven v4 Director's Cut edition of Meridian."""

from __future__ import annotations

import argparse
import hashlib
import html
import json
import re
import subprocess
import zipfile
from datetime import datetime, timezone
from pathlib import Path


BOOK_ID = "book-02-meridian"
TITLE = "Meridian"
AUTHOR = "Monroe Jackson"
EDITION = "Eleven v4 Director's Cut"
CHAPTER_COUNT = 48

MOVEMENT_TAGS = {
    1: "[Quiet, precise narration; restrained institutional pressure]",
    2: "[Focused, grounded narration; keep physical instruction clear]",
    3: "[Measured, compassionate narration; let the human cost land]",
    4: "[Steady travel narration; watchful tension beneath the words]",
    5: "[Taut, spatially clear narration; build controlled urgency]",
    6: "[Warm, intimate narration; keep emotion earned and restrained]",
}

DENSE_CHAPTERS = {21, 29, 33, 40}
CLIMAX_CHAPTERS = set(range(34, 41))
RETURN_HOLD_CHAPTERS = {44, 45}

SCENE_RULES = [
    (
        re.compile(r"\b(ward|doctor|blood|medicine|frame|pins?|fit|treatment|clinic|patient|wound)\b", re.I),
        "[Measured, compassionate narration; keep the clinical detail clear]",
    ),
    (
        re.compile(r"\b(form|card|office|review|ledger|account|contract|director|station|registry|clerk)\b", re.I),
        "[Dry, precise narration; quiet institutional pressure]",
    ),
    (
        re.compile(r"\b(yard|lane|drill|ash|hook|guard|edge|warding|training|practice)\b", re.I),
        "[Focused, grounded narration; make the physical instruction legible]",
    ),
    (
        re.compile(r"\b(mother|brother|tonk|hand|slept|sleep|laugh|smile|home|family)\b", re.I),
        "[Warm, intimate narration; hold the feeling lightly]",
    ),
    (
        re.compile(r"\b(road|cart|horse|mile|hill|camp|travel|track|ridge)\b", re.I),
        "[Steady, watchful narration; let distance and reserves register]",
    ),
    (
        re.compile(r"\b(ran|struck|hit|shouted|blade|husk|spawn|fell|broke|attack|fight|killed)\b", re.I),
        "[Taut, spatially clear narration; controlled urgency]",
    ),
]


def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def sha256_file(path: Path) -> str:
    return sha256_bytes(path.read_bytes())


def git_value(root: Path, *args: str) -> str:
    return subprocess.check_output(["git", *args], cwd=root, text=True).strip()


def clean_spoken_markdown(text: str) -> str:
    """Remove presentation-only Markdown while preserving spoken words and punctuation."""
    text = re.sub(r"(?m)^#{1,6}\s+", "", text)
    text = re.sub(r"(?<!\\)[*_`]", "", text)
    text = text.replace(r"\*", "*").replace(r"\_", "_").replace(r"\`", "`")
    return text


def spoken_tokens(text: str) -> list[str]:
    return re.findall(r"[\w’'-]+", text.casefold(), flags=re.UNICODE)


def parse_chapter(source: str) -> tuple[str, list[str]]:
    lines = source.replace("\r\n", "\n").splitlines()
    if not lines or not lines[0].startswith("# "):
        raise ValueError("Chapter is missing its level-one title")
    title = clean_spoken_markdown(lines[0][2:].strip())
    body = "\n".join(lines[1:]).strip()
    scenes = [clean_spoken_markdown(part.strip()) for part in re.split(r"(?m)^---\s*$", body)]
    scenes = [scene for scene in scenes if scene]
    if not scenes:
        raise ValueError(f"{title} has no prose")
    return title, scenes


def chapter_opening_tag(number: int) -> str:
    if number in DENSE_CHAPTERS:
        return "[Measured, lucid narration; give every name, number, and ledger turn room to land]"
    if number in RETURN_HOLD_CHAPTERS:
        return "[Urgent but grounded narration; keep movement and consequence sharply clear]"
    if number in CLIMAX_CHAPTERS:
        return "[Taut, spatially clear narration; build urgency without rushing]"
    movement = ((number - 1) // 8) + 1
    return MOVEMENT_TAGS[movement]


def scene_tag(scene: str, number: int, scene_index: int, scene_count: int) -> str:
    sample = " ".join(scene.split())[:900]
    for pattern, tag in SCENE_RULES:
        if pattern.search(sample):
            return tag
    if scene_index == scene_count - 1:
        if number >= 41:
            return "[Quietly reflective narration; let the realization settle]"
        return "[Measured narration; allow the scene to resolve before moving on]"
    movement = ((number - 1) // 8) + 1
    return MOVEMENT_TAGS[movement]


def paragraphize(scene: str) -> list[str]:
    return [part.strip() for part in re.split(r"\n\s*\n", scene) if part.strip()]


def build_directed_chapter(number: int, title: str, scenes: list[str]) -> tuple[str, list[dict[str, str]]]:
    blocks: list[str] = [title, "", chapter_opening_tag(number), ""]
    epub_blocks: list[dict[str, str]] = [
        {"type": "direction", "text": chapter_opening_tag(number)}
    ]
    for index, scene in enumerate(scenes):
        if index:
            tag = scene_tag(scene, number, index, len(scenes))
            blocks.extend([tag, ""])
            epub_blocks.append({"type": "direction", "text": tag})
        paragraphs = paragraphize(scene)
        for paragraph in paragraphs:
            blocks.extend([paragraph, ""])
            epub_blocks.append({"type": "prose", "text": paragraph})
    return "\n".join(blocks).rstrip() + "\n", epub_blocks


def xhtml_document(title: str, blocks: list[dict[str, str]], css_href: str = "../styles/book.css") -> str:
    rendered = []
    for block in blocks:
        cls = "direction" if block["type"] == "direction" else "prose"
        rendered.append(f'      <p class="{cls}">{html.escape(block["text"])}</p>')
    body = "\n".join(rendered)
    return f'''<?xml version="1.0" encoding="utf-8"?>
<!DOCTYPE html>
<html xmlns="http://www.w3.org/1999/xhtml" lang="en" xml:lang="en">
  <head>
    <meta charset="utf-8" />
    <title>{html.escape(title)}</title>
    <link rel="stylesheet" type="text/css" href="{css_href}" />
  </head>
  <body>
    <section class="chapter">
      <h1>{html.escape(title)}</h1>
{body}
    </section>
  </body>
</html>
'''


def make_epub(path: Path, chapters: list[dict], cover: Path | None) -> None:
    identifier = "urn:uuid:meridian-eleven-v4-directors-cut"
    nav_items = "\n".join(
        f'          <li><a href="text/chapter-{chapter["number"]:02d}.xhtml">{html.escape(chapter["title"])}</a></li>'
        for chapter in chapters
    )
    manifest_items = [
        '<item id="nav" href="nav.xhtml" media-type="application/xhtml+xml" properties="nav"/>',
        '<item id="css" href="styles/book.css" media-type="text/css"/>',
    ]
    spine_items = []
    if cover:
        manifest_items.append('<item id="cover" href="images/cover.jpg" media-type="image/jpeg" properties="cover-image"/>')
    for chapter in chapters:
        number = chapter["number"]
        manifest_items.append(
            f'<item id="chapter-{number:02d}" href="text/chapter-{number:02d}.xhtml" media-type="application/xhtml+xml"/>'
        )
        spine_items.append(f'<itemref idref="chapter-{number:02d}"/>')
    manifest_xml = "\n    ".join(manifest_items)
    spine_xml = "\n    ".join(spine_items)
    modified = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    opf = f'''<?xml version="1.0" encoding="utf-8"?>
<package xmlns="http://www.idpf.org/2007/opf" version="3.0" unique-identifier="book-id">
  <metadata xmlns:dc="http://purl.org/dc/elements/1.1/">
    <dc:identifier id="book-id">{identifier}</dc:identifier>
    <dc:title>{TITLE} — {EDITION}</dc:title>
    <dc:creator>{AUTHOR}</dc:creator>
    <dc:language>en</dc:language>
    <meta property="dcterms:modified">{modified}</meta>
  </metadata>
  <manifest>
    {manifest_xml}
  </manifest>
  <spine>
    {spine_xml}
  </spine>
</package>
'''
    nav = f'''<?xml version="1.0" encoding="utf-8"?>
<!DOCTYPE html>
<html xmlns="http://www.w3.org/1999/xhtml" xmlns:epub="http://www.idpf.org/2007/ops" lang="en">
  <head><meta charset="utf-8"/><title>Contents</title></head>
  <body><nav epub:type="toc"><h1>Contents</h1><ol>
{nav_items}
  </ol></nav></body>
</html>
'''
    container = '''<?xml version="1.0" encoding="UTF-8"?>
<container version="1.0" xmlns="urn:oasis:names:tc:opendocument:xmlns:container">
  <rootfiles><rootfile full-path="EPUB/content.opf" media-type="application/oebps-package+xml"/></rootfiles>
</container>
'''
    css = '''body { font-family: serif; line-height: 1.5; margin: 5%; }
h1 { page-break-before: always; text-align: center; margin: 2em 0; }
p { margin: 0 0 0.9em; }
.direction { font-family: sans-serif; font-style: italic; color: #555; margin: 1.5em 0 0.8em; }
'''
    with zipfile.ZipFile(path, "w") as archive:
        archive.writestr("mimetype", "application/epub+zip", compress_type=zipfile.ZIP_STORED)
        archive.writestr("META-INF/container.xml", container)
        archive.writestr("EPUB/content.opf", opf)
        archive.writestr("EPUB/nav.xhtml", nav)
        archive.writestr("EPUB/styles/book.css", css)
        if cover:
            archive.writestr("EPUB/images/cover.jpg", cover.read_bytes())
        for chapter in chapters:
            archive.writestr(
                f'EPUB/text/chapter-{chapter["number"]:02d}.xhtml',
                xhtml_document(chapter["title"], chapter["blocks"]),
            )


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--repo", type=Path, default=Path(__file__).resolve().parents[1])
    parser.add_argument("--cover", type=Path)
    args = parser.parse_args()
    repo = args.repo.resolve()
    manuscript = repo / "books" / BOOK_ID / "manuscript"
    output = repo / "books" / BOOK_ID / "editions" / "eleven-v4-directors-cut"
    chapter_output = output / "chapters"
    chapter_output.mkdir(parents=True, exist_ok=True)

    chapter_records = []
    full_text_parts = [
        f"{TITLE} — {EDITION}",
        AUTHOR,
        "",
        "Prepared for ElevenLabs Audio Editor / Studio long-form upload.",
        "Model: Eleven v4 (eleven_v4). Inline audio tags; no SSML.",
        "",
    ]
    total_spoken_words = 0
    total_tags = 0

    for number in range(1, CHAPTER_COUNT + 1):
        source_path = manuscript / f"chapter-{number:02d}.md"
        source_bytes = source_path.read_bytes()
        source = source_bytes.decode("utf-8")
        title, scenes = parse_chapter(source)
        directed, blocks = build_directed_chapter(number, title, scenes)

        canonical_spoken = "\n\n".join(scenes)
        directed_without_title_or_tags = "\n".join(
            line for index, line in enumerate(directed.splitlines())
            if index > 0 and not re.fullmatch(r"\[[^\n]+\]", line.strip())
        )
        canonical_tokens = spoken_tokens(canonical_spoken)
        directed_tokens = spoken_tokens(directed_without_title_or_tags)
        if canonical_tokens != directed_tokens:
            raise RuntimeError(f"Word lock failed for {source_path.name}")
        if re.search(r"<(?:speak|break)\b", directed, flags=re.I):
            raise RuntimeError(f"SSML found in {source_path.name}")

        chapter_path = chapter_output / f"chapter-{number:02d}.txt"
        chapter_path.write_text(directed, encoding="utf-8")
        spoken_word_count = len(canonical_tokens)
        tag_count = sum(1 for block in blocks if block["type"] == "direction")
        total_spoken_words += spoken_word_count
        total_tags += tag_count
        full_text_parts.extend([directed.rstrip(), ""])
        chapter_records.append(
            {
                "number": number,
                "title": title,
                "source": str(source_path.relative_to(repo)),
                "source_sha256": sha256_bytes(source_bytes),
                "directed_file": str(chapter_path.relative_to(repo)),
                "directed_sha256": sha256_file(chapter_path),
                "spoken_word_count": spoken_word_count,
                "scene_count": len(scenes),
                "direction_tag_count": tag_count,
                "word_lock": "verified",
                "blocks": blocks,
            }
        )

    full_text_path = output / "Meridian-Eleven-v4-Directors-Cut.txt"
    full_text_path.write_text("\n".join(full_text_parts).rstrip() + "\n", encoding="utf-8")
    epub_path = output / "Meridian-Eleven-v4-Directors-Cut.epub"
    cover = args.cover.resolve() if args.cover else None
    if cover and not cover.is_file():
        raise FileNotFoundError(cover)
    make_epub(epub_path, chapter_records, cover)

    manifest_chapters = [{key: value for key, value in record.items() if key != "blocks"} for record in chapter_records]
    manifest = {
        "schema_version": 1,
        "book_id": BOOK_ID,
        "title": TITLE,
        "author": AUTHOR,
        "edition": EDITION,
        "target_model": "eleven_v4",
        "format": "full-book long-form upload",
        "canonical_commit": git_value(repo, "rev-parse", "HEAD"),
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "chapter_count": CHAPTER_COUNT,
        "spoken_word_count": total_spoken_words,
        "direction_tag_count": total_tags,
        "word_lock": "verified for all chapters",
        "ssml": False,
        "outputs": {
            "epub": {"file": epub_path.name, "sha256": sha256_file(epub_path), "bytes": epub_path.stat().st_size},
            "plain_text": {"file": full_text_path.name, "sha256": sha256_file(full_text_path), "bytes": full_text_path.stat().st_size},
        },
        "chapters": manifest_chapters,
    }
    (output / "manifest.json").write_text(json.dumps(manifest, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({
        "output": str(output),
        "chapters": CHAPTER_COUNT,
        "spoken_words": total_spoken_words,
        "direction_tags": total_tags,
        "epub_sha256": manifest["outputs"]["epub"]["sha256"],
        "word_lock": manifest["word_lock"],
    }, indent=2))


if __name__ == "__main__":
    main()
