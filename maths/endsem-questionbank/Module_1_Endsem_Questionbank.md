# How to use this Maths Endsem Question Bank

**Mathematics for Computer Engineering (2023111)** · University of Mumbai · B.E. Computer Science and Engineering (Artificial Intelligence and Machine Learning) · Semester III · NEP 2020

This page is a **question-bank companion**, not a replacement for the Module 1 study guide. The study guide teaches the syllabus; this page takes the questions that were actually supplied, teaches the ideas each question needs, and then works every question out in full with independently checked arithmetic.

## What is being covered, and what is not

| Block | Source | Status on this page |
|---|---|---|
| Module I — eigenvalues and eigenvectors | MUSA 2026 bank, page 1, Q.1 (i)–(vii) | **Complete** (Part 1) |
| Module I — eigenvalues of matrix expressions | MUSA 2026 bank, page 1, Q.2 (i)–(ii) | Planned — Part 2 |
| Module I — Cayley–Hamilton theorem | MUSA 2026 bank, pages 1–2, Q.1–Q.8 | Planned — Part 3 |
| Module I — diagonalisation | MUSA 2026 bank, page 2, Q.1–Q.6 | Planned — Part 4 |
| Module II, III, V, VI | MUSA 2026 bank and practice paper | Not started |
| Module IV — Fourier series | Already covered by the existing Module 4 guide | Will be reconciled, not duplicated |

Nothing marked "planned" or "not started" has been written yet. An empty section is never shown as finished, and no progress number on this page is invented.

## The three sources behind every question

| Source | File on the project machine | SHA-256 (verified 16 November 2026) |
|---|---|---|
| MUSA question bank, Winter Session 2026 (9 pages) | `musa-question-bank-2026.pdf` | `1c24161e4d16e5c3624f610e56ee2034a705475b604a2d39f16849eb921a89f2` |
| MUSA solutions booklet (108 pages) | `maths-question-bank-solutions.pdf` | `523d42600fc54da00b87702edd6ea17dafd8469e286046a4e9ee0e7ffcc404c2` |
| MUSA practice paper, Set-I, Winter 2025 (3 pages) | `musa-practice-paper-set1-w2025.pdf` | `17fb8559daa4f7dec2ac625dc2053c56ab691ef7894650707c048f3ee125d404` |

Each hash matches the value already recorded in `maths/Source_Index.md`, so the files processed here are the files the project has been using.

**Which source is the authority for what:**

- **The question bank controls the wording and the numbers.** Every matrix below was read from the scanned page at 200–400 dpi and then compared against a second, enlarged crop. A question is never re-typed from memory or from the solution booklet.
- **The solution booklet is a secondary source.** It is a student-association booklet, and it is treated as a *claim to be checked*, not as an answer key. Its Module I section runs from PDF page 3 to PDF page 28 of the 108-page booklet.
- **Arithmetic is verified independently** with SymPy 1.14 using exact rational arithmetic, and every eigenvector is checked by substitution into \(AX=\lambda X\).

## How to study with this page

1. Read the teaching section for the part you are on (for now: Part 1). Do not skim it — the method it teaches is the method your teacher used.
2. Close the answer key. Attempt the questions in the question section on paper. Give a 3-mark question about 5 minutes and a 5-mark question about 8 minutes.
3. Check your work in the answer key. The key shows the row reduction, not only the final vector, so you can see exactly where a slip happened.
4. If two answers disagree, the answer key wins only after you have checked it yourself by substitution — that check is shown in every solution.

The key is a separate file (`Module_1_Endsem_Answer_Key.md`) and a separate section at the end of this page, so that a question is never answered while you are still reading it.

## Difficulty labels used below

- **Basic** — the idea in its simplest form; expect this as a first step, not as an exam question on its own.
- **Exam-level** — the standard University / question-bank standard for this topic.
- **Challenging** — longer arithmetic, a trap, or a result that needs interpretation.

---

# Part 1 · Learning: eigenvalues and eigenvectors

**Syllabus position.** Module I, prescribed topic 1: "Characteristic Equation, Eigenvalues and Eigenvectors, and properties (without proof)". Module I carries 5 teaching hours and maps to **CO1: Apply the concepts of eigenvalues and eigenvectors in engineering problems.**

**Where the course method comes from.** The teacher's handwritten Module 1 notes (PDF pages 1–11) define the terms, give a seven-step procedure, sort examples into four "types", and list the properties. This part follows that method. Where a second view helps, a human-authored textbook is named and linked.

## 1.1 The idea in one picture

A matrix is not just a table of numbers. Multiplying a matrix by a column vector \(X\) **moves** that vector: it may stretch it, squash it, rotate it, or reflect it. Write the moved vector as \(AX\).

For most vectors the move changes the direction. But for a few special vectors the move only changes the length: the vector stays on its own line through the origin and is simply scaled.

Take
\[A=\begin{bmatrix}4&1\\2&3\end{bmatrix}\]
and two vectors.

\[
A\begin{bmatrix}1\\0\end{bmatrix}=\begin{bmatrix}4\\2\end{bmatrix}
\qquad\text{(direction changed)}
\]

\[
A\begin{bmatrix}1\\1\end{bmatrix}=\begin{bmatrix}5\\5\end{bmatrix}=5\begin{bmatrix}1\\1\end{bmatrix}
\qquad\text{(direction unchanged, length }\times 5\text{)}
\]

The vector \((1,1)\) is special: the matrix produced a multiple of itself. That is an **eigenvector**, and the multiplier \(5\) is its **eigenvalue**. The German word *eigen* means "own" or "characteristic" — these are the matrix's own directions.

> **Human-authored explanation (primary source).** Margalit and Rabinoff, *Interactive Linear Algebra*, Georgia Institute of Technology, §5.1 "Eigenvalues and Eigenvectors" — the geometric picture of a vector that is not moved off its own line, with interactive examples: <https://textbooks.math.gatech.edu/ila/eigenvectors.html>. Licence: GNU Free Documentation License.

## 1.2 The definition, with every symbol explained

> **Definition.** Let \(A\) be an \(n\times n\) matrix. A nonzero column vector \(X\) is an **eigenvector** of \(A\) if there is a scalar \(\lambda\) such that
> \[AX=\lambda X.\]
> That scalar \(\lambda\) is the **eigenvalue** of \(A\) belonging to \(X\).

Reading the symbols one at a time:

- \(A\) — a square matrix, \(n\) rows and \(n\) columns. Eigenvalues are only defined for square matrices.
- \(X\) — a column vector with \(n\) entries \(x_1,\dots,x_n\). It is the "special direction".
- \(\lambda\) — a single number (Greek *lambda*). It may be positive, negative or zero. It is the "stretch factor".
- \(AX=\lambda X\) — the moved vector equals the original vector scaled. No rotation.

**Why \(X\neq 0\) is part of the definition.** If \(X\) were the zero vector then \(A\cdot 0=\lambda\cdot 0\) would be true for *every* number \(\lambda\), so every number would be an eigenvalue of every matrix. The definition excludes zero to make the idea mean something.

**The teacher's terminology.** The notes on PDF page 1 list the alternative names used in Indian textbooks, and the exam may use any of them: characteristic roots, latent roots, characteristic values, eigen values, proper values. All mean the same number. Likewise eigen vector / latent vector.

## 1.3 The characteristic equation

The equation \(AX=\lambda X\) contains the unknown vector \(X\) in two places, which is awkward. Rewrite it so that \(X\) appears only once:

\[
AX-\lambda X=0
\]
\[
(A-\lambda I)X=0
\]

Here \(I\) is the \(n\times n\) identity matrix (1s on the diagonal, 0s elsewhere). It is needed because you cannot subtract a number from a matrix: \(\lambda I\) is the matrix that has \(\lambda\) on its diagonal.

Now \(AX=\lambda X\) has a nonzero solution \(X\) **exactly when** the matrix \((A-\lambda I)\) is singular, i.e. when its determinant is zero. That gives the central equation of the whole module.

> **Definition.** For a square matrix \(A\),
> - \(A-\lambda I\) is the **characteristic matrix**,
> - \(|A-\lambda I|=0\) is the **characteristic equation**,
> - \(|A-\lambda I|\) (expanded) is the **characteristic polynomial**,
> - its roots are the **eigenvalues** of \(A\).

**Degree check.** For an \(n\times n\) matrix the characteristic polynomial has degree \(n\), so a \(3\times3\) matrix has exactly three eigenvalues (counting repeats), and a \(2\times2\) matrix has exactly two.

## 1.4 The teacher's shortcut for a \(3\times3\) matrix

Expanding a \(3\times3\) determinant with \(\lambda\) in it is slow and easy to get wrong. The course uses a formula that skips the expansion. For a \(3\times3\) matrix \(A\),

\[
\lambda^{3}-S_1\lambda^{2}+S_2\lambda-|A|=0
\]

where

- \(S_1=\) **sum of the three diagonal entries** \(=a_{11}+a_{22}+a_{33}\),
- \(S_2=\) **sum of the three principal \(2\times2\) minors**,
- \(|A|=\) the determinant of \(A\).

The three principal minors are the \(2\times2\) determinants you get by deleting one row and the column with the same number:

\[
S_2=\begin{vmatrix}a_{11}&a_{12}\\a_{21}&a_{22}\end{vmatrix}
+\begin{vmatrix}a_{11}&a_{13}\\a_{31}&a_{33}\end{vmatrix}
+\begin{vmatrix}a_{22}&a_{23}\\a_{32}&a_{33}\end{vmatrix}
\]

For a \(2\times2\) matrix the same idea gives

\[
\lambda^{2}-S_1\lambda+|A|=0,\qquad S_1=a_{11}+a_{22}.
\]

This is exactly how the teacher does it on PDF page 2 of the notes; the sequence "\(\lambda^3-S_1\lambda^2+S_2\lambda-|A|=0\)" appears there word for word.

**Two free checks that catch most mistakes.** If the roots are \(\lambda_1,\lambda_2,\lambda_3\), then

\[
\lambda_1+\lambda_2+\lambda_3=S_1,\qquad \lambda_1\lambda_2\lambda_3=|A|.
\]

If your roots do not add up to the trace and multiply to the determinant, the characteristic equation is wrong. Use these checks every time; they cost ten seconds and save whole questions.

## 1.5 The recipe: finding the eigenvectors

Once the eigenvalues are known, each eigenvalue gets its own eigenvector. The teacher's procedure (PDF page 2) has seven steps. Here it is with the reasons attached.

1. **Write \(|A-\lambda I|=0\).** This is the characteristic equation.
2. **Solve it** to get \(\lambda_1,\lambda_2,\lambda_3\). Factor by inspection or by the rational-root test.
3. **Fix one eigenvalue**, say \(\lambda_1\), and write the homogeneous system \((A-\lambda_1 I)X=0\).
4. **Row-reduce** the coefficient matrix to echelon form. Only row operations are allowed: swap rows, multiply a row by a nonzero number, add a multiple of one row to another.
5. **Count the free parameters.** If there are \(n\) unknowns and the reduced matrix has rank \(r\), there are \(n-r\) independent parameters. A \(3\times3\) matrix of rank 2 gives 1 parameter; rank 1 gives 2 parameters, and then that eigenvalue has *two* independent eigenvectors.
6. **Sometimes Cramer's rule is quicker** for a small system — the teacher's note on this step refers to cases where two of the three unknowns are already pinned down.
7. **Read off the eigenvectors.** Set each free parameter to 1 (the others to 0) in turn. Any nonzero multiple of an eigenvector is again an eigenvector, so \((1,2,3)\), \((2,4,6)\) and \((-1,-2,-3)\) are all acceptable answers for the same eigenvalue.

**Why the rank matters.** Step 5 is the part beginners skip. If the reduced matrix is
\[
\begin{bmatrix}1&0&-1\\0&1&2\\0&0&0\end{bmatrix}
\]
then \(r=2\) and \(n-r=1\): the equations give \(x_1=x_3\), \(x_2=-2x_3\), so every eigenvector is a multiple of \((1,-2,1)\). Reporting two "different" vectors here is a mistake — they would be the same direction.

## 1.6 The teacher's four types, and which bank questions they cover

The notes classify every example before solving it (PDF pages 2, 5, 7, 8), because the type tells you what to expect.

| Type | Matrix | Eigenvalues | What to expect | Bank questions in this part |
|---|---|---|---|---|
| I | non-symmetric | all distinct | one eigenvector per eigenvalue; three independent directions | Q1 (i) |
| II | symmetric | all distinct | same as Type I; eigenvectors of a real symmetric matrix are mutually perpendicular | Q1 (v), Q1 (vi), practice-paper Q4 (b) |
| III | non-symmetric | repeated | a repeated value may still give two independent eigenvectors | Q1 (ii), Q1 (iii), Q1 (vii) |
| IV | symmetric | repeated | a repeated value always gives two independent eigenvectors | Q1 (iv) |

"Repeated" means the same number occurs twice among the three eigenvalues. A full treatment of when a matrix can be diagonalised belongs to Part 4; here it is only a label.

## 1.7 Worked example A — a \(2\times2\) matrix, from zero

> **Question.** Find the eigenvalues and eigenvectors of \(A=\begin{bmatrix}4&1\\2&3\end{bmatrix}\).

**Step 1 — characteristic equation.** For a \(2\times2\) matrix, \(|A-\lambda I|=0\) means
\[
\begin{vmatrix}4-\lambda&1\\2&3-\lambda\end{vmatrix}=0.
\]
Expand the \(2\times2\) determinant (multiply the diagonal, subtract the other diagonal):
\[
(4-\lambda)(3-\lambda)-(1)(2)=0
\]
\[
12-4\lambda-3\lambda+\lambda^{2}-2=0
\]
\[
\lambda^{2}-7\lambda+10=0.
\]

**Step 2 — roots.** Factor: two numbers multiplying to \(10\) and adding to \(7\) are \(5\) and \(2\).
\[
(\lambda-5)(\lambda-2)=0\quad\Longrightarrow\quad \lambda_1=5,\ \lambda_2=2.
\]
Check: \(5+2=7=S_1\) (the trace \(4+3=7\)) and \(5\cdot2=10=|A|\) (because \(4\cdot3-1\cdot2=10\)). Both checks pass.

**Step 3 — eigenvector for \(\lambda=5\).** Subtract \(5\) from the diagonal:
\[
A-5I=\begin{bmatrix}-1&1\\2&-2\end{bmatrix},\qquad
\begin{bmatrix}-1&1\\2&-2\end{bmatrix}\begin{bmatrix}x_1\\x_2\end{bmatrix}=\begin{bmatrix}0\\0\end{bmatrix}.
\]
The two rows say \(-x_1+x_2=0\) and \(2x_1-2x_2=0\), which are the same statement: \(x_2=x_1\). Rank \(r=1\), so \(n-r=2-1=1\) parameter. Write \(x_1=t\), then \(x_2=t\):
\[
X_1=t\begin{bmatrix}1\\1\end{bmatrix}.
\]
Choose \(t=1\): \(X_1=(1,1)^T\).

**Step 4 — eigenvector for \(\lambda=2\).**
\[
A-2I=\begin{bmatrix}2&1\\2&1\end{bmatrix},\qquad 2x_1+x_2=0\quad\Longrightarrow\quad x_2=-2x_1.
\]
Again rank 1, one parameter: \(X_2=t(1,-2)^T\). Choose \(t=1\): \(X_2=(1,-2)^T\).

**Step 5 — verify by substitution.** This is not optional; it is the only proof that the answer is right.
\[
A X_1=\begin{bmatrix}4&1\\2&3\end{bmatrix}\begin{bmatrix}1\\1\end{bmatrix}=\begin{bmatrix}5\\5\end{bmatrix}=5X_1\ \checkmark
\]
\[
A X_2=\begin{bmatrix}4&1\\2&3\end{bmatrix}\begin{bmatrix}1\\-2\end{bmatrix}=\begin{bmatrix}4-2\\2-6\end{bmatrix}=\begin{bmatrix}2\\-4\end{bmatrix}=2X_2\ \checkmark
\]

**Answer.** \(\lambda=5\) with eigenvector \((1,1)^T\); \(\lambda=2\) with eigenvector \((1,-2)^T\).

## 1.8 Worked example B — a \(3\times3\) matrix with a repeated eigenvalue

> **Question.** Find the eigenvalues and eigenvectors of
> \[A=\begin{bmatrix}0&1&1\\1&0&1\\1&1&0\end{bmatrix}.\]

**Step 1 — the three numbers for the shortcut.** For this matrix
\[
S_1=0+0+0=0,
\]
\[
S_2=\begin{vmatrix}0&1\\1&0\end{vmatrix}+\begin{vmatrix}0&1\\1&0\end{vmatrix}+\begin{vmatrix}0&1\\1&0\end{vmatrix}=(-1)+(-1)+(-1)=-3,
\]
and the determinant, expanding along the first row,
\[
|A|=0\begin{vmatrix}0&1\\1&0\end{vmatrix}-1\begin{vmatrix}1&1\\1&0\end{vmatrix}+1\begin{vmatrix}1&0\\1&1\end{vmatrix}
=0-1(0-1)+1(1-0)=1+1=2.
\]

**Step 2 — characteristic equation.**
\[
\lambda^{3}-0\cdot\lambda^{2}+(-3)\lambda-2=0
\quad\Longrightarrow\quad
\lambda^{3}-3\lambda-2=0.
\]

**Step 3 — roots.** Try \(\lambda=2\): \(8-6-2=0\), so \((\lambda-2)\) is a factor. Divide:
\[
\lambda^{3}-3\lambda-2=(\lambda-2)(\lambda^{2}+2\lambda+1)=(\lambda-2)(\lambda+1)^{2}.
\]
So \(\lambda=2\) (once) and \(\lambda=-1\) (twice).

Check: \(2+(-1)+(-1)=0=S_1\) ✓ and \(2\cdot(-1)\cdot(-1)=2=|A|\) ✓.

**Step 4 — eigenvector for \(\lambda=2\).** Subtract 2 from the diagonal:
\[
A-2I=\begin{bmatrix}-2&1&1\\1&-2&1\\1&1&-2\end{bmatrix}.
\]
Equations: \(-2x_1+x_2+x_3=0\), \(x_1-2x_2+x_3=0\), \(x_1+x_2-2x_3=0\).

Subtract the second equation from the first: \(-3x_1+3x_2=0\), so \(x_1=x_2\). Put that into the third: \(2x_1-2x_3=0\), so \(x_3=x_1\). All three coordinates are equal; rank \(r=2\), one parameter:
\[
X_3=(1,1,1)^T.
\]

**Step 5 — eigenvectors for \(\lambda=-1\).** Add 1 to the diagonal:
\[
A+I=\begin{bmatrix}1&1&1\\1&1&1\\1&1&1\end{bmatrix}\ \longrightarrow\ \begin{bmatrix}1&1&1\\0&0&0\\0&0&0\end{bmatrix}.
\]
All three rows collapse to the single equation \(x_1+x_2+x_3=0\). Rank \(r=1\), so \(n-r=3-1=2\) parameters — this eigenvalue gets **two** independent eigenvectors.

Solve for \(x_1=-x_2-x_3\), then take the parameters two at a time:

- \(x_2=1,\ x_3=0\Rightarrow x_1=-1\): \(X_1=(-1,1,0)^T\).
- \(x_2=0,\ x_3=1\Rightarrow x_1=-1\): \(X_2=(-1,0,1)^T\).

**Step 6 — verify.**
\[
A X_1=\begin{bmatrix}0+1+0\\-1+0+0\\-1+0+0\end{bmatrix}=\begin{bmatrix}1\\-1\\0\end{bmatrix}=(-1)X_1\ \checkmark
\]
\[
A X_2=\begin{bmatrix}0+0+1\\-1+0+0\\-1+0+0\end{bmatrix}=\begin{bmatrix}1\\0\\-1\end{bmatrix}=(-1)X_2\ \checkmark
\]
\[
A X_3=\begin{bmatrix}0+1+1\\1+0+1\\1+1+0\end{bmatrix}=\begin{bmatrix}2\\2\\2\end{bmatrix}=2X_3\ \checkmark
\]

**Answer.** \(\lambda=2\) with \((1,1,1)^T\); \(\lambda=-1\) (repeated) with \((-1,1,0)^T\) and \((-1,0,1)^T\).

**What this example is really teaching.** A repeated eigenvalue is *not* automatically a problem. Here the rank dropped to 1, which produced two independent eigenvectors — as many as the multiplicity. Later, a matrix such as
\[
B=\begin{bmatrix}3&1&0\\0&3&0\\0&0&5\end{bmatrix}
\]
has \(\lambda=3\) repeated but \(B-3I\) has rank 2, so it yields only one eigenvector for that value. That gap is exactly what "non-diagonalisable" will mean in Part 4 (verified in `_work/endsem`, see the verification report).

## 1.9 Checking an answer in ten seconds

1. **Substitute.** Compute \(AX\) for each vector and see whether it is a multiple of \(X\). If not, the vector is wrong, whatever the algebra looked like.
2. **Add the roots.** They must equal the trace.
3. **Multiply the roots.** They must equal the determinant.
4. **Use the triangular shortcut.** If the matrix is triangular (all entries above or below the diagonal are zero), the eigenvalues are just the diagonal entries — no determinant needed (teacher's note ix, PDF page 10).
5. **Zero determinant.** If \(|A|=0\) then at least one eigenvalue is \(0\) — and a zero eigenvalue is a real answer, not a sign that the question has failed (teacher's note viii).

## 1.10 Common mistakes

| Mistake | What it looks like | The fix |
|---|---|---|
| Sign slip in the expansion | \(\lambda^2-7\lambda-10\) instead of \(+10\) | Check the sum and product of the roots against the trace and determinant |
| Using the wrong \(S_2\) | Summing all nine cofactors instead of the three principal minors | Only the three \(2\times2\) minors on the main diagonal count |
| Forgetting \(X\neq0\) | Writing "the eigenvector is the zero vector" | Every eigenvector is scaled to a nonzero representative |
| Stopping at one parameter | One eigenvector for a repeated eigenvalue that deserves two | Compute \(n-r\); if \(n-r=2\), produce two vectors |
| Reporting dependent vectors as two answers | \((1,1,1)\) and \((2,2,2)\) listed as a pair | They are the same direction; use independent parameters |
| Mixing the two determinant conventions | Starting with \(|\lambda I-A|\) and then quoting \(|A-\lambda I|\) coefficients | Both give the same roots; pick one and stay with it (this page uses \(|A-\lambda I|\)) |
| "Repeated eigenvalue means not diagonalisable" | Rejecting a perfectly diagonalisable matrix | Compare geometric and algebraic multiplicity — Part 4 |
| Arithmetic slip in row reduction | Dividing by a symbol that might be zero | Only divide by numbers you know are nonzero |
| Units of the answer | Giving vectors as rows or as fractions with no common factor | Column vectors, scaled to the smallest integers where convenient |

## 1.11 Which method for which question?

| If the question gives… | Do this |
|---|---|
| a \(2\times2\) matrix | \(\lambda^2-S_1\lambda+\lvert A\rvert=0\), then one row reduction per root |
| a \(3\times3\) matrix with distinct eigenvalues | \(S_1,S_2,\lvert A\rvert\), factor, one row reduction per root |
| a \(3\times3\) matrix with a repeated eigenvalue | Same, then compute \(n-r\) for the repeated value: expect 1 or 2 vectors |
| a triangular matrix | Read the diagonal for the eigenvalues; still do the row reduction for vectors |
| a matrix whose determinant is zero | Expect \(0\) as an eigenvalue; do not "correct" it away |
| an expression such as \(A^2-2A+I\) | Do not compute the matrix product. See Part 2 (eigenvalues of matrix expressions) |

---

# Part 1 · The bank questions

**Source:** `musa-question-bank-2026.pdf`, page 1 of 9, heading "MODULE 1 → Eigen Value and Eigen Vector". Printed numbering is preserved. The bank prints no marks for these questions, so none are invented here.

## Eigen Value and Eigen Vector — Q.1

> **Q.1) Find the eigenvalues and eigenvectors of the following matrix:**

| Internal ID | Printed label | Matrix | Difficulty |
|---|---|---|---|
| `M1-EV-Q1-i` | i) | see below | Basic |
| `M1-EV-Q1-ii` | ii) | see below | Exam-level |
| `M1-EV-Q1-iii` | iii) | see below | Exam-level |
| `M1-EV-Q1-iv` | iv) | see below | Exam-level |
| `M1-EV-Q1-v` | v) | see below | Exam-level |
| `M1-EV-Q1-vi` | v) *(printed a second time)* | see below | Exam-level |
| `M1-EV-Q1-vii` | vii) | see below | Exam-level |

> **Numbering note.** The sheet labels the sixth matrix "v)" a second time; the seventh is "vii)". The duplication is a printing slip in the source, not a merged question. Both matrices are kept, the printed labels are shown as they appear, and each has its own internal ID.

**i)** \(A=\begin{bmatrix}2&-1&1\\1&2&-1\\1&-1&2\end{bmatrix}\)

**ii)** \(A=\begin{bmatrix}2&2&1\\1&3&1\\1&2&2\end{bmatrix}\)

**iii)** \(A=\begin{bmatrix}2&1&1\\2&3&2\\3&3&4\end{bmatrix}\)

**iv)** \(A=\begin{bmatrix}6&-2&2\\-2&3&-1\\2&-1&3\end{bmatrix}\)

**v)** \(A=\begin{bmatrix}8&-6&2\\-6&7&-4\\2&-4&3\end{bmatrix}\)

**vi)** \(A=\begin{bmatrix}1&0&0\\0&3&-1\\0&-1&3\end{bmatrix}\) *(printed as "v)" — second occurrence)*

**vii)** \(A=\begin{bmatrix}-2&2&-3\\2&1&-6\\-1&-2&0\end{bmatrix}\)

## Supplementary — Winter 2025 practice paper

**Source:** `musa-practice-paper-set1-w2025.pdf`, page 2 of 3, Q.4 b). This paper is **not** the 2026 bank and is kept separate. It prints its own marks.

| Internal ID | Question | Marks | Difficulty |
|---|---|---|---|
| `PP25-Q4-b` | Find the eigen values and eigen vectors of \(\begin{bmatrix}3&-1&1\\-1&5&-1\\1&-1&3\end{bmatrix}\) | 5 | Exam-level |

> **Source note on the practice paper.** The printed instructions say "Attempt any three questions from Q.2 to Q.5", but the paper also contains a Q.6, and the official syllabus pattern is three questions answered out of six printed questions with Q.1 compulsory. The paper's own instruction line therefore does not match its contents. This is recorded, not silently corrected. See `PROGRESS.md`.

---

---

*End of Part 1 teaching and questions. The complete worked answers are in `Module_1_Endsem_Answer_Key.md` and in the answer-key section at the end of this page. Parts 2–4 of Module I, and Modules II–VI, are not yet written. See `PROGRESS.md` for the exact next action.*
