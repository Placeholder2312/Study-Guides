# OCR & Source Review Report — Module 4 (Fourier Series)

**Project:** Mathematics for Computer Engineering (2023111) — B.E. CSE (AI & ML), Semester III
**Review date:** 14 November 2026
**Reviewed sources:**

- `01_Original_Notes/Module_4/Module 4 CSE.pdf` — 8 handwritten pages
- `02_Tutorials/Tutorial 4.docx` — 1 page, 10 embedded equations
- `_work/sources/musa-practice-paper-set1-w2025.pdf` — 3 pages (scanned)
- `_work/sources/musa-question-bank-2026.pdf` — 9 pages (scanned)
- `_work/sources/maths-question-bank-solutions.pdf` — 108 pages; Module 4 = pages 46–77

This report is separate from `OCR_Review_Report.md`, which covers Module 1 and is unchanged.

---

## 1. Summary

| Question | Answer |
|---|---|
| Source documents identified | **5** (1 handwritten notes PDF, 1 tutorial DOCX, 3 examination/solution PDFs) |
| Source documents moved | **5 of 5**, contents unchanged |
| Duplicate files found | **None** |
| Handwritten pages processed | **8 of 8** (all) |
| Pages with unresolved unreadable mathematics | **0** |
| Pages with a flagged teacher slip | **1** (page 3, §7.1) |
| Tutorial equations recovered | **10 of 10** (5 questions complete) |
| Tutorial content genuinely missing | **None** — see §5 |
| Module 4 exam questions extracted | **25** (3 practice paper + 22 question bank) |
| Non-Module-4 material excluded | Modules 1, 2, 3, 5, 6 in all three PDFs |
| Symbolic verification | **Passed** for every example, every coefficient and every deduction |
| Paid services used | **None** |

---

## 2. Tooling (what was actually used)

The tooling decision from Module 1 was re-used rather than re-litigated; the tests are recorded in `OCR_Review_Report.md` §2 and were not repeated here.

| Tool | Role in this module |
|---|---|
| **PyMuPDF** | Page rendering at 150 dpi for visual reading; 300–700 dpi clips for doubtful symbols; text extraction from the born-digital solution booklet |
| **Native multimodal transcription (this model)** | Primary reading of the 8 handwritten pages and of the 12 scanned exam pages |
| **python-docx / raw OOXML parsing** | Structure inspection of `Tutorial 4.docx`; object/relationship map |
| **GDI+ (PowerShell `System.Drawing`)** | Vector rendering of the 8 WMF equation previews at 1400 px |
| **SymPy 1.14** | Independent derivation of every Fourier coefficient; numerical check of every series and every deduction |
| **RapidOCR** | Available and previously tested; **not used** for these sources. Module 1's test showed it cannot read this handwriting, and the exam PDFs are printed text that the model reads directly with higher accuracy than the OCR fragments it produced on the same material. |

No paid API, subscription or cloud service was used. No global OpenCode setting was changed.

### 2.1 Why no OCR pass was run on the exam PDFs

Both MUSA PDFs are image-only scans (zero characters of text layer on all 12 pages). A printed-text OCR pass would return the prose but not reliably the mathematics — fractions, \(\pi\) symbols, summation limits and piecewise braces. One careful visual pass per page, at 150 dpi with 300–700 dpi crops for the dense parts, produced a complete and unambiguous reading. The full text of every Module 4 question is in `03_Transcriptions/Exam_Questions_Module_4.md`.

### 2.2 Text layer in the solution booklet

`maths-question-bank-solutions.pdf` is a print-to-PDF of an HTML page, so it has a usable text layer. Its mathematics is broken across lines (a fraction arrives as three separate lines), which makes text extraction useless for equations but adequate for locating sections and reading stated results. All results used from it were re-derived; see §6.

---

## 3. Handwritten notes — page-by-page outcome

Legend: ✅ read and verified · ⚠️ read with a flagged issue

| PDF page | Content | Status | Notes |
|---:|---|---|---|
| 1 | Module heading, syllabus row, Dirichlet's conditions, \((c,c+2l)\), \((0,2l)\), \((0,2\pi)\) formulas | ✅ | The word "discontinuities" is written as two words; recorded `[as written]` |
| 2 | \((-l,l)\), \((-\pi,\pi)\), even/odd definitions, symmetric-limit property, even/odd series, two exponential integrals | ✅ | The heading "Property" is written as "Boperty"; recorded. Neither exponential integral is used later |
| 3 | Trig values; \(x^2\) on \((0,2)\); \(x\) on \((0,2\pi)\) | ⚠️ | Interval written "\((0,2l)\)" while the working uses \(2l=2\); cosine sum closes with \(4/\pi\) instead of \(4/\pi^2\) (§7.1) |
| 4 | \(b_n\) for \(x\); \(4-x^2\) on \((0,2\pi)\) | ✅ | The \(b_n\) bracket simplifies to \(4\pi/n\); every intermediate value checked |
| 5 | \(x\) on \((-\pi,\pi)\); \(x^2\) on \((-\pi,\pi)\) | ✅ | \(a_0\) written as \(\frac{1}{\pi}\int_0^\pi\), equivalent to \(\frac{1}{2\pi}\int_{-\pi}^{\pi}\) for an even function |
| 6 | \(x^2\) on \((-\pi,\pi)\) restated; three deductions | ✅ | All three deductions correct |
| 7 | \(x^2\) on \((0,2\pi)\); \(\left(\frac{\pi-x}{2}\right)^2\) to \(a_n\) | ✅ | |
| 8 | \(b_n=0\); final series for \(\left(\frac{\pi-x}{2}\right)^2\) | ✅ | Both brackets in \(b_n\) are identical, giving 0 |

**Total: 8 pages, 0 unreadable, 1 flagged slip.**

---

## 4. Readings that needed a second look

| Page | Doubtful item | Resolution |
|---:|---|---|
| 3 | Is the interval \((0,2l)\) or \((0,2)\)? | The marginal note says \(c=0,\ 2l=2\therefore l=1\), and the integrals run 0 to 2. Tutorial 4 Q1 confirms \((0,2)\). Transcribed as printed and annotated |
| 3 | Is the \(a_0\) denominator "\(\frac{1}{2l}\)" with a struck-through \(l\)? | Either reading gives the same value once \(l=1\); recorded as \(\frac{1}{2l}\) and the substitution is shown |
| 3 | Is the closing cosine factor \(\frac{4}{\pi}\) or \(\frac{4}{\pi^2}\)? | 600 dpi crop shows \(\frac{4}{\pi}\). It is a slip; see §7.1 |
| 7 | Is the second question \(x^2\) or \(\left(\frac{\pi-x}{2}\right)^2\)? | 600 dpi crop shows two separate questions: page top is \(f(x)=x^2\), mid-page is \(f(x)=\left(\frac{\pi-x}{2}\right)^2\) |
| 2 | Are the exponential-integral formulas correct? | Differentiated both: yes, both correct |

None of these required a guess: each was settled from a crop of the page.

---

## 5. Tutorial 4 — the "missing expressions" investigation

**The expressions are not missing.** They are Equation Editor 3.0 objects, exactly as in Tutorial 1.

Evidence chain:

1. `word/document.xml` contains 5 question paragraphs whose only visible text is "Expand Fourier series for … in …".
2. Each paragraph contains **two** `<w:object>` elements, each with an `<o:OLEObject ProgID="Equation.3">` and a `<v:imagedata>` vector preview.
3. There are 10 OLE objects and 8 preview files. Two previews are shared because two equations are duplicated: \(f(x)=x^2\) (Q1, Q2) and \((0,2\pi)\) (Q2, Q4, Q5). Byte-identical equations share one WMF.
4. The 8 previews were rendered at 1400 px and read directly; the object order in the XML fixes which expression belongs to which question.

Recovered questions:

| Q | Function | Interval |
|---|---|---|
| 1 | \(x^2\) | \((0,2)\) |
| 2 | \(x^2\) | \((0,2\pi)\) |
| 3 | \(x\) | \((-\pi,\pi)\) |
| 4 | \(x\) | \((0,2\pi)\) |
| 5 | \(\left(\frac{\pi-x}{2}\right)^2\) | \((0,2\pi)\) |

Full detail, including the rId → WMF map, is in `03_Transcriptions/Tutorial_4_Transcription.md`.

**Conclusion:** the tutorial is complete. No question had to be inferred, and no supplementary replacement was needed. The original DOCX is preserved unchanged.

---

## 6. Symbolic verification performed

The authoritative check is `_work/verify_m4_guide.py`, which was run to completion with **0 failures**. It works in the teacher's convention throughout, so a coefficient is compared with the exact form printed in the guide rather than with a differently normalised book formula. It covers all eight handwritten pages, all 25 supplied questions, the 16 graded practice items, the half-range, complex-form and Parseval material, the seven exact numerical series, and the endpoint/jump values.

Two earlier scripts, `_work/verify_m4.py` and `_work/verify_m4b.py`, were the first pass and are retained as audit artefacts. They are not the citation of record: an earlier revision of `verify_m4.py` was slow enough to hit the 120-second timeout on its 200,000-term numerical sums, and five of its typed \(a_0\) expectations had been written in the book's \(a_0/2\) convention rather than the teacher's \(a_0\) convention. Those five were B10 (\(\pi\) vs \(\pi/2\)), B16 (\(-2\pi^2/3\) vs \(-\pi^2/3\)), B17 (\(\pi\) vs \(\pi/2\)), B18 (\(4/3\) vs \(2/3\)) and B25 (\(4\sqrt2/\pi\) vs \(2\sqrt2/\pi\)); they have since been corrected in place, and the partial-sum limit reduced to 20,000 terms. `verify_m4_guide.py` remains the authoritative script cited in the guide (§9.5).

Each coefficient is derived from the definition on the stated interval and compared symbolically with the claimed closed form; each series is then evaluated numerically at points inside the interval and compared with the function value.

| Group | Checks | Result |
|---|---|---|
| The teacher's 7 examples (including both versions of \(x^2\)) | 20 coefficient identities + 7 series spot checks | ✅ all pass |
| Tutorial 4 (5 questions, all duplicates of teacher examples) | covered above | ✅ |
| Question bank, all 22 questions | 40+ coefficient identities, including odd-\(n\) / even-\(n\) cases and the \(n=1\) special case of \(x\sin x\) and \(x\cos x\) | ✅ all pass |
| Practice paper (3 questions) | coefficient identities | ✅ all pass |
| Deductions | \(\pi^2/6,\ \pi^2/12,\ \pi^2/8,\ \pi^4/90,\ \sum 1/(n^2-1)=3/4,\ \sum 1/(4n^2-1)=1/2,\ \pi/4\) | ✅ all confirmed to 6+ digits by direct partial summation |
| Endpoint/discontinuity values | \(x^2\) on \((0,2\pi)\) at \(x=0,2\pi\); \(4-x^2\) on \((0,2)\) at \(x=2\) | ✅ series limit equals the Dirichlet average |

The one place where the check **failed against the source** is QB-16, where the printed function is inconsistent with its own required deduction (§7.2). That is a source error, not a transcription error.

---

## 7. Errors and oddities found in the sources

### 7.1 Teacher's notes, page 3 — missing factor

The cosine coefficients are computed correctly as \(a_n=\dfrac{4}{n^2\pi^2}\), but the final series is closed with the common factor \(\dfrac{4}{\pi}\):
\[
x^2=\frac43+\frac{4}{\pi}\left[\frac{\cos\pi x}{1^2}+\frac{\cos 2\pi x}{2^2}+\cdots\right]-\frac{4}{\pi}\left[\frac{\sin \pi x}{1}+\cdots\right].
\]
Correct: \(\dfrac{4}{\pi^2}\) on the cosine sum. **Status:** reproduced unchanged in the transcription, flagged there, corrected in the study guide (§2.9 and §7.4). This is the only numerical error in the eight pages.

### 7.2 Question bank — QB-16 data inconsistency

Printed: \(f(x)=x+\dfrac{2x}{\pi}\) on \((-\pi,0)\), \(\dfrac{\pi}{2}-x\) on \((0,\pi)\), "hence deduce \(\pi^2/8=\sum_{\text{odd}}1/n^2\)". The first branch makes \(f\) neither even nor odd, and the deduction does not follow. The intended even function is \(\dfrac{\pi}{2}+x\) on \((-\pi,0)\). **Status:** printed form preserved in `Exam_Questions_Module_4.md`; the study guide solves the corrected version, states the correction explicitly, and also shows why the deduction works only for the corrected data.

### 7.3 Question bank — QB-6(ii) misprint

Printed \(\pi^2/90\) against a sum of fourth powers; must be \(\pi^4/90\). The printed form is a dimensional impossibility (\(\pi^2/90 \approx 0.11\), while the series is \(\approx 1.0823\)). **Status:** recorded; the guide proves \(\pi^4/90\) and says so.

### 7.4 Question bank — structural oddities (not errors)

- Two different questions are both numbered "Q.2" in the \((0,2l)\) section.
- QB-7 is filed under "(0, 2π)" but is set on \((-\pi,\pi)\).
- QB-8 writes \((0,a)\) where the half-period letter is normally \(l\).
- QB-22 repeats "\(f(x)=f(x)=\)".
- QB-6 ends with a stray "d".
- The practice paper writes "Find Fourier to represent" instead of "Find the Fourier series to represent".

All are preserved verbatim with `[as printed]` notes.

### 7.5 Solution booklet — convention, not error

`SOL-M4` uses \(f(x)=\frac{a_0}{2}+\sum(a_n\cos nx+b_n\sin nx)\) with \(a_0=\frac1\pi\int f\). The teacher uses \(a_0\) as the constant term with \(a_0=\frac{1}{2l}\int f\). Both are correct and the answers agree once converted. The guide explains the conversion once (§2.4) and never mixes the two inside a single derivation.

---

## 8. Items verified by hand as well as by machine

The following were checked on paper as well as by SymPy, because they are the steps a student will reproduce in an exam and a machine check alone would not reveal a confusing presentation:

1. Integration by parts for \(\int x^2\cos nx\,dx\), \(\int x^2\sin nx\,dx\), \(\int x\cos nx\,dx\), \(\int x\sin nx\,dx\), \(\int (4-x^2)\cos nx\,dx\), \(\int (4-x^2)\sin nx\,dx\), \(\int (\pi-x)^2\cos nx\,dx\), \(\int(\pi-x)^2\sin nx\,dx\).
2. The four trigonometric substitutions \(\sin n\pi=0\), \(\sin 2n\pi=0\), \(\cos n\pi=(-1)^n\), \(\cos 2n\pi=1\), including the sign produced when \((-1)^n\) multiplies \((-1)^n\).
3. The Dirichlet average at the endpoints of \((0,2\pi)\) and \((0,2)\), where substituting \(x=0\) into \(f\) gives the wrong number.
4. The three additions/subtractions that produce \(\pi^2/6\), \(\pi^2/12\) and \(\pi^2/8\) from the same series.

---

## 9. Residual uncertainties

| Item | Status |
|---|---|
| Teacher's page 3 interval label "(0,2l)" | Annotated; both readings give the same working because \(2l=2\) |
| Teacher's page 1 wording "and its integrals are finite" | Reproduced as written; the standard Dirichlet statement is discussed in the guide |
| QB-16 first branch | Genuinely inconsistent in the source; corrected version solved and labelled |
| QB-6(ii) exponent | Misprint identified beyond reasonable doubt (see §7.3) |
| Whether the MUSA documents mirror any actual University paper | **Unknown and not claimed.** They are student-association materials, and are labelled as such everywhere |

No formula, coefficient or limit in the eight handwritten pages was left unresolved.
