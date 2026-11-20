# SOURCE MAP — Endsem Questionbank

Which original file each part of the guide comes from, page by page, and which human-authored source explains each concept.

---

## 1. Original question documents (local, not in this repository)

| Role | File | Pages | SHA-256 |
|---|---|---|---|
| Question bank (authority for wording and numbers) | `musa-question-bank-2026.pdf` | 9 | `1c24161e4d16e5c3624f610e56ee2034a705475b604a2d39f16849eb921a89f2` |
| Solutions booklet (secondary; every claim checked) | `maths-question-bank-solutions.pdf` | 108 | `523d42600fc54da00b87702edd6ea17dafd8469e286046a4e9ee0e7ffcc404c2` |
| Practice paper, Set-I, Winter 2025 (supplementary) | `musa-practice-paper-set1-w2025.pdf` | 3 | `17fb8559daa4f7dec2ac625dc2053c56ab691ef7894650707c048f3ee125d404` |

All three hashes match `maths/Source_Index.md`. The files are stored on the project machine under `_work/sources/` and are not tracked by Git.

## 2. Page map — question bank

| File page | Content used | Used in |
|---|---|---|
| 1 | Header, "MODULE 1", Eigen Value and Eigen Vector Q.1 (i)–(vii), Q.2 (i)–(ii), Cayley Hamilton Q.1–Q.7 (Q.7's matrix continues on page 2) | Part 1 (Q.1), inventory |
| 2 | Q.7's matrix, Cayley Hamilton Q.8, "Diagonalizable" Q.1–Q.6, then Module II begins | Inventory; Parts 3–4 pending |
| 3–9 | Modules II, IV, V, VI | Out of scope for Module I |

## 3. Page map — solutions booklet (Module I)

| File page | Content | Used in |
|---|---|---|
| 2 | Table of contents: Module 1 "Eigenvalues & Eigenvectors, Cayley-Hamilton Theorem, Diagonalization" | Confirms Module I scope |
| 3 | "MODULE 1" divider and its own table of contents (Topic 1 Eigen values and vectors, Topic 1 Q.2 expressions, Topic 2 Cayley–Hamilton, Topic 3 Diagonalization) | Structure reference |
| 4–7 | Topic 1 Q.1 (i)–(vi): characteristic equations and eigenvectors | Compared with Part 1 answers |
| 8–11 | Topic 1 Q.1 (vii), then Topic 1 Q.2 (matrix expressions) | Q.1 (vii) compared; Q.2 to be used in Part 2 |
| 12–28 | Cayley–Hamilton and diagonalisation solutions ("End of Module 1 Solutions" on page 28) | Parts 3–4; page 17 holds discrepancy D3 |
| 29–44 | Module 2 | Out of scope now |
| 46 onward | Module 4 (Fourier series); page 70 holds discrepancy D4 | Out of scope now |

The booklet has **no Module 3 section**. This matters later: Module III will have to be built from the practice paper and the syllabus.

## 4. Page map — practice paper

| File page | Content used | Used in |
|---|---|---|
| 1 | Header, instructions, Q.1 a) (eigenvalues of an expression) | Part 2 (`PP25-Q1-a`, `PP25-Q1-a-OR`); D2 |
| 2 | Q.2 a) Cayley–Hamilton; Q.4 b) eigenvalues/eigenvectors; Q.5 c) diagonalisation | Parts 1, 3, 4 |
| 3 | Q.5 c) second matrix; Q.6 (Modular arithmetic, regression, normal distribution) | Part 4; Module III later |

## 5. Course material

| Local file | Relevant pages | What it contributes |
|---|---|---|
| `maths/Module_1_Transcription.md` | PDF page 1 (definitions, sum/product of eigenvalues), page 2 (seven-step procedure, \(S_1,S_2,\lvert A\rvert\) shortcut, Type I), page 5 (Type II), page 7 (Type III), page 8 (Type IV), page 10 (properties i–ix) | The course method used throughout Part 1 |
| `maths/Syllabus_Coverage.md` | Module I entry | Prescribed scope, 5 teaching hours, CO1 |
| `maths/OCR_Review_Report.md` | Module 1 entries | Known reading uncertainties in the handwritten notes |

The teacher's own worked examples are the matrices of `M1-EV-Q1-i` (PDF pp. 2–4), `M1-EV-Q1-v` (pp. 5–6), `M1-EV-Q1-ii` (p. 7) and `M1-EV-Q1-iv` (pp. 8–9). The student therefore already has a human-written model solution for four bank questions.

## 6. Human-authored explanations used

| Author / institution | Resource | Section | URL | Used for |
|---|---|---|---|---|
| D. Margalit and J. Rabinoff, Georgia Institute of Technology | *Interactive Linear Algebra* (GNU FDL) | §5.1 Eigenvalues and Eigenvectors | <https://textbooks.math.gatech.edu/ila/eigenvectors.html> | The geometric idea of an eigenvector; the non-zero condition |
| Same | Same | §5.2 The Characteristic Polynomial | <https://textbooks.math.gatech.edu/ila/characteristic-polynomial.html> | Characteristic polynomial and the trace/determinant coefficients used as checks |
| W. K. Nicholson, *Linear Algebra with Applications*, Open Edition (LibreTexts, CC BY-NC-SA) | LibreTexts | §3.3 Eigenvalues and Eigenvectors | <https://math.libretexts.org/Bookshelves/Linear_Algebra/Linear_Algebra_with_Applications_%28Nicholson%29/03%3A_Determinants_and_Diagonalization/3.03%3A_Eigenvalues_and_Eigenvectors> | Independent first-course treatment of the same definition; used as a cross-check, not quoted |
| Official syllabus online references | NPTEL courses | — | <https://nptel.ac.in/courses/111/104/111104085/> | Listed by the syllabus itself as the course's online reference |

Only these sources are cited, and each is cited for a claim it actually supports. No quotation is invented. AI-written material in the guide is limited to explanation and is never attributed to a person.

## 7. What is *not* a source

- The solutions booklet is **not** an authority. It is a student-association document that has already been shown to contain a silent matrix substitution (page 17).
- No past paper other than the two supplied documents is used. No claim is made that any question is "frequently asked".
- No AI-generated question is presented as a bank question.
