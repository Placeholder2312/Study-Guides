# Module VI — OCR / Extraction Report

**Subject:** AOA (2023113) · **Module VI:** String Matching Algorithms
**Source PDF:** `Module VI String Matching-Algorithms.pptx.pdf` (17 pages, 74,768 bytes)
**Companion DOCX:** `Assignment 6.docx` (11,760 bytes)
**Extraction date:** 2026-11-20

## 1. Method

The PDF is a **slide export with an embedded text layer**, not a scanned document. Extraction was therefore done with PyMuPDF's text-layer reader rather than raster OCR (Tesseract is not installed on this machine and was not required). A raster pass would have introduced errors that the text layer avoids.

- Tool: PyMuPDF (`fitz`) `Page.get_text()`
- Output: `aoa/03_Transcriptions/Module_6_String_Matching_Transcription.md`
- Raw dump: page-separated text, 5,635 characters total
- `Assignment 6.docx` read with `python-docx` (paragraphs and tables)

## 2. Per-page yield

| Page | Characters | Content |
|---|---|---|
| 1 | 135 | Title and three algorithm names |
| 2 | 366 | Definition and applications |
| 3 | 127 | Agenda repeat |
| 4 | 375 | Naïve algorithm properties |
| 5 | 138 | Text/pattern diagram labels |
| 6–8 | 93 each | Shifts S = 0, 1, 2 |
| 9 | 163 | Shift S = 3, valid shift |
| 10 | 93 | Shift S = 4 |
| 11 | 142 | Shift S = 5, shift count |
| 12 | 412 | Naïve pseudocode |
| 13 | 149 | Comparison-counting exercise |
| 14 | 1,027 | Rabin–Karp explanation |
| 15 | 363 | Rabin–Karp pseudocode |
| 16 | 710 | Worked example, q = 13 |
| 17 | 825 | Worked example, q = 11 |

## 3. Quality assessment

| Issue | Effect | Handling |
|---|---|---|
| No scanned pages | No character-recognition noise | Nothing to correct |
| Slide bullets stored as separate text runs | Text order can interleave across columns (slides 5–11, 16–17) | Reconstructed in reading order in the transcription |
| `×`, `—`, `−` encoded as `�` in one pass | Cosmetic in raw dump only | Re-typed with the correct symbols in the transcription |
| Slide 11 says "9 − 4 = 5" shifts | Ambiguous wording (5 moves vs 6 alignments) | Explained in the guide, Section 2.7 |
| Slide 16 hashes listed in two interleaved columns | Order is not the text order | Re-ordered by shift and verified with Python |
| **KMP has no slides** | The deck does not cover one of the three prescribed algorithms | KMP written from the syllabus/textbook and marked *Supplementary section* |

## 4. Verification performed

Every numerical claim in the guide was recomputed independently in Python:

- Naïve: `aab` in `abaabcab` → shift 2, 10 comparisons, 6 alignments.
- Naïve: `aabc` in `abaaabccb` → shift 3.
- Naïve: `0001` in `000010001010001` → shifts 1, 5, 11; 31 comparisons; 12 alignments.
- Rabin–Karp q = 13 → pattern hash 7; valid shift 6; spurious at 12; all 15 window hashes match the slide.
- Rabin–Karp q = 11 → pattern hash 4; valid shift 6; spurious at 3, 4, 5; all 15 window hashes match the slide.
- KMP: prefix function of `ababaca` = `[0,0,1,2,3,0,1]`; match in `abababacaba` at shift 2; 12-step trace confirmed.
- KMP: prefix function of `aabaabaaa` = `[0,1,0,1,2,3,4,5,2]`; single match in `T = aabaabaabaabaaa` at shift 6 — an earlier draft claimed a match at 0, which the verification caught and corrected.

## 5. Coverage against the syllabus

| Syllabus item | Slides | Guide section |
|---|---|---|
| The Naïve string-matching algorithm | 4–13 | 2 |
| The Rabin Karp algorithm | 14–17 | 3 |
| The Knuth-Morris-Pratt algorithm | none | 4 (supplementary) |
| Real-life applications (self-learning) | slide 2 (partial) | 6 |

## 6. Limitations

- No KMP slide material exists in the supplied folder; the KMP section cannot be attributed to the class deck.
- The deck contains no University examination questions for Module VI, so the guide uses the assignment and the slide exercises as practice, each labelled with its provenance.
- The guide does not reproduce the alignment drawings from slides 5–11; it reconstructs them as text tables, which is sufficient for examination answers.
