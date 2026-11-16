# VERIFICATION REPORT — Part 1 (eigenvalues and eigenvectors)

**Date:** 16 November 2026
**Tool:** Python 3.12, SymPy 1.14.0, exact rational arithmetic (no floating point anywhere).
**Scope:** Module I eigenquestions of the supplied 2026 bank, plus the Winter 2025 practice-paper eigenquestion, plus the two teaching examples used in Part 1.

## 1. Method

1. **Visual read.** Each matrix was rendered at 200 dpi from the original PDF and then re-read from a 300–400 dpi crop of the same region. The crops are `_work/endsem/pages/crop_qb1_q1.png`, `crop_qb1_q1b.png`, `crop_qb1_q2.png`, `crop_qb1_ch34.png`, `crop_pp2_q4b.png`.
2. **Transcription.** The matrix was typed into SymPy exactly as read.
3. **Independent solve.** `charpoly`, `eigenvals`, `nullspace` and `is_diagonalizable` computed by SymPy.
4. **Cross-check.** Sum of eigenvalues against the trace; product against the determinant; every eigenvector substituted back into \(AX=\lambda X\).
5. **Intermediate-step audit.** Every row-reduced matrix printed in the answer key was checked to have the *same null space* as the matrix it replaced (`verify_steps.py`).
6. **Comparison with the supplied booklet.** Its stated eigenvalues and eigenvectors were compared with the independent result.
7. **Limitation.** SymPy proves that the *transcribed* matrix has these eigenvalues. It cannot prove that the scan was read correctly. That is why step 1 exists, and why the doubtful corners were cropped and re-read.

## 2. Results

| ID | Matrix | Characteristic polynomial | \(S_1\) | \(S_2\) | \(\lvert A\rvert\) | Eigenvalues | Diagonalisable | Booklet agrees |
|---|---|---|---|---|---|---|---|---|
| `M1-EV-Q1-i` | \([[2,-1,1],[1,2,-1],[1,-1,2]]\) | \(\lambda^3-6\lambda^2+11\lambda-6=(\lambda-1)(\lambda-2)(\lambda-3)\) | 6 | 11 | 6 | 1, 2, 3 | Yes | Yes |
| `M1-EV-Q1-ii` | \([[2,2,1],[1,3,1],[1,2,2]]\) | \(\lambda^3-7\lambda^2+11\lambda-5=(\lambda-5)(\lambda-1)^2\) | 7 | 11 | 5 | 5, 1, 1 | Yes | Yes |
| `M1-EV-Q1-iii` | \([[2,1,1],[2,3,2],[3,3,4]]\) | \(\lambda^3-9\lambda^2+15\lambda-7=(\lambda-7)(\lambda-1)^2\) | 9 | 15 | 7 | 7, 1, 1 | Yes | Yes |
| `M1-EV-Q1-iv` | \([[6,-2,2],[-2,3,-1],[2,-1,3]]\) | \(\lambda^3-12\lambda^2+36\lambda-32=(\lambda-8)(\lambda-2)^2\) | 12 | 36 | 32 | 8, 2, 2 | Yes | Yes |
| `M1-EV-Q1-v` | \([[8,-6,2],[-6,7,-4],[2,-4,3]]\) | \(\lambda^3-18\lambda^2+45\lambda=\lambda(\lambda-3)(\lambda-15)\) | 18 | 45 | 0 | 15, 3, 0 | Yes | Yes |
| `M1-EV-Q1-vi` | \([[1,0,0],[0,3,-1],[0,-1,3]]\) | \(\lambda^3-7\lambda^2+14\lambda-8=(\lambda-1)(\lambda-2)(\lambda-4)\) | 7 | 14 | 8 | 1, 2, 4 | Yes | Yes |
| `M1-EV-Q1-vii` | \([[-2,2,-3],[2,1,-6],[-1,-2,0]]\) | \(\lambda^3+\lambda^2-21\lambda-45=(\lambda-5)(\lambda+3)^2\) | −1 | −21 | 45 | 5, −3, −3 | Yes | Yes |
| `PP25-Q4-b` | \([[3,-1,1],[-1,5,-1],[1,-1,3]]\) | \(\lambda^3-11\lambda^2+36\lambda-36=(\lambda-2)(\lambda-3)(\lambda-6)\) | 11 | 36 | 36 | 2, 3, 6 | Yes | Not in the bank |

Every eigenvector published in the answer key passed the substitution test; see `scripts/out_part1_vectors.txt` for the full table of \(A v\) values.

**Rank / multiplicity detail for the repeated eigenvalues.** `Q1-ii`, `Q1-iii`, `Q1-iv` and `Q1-vii` each have a repeated eigenvalue with geometric multiplicity 2 (rank of \(A-\lambda I\) equal to 1), so each produced two independent eigenvectors. `Q1-v`'s eigenvalue 0 is simple, not repeated, and came with the single vector \((1,2,2)^T\).

## 3. Errors found and fixed during authoring

Recorded because a report that claims a clean first pass would not be credible.

| # | Where | The error | How it was caught | Fix |
|---|---|---|---|---|
| E1 | Answer key, `M1-EV-Q1-v`, \(\lambda=15\) | The relation between \(x_1,x_2,x_3\) was written wrongly, so the reduced matrix implied a null space different from the original | `verify_steps.py` compared null spaces | Reduced matrix corrected to \([[1,0,-2],[0,1,2]]\), giving \((2,-2,1)^T\) |
| E2 | Answer key, `M1-EV-Q1-v`, \(\lambda=3\) | Reduced matrix printed as \([[1,0,2],[0,1,1]]\), whose null space is not that of \(A-3I\) | `verify_steps.py` | Corrected to \([[1,0,1],[0,1,1/2]]\), giving \((2,1,-2)^T\) |
| E3 | Answer key, `M1-EV-Q1-iv`, \(\lambda=2\) | Two parameter choices were claimed to be proportional when they were not | Recomputed with SymPy | Parameter choices replaced so that the two published vectors are exactly \((1,2,0)^T\) and \((1,0,-2)^T\) |
| E4 | Answer key, `M1-EV-Q1-i` | Determinant of the eigenvector matrix stated as −2 | Recomputed | Stated as −1 |
| E5 | Answer key, `M1-EV-Q1-vii` | \(S_2\) first written as −18 | Recomputed minors | Corrected to −21, and the three minors are now shown individually in the guide |

All five were corrected before publication. The corrected file was re-run through both scripts, and the final line of `scripts/out_part1_steps.txt` reads `ALL INTERMEDIATE-STEP CHECKS PASSED: True`.

## 4. Claims checked in the teaching section

| Claim in the guide | Check |
|---|---|
| \(A=\begin{bmatrix}4&1\\2&3\end{bmatrix}\) has eigenvalues 5 and 2 with \((1,1)^T\) and \((1,-2)^T\) | Verified in `verify_part1_vectors.py` (`TEACH-2x2`) |
| \(A=\begin{bmatrix}0&1&1\\1&0&1\\1&1&0\end{bmatrix}\) has \(\lambda=2\) and \(\lambda=-1\) (twice), the latter with two independent eigenvectors | Verified (`TEACH-3x3`), null spaces checked |
| \(B=\begin{bmatrix}3&1&0\\0&3&0\\0&0&5\end{bmatrix}\) is **not** diagonalisable although \(\lambda=3\) is repeated | Verified: characteristic polynomial \((\lambda-5)(\lambda-3)^2\), rank of \(B-3I\) is 2, geometric multiplicity 1, `is_diagonalizable()` is False |
| A triangular matrix has its diagonal entries as eigenvalues | Standard result, used as a check on `M1-EV-Q1-vi` and `Q2`'s matrices |

## 5. What was **not** verified

- The solutions booklet was read for pages 3–7 in detail only. Pages 8–28 (the rest of Module I) have not been compared yet; that comparison belongs to Parts 2–4.
- Discrepancy **D3** (Cayley–Hamilton, booklet page 17) has been identified from the brief and from the printed matrix in the bank, but the full independent solution has **not** been written yet. It will be investigated and documented in Part 3.
- Discrepancy **D4** (Fourier series, booklet page 70) is untouched.
- The printed polynomial in `M1-CH-Q7` is not yet confirmed character by character (D5); it will be re-read before Part 3.
- No browser test of the *mathematics* is claimed here. Rendering was inspected separately and is reported in the session notes; only what was actually seen is claimed.
