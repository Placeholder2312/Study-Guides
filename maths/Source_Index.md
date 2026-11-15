# Source Index

This index maps every transcription to its original source document, PDF page numbers and integrity hash. Originals are preserved unchanged.

---

## 1. Source library

| ID | Original file | Location | Type | Extent | SHA-256 |
|---|---|---|---|---|---|
| SRC-01 | `Portion (6.21-N-B.E.-AI-ML-sem-III-IV).pdf` | `00_University_Syllabus/` | Official University of Mumbai programme/syllabus PDF (digital, text layer) | 72 PDF pages; Mathematics section on PDF pages 16–18 | `a89900f9984645a6888d71277051d990eadb50e12fc5684ffd8876501df0a7bd` |
| SRC-02 | `CSE Module 1.pdf` | `01_Original_Notes/Module_1/` | Handwritten teacher notes, scanned (Adobe Scan for iOS) | 20 PDF pages | `b1241d8f896c64ba88d99c47af1d549ce75add84ae2be9878124a697d4a9f5bf` |
| SRC-03 | `Tutorial 1.docx` | `02_Tutorials/` | Word tutorial sheet with 7 embedded Equation Editor 3.0 objects | 1 document page | `5a3fe20a32d275a76f7606119f0188904b7ea51628a5620263e85e507b5b0c73` |
| SRC-04 | `Module 4 CSE.pdf` | `01_Original_Notes/Module_4/` | Handwritten teacher notes, scanned (no text layer) | 8 PDF pages | `4182e1077f880795261dba0e87db84b62371778061959ece3c513337c5b9b9af` |
| SRC-05 | `Tutorial 4.docx` | `02_Tutorials/` | Word tutorial sheet with 10 embedded Equation Editor 3.0 objects (8 distinct WMF previews) | 1 document page | `e75d54d6c692426bd049916ddb580e70cd585795afb106fe13e0cc4c270690b8` |
| SRC-06 | `musa-practice-paper-set1-w2025.pdf` | `_work/sources/` | MUSA practice paper, Winter Session 2025, scanned (no text layer) | 3 PDF pages | `17fb8559daa4f7dec2ac625dc2053c56ab691ef7894650707c048f3ee125d404` |
| SRC-07 | `musa-question-bank-2026.pdf` | `_work/sources/` | MUSA question bank, Winter Session 2026, scanned (no text layer) | 9 PDF pages | `1c24161e4d16e5c3624f610e56ee2034a705475b604a2d39f16849eb921a89f2` |
| SRC-08 | `maths-question-bank-solutions.pdf` | `_work/sources/` | Third-party worked-solution booklet (digital, text layer); Module 4 = pages 46–77 | 108 PDF pages | `523d42600fc54da00b87702edd6ea17dafd8469e286046a4e9ee0e7ffcc404c2` |

No duplicate files were found. No original file was deleted, overwritten or modified.

---

## 2. Transcription map

### 2.1 Syllabus

| Generated file | Source | Source pages | Coverage |
|---|---|---|---|
| `00_University_Syllabus/Syllabus_Coverage.md` | SRC-01 | PDF pages **16, 17, 18** | Course identification, rationale, all six objectives and outcomes, prerequisite, all six modules, all prescribed topics, all self-learning topics, hours, CO mapping, books, references, assessment and question-paper format |

The remainder of SRC-01 (PDF pages 1–15 and 19–72) covers other Semester III/IV courses and was not part of this subject's extraction.

### 2.2 Module 1 notes

| Generated file | Source | Source pages | Coverage |
|---|---|---|---|
| `03_Transcriptions/Module_1_Transcription.md` | SRC-02 | PDF pages **1–20** (all) | Complete transcription: definitions, procedure, four example types, eigenvector examples, properties, two Cayley–Hamilton verifications, similarity and two diagonalisation examples |

Page-level map:

| PDF page | Content transcribed |
|---:|---|
| 1 | Module heading, syllabus topics, characteristic equation, eigenvalues, eigenvectors, sum/product properties |
| 2 | Procedure (7 steps), Type I, first example and characteristic equation |
| 3 | Example: \(\lambda=1\), \(\lambda=2\) |
| 4 | Example: \(\lambda=3\), eigenvector list, linear-independence proof |
| 5 | Type II, second example, characteristic equation, \(\lambda=0\) |
| 6 | Second example: \(\lambda=3\), \(\lambda=15\) |
| 7 | Type III, third example, characteristic equation, \(\lambda=1\) |
| 8 | Third example: \(\lambda=5\); Type IV, fourth example characteristic equation |
| 9 | Fourth example: \(\lambda=2\) (two eigenvectors), \(\lambda=5\) |
| 10 | Theorems 1–4, nine notes on eigenvalue properties, sum/product example |
| 11 | Eigenvalues of \(A^2-2A+I\); eigenvalues of adjoint |
| 12 | Fifth example: characteristic equation and \(\lambda=1\) |
| 13 | Fifth example: \(\lambda=2\); Cayley–Hamilton statement and first verification setup |
| 14 | First Cayley–Hamilton verification completed; second example setup |
| 15 | Second Cayley–Hamilton verification; \(A^{-1}\) and \(A^4\) |
| 16 | Similarity, diagonalisable matrices, theorem, five notes |
| 17 | Diagonalisation example: statement and \(\lambda=0\) |
| 18 | \(\lambda=3\), \(\lambda=15\), diagonal matrix \(D\), transforming matrix \(M\) |
| 19 | Repeated-eigenvalue example: characteristic equation and \(\lambda=-1\) |
| 20 | \(\lambda=3\), diagonal matrix, transforming matrix, final multiplicity statement |

### 2.3 Tutorial 1

| Generated file | Source | Source location | Coverage |
|---|---|---|---|
| `03_Transcriptions/Tutorial_1_Transcription.md` | SRC-03 | Whole document (1 page) | Header and all five questions, including all seven embedded equations |

Embedded object map:

| Question | OLE object | WMF preview | Content |
|---|---|---|---|
| 1 | `word/embeddings/oleObject1.bin` | `word/media/image1.wmf` | Matrix \(A\) |
| 2 | `oleObject2.bin` | `image2.wmf` | Matrix \(A\) |
| 3 | `oleObject3.bin` | `image3.wmf` | Matrix polynomial |
| 3 | `oleObject4.bin` | `image4.wmf` | Matrix \(A\) |
| 4 | `oleObject5.bin` | `image5.wmf` | Matrix \(A\) |
| 5 | `oleObject6.bin` | `image6.wmf` | Matrix \(A\) |
| 5 | `oleObject7.bin` | `image7.wmf` | Identity \(A^{-1}=A^2-5A+9I\) |

The unused media file `word/media/image8.jpg` is the college letterhead graphic, not mathematical content.

### 2.4 Module 4 notes

| Generated file | Source | Source pages | Coverage |
|---|---|---|---|
| `03_Transcriptions/Module_4_Transcription.md` | SRC-04 | PDF pages **1–8** (all) | Complete transcription: syllabus row, Dirichlet's conditions, the general interval formula and its four special cases, even/odd theory, and all seven worked expansions including the three numerical deductions |

Page-level map:

| PDF page | Content transcribed |
|---:|---|
| 1 | Module heading, syllabus row, Dirichlet's conditions, \(f(x)\) on \((c,c+2l)\), the special cases \((0,2l)\) and \((0,2\pi)\) |
| 2 | \((-l,l)\), \((-\pi,\pi)\), even/odd definitions, symmetric-limit integral property, even/odd series, two exponential integrals (unused) |
| 3 | Four standard trigonometric values; \(f(x)=x^2\) on \((0,2)\) — \(a_0,a_n,b_n\) and series; \(f(x)=x\) on \((0,2\pi)\) — \(a_0,a_n\) |
| 4 | \(b_n\) for \(f(x)=x\); final sine series; \(f(x)=4-x^2\) on \((0,2\pi)\) complete |
| 5 | \(f(x)=x\) on \((-\pi,\pi)\) (odd); \(f(x)=x^2\) on \((-\pi,\pi)\) (even) to \(a_n\) |
| 6 | Same \(x^2\) example restated; deductions \(\pi^2/6\), \(\pi^2/12\), \(\pi^2/8\) |
| 7 | \(f(x)=x^2\) on \((0,2\pi)\) complete; \(f(x)=\left(\frac{\pi-x}{2}\right)^2\) — \(a_0,a_n\) |
| 8 | \(b_n=0\); final cosine series for \(\left(\frac{\pi-x}{2}\right)^2\) |

### 2.5 Tutorial 4

| Generated file | Source | Source location | Coverage |
|---|---|---|---|
| `03_Transcriptions/Tutorial_4_Transcription.md` | SRC-05 | Whole document (1 page) | Header and all five questions, including all ten embedded equations |

Embedded object map:

| Question | OLE objects | WMF previews | Content |
|---|---|---|---|
| 1 | `oleObject1.bin`, `oleObject2.bin` | `image1.wmf`, `image2.wmf` | \(f(x)=x^2\), \((0,2)\) |
| 2 | `oleObject3.bin`, `oleObject4.bin` | `image1.wmf` (reused), `image3.wmf` | \(f(x)=x^2\), \((0,2\pi)\) |
| 3 | `oleObject5.bin`, `oleObject6.bin` | `image4.wmf`, `image5.wmf` | \(f(x)=x\), \((-\pi,\pi)\) |
| 4 | `oleObject7.bin`, `oleObject8.bin` | `image6.wmf`, `image7.wmf` | \(f(x)=x\), \((0,2\pi)\) |
| 5 | `oleObject9.bin`, `oleObject10.bin` | `image8.wmf`, `image7.wmf` (reused) | \(f(x)=\left(\frac{\pi-x}{2}\right)^2\), \((0,2\pi)\) |

`word/media/image9.jpg` is the college letterhead graphic.

### 2.6 Module 4 examination sources

| Generated file | Sources | Source pages | Coverage |
|---|---|---|---|
| `03_Transcriptions/Exam_Questions_Module_4.md` | SRC-06, SRC-07, SRC-08 | SRC-06 p. 2; SRC-07 pp. 4–5; SRC-08 pp. 46–77 | All 25 Module 4 questions with original wording, functions, intervals, marks and deductions; provenance and duplicate map |

Module 4 material inside each source:

| Source | Pages holding Module 4 content | Questions | Excluded |
|---|---|---:|---|
| SRC-06 | page 2 only (Q2 b, Q3 c, Q5 a) | 3 | Modules 1, 2, 3, 5, 6 on pages 1–3 |
| SRC-07 | page 4 (bottom) and page 5 (top two-thirds) | 22 | Pages 1–4 (top) = Modules 1–2; pages 6–9 = Modules 5–6 |
| SRC-08 | pages 46–77 | 22 (same set as SRC-07) | Pages 1–45 = Modules 1–2; pages 78–108 = later modules |

---

## 3. Not transcribed / excluded

| Item | Reason |
|---|---|
| SRC-01 pages 1–15, 19–72 | Programme structure and other subjects; outside Mathematics for Computer Engineering |
| SRC-03 letterhead image | Decorative header, no mathematical content |
| SRC-02 page 11 synthetic-division table | Auxiliary root-check table; values already recorded in the characteristic equation. Layout not transcribed. |
| SRC-02 page 11 and 14 struck-out working | Reproduced in the transcription where meaningful; the crossed-out version is not treated as content |
| SRC-04 page 2, two exponential integrals | Written on the page but never used in any worked example; recorded as a page note, not as taught content |
| SRC-04 page 3 trigonometric table | Read and used, but reproduced as a four-row table rather than as the teacher's handwritten layout |
| SRC-05 letterhead image (`word/media/image9.jpg`) | Decorative header, no mathematical content |
| SRC-06 Modules 1, 2, 3, 5, 6 questions | Other modules; only the three Module 4 questions on page 2 were extracted |
| SRC-07 Modules 1–2 (pages 1–4 top) and 5–6 (pages 6–9) | Other modules; only the Module 4 questions on pages 4–5 were extracted |
| SRC-08 pages 1–45 and 78–108 | Other modules; only the Module 4 solutions on pages 46–77 were used, and then only to confirm readings |

---

## 4. Verification artefacts

| File | Purpose |
|---|---|
| `04_OCR_Reports/OCR_Review_Report.md` | OCR/tool investigation, page outcomes, uncertainties, possible errors, SymPy verification results and manual-verification list (Module 1) |
| `04_OCR_Reports/OCR_Review_Report_Module_4.md` | Same, for Module 4: DOCX equation recovery, page readings, source errata in the examination PDFs, and the SymPy verification summary |
| `03_Transcriptions/Module_1_Transcription.md` | Page-referenced transcription with inline `[as written]` notes |
| `03_Transcriptions/Module_4_Transcription.md` | Page-referenced transcription of SRC-04, with the page-3 coefficient slip flagged |
| `03_Transcriptions/Tutorial_1_Transcription.md` | Question-by-question transcription with equation map |
| `03_Transcriptions/Tutorial_4_Transcription.md` | Question-by-question transcription with OLE-object and WMF-preview map |
| `03_Transcriptions/Exam_Questions_Module_4.md` | 25 Module 4 examination questions with provenance codes, original wording and duplicate map |

Working files (rendered page images, OCR test outputs, verification scripts) are kept in `_work/` and are not part of the study library.
