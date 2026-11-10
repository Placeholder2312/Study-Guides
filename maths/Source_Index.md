# Source Index

This index maps every transcription to its original source document, PDF page numbers and integrity hash. Originals are preserved unchanged.

---

## 1. Source library

| ID | Original file | Location | Type | Extent | SHA-256 |
|---|---|---|---|---|---|
| SRC-01 | `Portion (6.21-N-B.E.-AI-ML-sem-III-IV).pdf` | `00_University_Syllabus/` | Official University of Mumbai programme/syllabus PDF (digital, text layer) | 72 PDF pages; Mathematics section on PDF pages 16–18 | `a89900f9984645a6888d71277051d990eadb50e12fc5684ffd8876501df0a7bd` |
| SRC-02 | `CSE Module 1.pdf` | `01_Original_Notes/Module_1/` | Handwritten teacher notes, scanned (Adobe Scan for iOS) | 20 PDF pages | `b1241d8f896c64ba88d99c47af1d549ce75add84ae2be9878124a697d4a9f5bf` |
| SRC-03 | `Tutorial 1.docx` | `02_Tutorials/` | Word tutorial sheet with 7 embedded Equation Editor 3.0 objects | 1 document page | `5a3fe20a32d275a76f7606119f0188904b7ea51628a5620263e85e507b5b0c73` |

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

---

## 3. Not transcribed / excluded

| Item | Reason |
|---|---|
| SRC-01 pages 1–15, 19–72 | Programme structure and other subjects; outside Mathematics for Computer Engineering |
| SRC-03 letterhead image | Decorative header, no mathematical content |
| SRC-02 page 11 synthetic-division table | Auxiliary root-check table; values already recorded in the characteristic equation. Layout not transcribed. |
| SRC-02 page 11 and 14 struck-out working | Reproduced in the transcription where meaningful; the crossed-out version is not treated as content |

---

## 4. Verification artefacts

| File | Purpose |
|---|---|
| `04_OCR_Reports/OCR_Review_Report.md` | OCR/tool investigation, page outcomes, uncertainties, possible errors, SymPy verification results and manual-verification list |
| `03_Transcriptions/Module_1_Transcription.md` | Page-referenced transcription with inline `[as written]` notes |
| `03_Transcriptions/Tutorial_1_Transcription.md` | Question-by-question transcription with equation map |

Working files (rendered page images, OCR test outputs, verification scripts) are kept in `_work/` and are not part of the study library.
