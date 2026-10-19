# Sampled identity review — 2026-10-19

This is objective diagnostic evidence, not human listening, accent approval,
full-book identity coverage or delivery acceptance. Production audio is unchanged.

## Frozen sample and controls

`voice-screen-v1` checks24 eligible takes per chapter:1,152 samples across48
chapters, using the separate frozen v1 repair editions for11 chapters and original
editions otherwise. Median cosine similarity is .9491. All50 failures below the
inherited .84 threshold are retained in the raw report; the threshold was not
lowered. Forty-six failures are shorter than3 seconds; the other four are chapter
headings18 s001 (3.52s),30 s001 (3.52s),34 s001 (4.24s), and48 s112 (44.8s).

`voice-controls-v1` contains10 known-positive crops of the locked Calder reference.
Short reference crops themselves can fail (.7234 for one1.5-second crop, .7795 for
one2-second crop). Therefore short duration is a plausible confound, not evidence
that any individual failed production take is acceptable. Short failures and the
three headings remain listening/review items. The62 separately checked adjacent
takes of at least5 seconds all pass (minimum .9188, median .9629). These neighbors
were not averaged with failed takes to hide failures.

Original48 s112 is different: all8 six-second temporal windows fail, ranging
.7357–.7582, median .7474. Its DNSMOS OVRL3.4300/SIG3.6479/BAK4.1850 and P8084.1790
are only signal/background diagnostics; they do not override the identity result.

## One bounded replacement, not promoted

Batch6 preserves the original48 s112 and creates one word-locked native Breeze
candidate,42.16seconds, SHA256
`8b439fb9a1f1e8e4f99ce712ccc39a103230303e4d132422189afa09061f2f95`.
Isolated and original-neighbor context ASR show no additions or omissions, with
proper-name/homophone spelling differences retained. All8 candidate six-second
identity windows pass .9281–.9551 (median .9457), using the same reference and
threshold. This supports retaining the candidate for further review, not claiming
perceived voice/prosody approval. Evidence is in `diagnostic-instruction-leak-v6`
and `voice-pickup-batch-6`. The frozen v1 repair editions do not include it.

## Remaining work

The UTMOSv2 screen uses the same frozen sample ledger, including the old48 s112,
so its results must not be attributed to later candidates. Naturalness scores
require outlier review and cannot prove exact spoken words or human performance
quality. Coverage residuals, short identity failures, pace/mastering decisions and
owner listening remain open. GitHub LFS budget holds remain in force.
