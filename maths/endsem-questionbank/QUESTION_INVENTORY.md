# QUESTION INVENTORY — Module I, supplied question bank

Complete inventory of the Module I questions in the two supplied question documents. Nothing here is merged, renumbered or paraphrased: the printed numbering is kept, a stable internal ID is added, and the original PDF page is recorded.

**Primary source:** `musa-question-bank-2026.pdf` — MUSA (Mumbai University Students Association), "Question Bank of Mathematics for Computer Engineering", S.E. Sem-III, NEP 2020, Winter Session 2026, branches COMPS/AIML/AIDS/IOT/CS/DS, batch Regular & KT. Nine pages.
**Supplementary source:** `musa-practice-paper-set1-w2025.pdf` — "Practice Paper Set-I", Winter Session 2025, 2 hours, 60 marks, three pages.

Marks: the 2026 bank prints **no marks** for its questions. The practice paper prints marks for some parts. No mark has been invented.

---

## 1. Eigenvalues and eigenvectors (bank page 1)

Heading as printed: **"Eigen Value and Eigen Vector"**.

| ID | Printed | Matrix | Type (teacher's classification) | Part | Status |
|---|---|---|---|---|---|
| `M1-EV-Q1-i` | Q.1 i) | \(\begin{bmatrix}2&-1&1\\1&2&-1\\1&-1&2\end{bmatrix}\) | I (non-symmetric, distinct) | 1 | Done |
| `M1-EV-Q1-ii` | Q.1 ii) | \(\begin{bmatrix}2&2&1\\1&3&1\\1&2&2\end{bmatrix}\) | III (non-symmetric, repeated) | 1 | Done |
| `M1-EV-Q1-iii` | Q.1 iii) | \(\begin{bmatrix}2&1&1\\2&3&2\\3&3&4\end{bmatrix}\) | III | 1 | Done |
| `M1-EV-Q1-iv` | Q.1 iv) | \(\begin{bmatrix}6&-2&2\\-2&3&-1\\2&-1&3\end{bmatrix}\) | IV (symmetric, repeated) | 1 | Done |
| `M1-EV-Q1-v` | Q.1 v) | \(\begin{bmatrix}8&-6&2\\-6&7&-4\\2&-4&3\end{bmatrix}\) | II (symmetric, distinct) | 1 | Done |
| `M1-EV-Q1-vi` | Q.1 v) *printed twice* | \(\begin{bmatrix}1&0&0\\0&3&-1\\0&-1&3\end{bmatrix}\) | II | 1 | Done |
| `M1-EV-Q1-vii` | Q.1 vii) | \(\begin{bmatrix}-2&2&-3\\2&1&-6\\-1&-2&0\end{bmatrix}\) | III | 1 | Done |

**D1 (source issue):** the sixth matrix is labelled `v)` a second time. Both matrices are kept.

## 2. Eigenvalues of matrix expressions (bank page 1)

Heading as printed: **"Q.2) Find the Eigen values the following:"** *[as written — the word "of" is missing in the source]*

| ID | Printed | Question | Part | Status |
|---|---|---|---|---|
| `M1-EV-Q2-i` | Q.2 i) | Find the eigenvalues of \(A^3+5A+8I\) if \(A=\begin{bmatrix}-1&2&3\\0&3&5\\0&0&-2\end{bmatrix}\) | 2 | Outstanding |
| `M1-EV-Q2-ii` | Q.2 ii) | Find the eigenvalues of \(A^2-2A+I\) if \(A=\begin{bmatrix}2&3&4\\0&4&2\\0&0&3\end{bmatrix}\) | 2 | Outstanding |

## 3. Cayley–Hamilton theorem (bank pages 1–2)

Heading as printed: **"Cayley Hamilton Theorem"**.

| ID | Printed | Question (as printed, condensed) | Matrix | Part | Status |
|---|---|---|---|---|---|
| `M1-CH-Q1` | Q.1 | Verify Cayley–Hamilton for \(A\) and hence find \(A^{-1}, A^{-2}, A^{4}\). "Prove that \(A^{-1}=A^2-5A+9I\)." | \(\begin{bmatrix}1&2&-2\\-1&3&0\\0&-2&1\end{bmatrix}\) | 3 | Outstanding |
| `M1-CH-Q2` | Q.2 | Find the characteristic equation and verify it is satisfied by \(A\); hence obtain \(A^{-1}\). | \(\begin{bmatrix}2&-1&1\\-1&2&-1\\1&-1&2\end{bmatrix}\) | 3 | Outstanding |
| `M1-CH-Q3` | Q.3 | Use Cayley–Hamilton to find \(2A^4-5A^3-7A+6I\). | \(\begin{bmatrix}1&2\\2&2\end{bmatrix}\) | 3 | Outstanding |
| `M1-CH-Q4` | Q.4 | Apply Cayley–Hamilton and deduce \(A^8=625I\). | \(\begin{bmatrix}1&2\\2&2\end{bmatrix}\) | 3 | Outstanding — see D3 |
| `M1-CH-Q5` | Q.5 | Find the characteristic equation, verify Cayley–Hamilton, hence find \(A^{-1}\) and \(A^4\). | \(\begin{bmatrix}2&0&-1\\0&2&0\\-1&0&2\end{bmatrix}\) | 3 | Outstanding |
| `M1-CH-Q6` | Q.6 | Verify \(A\) satisfies its characteristic equation; hence find \(A^{-2}\). | \(\begin{bmatrix}1&2&0\\2&-1&0\\0&0&-1\end{bmatrix}\) | 3 | Outstanding |
| `M1-CH-Q7` | Q.7 | Find the characteristic equation and the matrix represented by the given polynomial in \(A\). | \(\begin{bmatrix}2&1&1\\0&1&0\\1&1&2\end{bmatrix}\) (printed at the top of page 2) | 3 | Outstanding — see D5 |
| `M1-CH-Q8` | Q.8 | Find the characteristic equation, show \(A\) satisfies it, hence find (a) \(A^{-1}\), (b) \(A^{-2}\), (c) \(A^4\). | \(\begin{bmatrix}1&2&3\\2&-1&4\\3&1&-1\end{bmatrix}\) | 3 | Outstanding |

**D3:** the printed matrix in Q.4 is \(\begin{bmatrix}1&2\\2&2\end{bmatrix}\) and it does **not** satisfy \(A^8=625I\); the solutions booklet silently substitutes \(\begin{bmatrix}1&2\\2&-1\end{bmatrix}\). To be documented fully in Part 3.

**D5:** the polynomial printed in Q.7 looks like \(A^8-6A^5+7A^6-3A^5+A^4-5A^3+8A^2-2A+I\), with a repeated \(A^5\) term and unusual ordering. It must be re-read from an enlarged crop before Part 3; do not trust this line yet.

## 4. Diagonalisation (bank page 2)

Heading as printed: **"Diagonalizable"**.

| ID | Printed | Question | Matrix | Part | Status |
|---|---|---|---|---|---|
| `M1-DIAG-Q1` | Q.1 | Show \(A\) is diagonalisable; find the diagonal form \(D\) and the diagonalising matrix \(M\). | \(\begin{bmatrix}-9&4&4\\-8&3&4\\-16&8&7\end{bmatrix}\) | 4 | Outstanding |
| `M1-DIAG-Q2` | Q.2 | Show \(A\) is diagonalisable; find the transforming matrix and the diagonal matrix. | \(\begin{bmatrix}8&-6&2\\-6&7&-4\\2&-4&3\end{bmatrix}\) | 4 | Outstanding |
| `M1-DIAG-Q3-i` | Q.3 i) | Show the matrix is similar to a diagonal matrix; find the diagonal form and the diagonalising matrix. | \(\begin{bmatrix}4&2&-2\\-5&3&2\\-2&4&1\end{bmatrix}\) | 4 | Outstanding |
| `M1-DIAG-Q3-ii` | Q.3 ii) | Same instruction. | \(\begin{bmatrix}-2&2&-3\\2&1&-6\\-1&-2&0\end{bmatrix}\) | 4 | Outstanding |
| `M1-DIAG-Q4` | Q.4 | Show \(A\) is diagonalisable; find the transforming matrix and the diagonal matrix. | \(\begin{bmatrix}8&-8&-2\\4&-3&-2\\3&-4&1\end{bmatrix}\) | 4 | Outstanding |
| `M1-DIAG-Q5` | Q.5 | Show \(A\) is diagonalisable; find the transforming matrix and the diagonal matrix. | \(\begin{bmatrix}2&1&1\\1&2&1\\0&0&1\end{bmatrix}\) | 4 | Outstanding |
| `M1-DIAG-Q6` | Q.6 | Show \(A\) is diagonalisable; find the transforming matrix and the diagonal matrix. | \(\begin{bmatrix}2&2&1\\1&3&1\\1&2&2\end{bmatrix}\) | 4 | Outstanding |

Count: 7 diagonalisation items across 6 printed questions, because Q.3 has two matrices.

## 5. Supplementary — Winter 2025 practice paper (Module I only)

These are **not** part of the 2026 bank and are kept in a separate section of the guide.

| ID | Printed | Question | Marks | Part | Status |
|---|---|---|---|---|---|
| `PP25-Q1-a` | Q.1 a) | If \(A=\begin{bmatrix}2&3&4\\0&4&2\\0&0&3\end{bmatrix}\), find the eigenvalues of \(A^2-2A+I\). | 3 | 2 | Outstanding |
| `PP25-Q1-a-OR` | Q.1 a) OR | If \(A=\begin{bmatrix}2&4\\0&3\end{bmatrix}\), find the eigenvalues of \(6A^{-1}+A^3+2I\). | 3 (printed once for the pair) | 2 | Outstanding |
| `PP25-Q2-a` | Q.2 a) | Use Cayley–Hamilton to find \(2A^4-5A^3-7A+6I\) where \(A=\begin{bmatrix}1&2\\2&2\end{bmatrix}\). | 4 | 3 | Outstanding |
| `PP25-Q2-a-OR` | Q.2 a) OR | Verify Cayley–Hamilton for \(A=\begin{bmatrix}1&2&-2\\-1&3&0\\0&-2&1\end{bmatrix}\) and hence find \(A^{-1}, A^{-2}\). | (continuation of the 4) | 3 | Outstanding |
| `PP25-Q4-b` | Q.4 b) | Find the eigen values and eigen vectors of \(\begin{bmatrix}3&-1&1\\-1&5&-1\\1&-1&3\end{bmatrix}\). | 5 | 1 | **Done** |
| `PP25-Q5-c` | Q.5 c) | Show \(A=\begin{bmatrix}-9&4&4\\-8&3&4\\-16&8&7\end{bmatrix}\) is diagonalisable; find \(D\) and \(M\). | 6 | 4 | Outstanding |
| `PP25-Q5-c-OR` | Q.5 c) OR | Show \(A=\begin{bmatrix}8&-6&2\\-6&7&-4\\2&-4&3\end{bmatrix}\) is diagonalisable; find the transforming and diagonal matrices. | not printed separately | 4 | Outstanding |

**D2 (source issue):** the practice paper's instructions say "Attempt any three questions from Q.2 to Q.5", but the paper contains a Q.6 as well. The official University pattern is six printed questions with Q.1 compulsory and three answers required. Recorded, not silently corrected.

## 6. Totals

| Block | Items |
|---|---|
| Eigenvalues and eigenvectors (bank) | 7 |
| Eigenvalues of expressions (bank) | 2 |
| Cayley–Hamilton (bank) | 8 |
| Diagonalisation (bank) | 7 |
| **Bank total** | **24** |
| Supplementary practice paper (Module I) | 7 |
| **Grand total** | **31** |
| Done (Part 1) | 8 |
