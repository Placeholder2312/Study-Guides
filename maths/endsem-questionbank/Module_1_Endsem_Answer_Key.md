**Separate answer key — nothing below this line reveals an answer to a question you have not yet attempted.**

# Part 1 · Answer key

Fully worked answers for every question in Part 1. Each solution shows the characteristic equation, the roots, the row reduction that produces the eigenvectors, and a substitution check. Every number below was recomputed exactly with SymPy; the raw output is in `_work/endsem/out_part1_vectors.txt`.

## `M1-EV-Q1-i` — the teacher's Type I example

\[A=\begin{bmatrix}2&-1&1\\1&2&-1\\1&-1&2\end{bmatrix}\]

**Characteristic equation** (teacher's shortcut, PDF page 2):
\[
S_1=2+2+2=6,\qquad
S_2=(4-1)+(4-1)+(4+1)=3+3+5=11,\qquad
|A|=6
\]
\[
\lambda^{3}-6\lambda^{2}+11\lambda-6=0
\quad\Longrightarrow\quad
(\lambda-1)(\lambda-2)(\lambda-3)=0
\]
Checks: \(1+2+3=6=S_1\) ✓ and \(1\cdot2\cdot3=6=|A|\) ✓.

**Eigenvectors.**

For \(\lambda=1\):
\[
A-I=\begin{bmatrix}1&-1&1\\1&1&-1\\1&-1&1\end{bmatrix}
\ \xrightarrow{R_2-R_1}\
\begin{bmatrix}1&-1&1\\0&2&-2\\0&0&0\end{bmatrix}
\]
\(2x_2-2x_3=0\Rightarrow x_2=x_3\); then \(x_1-x_2+x_3=0\Rightarrow x_1=0\). With \(x_3=t\): \(X_1=(0,1,1)^T\).

For \(\lambda=2\):
\[
A-2I=\begin{bmatrix}0&-1&1\\1&0&-1\\1&-1&0\end{bmatrix}
\ \xrightarrow{}\
\begin{bmatrix}1&0&-1\\0&-1&1\\0&0&0\end{bmatrix}
\]
\(x_1=x_3\) and \(x_2=x_3\). With \(x_3=t\): \(X_2=(1,1,1)^T\).

For \(\lambda=3\):
\[
A-3I=\begin{bmatrix}-1&-1&1\\1&-1&-1\\1&-1&-1\end{bmatrix}
\ \xrightarrow{}\
\begin{bmatrix}1&1&-1\\0&-2&0\\0&0&0\end{bmatrix}
\]
\(x_2=0\), then \(x_1=x_3\). With \(x_3=t\): \(X_3=(1,0,1)^T\).

**Check.** \(A(0,1,1)^T=(0,1,1)^T\) ✓, \(A(1,1,1)^T=(2,2,2)^T\) ✓, \(A(1,0,1)^T=(3,0,3)^T\) ✓.

**Answer.** \(\lambda=1,2,3\) with \(X=(0,1,1)^T,(1,1,1)^T,(1,0,1)^T\). The three vectors are linearly independent (the matrix having them as columns has determinant \(-1\neq0\)).

**Supplied booklet (PDF page 4–5):** checked; same eigenvalues and the same three vectors.

> This question is literally the teacher's worked example (notes PDF pages 2–4). Read those pages if you want to see the identical working in the teacher's hand.

## `M1-EV-Q1-ii`

\[A=\begin{bmatrix}2&2&1\\1&3&1\\1&2&2\end{bmatrix}\]

\[
S_1=2+3+2=7,\quad
S_2=(6-2)+(4-1)+(6-2)=4+3+4=11,\quad
|A|=5
\]
\[
\lambda^{3}-7\lambda^{2}+11\lambda-5=0
\quad\Longrightarrow\quad
(\lambda-5)(\lambda-1)^{2}=0
\]
Check: \(5+1+1=7=S_1\) ✓, \(5\cdot1\cdot1=5=|A|\) ✓.

For \(\lambda=5\):
\[
A-5I=\begin{bmatrix}-3&2&1\\1&-2&1\\1&2&-3\end{bmatrix}
\ \longrightarrow\
\begin{bmatrix}1&-2&1\\0&-4&4\\0&4&-4\end{bmatrix}
\]
\(x_2=x_3\), \(x_1=2x_2-x_3=x_2\): \(X_3=(1,1,1)^T\).

For \(\lambda=1\):
\[
A-I=\begin{bmatrix}1&2&1\\1&2&1\\1&2&1\end{bmatrix}
\ \longrightarrow\
\begin{bmatrix}1&2&1\\0&0&0\\0&0&0\end{bmatrix}
\]
Rank 1, so two parameters. Equation \(x_1+2x_2+x_3=0\):

- \(x_2=1,x_3=0\Rightarrow x_1=-2\): \(X_1=(-2,1,0)^T\);
- \(x_2=0,x_3=1\Rightarrow x_1=-1\): \(X_2=(-1,0,1)^T\).

**Check.** \(A(1,1,1)^T=(5,5,5)^T\) ✓, \(A(-2,1,0)^T=(-2,1,0)^T\) ✓, \(A(-1,0,1)^T=(-1,0,1)^T\) ✓.

**Answer.** \(\lambda=5\): \((1,1,1)^T\); \(\lambda=1\) (repeated): \((-2,1,0)^T\) and \((-1,0,1)^T\).

**Supplied booklet (PDF pages 5–6):** checked; same results (its final-answer box omits the \(\lambda=5\) row, but the working above it gives \((1,1,1)^T\)).

## `M1-EV-Q1-iii`

\[A=\begin{bmatrix}2&1&1\\2&3&2\\3&3&4\end{bmatrix}\]

\[
S_1=2+3+4=9,\quad
S_2=(6-2)+(8-3)+(12-6)=4+5+6=15,\quad
|A|=7
\]
\[
\lambda^{3}-9\lambda^{2}+15\lambda-7=0
\quad\Longrightarrow\quad
(\lambda-7)(\lambda-1)^{2}=0
\]
Check: \(7+1+1=9=S_1\) ✓, \(7\cdot1\cdot1=7=|A|\) ✓.

For \(\lambda=7\):
\[
A-7I=\begin{bmatrix}-5&1&1\\2&-4&2\\3&3&-3\end{bmatrix}
\ \longrightarrow\
\begin{bmatrix}1&0&-1/3\\0&1&-2/3\\0&0&0\end{bmatrix}
\]
so \(x_1=x_3/3\) and \(x_2=2x_3/3\). With \(x_3=3t\): \(X_3=(1,2,3)^T\).

For \(\lambda=1\):
\[
A-I=\begin{bmatrix}1&1&1\\2&2&2\\3&3&3\end{bmatrix}
\ \longrightarrow\
\begin{bmatrix}1&1&1\\0&0&0\\0&0&0\end{bmatrix}
\]
Equation \(x_1+x_2+x_3=0\), two parameters:

- \(x_2=1,x_3=0\): \(X_1=(-1,1,0)^T\);
- \(x_2=0,x_3=1\): \(X_2=(-1,0,1)^T\).

**Check.** \(A(1,2,3)^T=(7,14,21)^T\) ✓, \(A(-1,1,0)^T=(-1,1,0)^T\) ✓, \(A(-1,0,1)^T=(-1,0,1)^T\) ✓.

**Answer.** \(\lambda=7\): \((1,2,3)^T\); \(\lambda=1\) (repeated): \((-1,1,0)^T\) and \((-1,0,1)^T\).

**Supplied booklet:** checked; same results.

## `M1-EV-Q1-iv`

\[A=\begin{bmatrix}6&-2&2\\-2&3&-1\\2&-1&3\end{bmatrix}\]

\[
S_1=6+3+3=12,\quad
S_2=(18-4)+(18-4)+(9-1)=14+14+8=36,\quad
|A|=32
\]
\[
\lambda^{3}-12\lambda^{2}+36\lambda-32=0
\quad\Longrightarrow\quad
(\lambda-8)(\lambda-2)^{2}=0
\]
Check: \(8+2+2=12=S_1\) ✓, \(8\cdot2\cdot2=32=|A|\) ✓.

For \(\lambda=8\):
\[
A-8I=\begin{bmatrix}-2&-2&2\\-2&-5&-1\\2&-1&-5\end{bmatrix}
\ \longrightarrow\
\begin{bmatrix}1&1&-1\\0&-3&-3\\0&0&0\end{bmatrix}
\]
\(x_2=-x_3\), \(x_1=-x_2+x_3=2x_3\): \(X_3=(2,-1,1)^T\).

For \(\lambda=2\):
\[
A-2I=\begin{bmatrix}4&-2&2\\-2&1&-1\\2&-1&1\end{bmatrix}
\ \longrightarrow\
\begin{bmatrix}2&-1&1\\0&0&0\\0&0&0\end{bmatrix}
\]
Rank 1, two parameters, equation \(2x_1-x_2+x_3=0\):

- \(x_1=1,\ x_2=2\Rightarrow x_3=0\): \(X_1=(1,2,0)^T\);
- \(x_1=1,\ x_2=0\Rightarrow x_3=-2\): \(X_2=(1,0,-2)^T\).

**Check.** \(A(2,-1,1)^T=(16,-8,8)^T\) ✓, \(A(1,2,0)^T=(2,4,0)^T\) ✓, \(A(1,0,-2)^T=(2,0,-4)^T\) ✓.

**Answer.** \(\lambda=8\): \((2,-1,1)^T\); \(\lambda=2\) (repeated): \((1,2,0)^T\) and \((1,0,-2)^T\).

**Supplied booklet:** checked; same results.

## `M1-EV-Q1-v` — the teacher's Type II example

\[A=\begin{bmatrix}8&-6&2\\-6&7&-4\\2&-4&3\end{bmatrix}\]

\[
S_1=8+7+3=18,\quad
S_2=(56-36)+(24-4)+(21-16)=20+20+5=45,\quad
|A|=0
\]
\[
\lambda^{3}-18\lambda^{2}+45\lambda-0=0
\quad\Longrightarrow\quad
\lambda(\lambda-3)(\lambda-15)=0
\]
Check: \(0+3+15=18=S_1\) ✓, \(0\cdot3\cdot15=0=|A|\) ✓. A zero eigenvalue is expected here precisely because \(|A|=0\).

For \(\lambda=15\):
\[
A-15I=\begin{bmatrix}-7&-6&2\\-6&-8&-4\\2&-4&-12\end{bmatrix}
\ \longrightarrow\
\begin{bmatrix}1&0&-2\\0&1&2\\0&0&0\end{bmatrix}
\]
\(x_1=2x_3\) and \(x_2=-2x_3\): with \(x_3=1\), \(X_3=(2,-2,1)^T\).

For \(\lambda=3\):
\[
A-3I=\begin{bmatrix}5&-6&2\\-6&4&-4\\2&-4&0\end{bmatrix}
\ \longrightarrow\
\begin{bmatrix}1&0&1\\0&1&1/2\\0&0&0\end{bmatrix}
\]
\(x_1=-x_3\) and \(x_2=-\tfrac12x_3\): with \(x_3=-2\), \(X_2=(2,1,-2)^T\).

For \(\lambda=0\):
\[
A-0I=A=\begin{bmatrix}8&-6&2\\-6&7&-4\\2&-4&3\end{bmatrix}
\ \longrightarrow\
\begin{bmatrix}1&0&-1/2\\0&1&-1\\0&0&0\end{bmatrix}
\]
\(x_1=x_3/2\), \(x_2=x_3\): \(X_1=(1,2,2)^T\).

**Check.** \(A(2,-2,1)^T=(30,-30,15)^T\) ✓, \(A(2,1,-2)^T=(6,3,-6)^T\) ✓, \(A(1,2,2)^T=(0,0,0)^T\) ✓.

**Answer.** \(\lambda=15\): \((2,-2,1)^T\); \(\lambda=3\): \((2,1,-2)^T\); \(\lambda=0\): \((1,2,2)^T\).

**Supplied booklet:** checked; same results.

## `M1-EV-Q1-vi` (printed as "v)" a second time)

\[A=\begin{bmatrix}1&0&0\\0&3&-1\\0&-1&3\end{bmatrix}\]

This matrix is block-triangular, so its first eigenvalue is visible immediately: the first row has a single 1 on the diagonal.

\[
S_1=1+3+3=7,\quad
S_2=(3-0)+(3-0)+(9-1)=3+3+8=14,\quad
|A|=1\cdot(9-1)=8
\]
\[
\lambda^{3}-7\lambda^{2}+14\lambda-8=0
\quad\Longrightarrow\quad
(\lambda-1)(\lambda-2)(\lambda-4)=0
\]
Check: \(1+2+4=7=S_1\) ✓, \(1\cdot2\cdot4=8=|A|\) ✓.

For \(\lambda=1\): \(A-I=\begin{bmatrix}0&0&0\\0&2&-1\\0&-1&2\end{bmatrix}\). The first row vanishes, so \(x_1\) is free; the other two rows force \(2x_2-x_3=0\) and \(-x_2+2x_3=0\), whose only solution is \(x_2=x_3=0\). Hence \(X_1=(1,0,0)^T\).

For \(\lambda=2\): \(A-2I=\begin{bmatrix}-1&0&0\\0&1&-1\\0&-1&1\end{bmatrix}\) gives \(x_1=0\) and \(x_2=x_3\), so \(X_2=(0,1,1)^T\).

For \(\lambda=4\): \(A-4I=\begin{bmatrix}-3&0&0\\0&-1&-1\\0&-1&-1\end{bmatrix}\) gives \(x_1=0\) and \(x_2=-x_3\), so \(X_3=(0,1,-1)^T\).

**Check.** \(A(1,0,0)^T=(1,0,0)^T\) ✓, \(A(0,1,1)^T=(0,2,2)^T\) ✓, \(A(0,1,-1)^T=(0,4,-4)^T\) ✓.

**Answer.** \(\lambda=1,2,4\) with \((1,0,0)^T,(0,1,1)^T,(0,1,-1)^T\).

**Supplied booklet:** checked; same results (it writes the third vector as \((0,1,-1)^T\), the negative of the one here — the same direction, so the same eigenvector).

## `M1-EV-Q1-vii`

\[A=\begin{bmatrix}-2&2&-3\\2&1&-6\\-1&-2&0\end{bmatrix}\]

\[
S_1=-2+1+0=-1
\]

> **Careful with this one.** The three principal minors are
> \(\begin{vmatrix}-2&2\\2&1\end{vmatrix}=-2-4=-6\),
> \(\begin{vmatrix}-2&-3\\-1&0\end{vmatrix}=0-3=-3\),
> \(\begin{vmatrix}1&-6\\-2&0\end{vmatrix}=0-12=-12\).
> So \(S_2=-6-3-12=-21\). Mis-pairing the minors here is the classic slip in this question.

\[
|A|=-2(0-12)-2(0-6)+(-3)(-4+1)=24+12+9=45
\]
\[
\lambda^{3}+\lambda^{2}-21\lambda-45=0
\quad\Longrightarrow\quad
(\lambda-5)(\lambda+3)^{2}=0
\]
Check: \(5-3-3=-1=S_1\) ✓, \(5\cdot(-3)\cdot(-3)=45=|A|\) ✓.

For \(\lambda=5\):
\[
A-5I=\begin{bmatrix}-7&2&-3\\2&-4&-6\\-1&-2&-5\end{bmatrix}
\ \longrightarrow\
\begin{bmatrix}1&0&1\\0&1&2\\0&0&0\end{bmatrix}
\]
\(x_1=-x_3\), \(x_2=-2x_3\): with \(x_3=-1\), \(X_3=(1,2,-1)^T\).

For \(\lambda=-3\):
\[
A+3I=\begin{bmatrix}1&2&-3\\2&4&-6\\-1&-2&3\end{bmatrix}
\ \longrightarrow\
\begin{bmatrix}1&2&-3\\0&0&0\\0&0&0\end{bmatrix}
\]
Equation \(x_1+2x_2-3x_3=0\), two parameters:

- \(x_2=1,x_3=0\Rightarrow x_1=-2\): \(X_1=(-2,1,0)^T\);
- \(x_2=0,x_3=1\Rightarrow x_1=3\): \(X_2=(3,0,1)^T\).

**Check.** \(A(1,2,-1)^T=(5,10,-5)^T\) ✓, \(A(-2,1,0)^T=(6,-3,0)^T=-3(-2,1,0)^T\) ✓, \(A(3,0,1)^T=(-9,0,-3)^T=-3(3,0,1)^T\) ✓.

**Answer.** \(\lambda=5\): \((1,2,-1)^T\); \(\lambda=-3\) (repeated): \((-2,1,0)^T\) and \((3,0,1)^T\).

**Supplied booklet:** checked; same results.

## `PP25-Q4-b` — supplementary, Winter 2025 practice paper Q.4 b) [5 marks]

\[A=\begin{bmatrix}3&-1&1\\-1&5&-1\\1&-1&3\end{bmatrix}\]

\[
S_1=3+5+3=11,\quad
S_2=(15-1)+(9-1)+(15-1)=14+8+14=36,\quad
|A|=36
\]
\[
\lambda^{3}-11\lambda^{2}+36\lambda-36=0
\quad\Longrightarrow\quad
(\lambda-2)(\lambda-3)(\lambda-6)=0
\]
Check: \(2+3+6=11=S_1\) ✓, \(2\cdot3\cdot6=36=|A|\) ✓.

For \(\lambda=2\):
\[
A-2I=\begin{bmatrix}1&-1&1\\-1&3&-1\\1&-1&1\end{bmatrix}
\ \longrightarrow\
\begin{bmatrix}1&-1&1\\0&2&0\\0&0&0\end{bmatrix}
\]
\(x_2=0\), \(x_1=-x_3\): \(X_1=(1,0,-1)^T\), equivalently \((-1,0,1)^T\).

For \(\lambda=3\):
\[
A-3I=\begin{bmatrix}0&-1&1\\-1&2&-1\\1&-1&0\end{bmatrix}
\ \longrightarrow\
\begin{bmatrix}1&0&-1\\0&1&-1\\0&0&0\end{bmatrix}
\]
\(x_1=x_3\), \(x_2=x_3\): \(X_2=(1,1,1)^T\).

For \(\lambda=6\):
\[
A-6I=\begin{bmatrix}-3&-1&1\\-1&-1&-1\\1&-1&-3\end{bmatrix}
\ \longrightarrow\
\begin{bmatrix}1&0&-1\\0&1&2\\0&0&0\end{bmatrix}
\]
\(x_1=x_3\), \(x_2=-2x_3\): \(X_3=(1,-2,1)^T\).

**Check.** \(A(1,0,-1)^T=(2,0,-2)^T\) ✓, \(A(1,1,1)^T=(3,3,3)^T\) ✓, \(A(1,-2,1)^T=(6,-12,6)^T\) ✓.

**Answer.** \(\lambda=2\): \((-1,0,1)^T\); \(\lambda=3\): \((1,1,1)^T\); \(\lambda=6\): \((1,-2,1)^T\).

**Supplied booklet:** this question is not in the 2026 bank, so the booklet (which follows the bank) does not cover it. Solved and verified independently here.

---

*End of Part 1. Parts 2–4 of Module I, and Modules II–VI, are not yet written. See `PROGRESS.md` for the exact next action.*
