# OCR Review Report

**Project:** Mathematics for Computer Engineering (2023111) — B.E. CSE (AI & ML), Semester III
**Review date:** 10 November 2026
**Reviewed sources:**
- `00_University_Syllabus/Portion (6.21-N-B.E.-AI-ML-sem-III-IV).pdf`
- `01_Original_Notes/Module_1/CSE Module 1.pdf`
- `02_Tutorials/Tutorial 1.docx`

---

## 1. Summary

| Question | Answer |
|---|---|
| Source documents identified | **3** (1 syllabus PDF, 1 handwritten notes PDF, 1 tutorial DOCX) |
| Source documents moved | **3 of 3**, contents unchanged |
| Duplicate files found | **None** |
| Syllabus pages extracted | **3** (PDF pages 16–18) — all six modules |
| Handwritten pages processed | **20 of 20** |
| Tutorial questions extracted | **5 of 5**, all 7 embedded equations recovered |
| Pages with unresolved unreadable mathematics | **0** |
| Pages with flagged transcription/teacher issues | **6** (pages 3, 4, 12, 14, 16, 18) |
| Symbolic verification | **Passed** for all 20 pages and all 5 tutorial questions |
| Paid services used | **None** |

---

## 2. OCR tool investigation

The preference was free, open-source, locally running software. The actual nature of the sources determined the choice: the syllabus is a born-digital PDF with a text layer, the notes are cursive handwriting with matrices, and the tutorial equations are embedded Equation Editor 3.0 objects.

| Tool | Status on this machine | Assessment | Decision |
|---|---|---|---|
| **PyMuPDF 2.1** | Installed during this session | Exact text extraction from the digital syllabus; high-resolution page rendering (150 dpi) for visual reading | **Used** for syllabus extraction and page rendering |
| **RapidOCR 1.4.4** (`rapidocr-onnxruntime`, PP-OCR ONNX models) | Installed and tested | Free, offline, printed-text detector. On handwritten page 1 it returned 23 noisy fragments such as `Maduo1`, `Lma Agua (Thany`, `Pyromialy`, and no usable mathematics. Unsuitable for cursive handwriting. | Tested, **not used** for transcription |
| **Tesseract** | Not installed; no binary on PATH | Printed-text OCR; no native handwritten-math or matrix reconstruction. Would require a system install (winget available) and would still fail on this notebook. | **Not installed** |
| **PaddleOCR 3.7.0** | Available on PyPI; not installed | Current releases include PP-Structure/PP-FormulaNet for **printed** formula recognition. Requires a large PaddlePaddle runtime download. No reliable cursive-handwriting math mode. | Investigated, **not installed** |
| **pix2tex / LaTeX-OCR 0.1.4** | Available on PyPI; not installed | Open-source image-to-LaTeX for **printed** formulas; requires PyTorch (multi-GB). Not designed for handwritten prose plus matrices. | Investigated, **not installed** |
| **MathOCR** | No matching PyPI distribution | Could not be obtained as a maintained, installable FOSS package; the historic project is not practical here. | **Unavailable** |
| **Native multimodal transcription** (this model) | Available | The model's image input was tested and confirmed (see §3). It reads the handwriting, matrices, signs and layout directly. Combined with SymPy for independent verification. | **Selected** |
| **SymPy 1.14** | Installed during this session | Exact symbolic checks of characteristic polynomials, eigenvalues, eigenvectors, Cayley–Hamilton identities and matrix products | **Used for verification** |
| **python-docx 1.2.0** | Installed during this session | DOCX structure inspection; used alongside raw OOXML parsing | **Used** |

No paid API, subscription or cloud OCR service was used. No global OpenCode settings or plugins were changed. Packages were installed into the existing user Python 3.12 environment only.

### 2.1 RapidOCR test evidence

Command: `python _work/test_ocr.py _work/pages/m1_p01.png`
Engine: RapidOCR 1.4.4 (PP-OCR ONNX, printed-text models)
Detections: 23

Representative output:

```text
0.71  Maduo1
0.93  CSE(AIML)
0.69  Lma Agua (Thany
0.60  W.Sma
0.66  uama,
0.73  [A-dI丨 =O  Chnatuc qudion d A-
0.68  EaonValcsPopvalce. Hhmattn A
```

This is sufficient to show that printed-text OCR cannot be used as the primary transcription engine for this notebook.

---

## 3. Model image-input capability — verified, not assumed

The model's vision capability was tested before relying on it:

1. Page 1 of the notebook was rendered to PNG at 150 dpi with PyMuPDF.
2. The PNG was opened through the image-reading tool and returned successfully.
3. The model read the handwritten title, the three syllabus bullets, and the definitions of characteristic equation, eigenvalues and eigenvectors.
4. As a stronger test, page 2's handwritten \(3\times3\) matrix was read as
   \(\begin{bmatrix}2&-1&1\\1&2&-1\\1&-1&2\end{bmatrix}\). SymPy independently produced the same characteristic polynomial written by the teacher, \(\lambda^3-6\lambda^2+11\lambda-6\), with eigenvalues \(1,2,3\).
5. Every subsequent matrix was cross-checked the same way.

**Conclusion:** the model supports image input, and it was used as the primary transcription path. OCR was not assumed to work; it was demonstrated on the actual documents.

---

## 4. Processing outcomes by page

Legend: ✅ processed and verified · ⚠️ processed with a flagged reading · ❌ unreadable

### 4.1 Syllabus PDF (SRC-01)

| PDF page | Content | Status |
|---:|---|---|
| 16 | Course header, teaching/exam scheme, rationale, objectives, outcomes | ✅ |
| 17 | Detailed syllabus table: prerequisite, Modules I–VI, hours, CO mapping, self-learning topics | ✅ |
| 18 | Books, online references, assessment, term work, question-paper format | ✅ |

Text was extracted from the PDF text layer, so there is no character-recognition uncertainty on these pages. Table cells were reassembled by reading the rendered page alongside the extracted text where column order was ambiguous.

### 4.2 Handwritten Module 1 notes (SRC-02)

| PDF page | Content | Status | Notes |
|---:|---|---|---|
| 1 | Module heading, topics, definitions | ✅ | Clear |
| 2 | Procedure, Type I, example setup | ✅ | Clear |
| 3 | \(\lambda=1\), \(\lambda=2\) | ⚠️ | Cramer sign issue, see §5.1 |
| 4 | \(\lambda=3\), independence proof | ⚠️ | “From (i)” slip, see §5.2 |
| 5 | Type II, \(\lambda=0\) | ✅ | Clear |
| 6 | \(\lambda=3\), \(\lambda=15\) | ✅ | Clear |
| 7 | Type III, \(\lambda=1\) | ✅ | Row-reordering label noted |
| 8 | \(\lambda=5\); Type IV setup | ✅ | Clear after close reading |
| 9 | \(\lambda=2\) (two vectors), \(\lambda=5\) | ✅ | Clear |
| 10 | Theorems, nine properties, sum/product | ✅ | Two wording slips, see §5.7 |
| 11 | \(A^2-2A+I\); adjoint eigenvalues | ⚠️ | Final diagonal entry read as 4; synthetic-division table not transcribed |
| 12 | Fifth example, \(\lambda=1\) | ⚠️ | \(S_2\) bracket ambiguity, see §5.3 |
| 13 | \(\lambda=2\); CHT statement and setup | ✅ | Clear |
| 14 | CHT verification; second CHT setup | ⚠️ | Struck-out \(9A-3I\), see §5.4 |
| 15 | Second CHT; \(A^{-1}\), \(A^4\) | ✅ | Every entry verified symbolically |
| 16 | Similarity, diagonalisability, notes | ⚠️ | Notes (iii) and (v), see §5.7 |
| 17 | Diagonalisation example, \(\lambda=0\) | ✅ | Clear |
| 18 | \(\lambda=3\), \(\lambda=15\), \(D\), \(M\) | ⚠️ | Determinant sign, see §5.5 |
| 19 | Repeated-eigenvalue example, \(\lambda=-1\) | ✅ | Matrix entries confirmed by char. poly |
| 20 | \(\lambda=3\), \(D\), \(M\), conclusion | ✅ | Clear |

**Total: 20/20 pages successfully processed.**

### 4.3 Tutorial 1 (SRC-03)

| Part | Status | Method |
|---|---|---|
| Header text | ✅ | OOXML text extraction |
| Q1 matrix | ✅ | Vector WMF preview + file-relation order |
| Q2 matrix | ✅ | Vector WMF preview |
| Q3 matrix polynomial | ✅ | Vector WMF preview |
| Q3 matrix | ✅ | Vector WMF preview |
| Q4 matrix | ✅ | Vector WMF preview |
| Q5 matrix | ✅ | Vector WMF preview |
| Q5 identity | ✅ | Vector WMF preview |

No equation was missing from the previews, and no expression had to be reconstructed from surrounding prose.

---

## 5. Uncertain handwriting and possible errors

### 5.1 PDF page 3 — Cramer ratio for \(\lambda=1\)

- Written: \(\dfrac{x_1}{0}=\dfrac{x_2}{-2}=\dfrac{x_3}{2}\).
- The determinant directly above the middle term is \(\begin{vmatrix}1&1\\1&-1\end{vmatrix}=-2\), and the numerator is \(-x_2\), which gives \(+x_2/2\), not \(x_2/(-2)\).
- The next line states \(x_1=0,\ x_2=2,\ x_3=2\).
- **Status:** transcription preserved exactly; flagged inline. Final eigenvector \([0,1,1]^T\) is correct.

### 5.2 PDF page 4 — “From (i), \(k_1=-k_2\)”

- Equation (i) is \(k_2+k_3=0\); the relation \(k_1=-k_2\) follows from equation (ii).
- **Status:** preserved as written; flagged inline. The independence conclusion is correct.

### 5.3 PDF page 12 — \(S_2\) third bracket

- Written: \((2-6)\), followed by “\(=4-2+6=8\)”.
- The correct minor is \(12-6=6\); the “1” is not clearly visible in the scan.
- **Status:** preserved as \((2-6)\); flagged inline. The characteristic polynomial and all later values are correct.

### 5.4 PDF page 14 — struck-out terms

- The working line is written as \(A^3-6A^2+9A-3I\), with \(9A\) and \(3I\) struck through, then \(+2A\).
- The matrices for \(3A\) and \(3I\) are also present and struck through.
- **Status:** reproduced exactly with a note. The surviving identity \(A^3-6A^2+2A=0\) is verified.

### 5.5 PDF page 18 — determinant sign

- The first Cramer determinant is written with \(+6\) in the top-left position; the coefficient matrix has \(-6\).
- The evaluated value \(16\) matches \(-6\), not \(+6\).
- **Status:** flagged inline; value preserved as written.

### 5.6 PDF page 11 — final diagonal entry of \(A\)

- The glyph could resemble “3”, but the text states the eigenvalues are \(2,1,4\), and the working uses \(f(4)=9\).
- The matrix \(\begin{bmatrix}2&0&-2\\0&1&-4\\0&0&4\end{bmatrix}\) reproduces every stated value exactly.
- **Status:** transcribed as 4; confidence high, based on the teacher's own explicit eigenvalue statement and \(f(4)\).

### 5.7 PDF pages 10 and 16 — terminology slips

- Page 10, note (viii): “at least one zero is eigen value” (meaning: at least one eigenvalue is zero).
- Page 16, note (iii): “algebraic multiplicity ≠ algebraic multiplicity” (normally algebraic ≠ geometric).
- Page 16, note (v): the number of independent eigenvectors is called “algebraic multiplicity” (normally geometric multiplicity).
- **Status:** all preserved verbatim and flagged inline.

### 5.8 PDF page 7–8 — row-operation label

- “By \(R_{13}\)” produces the row order \(\begin{bmatrix}1&2&-3\\1&-2&1\\-3&2&1\end{bmatrix}\).
- With that order, the labels \(R_2\to R_2-R_1\) and \(R_3\to R_3+3R_1\) produce exactly the next matrix, so the working is internally consistent.
- **Status:** transcribed the actual matrix and operations; no correction needed.

### 5.9 Fully unreadable expressions

**None.** No matrix entry or formula required an `[UNCLEAR — PDF PAGE X]` marker. The only element deliberately not transcribed is the small synthetic-division table on page 11, which is an auxiliary root check and adds no mathematical content.

---

## 6. Symbolic verification (SymPy 1.14)

Verification scripts: `_work/verify_math.py` and `_work/verify_math2.py`.

### 6.1 Module 1 notes

| PDF pages | Matrix / claim | SymPy result | Match |
|---:|---|---|---|
| 2–4 | \(A=\begin{bmatrix}2&-1&1\\1&2&-1\\1&-1&2\end{bmatrix}\) | char. poly \(\lambda^3-6\lambda^2+11\lambda-6\); eigenvalues \(1,2,3\); vectors \([0,1,1],[1,1,1],[1,0,1]\) | ✅ |
| 5–6 | \(A=\begin{bmatrix}8&-6&2\\-6&7&-4\\2&-4&3\end{bmatrix}\) | char. poly \(\lambda^3-18\lambda^2+45\lambda\); eigenvalues \(0,3,15\); vectors \([1,2,2],[2,1,-2],[2,-2,1]\) (up to scale) | ✅ |
| 7–8 | \(A=\begin{bmatrix}2&2&1\\1&3&1\\1&2&2\end{bmatrix}\) | \(\lambda^3-7\lambda^2+11\lambda-5\); eigenvalues \(1,1,5\); vectors \([2,-1,0],[1,0,-1],[1,1,1]\) | ✅ |
| 8–9 | \(A=\begin{bmatrix}3&-1&1\\-1&3&-1\\1&-1&3\end{bmatrix}\) | \(\lambda^3-9\lambda^2+24\lambda-20\); eigenvalues \(2,2,5\); vectors \([1,1,0],[-1,0,1],[1,-1,1]\) | ✅ |
| 10 | \(A=\begin{bmatrix}-17&18&-6\\-18&19&-6\\-9&9&-2\end{bmatrix}\) | trace \(0\), determinant \(-2\) — matches stated sum and product | ✅ |
| 11 | \(A=\begin{bmatrix}2&0&-2\\0&1&-4\\0&0&4\end{bmatrix}\), \(A^2-2A+I\) | eigenvalues \(2,1,4\); \(f(A)\) eigenvalues \(1,0,9\) | ✅ |
| 11 | \(A=\begin{bmatrix}2&0&-1\\0&2&0\\-1&0&2\end{bmatrix}\), adjoint | char. poly \(\lambda^3-6\lambda^2+11\lambda-6\); eigenvalues \(1,2,3\); \(\operatorname{adj}\) eigenvalues \(6,3,2\) | ✅ |
| 12–13 | \(A=\begin{bmatrix}4&6&6\\1&3&2\\-1&-5&-2\end{bmatrix}\) | \(\lambda^3-5\lambda^2+8\lambda-4\); eigenvalues \(1,2,2\); vectors \([4,1,-3]\) and \([3,1,-2]\) | ✅ |
| 13–14 | CHT: \(A=\begin{bmatrix}3&2&1\\1&2&2\\3&2&1\end{bmatrix}\) | \(A^3-6A^2+2A=0\) exactly | ✅ |
| 14–15 | CHT: \(A=\begin{bmatrix}1&2&3\\2&-1&4\\3&1&-1\end{bmatrix}\) | \(A^3+A^2-18A-40I=0\); \(A^{-1}=\frac{1}{40}\begin{bmatrix}-3&5&11\\14&-10&2\\5&5&-5\end{bmatrix}\); \(A^4=\begin{bmatrix}248&101&218\\272&109&50\\104&98&204\end{bmatrix}\) | ✅ |
| 17–18 | \(D=M^{-1}AM\), \(D=\operatorname{diag}(0,3,15)\) | Exact equality with \(M=\begin{bmatrix}1&2&2\\2&1&-2\\2&-2&1\end{bmatrix}\) | ✅ |
| 19–20 | \(D=M^{-1}AM\), \(D=\operatorname{diag}(-1,-1,3)\) | Exact equality with \(M=\begin{bmatrix}1&1&1\\2&0&1\\0&2&2\end{bmatrix}\) | ✅ |

### 6.2 Tutorial 1

| Question | SymPy result | Match |
|---|---|---|
| Q1 | \(\lambda^3-\lambda^2-5\lambda-3\); eigenvalues \(3,-1,-1\); eigenvectors \([1,1,2],[1,2,0],[1,0,2]\) (up to scale) | ✅ |
| Q2 | \(\lambda^3-6\lambda^2+11\lambda-6\); eigenvalues \(1,2,3\) — all distinct, so diagonalisable | ✅ |
| Q3 | char. poly \(\lambda^3-7\lambda^2+16\lambda-12\); the given polynomial leaves remainder \(2A-I\) | ✅ |
| Q4 | char. poly \(\lambda^3-2\lambda^2-23\lambda+24\); three distinct real eigenvalues \(1,\frac12\pm\frac{\sqrt{97}}{2}\), so diagonalisable | ✅ |
| Q5 | char. poly \(\lambda^3-5\lambda^2+9\lambda-1\); \(A^{-1}=A^2-5A+9I\) exactly | ✅ |

Every matrix, determinant, characteristic polynomial, eigenvalue and eigenvector in the source was reproduced by SymPy without contradiction.

---

## 7. Duplicate-file report

No duplicates were found. The three source files have distinct content, names and hashes:

| File | SHA-256 | Duplicate? |
|---|---|---|
| `Portion (6.21-N-B.E.-AI-ML-sem-III-IV).pdf` | `a89900f9…0a7bd` | No |
| `CSE Module 1.pdf` | `b1241d8f…9f5bf` | No |
| `Tutorial 1.docx` | `5a3fe20a…b0c73` | No |

All originals were moved, not copied, and none was overwritten.

---

## 8. Items requiring your attention

1. **Course-code mismatch.** Tutorial 1 is headed **(2163111)**, while the official syllabus and programme structure give **2023111**. The tutorial may be from an older edition or contain a typo. Both are recorded; no file was altered.
2. **Six teacher slips/ambiguities** are documented in §5. They are reproduced in the transcription, not corrected. If your teacher clarifies any of them in class, update the transcription with a dated note.
3. **Tutorial Q4** has irrational eigenvalues \(1,\frac12\pm\frac{\sqrt{97}}{2}\). The matrix was recovered exactly from the document's vector equation object, so this is the printed question, not a transcription error. If the class expected integer eigenvalues, confirm with your teacher that this is the intended matrix.
4. **Module coverage.** Only Module 1 notes have been supplied so far. `01_Original_Notes/Module_2` through `Module_6` are created and empty, ready for future uploads.
5. **Page 11 synthetic-division table.** Its individual layout was not transcribed because it is an auxiliary root check; the coefficients and roots it confirms are all present in the transcription.
6. **Handwriting-only source.** There is no second printed copy of the notes to cross-check against. Verification here is mathematical (SymPy) and internal-consistency based, not a comparison with another edition.

---

## 9. Files produced by this review

| File | Purpose |
|---|---|
| `00_University_Syllabus/Syllabus_Coverage.md` | Full syllabus extraction |
| `03_Transcriptions/Module_1_Transcription.md` | 20-page faithful transcription |
| `03_Transcriptions/Tutorial_1_Transcription.md` | Five-question tutorial transcription |
| `03_Transcriptions/Source_Index.md` | Source-to-transcription mapping |
| `04_OCR_Reports/OCR_Review_Report.md` | This report |
| `AGENTS.md` | Project instructions for future sessions |

Rendered page images, WMF previews, OCR test output and verification scripts are retained in `_work/` for audit purposes.
