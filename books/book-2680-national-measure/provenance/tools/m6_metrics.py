#!/usr/bin/env python3
"""Movement Six numerical pass (copy of m5_metrics.py, same definitions; only chapter range, output labels and POV map changed). Pure stdlib. Usage: python3 -I m6_metrics.py <manuscript_dir>"""
import re, sys, statistics as st, json, collections, os

MD = sys.argv[1]
CHS = list(range(41, 49))
FILES = [os.path.join(MD, f"chapter-{i:02d}.md") for i in CHS]

# POV segments: (chapter, 0-based section index) -> lens. Sections split on '---' lines; section 0 includes the heading.
POV = {(42, 1): "Anwen", (45, 0): "Mara", (45, 1): "Kellan", (45, 3): "Mara", (45, 5): "Kellan",
       (46, 6): "Orla", (48, 2): "Rhea"}
# 47/2 ("Orla found her") and 48/4 ("Mara signed it") are narrated from Kiva's side; 47/8 (the Tanyard) is Kiva's (see report)

ABBR = re.compile(r"\b(Mrs|Mr|Dr|St|Mt)\.")
INIT = re.compile(r"\b([A-Z])\.(?=\s*[A-Z])")  # K. Rowan, J.H., M.R.

def clean(t):
    t = t.replace("—", " — ")
    t = re.sub(r"[*_]", "", t)
    return t

def sentences(par):
    p = ABBR.sub(lambda m: m.group(1) + "<DOT>", par)
    p = INIT.sub(lambda m: m.group(1) + "<DOT>", p)
    parts = re.split(r"(?<=[.!?])[\"”’')]*\s+(?=[\"“‘(]?[A-Z0-9])", p)
    out = []
    for s in parts:
        s = s.replace("<DOT>", ".").strip()
        if words(s):
            out.append(s)
    return out

WORD = re.compile(r"[A-Za-z0-9]+(?:['’\-][A-Za-z0-9]+)*")
def words(s):
    return WORD.findall(s)

def syllables(w):
    w = w.lower()
    if w.isdigit():
        return max(1, len(w))  # digits rare; crude
    w = re.sub(r"[^a-z]", "", w)
    if not w:
        return 0
    if len(w) <= 3:
        return 1
    w2 = re.sub(r"(?:[^laeiouy]es|ed|[^laeiouy]e)$", "", w)
    w2 = re.sub(r"^y", "", w2)
    n = len(re.findall(r"[aeiouy]{1,2}", w2))
    return max(1, n)

chapters = []
for ci, path in zip(CHS, FILES):
    raw = open(path, encoding="utf-8").read()
    secs = re.split(r"\n\s*---\s*\n", raw)
    chapters.append(secs)

all_sents, all_pars, sec_rows = [], [], []
corpus_words = []
pov_words = collections.Counter()
for ci, secs in zip(CHS, chapters):
    for si, sec in enumerate(secs):
        lens = POV.get((ci, si), "Kiva")
        pars = [p.strip() for p in re.split(r"\n\s*\n", sec) if p.strip()]
        sec_w = 0
        for p in pars:
            if p.startswith("#"):
                continue
            c = clean(p)
            w = words(c)
            all_pars.append(len(w))
            sec_w += len(w)
            corpus_words.extend(w)
            for s in sentences(c):
                all_sents.append((ci, si, len(words(s)), s))
        pov_words[lens] += sec_w
        sec_rows.append((ci, si, lens, sec_w))

N = len(corpus_words)
sl = [x[2] for x in all_sents]
res = {}
res["words_body"] = N
res["sentences"] = len(sl)
res["sent_mean"] = round(st.mean(sl), 2)
res["sent_median"] = st.median(sl)
res["sent_pstdev"] = round(st.pstdev(sl), 2)
res["share_le5"] = round(100 * sum(1 for x in sl if x <= 5) / len(sl), 1)
res["share_ge40"] = round(100 * sum(1 for x in sl if x >= 40) / len(sl), 1)
res["max_sentence"] = max(sl)
res["paragraphs"] = len(all_pars)
res["par_mean"] = round(st.mean(all_pars), 1)
res["par_median"] = st.median(all_pars)
res["par_share_over_60"] = round(100 * sum(1 for x in all_pars if x > 60) / len(all_pars), 1)
res["sections"] = len(sec_rows)
res["sec_mean"] = round(N / len(sec_rows))
res["breaks_per_10k_incl_chapter_starts"] = round(len(sec_rows) / N * 10000, 2)
res["breaks_per_10k_internal_only"] = round((len(sec_rows) - 8) / N * 10000, 2)
syl = sum(syllables(w) for w in corpus_words)
wps = N / len(sl)
spw = syl / N
res["flesch_reading_ease"] = round(206.835 - 1.015 * wps - 84.6 * spw, 1)
res["fk_grade"] = round(0.39 * wps + 11.8 * spw - 15.59, 1)
res["syll_per_word"] = round(spw, 3)

# per chapter sentence stats
perch = {}
for ci in CHS:
    s = [x[2] for x in all_sents if x[0] == ci]
    cw = sum(r[3] for r in sec_rows if r[0] == ci)
    perch[ci] = dict(words=cw, sents=len(s), mean=round(st.mean(s), 1), median=st.median(s),
                     le5=round(100 * sum(1 for x in s if x <= 5) / len(s), 1),
                     ge40=round(100 * sum(1 for x in s if x >= 40) / len(s), 1),
                     sections=sum(1 for r in sec_rows if r[0] == ci))
res["per_chapter"] = perch
res["pov_words"] = dict(pov_words)
res["pov_pct"] = {k: round(100 * v / N, 1) for k, v in pov_words.items()}
res["sections_rows"] = sec_rows

text = " ".join(clean(open(p, encoding="utf-8").read()) for p in FILES)
tl = text.lower()

def per10k(n): return round(n / N * 10000, 1)

# Progression lexicon (project-specific; case-sensitive where the stat name collides with ordinary English)
PROG_CS = [r"\bDraw\b", r"\bHold\b", r"\bEdge\b", r"\bStance\b", r"\bWard\b", r"\bRank\b", r"\bFlame\b", r"\bFire\b",
           r"\bTorch\b", r"\bBlaze\b", r"\bGlory\b", r"\bKindled\b", r"\bEmber\b", r"\bHandful\b", r"\bFlask\b", r"\bBarrel\b", r"\bWell\b(?= class)"]
PROG_CI = [r"\brank\b", r"\branks\b", r"\bdoors?\b", r"\bcrossings?\b", r"\bcrossed\b", r"\bstack(s|ed)?\b", r"\bcertif\w*", r"\bclassif\w*",
           r"\bunclassified\b", r"\blicen[cs]e[sd]?\b", r"\bsecond step\b", r"\bfirst step\b", r"\bthimble\b", r"\bre-reading\b",
           r"\bsanctioned mast\b", r"\bcliff\b", r"\bseated\b", r"\bnational license roll\b", r"\bcolumn for\b"]
prog_hits = collections.Counter()
for pat in PROG_CS:
    prog_hits[pat] = len(re.findall(pat, text))
for pat in PROG_CI:
    # avoid double count of 'rank' already counted case-sensitive 'Rank'
    prog_hits[pat] = len(re.findall(pat, text if pat == r"\brank\b" else tl))
# 'Rank' CS and 'rank' CS are disjoint because CI pattern above for rank uses original case text (lowercase only)
prog_total = sum(prog_hits.values())
res["prog_hits"] = {k: v for k, v in prog_hits.items() if v}
res["prog_total"] = prog_total
res["prog_per10k"] = per10k(prog_total)
# by movement thirds (equal word count)
third = N // 3
idx_words = WORD.findall(text)
bounds = [0, third, 2 * third, len(idx_words)]
def prog_in(span_words):
    t = " ".join(span_words)
    n = sum(len(re.findall(p, t)) for p in PROG_CS)
    n += sum(len(re.findall(p, t if p == r"\brank\b" else t.lower())) for p in PROG_CI)
    return n
res["prog_by_movement_third"] = [prog_in(idx_words[bounds[i]:bounds[i + 1]]) for i in range(3)]
# broad tier: ash economy
ECON = [r"\bdrams?\b", r"\bash\b", r"\bheld\b(?=:)", r"\bwarrant\b", r"\bhundredths\b", r"\btenths\b"]
econ = {p: len(re.findall(p, tl)) for p in ECON}
res["econ_hits"] = econ
res["econ_per10k"] = per10k(sum(econ.values()))

# -ly words
ly = re.findall(r"\b[a-z]+ly\b", tl)
LY_EXCL = {"only", "early", "family", "likely", "ugly", "holy", "july", "reply", "apply", "supply", "fly", "belly", "jelly",
           "rally", "ally", "lily", "silly", "bully", "folly", "hilly", "curly", "oily", "lonely", "lovely", "friendly", "elderly",
           "orderly", "kindly_adj", "daily", "weekly", "monthly", "yearly", "nightly", "costly", "deadly", "lively", "comely",
           "unlikely", "wily", "jolly", "woolly", "assembly", "anomaly", "italy", "sly", "ply", "dolly", "gully", "sully", "tally",
           "rely", "imply", "comply", "multiply", "underbelly", "manly", "womanly", "homely", "surly", "burly", "chilly", "grisly",
           "measly", "steely", "princely", "stately", "unruly", "beastly", "ghostly", "leisurely", "cowardly", "scholarly",
           "kelly", "ely", "billy", "bully", "fully_never"}
ly_raw = len(ly)
ly_f = [w for w in ly if w not in LY_EXCL]
res["ly_raw_per10k"] = per10k(ly_raw)
res["ly_filtered_per10k"] = per10k(len(ly_f))
res["ly_top"] = collections.Counter(ly_f).most_common(15)

REPORT = r"\b(said|says|asked|replied|answered|shouted|whispered|muttered|murmured|added|cried|called|told)\b"
rep = re.findall(REPORT, tl)
res["reporting_per10k"] = per10k(len(rep))
res["said_per10k"] = per10k(tl.split().count("said") + len(re.findall(r"\bsaid\b", tl)) - tl.split().count("said"))
res["reporting_top"] = collections.Counter(rep).most_common(10)

COMBAT = r"\b(blade|blades|cut|cuts|cutting|strike|struck|hit|hits|kill|kills|killed|fight|fought|fighting|block|blocked|dodge|dodged|attack|attacked|lunge|swing|swung|slash|wound|wounds|hurt)\b"
cb = re.findall(COMBAT, tl)
res["combat_per10k"] = per10k(len(cb))
res["combat_top"] = collections.Counter(cb).most_common(12)

FILL = ["that", "just", "almost", "felt", "seemed", "since", "rather", "quite", "one", "a good deal"]
res["fillers_per10k"] = {f: per10k(len(re.findall(r"\b" + f + r"\b", tl))) for f in FILL}

TICS = {"I'd like it known": r"i'd like it known", "I want it said": r"i want it said", "That adds": r"that adds",
        "nearly smiled": r"nearly smiled", "scratched his jaw": r"scratched his jaw", "went pink": r"went pink",
        "went scarlet/red": r"went (scarlet|red)", "ears (went|had gone) white": r"ears (went|had gone) white",
        "a good deal": r"a good deal", "four-and-twenty style numerals": r"\b(\w+)-and-(twenty|thirty|forty|fifty)\b",
        "as one ...s (generic 'one')": r"\bas one \w+s\b", "with care": r"with care",
        "for some time": r"for some time", "said nothing": r"said nothing", "I'd sooner": r"i'd sooner"}
res["tics"] = {k: len(re.findall(v, tl)) for k, v in TICS.items()}

# 3-grams
toks = [w.lower() for w in idx_words]
tg = collections.Counter(zip(toks, toks[1:], toks[2:]))
res["top_trigrams_per10k"] = [(" ".join(k), v, per10k(v)) for k, v in tg.most_common(15)]
for ph in [("out", "of", "the"), ("one", "of", "the"), ("for", "a", "moment")]:
    res.setdefault("ref_trigrams", {})[" ".join(ph)] = per10k(tg[ph])

# development proxy (regex): Kiva/she within 120 chars of marker
MARK = r"(realized|realised|decided|for the first time|swore|no longer|found that|understood|made herself|saw that|knew that|had not known|had thought)"
prox = 0
for m in re.finditer(MARK, text):
    win = text[max(0, m.start() - 120): m.end() + 120]
    if re.search(r"\b(Kiva|she|She|her)\b", win):
        prox += 1
res["dev_proxy_markers_total"] = len(re.findall(MARK, text))
res["dev_proxy_kiva_window"] = prox
res["dev_proxy_per10k"] = per10k(prox)

# longest sentences
res["longest"] = [(c, s, n, t[:160]) for c, s, n, t in sorted(all_sents, key=lambda x: -x[2])[:6]]
# month names
res["month_names"] = re.findall(r"\b(January|February|March|April|June|July|August|September|October|November|December)\b", text)
res["reserved_terms"] = {t: len(re.findall(t, text)) for t in ["Unroofed", "Breach", "handed crossing"]}


# ---- Movement Two additions, unchanged (definitions as described in the M1 review's section 7 prose) ----
DOORLIT = r"\b(by the|open|green|house|through the|at the|to the|oven|shed|colleague's|laundry|side|every|front|kitchen|cage|mill|back) doors?\b"
res["literal_door_phrases"] = len(re.findall(DOORLIT, tl))
res["door_hits_total"] = len(re.findall(r"\bdoors?\b", tl))
# narration vs dialogue split: quoted spans removed
def stats(lst):
    return dict(n=len(lst), mean=round(st.mean(lst),1), median=st.median(lst), pstdev=round(st.pstdev(lst),1),
                le5=round(100*sum(1 for x in lst if x<=5)/len(lst),1), ge40=round(100*sum(1 for x in lst if x>=40)/len(lst),1))
narr, dial = [], []
dial_words = 0
for path in FILES:
    for p in re.split(r"\n\s*\n", open(path, encoding="utf-8").read()):
        p = p.strip()
        if not p or p.startswith("#") or p == "---":
            continue
        c = clean(p)
        q = re.findall(r'"[^"]*"', c)
        for qq in q:
            dial_words += len(words(qq))
            for s_ in sentences(qq.strip('"')):
                dial.append(len(words(s_)))
        n = re.sub(r'"[^"]*"', " ", c)
        for s_ in sentences(n):
            narr.append(len(words(s_)))
res["narration_only"] = stats(narr)
res["dialogue_only"] = stats(dial)
res["dialogue_word_share_pct"] = round(100*dial_words/N,1)
TAGS = r'["\u201d]\s+(said|asked|answered|replied|called|shouted|added|told|whispered|murmured|cried)\b'
res["quote_adjacent_tags"] = len(re.findall(TAGS, text))
res["quote_adjacent_tags_per10k"] = per10k(res["quote_adjacent_tags"])
res["house_constructions_per10k"] = {k: per10k(len(re.findall(k, tl))) for k in ["there was a", "it was a", "she did not", "that she had"]}
EXTRA = {"nobody (all)": r"\bnobody\b", "tied a knot": r"tied a knot",
         "pale eyes": r"pale eyes", "like a man": r"like a man", "as one ": r"\bas one \w+", "I'd want": r"i'd want",
         "under my name": r"under (my|its|his) (own )?(captain's )?name", "for a hand": r"for a hand",
         "since (causal or temporal)": r"\bsince\b", "went red": r"went red", "went pink": r"went pink", "scarlet": r"scarlet",
         "something moved at the corner": r"something (moved|happened) at (the|one) corner", "a queer": r"\bqueer\b"}
res["tics_m2_lexicon"] = {k: len(re.findall(v, tl)) for k, v in EXTRA.items()}
json.dump(res, sys.stdout, indent=1, default=str)
