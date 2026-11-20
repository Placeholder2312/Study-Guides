# PROGRESS — Mathematics Endsem Questionbank

**Last updated:** 16 November 2026
**Current module:** Module I — Linear Algebra (Theory of Matrices)
**Current part:** Part 1 published and verified. Part 2 is the next build.
**Live route:** `/maths/endsem-questionbank` (source: `maths/endsem-questionbank/index.html`)

This file is the durable state of the project. Another session must be able to continue from here without reading the whole conversation.

---

## 1. What is finished

| Part | Topic | Questions covered | Verified | Published |
|---|---|---|---|---|
| 1 | Eigenvalues and eigenvectors | `M1-EV-Q1-i` … `M1-EV-Q1-vii` (7) + `PP25-Q4-b` (1) | Yes | Yes — `index.html` |

Part 1 contains: intuition and definitions, the teacher's \(S_1,S_2,|A|\) shortcut, the seven-step recipe, the teacher's Type I–IV classification, two fully worked teaching examples (a \(2\times2\) and a \(3\times3\) with a repeated eigenvalue), a ten-second checking routine, a common-mistakes table, a method-selection table, all 8 questions with printed provenance, and a separate answer key with row reduction and substitution checks.

## 2. What is in progress

Nothing. Part 1 was closed before Part 2 was started, deliberately.

## 3. Original questions processed

**Module I, MUSA 2026 bank (page 1–2 of 9):**

| ID | Printed as | Status |
|---|---|---|
| `M1-EV-Q1-i` … `-vii` | Eigen Value and Eigen Vector Q.1 i)–vii) | **Done** (Part 1) |
| `M1-EV-Q2-i`, `M1-EV-Q2-ii` | Q.2 i), ii) — eigenvalues of matrix expressions | Outstanding (Part 2) |
| `M1-CH-Q1` … `M1-CH-Q8` | Cayley Hamilton Q.1–Q.8 | Outstanding (Part 3) |
| `M1-DIAG-Q1` … `M1-DIAG-Q6` (Q3 has parts i and ii) | Diagonalizable Q.1–Q.6 | Outstanding (Part 4) |

Full inventory with page numbers, matrices and printed marks: `QUESTION_INVENTORY.md`.

**Supplementary, Winter 2025 practice paper:**

| ID | Status |
|---|---|
| `PP25-Q4-b` (eigenvalues and eigenvectors, 5 marks) | **Done** (Part 1) |
| `PP25-Q1-a` (eigenvalues of \(A^2-2A+I\)) | Outstanding (Part 2) |
| `PP25-Q1-a-OR` (eigenvalues of \(6A^{-1}+A^3+2I\)) | Outstanding (Part 2) |
| `PP25-Q2-a` (Cayley–Hamilton, \(2A^4-5A^3-7A+6I\)) | Outstanding (Part 3) |
| `PP25-Q2-a-OR` (verify Cayley–Hamilton, find \(A^{-1}\), \(A^{-2}\)) | Outstanding (Part 3) |
| `PP25-Q5-c` (diagonalise, 6 marks) | Outstanding (Part 4) |
| `PP25-Q5-c-OR` (diagonalise, second matrix) | Outstanding (Part 4) |

Progress: **8 of 31** Module I question items done — 8 of 24 bank items (7 eigenvalues + 1 practice-paper) and 1 of 7 supplementary items.

## 4. Solutions verified

- Every eigenvalue in Part 1 recomputed exactly with SymPy 1.14.
- Every eigenvector checked by substitution \(AX=\lambda X\) (`scripts/verify_part1_vectors.py`, output `scripts/out_part1_vectors.txt`).
- Every printed intermediate row-reduced matrix checked to have the *same null space* as the matrix it came from (`scripts/verify_steps.py`). This caught two wrong intermediate reductions during authoring, which were fixed.
- The supplied booklet's Module I eigenvalue answers were compared question by question and agree with the independent solutions, up to a scalar multiple of an eigenvector (which is still the same eigenvector).

## 5. Known source issues and discrepancies

| # | Where | What | Status |
|---|---|---|---|
| D1 | Bank page 1, Q.1 | The sixth matrix is labelled `v)` a second time; the seventh is `vii)`. Printing slip, recorded not corrected. | Recorded in the guide |
| D2 | Practice paper page 1, instructions | "Attempt any three questions from Q.2 to Q.5", but the paper also prints a Q.6; official pattern is three answers out of six questions with Q.1 compulsory. | Recorded in the guide |
| D3 | Solutions booklet PDF page 17 | Cayley–Hamilton question with \(A=\begin{bmatrix}1&2\\2&2\end{bmatrix}\) asks to deduce \(A^8=625I\). The booklet substitutes \(A=\begin{bmatrix}1&2\\2&-1\end{bmatrix}\). The printed matrix does **not** satisfy \(A^8=625I\). | To be investigated and documented in Part 3 |
| D4 | Solutions booklet PDF page 70 | Fourier series: a solution replaces the given piecewise function with a canonical one. | Out of scope until Module IV is reconciled |
| D5 | Bank page 1, Q.7 (Cayley–Hamilton) | The printed polynomial has a suspicious ordering/repetition of powers (`A^8 - 6A^5 + 7A^6 - 3A^5 + ...`). Must be re-read from an enlarged crop before Part 3 is written. | Outstanding |

## 6. Source pages already inspected

- `musa-question-bank-2026.pdf`: page 1 and page 2 (Module I complete; page 2 also shows the start of Module II, not yet transcribed).
- `musa-practice-paper-set1-w2025.pdf`: pages 1, 2 and 3 (all Module I items extracted; the rest of the paper belongs to other modules).
- `maths-question-bank-solutions.pdf`: pages 3–7 read in detail (Eigen Value Q.1 (i)–(vi)); pages 8–28 not yet read.
- `maths/Module_1_Transcription.md`: pages 1–2 and 10 (definitions, procedure, properties); pages 5, 7, 8 headings (Type II–IV); rest not yet consulted.
- Rendered page images: `_work/endsem/pages/` (local machine, not in the repository).

## 7. Verification scripts

Committed in `scripts/`:

| Script | What it proves |
|---|---|
| `verify_part1_eigen.py` | Characteristic polynomial, trace, determinant, eigenvalues, eigenvectors, diagonalisability for all 7 bank matrices and both expression questions of Q.2 |
| `verify_part1_vectors.py` | Every published eigenvector satisfies \(AX=\lambda X\); also checks the two teaching examples |
| `verify_steps.py` | Each printed row-reduction has the same null space as the matrix it replaced; confirms the non-diagonalisable example \(B\) |
| `verify_pp_teach.py`, `verify_q1v.py` | Ad-hoc checks used while writing (practice-paper matrix, teaching examples, \(S_2\) of `M1-EV-Q1-v`) |

Re-run any of them with `python scripts/<name>.py` from the repository root.

## 8. Local-only audit artefacts

- `_work/sources/` — the three original PDFs (not tracked in Git).
- `_work/endsem/pages/` — 200 dpi renders and 300–400 dpi crops used for visual comparison.
- `_work/endsem/solutions_text.txt` — extracted text of the 108-page solutions booklet.

None of these are required to read the published guide; they are the evidence behind it.

## 9. Exact next action

Write **Part 2 — eigenvalues of matrix expressions**:

1. Re-read bank page 1, Q.2 (i)–(ii) from the crop `crop_qb1_q2.png` and record the exact wording.
2. Read teacher's notes PDF page 11 (`maths/Module_1_Transcription.md`, "Eigenvalues of a matrix polynomial and of an adjoint") and use that method.
3. Solve `M1-EV-Q2-i` (\(A^3+5A+8I\)) and `M1-EV-Q2-ii` (\(A^2-2A+I\)) — already computed once, see `scripts/out_part1_eigen.txt`; re-verify.
4. Add `PP25-Q1-a` and `PP25-Q1-a-OR`, including the \(6A^{-1}+A^3+2I\) case, which needs the inverse-eigenvalue property.
5. Add a properties table (teacher's notes i–ix) marked as examinable "without proof".
6. Append Part 2 to `Module_1_Endsem_Questionbank.md` and the answers to `Module_1_Endsem_Answer_Key.md`.
7. Run `python maths/endsem-questionbank/_build/build.py`, open the page, repeat the visual QA, commit, push, verify the deployment.

Do not start Part 3 until Part 2 is published.

## 10. Publishing state

| Field | Value |
|---|---|
| Branch used | `maths-endsem-questionbank` |
| Files changed | `maths/index.html`, `maths/endsem-questionbank/*` |
| Deployed | See the Git commit message and the deployment check in the session report; this file is updated at each checkpoint |
