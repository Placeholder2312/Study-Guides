# Module 1 — Linear Algebra (Theory of Matrices)

**Transcription of:** `01_Original_Notes/Module_1/CSE Module 1.pdf`
**Document type:** Handwritten teacher notes, 20 scanned pages (Adobe Scan for iOS)
**Subject:** Mathematics for Computer Engineering (2023111) — B.E. CSE (AI & ML), Semester III
**Transcription status:** Complete — all 20 PDF pages transcribed.

---

## Transcription conventions

- This is a **faithful transcription**, not a study guide. The teacher's order, wording, examples and working are preserved.
- Each section is tied to its original **PDF page number**.
- `λ` is used for the eigenvalue symbol (the handwriting uses a stylised `λ`, sometimes resembling `d`).
- Matrices are reproduced with their exact entries and dimensions.
- Handwriting that is genuinely ambiguous is marked `[UNCLEAR — PDF PAGE X]`.
- The teacher's own numerical or notational slips are **reproduced as written** and tagged `[as written]`, with an explanation in a **Transcription note** at the end of that page. They are never silently corrected.
- Editorial insertions needed to make the page readable (for example, a missing bracket) are placed in square brackets `[...]`.

---

## Page 1 — Module heading, prescribed topics and basic definitions

**Source: PDF page 1**

# Module 1
## CSE (AIML)
## Linear Algebra (Theory of Matrices)

1. Characteristic Equation, Eigenvalues and Eigenvectors and properties (without proof)
2. Cayley–Hamilton Theorem (without proof), verification and reduction of higher degree polynomials.
3. Similarity of matrices, diagonalizable and non-diagonalizable matrices.

### Characteristic Equation:

If \(A\) is any \(n \times n\) square matrix, then \(A-\lambda I\) is called the characteristic matrix, where \(\lambda\) is scalar and \(I\) is unit matrix of order \(n\).

\[
|A-\lambda I| = 0
\]

is characteristic equation of \(A\).

### Eigen values:

The roots of the characteristic equation are called the characteristic roots or latent roots or characteristic values or eigen values or proper values of the matrix \(A\).

### Eigen vectors:

Suppose \(|A-\lambda I|=0\), we find a non-zero vector column matrix \(X\) such that

\[
[A-\lambda I]X = 0,
\]

the vector \(X\) is called eigen vector or latent vector corresponding to \(\lambda\).

**Sum of the Eigen values:**

\[
\lambda_1+\lambda_2+\lambda_3 = \text{sum of the diagonal elements.}
\]

**Product of eigen values:**

\[
\lambda_1\cdot\lambda_2\cdot\lambda_3 = |A|.
\]

---

## Page 2 — Procedure; Type I (non-symmetric, distinct eigenvalues); first example

**Source: PDF page 2**

### Procedure to find Eigen values and Eigen vectors

1. First write \(|A-\lambda I|=0\).
2. Solve above equations and find the roots say \(\lambda_1,\lambda_2,\lambda_3\).
3. For \(\lambda=\lambda_1\), consider the matrix equality \([A-\lambda_1 I]x=0\).
4. Apply elementary row transformations and reduce the above matrix to echelon form.
5. Now write equations. If there are \(n\) unknowns and the rank of the matrix is \(r\), then there will be \((n-r)\) independent parameters.
6. Some times we will require to use Cramer's rule.
7. Solve equations and get the eigen vectors \(x_1,x_2,\ldots\)

### Type I

If \(A\) is non-symmetric matrix and eigen values are distinct.

**Q.** Find eigen values and eigen vectors of the following matrix [verify that the eigen vectors are linearly independent]

\[
A=\begin{bmatrix}
2 & -1 & 1\\
1 & 2 & -1\\
1 & -1 & 2
\end{bmatrix}
\]

**Sol.** The characteristic equation is

\[
|A-\lambda I|=0 \quad \text{gives}
\]

\[
\begin{vmatrix}
2-\lambda & -1 & 1\\
1 & 2-\lambda & -1\\
1 & -1 & 2-\lambda
\end{vmatrix}=0
\]

or

\[
\lambda^3-S_1\lambda^2+S_2\lambda-|A|=0
\]

\[
S_1=2+2+2=6
\]

\[
S_2=
\begin{vmatrix}2&-1\\-1&2\end{vmatrix}
+
\begin{vmatrix}2&1\\1&2\end{vmatrix}
+
\begin{vmatrix}2&-1\\1&2\end{vmatrix}
\]

\[
=(4-1)+(4-1)+(4+1)=11
\]

\[
|A|=2(3)+1(3)+1(-3)=6
\]

\(\therefore\) characteristic equation is

\[
\lambda^3-6\lambda^2+11\lambda-6=0
\qquad \therefore \lambda=1,2,3
\]

---

## Page 3 — Example continued: \(\lambda=1\) and \(\lambda=2\)

**Source: PDF page 3**

**i) For \(\lambda=1\),** \([A-\lambda_1 I]x=0\) gives

\[
\begin{bmatrix}
1&-1&1\\
1&1&-1\\
1&-1&1
\end{bmatrix}
\begin{bmatrix}x_1\\x_2\\x_3\end{bmatrix}
=
\begin{bmatrix}0\\0\\0\end{bmatrix}
\]

\[
x_1-x_2+x_3=0
\]
\[
x_1+x_2-x_3=0
\]
\[
x_1-x_2+x_3=0
\]

Solving by Cramer's rule,

\[
\frac{x_1}{\begin{vmatrix}-1&1\\1&-1\end{vmatrix}}
=
\frac{-x_2}{\begin{vmatrix}1&1\\1&-1\end{vmatrix}}
=
\frac{x_3}{\begin{vmatrix}1&-1\\1&1\end{vmatrix}}
\]

or

\[
\frac{x_1}{0}=\frac{x_2}{-2}=\frac{x_3}{2}
\]

i.e. \(x_1=0,\ x_2=2,\ x_3=2\).

Hence corresponding eigen value \(1\), we get eigen vector

\[
\begin{bmatrix}0\\2\\2\end{bmatrix}
=2\begin{bmatrix}0\\1\\1\end{bmatrix}
\quad \text{or} \quad
\begin{bmatrix}0\\1\\1\end{bmatrix}
\quad \text{or} \quad
[0\ 1\ 1]'
\]

**ii) For \(\lambda=2\),** \([A-\lambda_2 I]x=0\) gives

\[
\begin{bmatrix}
0&-1&1\\
1&0&-1\\
1&-1&0
\end{bmatrix}
\begin{bmatrix}x_1\\x_2\\x_3\end{bmatrix}
=
\begin{bmatrix}0\\0\\0\end{bmatrix}
\]

\[
\begin{aligned}
-x_2+x_3&=0 &\text{or}\quad 0x_1-x_2+x_3&=0\\
x_1-x_3&=0 &\text{or}\quad x_1+0x_2-x_3&=0\\
x_1-x_2&=0 &\text{or}\quad x_1-x_2+0x_3&=0
\end{aligned}
\]

By Cramer's rule,

\[
\frac{x_1}{\begin{vmatrix}-1&1\\0&-1\end{vmatrix}}
=
\frac{-x_2}{\begin{vmatrix}0&1\\1&-1\end{vmatrix}}
=
\frac{x_3}{\begin{vmatrix}0&-1\\1&0\end{vmatrix}}
\]

or

\[
\frac{x_1}{1}=\frac{-x_2}{-1}=\frac{x_3}{1}
\]

or

\[
\frac{x_1}{1}=\frac{x_2}{1}=\frac{x_3}{1}
\]

\(\therefore\) Eigen vector

\[
[1\ 1\ 1]'
\quad \text{or} \quad
\begin{bmatrix}1\\1\\1\end{bmatrix}
\]

> **Transcription note (PDF page 3).** In the “or” line the teacher writes \(x_2/(-2)\) although the determinant immediately above it is \(-2\) and the numerator is \(-x_2\). As written the line reads \(x_1/0=x_2/(-2)=x_3/2\), which would give \(x_2=-x_3\); the very next line nevertheless states \(x_1=0,\ x_2=2,\ x_3=2\). The final eigenvector \([0,1,1]^T\) is correct for \(\lambda=1\). This is reproduced without correction.

---

## Page 4 — Example continued: \(\lambda=3\), eigenvector list and linear independence

**Source: PDF page 4**

**iii) For \(\lambda=3\),**

\[
[A-\lambda_3 I]x=0 \quad \text{gives}
\]

\[
\begin{bmatrix}
-1&-1&1\\
1&-1&-1\\
1&-1&-1
\end{bmatrix}
\begin{bmatrix}x_1\\x_2\\x_3\end{bmatrix}
=
\begin{bmatrix}0\\0\\0\end{bmatrix}
\]

\[
-x_1-x_2+x_3=0
\]
\[
x_1-x_2-x_3=0
\]
\[
x_1-x_2-x_3=0
\]

By Cramer's rule,

\[
\frac{x_1}{\begin{vmatrix}-1&1\\-1&-1\end{vmatrix}}
=
\frac{-x_2}{\begin{vmatrix}-1&1\\1&-1\end{vmatrix}}
=
\frac{x_3}{\begin{vmatrix}-1&-1\\1&-1\end{vmatrix}}
\]

or

\[
\frac{x_1}{2}=\frac{-x_2}{0}=\frac{x_3}{2}
\]

\(\therefore\) Eigen vector

\[
\begin{bmatrix}2\\0\\2\end{bmatrix}
=2\begin{bmatrix}1\\0\\1\end{bmatrix}
\quad \text{or} \quad
\begin{bmatrix}1\\0\\1\end{bmatrix}
\quad \text{or} \quad
[1\ 0\ 1]'
\]

\(\therefore\) Eigen vectors

\[
x_1=\begin{bmatrix}0\\1\\1\end{bmatrix},
\qquad
x_2=\begin{bmatrix}1\\1\\1\end{bmatrix},
\qquad
x_3=\begin{bmatrix}1\\0\\1\end{bmatrix}
\]

To verify linear independent of vectors, consider

\[
k_1x_1+k_2x_2+k_3x_3=0
\]

\[
\therefore\quad
k_1\begin{bmatrix}0\\1\\1\end{bmatrix}
+k_2\begin{bmatrix}1\\1\\1\end{bmatrix}
+k_3\begin{bmatrix}1\\0\\1\end{bmatrix}
=
\begin{bmatrix}0\\0\\0\end{bmatrix}
\]

\[
0k_1+k_2+k_3=0 \tag{i}
\]
\[
k_1+k_2+0k_3=0 \tag{ii}
\]
\[
k_1+k_2+k_3=0 \tag{iii}
\]

From (i), \(k_1=-k_2\).  
From (iii), \(-k_2+k_2+k_3=0\) i.e. \(k_3=0\).

\[
\therefore k_2=0,\quad k_1=0
\]

\(\therefore\) vectors \(x_1,x_2,x_3\) are linearly independent.

> **Transcription note (PDF page 4).** The line “From (i), \(k_1=-k_2\)” is reproduced as written, but equation (i) is \(k_2+k_3=0\); the relation \(k_1=-k_2\) actually follows from equation (ii). The conclusion is unaffected.

---

## Page 5 — Type II (symmetric, distinct eigenvalues); example \(\lambda=0\)

**Source: PDF page 5**

### Type II

\(A\) is symmetric and eigen values are distinct.

**Q.** Find eigen values and eigen vectors of

\[
A=\begin{bmatrix}
8&-6&2\\
-6&7&-4\\
2&-4&3
\end{bmatrix}
\]

**Sol.** The characteristic equation is

\[
\begin{vmatrix}
8-\lambda&-6&2\\
-6&7-\lambda&-4\\
2&-4&3-\lambda
\end{vmatrix}=0
\]

or

\[
\lambda^3-S_1\lambda^2+S_2\lambda-|A|=0
\]

\[
\lambda^3-18\lambda^2+45\lambda=0
\]

\[
\lambda(\lambda^2-18\lambda+45)=0
\]

\[
\lambda=0,\ 3,\ 15
\]

\[
\therefore \text{Eigen values are }(0,3,15)
\]

Beside the characteristic equation:

\[
S_1=18
\]

\[
\begin{aligned}
S_2&=(21-16)+(24-4)+(56-36)\\
&=5+20+20=45
\end{aligned}
\]

\[
\begin{aligned}
|A|&=8(5)+6(-18+8)+2(24-14)\\
&=40-60+20\\
&=0
\end{aligned}
\]

**i) For \(\lambda=0\),** \([A-\lambda_1 I]x=0\) gives

\[
\begin{bmatrix}
8&-6&2\\
-6&7&-4\\
2&-4&3
\end{bmatrix}
\begin{bmatrix}x_1\\x_2\\x_3\end{bmatrix}
=
\begin{bmatrix}0\\0\\0\end{bmatrix}
\]

First two rows gives,

\[
8x_1-6x_2+2x_3=0
\]
\[
-6x_1+7x_2-4x_3=0
\]

By Cramer's rule,

\[
\frac{x_1}{\begin{vmatrix}-6&2\\7&-4\end{vmatrix}}
=
\frac{-x_2}{\begin{vmatrix}8&2\\-6&-4\end{vmatrix}}
=
\frac{x_3}{\begin{vmatrix}8&-6\\-6&7\end{vmatrix}}
\]

or

\[
\frac{x_1}{10}=\frac{-x_2}{-20}=\frac{x_3}{20}
\]

or

\[
\frac{x_1}{1}=\frac{x_2}{2}=\frac{x_3}{2}
\]

\(\therefore\) corresponding eigen value \(0\), the eigen vector is

\[
\begin{bmatrix}1\\2\\2\end{bmatrix}
\quad \text{or} \quad
[1\ 2\ 2]'
\]

---

## Page 6 — Example continued: \(\lambda=3\) and \(\lambda=15\)

**Source: PDF page 6**

**ii) For \(\lambda=3\),** \([A-\lambda_2 I]x=0\) gives

\[
\begin{bmatrix}
5&-6&2\\
-6&4&-4\\
2&-4&0
\end{bmatrix}
\begin{bmatrix}x_1\\x_2\\x_3\end{bmatrix}
=
\begin{bmatrix}0\\0\\0\end{bmatrix}
\]

First two equations gives,

\[
5x_1-6x_2+2x_3=0
\]
\[
-6x_1+4x_2-4x_3=0
\]

By Cramer's rule,

\[
\frac{x_1}{\begin{vmatrix}-6&2\\4&-4\end{vmatrix}}
=
\frac{-x_2}{\begin{vmatrix}5&2\\-6&-4\end{vmatrix}}
=
\frac{x_3}{\begin{vmatrix}5&-6\\-6&4\end{vmatrix}}
\]

or

\[
\frac{x_1}{16}=\frac{x_2}{8}=\frac{x_3}{-16}
\]

or

\[
\frac{x_1}{2}=\frac{x_2}{1}=\frac{x_3}{-2}
\]

\(\therefore\) corresponding eigen value \(3\), eigen vector

\[
[2\ 1\ -2]'
\quad \text{or} \quad
\begin{bmatrix}2\\1\\-2\end{bmatrix}
\]

**iii) For \(\lambda=15\),** \([A-\lambda_3 I]x=0\) gives

\[
\begin{bmatrix}
-7&-6&2\\
-6&-8&-4\\
2&-4&-12
\end{bmatrix}
\begin{bmatrix}x_1\\x_2\\x_3\end{bmatrix}
=
\begin{bmatrix}0\\0\\0\end{bmatrix}
\]

First two rows gives,

\[
-7x_1-6x_2+2x_3=0
\]
\[
-6x_1-8x_2-4x_3=0
\]

By Cramer's rule,

\[
\frac{x_1}{\begin{vmatrix}-6&2\\-8&-4\end{vmatrix}}
=
\frac{-x_2}{\begin{vmatrix}-7&2\\-6&-4\end{vmatrix}}
=
\frac{x_3}{\begin{vmatrix}-7&-6\\-6&-8\end{vmatrix}}
\]

or

\[
\frac{x_1}{40}=\frac{x_2}{-40}=\frac{x_3}{20}
\]

or

\[
\frac{x_1}{2}=\frac{x_2}{-2}=\frac{x_3}{1}
\]

\(\therefore\) corresponding eigen value \(15\), eigen vector

\[
[2\ -2\ 1]'
\quad \text{or} \quad
\begin{bmatrix}2\\-2\\1\end{bmatrix}
\]

---

## Page 7 — Type III (non-symmetric, repeated); example \(\lambda=1\)

**Source: PDF page 7**

### Type III

\(A\) is non symmetric, eigen values repeated.

**Q.** Find eigen values and eigen vectors of

\[
A=\begin{bmatrix}
2&2&1\\
1&3&1\\
1&2&2
\end{bmatrix}
\]

**Sol.** The characteristic equation is

\[
|A-\lambda I|=0,
\]

\[
\begin{vmatrix}
2-\lambda&2&1\\
1&3-\lambda&1\\
1&2&2-\lambda
\end{vmatrix}=0
\]

or

\[
\lambda^3-S_1\lambda^2+S_2\lambda-|A|=0
\]

\[
S_1=7
\]

\[
S_2=(6-2)+3+4=11
\]

\[
|A|=2(4)-2(1)+1(-1)=5
\]

\(\therefore\) characteristic equation is

\[
\lambda^3-7\lambda^2+11\lambda-5=0
\]

\[
\lambda=1,1,5
\]

**i) For \(\lambda=1\),** \([A-\lambda_1 I]x=0\) gives

\[
\begin{bmatrix}
1&2&1\\
1&2&1\\
1&2&1
\end{bmatrix}
\begin{bmatrix}x_1\\x_2\\x_3\end{bmatrix}
=
\begin{bmatrix}0\\0\\0\end{bmatrix}
\]

\[
R_2\to R_2-R_1,\qquad R_3\to R_3-R_1
\]

\[
\begin{bmatrix}
1&2&1\\
0&0&0\\
0&0&0
\end{bmatrix}
\begin{bmatrix}x_1\\x_2\\x_3\end{bmatrix}
=
\begin{bmatrix}0\\0\\0\end{bmatrix}
\]

\[
\therefore x_1+2x_2+x_3=0
\]

Put \(x_3=t,\ x_2=s\).

\[
\therefore x_1=-2s-t
\]

\[
\therefore
\begin{bmatrix}x_1\\x_2\\x_3\end{bmatrix}
=
\begin{bmatrix}-2s-t\\s\\t\end{bmatrix}
=
(-1)\begin{bmatrix}2s+t\\-s+0t\\0s-t\end{bmatrix}
\]

\[
\therefore \text{Eigen vectors are }
\begin{bmatrix}2\\-1\\0\end{bmatrix}
\quad \text{or} \quad
\begin{bmatrix}1\\0\\-1\end{bmatrix}
\]

or

\[
[2\ -1\ 0]'
\quad \text{and} \quad
[1\ 0\ -1]'
\]

Beside the working:

\[
\left.
\begin{aligned}
r&=1\\
n&=3\\
n-r&=3-1=2
\end{aligned}
\right\}
\text{independent solutions.}
\]

---

## Page 8 — Example continued: \(\lambda=5\); Type IV (symmetric, repeated)

**Source: PDF page 8**

**ii) For \(\lambda=5\),** \([A-\lambda_3 I]x=0\) gives

\[
\begin{bmatrix}
-3&2&1\\
1&-2&1\\
1&2&-3
\end{bmatrix}
\begin{bmatrix}x_1\\x_2\\x_3\end{bmatrix}
=
\begin{bmatrix}0\\0\\0\end{bmatrix}
\]

By \(R_{13}\),

\[
\begin{bmatrix}
1&2&-3\\
1&-2&1\\
-3&2&1
\end{bmatrix}
\begin{bmatrix}x_1\\x_2\\x_3\end{bmatrix}
=
\begin{bmatrix}0\\0\\0\end{bmatrix}
\]

\[
R_2\to R_2-R_1,\qquad R_3\to R_3+3R_1
\]

\[
\begin{bmatrix}
1&2&-3\\
0&-4&4\\
0&8&-8
\end{bmatrix}
\begin{bmatrix}x_1\\x_2\\x_3\end{bmatrix}
=
\begin{bmatrix}0\\0\\0\end{bmatrix}
\]

\[
R_3\to R_3+2R_2
\]

\[
\begin{bmatrix}
1&2&-3\\
0&-4&4\\
0&0&0
\end{bmatrix}
\begin{bmatrix}x_1\\x_2\\x_3\end{bmatrix}
=
\begin{bmatrix}0\\0\\0\end{bmatrix}
\]

\[
\therefore x_1+2x_2-3x_3=0
\]
\[
-4x_2+4x_3=0
\]

Put \(x_3=t\).

\[
\therefore x_2=t
\]
\[
\therefore x_1=t
\]

\[
\therefore X=\begin{bmatrix}t\\t\\t\end{bmatrix}=t\begin{bmatrix}1\\1\\1\end{bmatrix}
\]

\[
\therefore \text{Eigen vector }
\begin{bmatrix}1\\1\\1\end{bmatrix}
\quad \text{or} \quad
[1\ 1\ 1]'
\]

Beside the working:

\[
\left.
\begin{aligned}
r&=2\\
n&=3\\
n-r&=(3-2)=1
\end{aligned}
\right\}
\text{independent solution.}
\]

### Type IV

\(A\) is symmetric and eigen values are repeated.

**Q.** Find eigen values and eigen vectors of

\[
A=\begin{bmatrix}
3&-1&1\\
-1&3&-1\\
1&-1&3
\end{bmatrix}
\]

**Sol.** The characteristic equation is \(|A-\lambda I|=0\) gives

\[
\lambda^3-S_1\lambda^2+S_2\lambda-|A|=0
\]

\[
\lambda^3-9\lambda^2+24\lambda-20=0
\]

\[
\therefore \lambda=2,2,5
\]

\[
S_1=9,
\qquad
S_2=8+8+8=24
\]

\[
|A|=3(8)+1(-2)+1(-2)=20
\]

**i) For \(\lambda=2\),** \([A-\lambda_1 I]x=0\) gives [continues on PDF page 9]

---

## Page 9 — Type IV example continued: \(\lambda=2\) and \(\lambda=5\)

**Source: PDF page 9**

\[
\begin{bmatrix}
1&-1&1\\
-1&1&-1\\
1&-1&1
\end{bmatrix}
\begin{bmatrix}x_1\\x_2\\x_3\end{bmatrix}
=
\begin{bmatrix}0\\0\\0\end{bmatrix}
\]

\[
R_2\to R_2+R_1,\qquad R_3\to R_3-R_1
\]

\[
\begin{bmatrix}
1&-1&1\\
0&0&0\\
0&0&0
\end{bmatrix}
\begin{bmatrix}x_1\\x_2\\x_3\end{bmatrix}
=
\begin{bmatrix}0\\0\\0\end{bmatrix}
\]

\[
x_1-x_2+x_3=0
\]

Put \(x_3=t,\ x_2=s\).

\[
\therefore x_1-s+t=0
\]
\[
x_1=s-t
\]

\[
\therefore
\begin{bmatrix}x_1\\x_2\\x_3\end{bmatrix}
=
\begin{bmatrix}s-t\\s+0t\\0s+t\end{bmatrix}
=
s\begin{bmatrix}1\\1\\0\end{bmatrix}
+t\begin{bmatrix}-1\\0\\1\end{bmatrix}
\]

\[
\therefore X=
\begin{bmatrix}s-t\\s+0t\\0s+t\end{bmatrix}
=
s\begin{bmatrix}1\\1\\0\end{bmatrix}
+t\begin{bmatrix}-1\\0\\1\end{bmatrix}
\]

\[
x_1=\begin{bmatrix}1\\1\\0\end{bmatrix}
\quad \text{or} \quad [1\ 1\ 0]'
\]

\[
x_2=\begin{bmatrix}-1\\0\\1\end{bmatrix}
\quad \text{or} \quad [-1\ 0\ 1]'
\]

Beside the working:

\[
\left.
\begin{aligned}
r&=1\\
n&=3\\
n-r&=3-1=2
\end{aligned}
\right\}
\begin{array}{l}
\text{independent}\\
\text{sol.}
\end{array}
\]

**ii) For \(\lambda=5\),** \([A-\lambda_3 I]x=0\) gives

\[
\begin{bmatrix}
-2&-1&1\\
-1&-2&-1\\
1&-1&-2
\end{bmatrix}
\begin{bmatrix}x_1\\x_2\\x_3\end{bmatrix}
=
\begin{bmatrix}0\\0\\0\end{bmatrix}
\]

First two rows gives,

\[
-2x_1-x_2+x_3=0
\]
\[
-x_1-2x_2-x_3=0
\]

By Cramer's rule,

\[
\frac{x_1}{\begin{vmatrix}-1&1\\-2&-1\end{vmatrix}}
=
\frac{-x_2}{\begin{vmatrix}-2&1\\-1&-1\end{vmatrix}}
=
\frac{x_3}{\begin{vmatrix}-2&-1\\-1&-2\end{vmatrix}}
\]

or

\[
\frac{x_1}{3}=\frac{x_2}{-3}=\frac{x_3}{3}
\]

or

\[
\frac{x_1}{1}=\frac{x_2}{-1}=\frac{x_3}{1}
\]

\[
\therefore x_3=[1\ -1\ 1]'
\quad \text{or} \quad
\begin{bmatrix}1\\-1\\1\end{bmatrix}
\quad \text{as eigen vector.}
\]

> **Transcription note (PDF page 9).** The final vector is labelled \(x_3\) in the notes even though it is the eigenvector belonging to \(\lambda=5\); the two vectors for \(\lambda=2\) had already been labelled \(x_1\) and \(x_2\). Reproduced as written.

---

## Page 10 — Properties of eigenvalues and eigenvectors; sum and product example

**Source: PDF page 10**

## Properties of Eigen values and Eigen vectors

**Theorem 1.** \(\lambda\) is an eigen value of the matrix \(A\) iff there exists a non-zero vector \(X\), such that \(AX=\lambda X\).

**Theorem 2.** If \(X\) is an eigen vector of \(A\) corresponding to eigen value \(\lambda\), then \(kX\) is also an eigen vector of \(A\) (\(k\) is non zero scalar).

**Th 3 (Uniqueness of eigen vector).** If \(X\) is a eigen vector of matrix \(A\), then \(X\) can not correspond to more than one eigen values of \(A\).

**Th 4.** Eigen vectors corresponding to distinct eigen values of a matrix are linearly independent.

### Note:

i) \(A\) and \(A'\) have same eigen values.

ii) If \(\lambda\) is eigen value of \(A\) then \(\lambda^m\) is eigen value of \(A^m\).

iii) Eigen value of \(A^{-1}=\dfrac{1}{\lambda}\), (\(\lambda\) is eigen value of \(A\)).

iv) \(k\lambda_1,\ k\lambda_2,\ k\lambda_3,\ldots\) are eigen values of \(kA\).

v) Eigen value of \(\operatorname{adj}A=\dfrac{|A|}{\lambda}\).

vi) Eigen value of \(I\) is \(1\).

vii) \(''\quad ''\quad ''\quad kI=k\).

viii) If \(|A|=0\) then at least one zero is eigen value.

ix) Eigen value of triangular matrix are diagonal elements.

**Q.** Find the sum and product of the eigen values of

\[
A=\begin{bmatrix}
-17&18&-6\\
-18&19&-6\\
-9&9&-2
\end{bmatrix}
\]

**Sol.**

\[
\text{Sum}=-17+19-2=0
\]

\[
\begin{aligned}
\text{Product of eigen value }&=|A|\\
&=-17(-38+54)-18(36-54)-6(-162+171)\\
&=-2
\end{aligned}
\]

> **Transcription note (PDF page 10).** Note (viii) is written “at least one zero is eigen value”; read literally it means “at least one eigenvalue is zero”. Note (ix) omits “the” before “diagonal elements”. Both are reproduced as written.

---

## Page 11 — Eigenvalues of a matrix polynomial and of an adjoint

**Source: PDF page 11**

**Q.** Find the eigen values of \(A^2-2A+I\), if

\[
A=\begin{bmatrix}
2&0&-2\\
0&1&-4\\
0&0&4
\end{bmatrix}
\]

**Sol.** Since \(A\) is upper triangular matrix, its eigen values are \(2,1,4\).

Now

\[
f(A)=A^2-2A+I
\]

\[
\therefore \text{Eigen values of }f(A)=\lambda^2-2\lambda+1=(\lambda-1)^2=f(\lambda)
\]

when \(\lambda=2\),

\[
f(2)=(2-1)^2=1
\]
\[
f(1)=0
\]
\[
f(4)=(4-1)^2=9
\]

\[
\therefore \text{Eigen values of }A^2-2A+I\text{ are }(1,0,9).
\]

**Q.** Find the eigen values of adjoint of

\[
A=\begin{bmatrix}
2&0&-1\\
0&2&0\\
-1&0&2
\end{bmatrix}
\]

**Sol.**

\[
|A-\lambda I|=0 \quad \text{i.e.}
\]

\[
\lambda^3-S_1\lambda^2+S_2\lambda-|A|=0
\]

\[
\lambda^3-6\lambda^2+11\lambda-6=0
\]

\[
\lambda=1,2,3
\]

Beside the working:

\[
S_1=6
\]
\[
S_2=4+3+4=11
\]
\[
|A|=2(4)-0-1(2)=6
\]

\[
\therefore \text{Eigen value of }\operatorname{adj}A=\frac{|A|}{\lambda}
\]

\[
\lambda=1,\quad \frac{6}{1}=6
\]
\[
\lambda=2,\quad \frac{6}{2}=3
\]
\[
\lambda=3,\quad \frac{6}{3}=2
\]

\[
\therefore \text{Eigen values of }\operatorname{adj}A=6,3,2
\]

To the right of this working is a small synthetic-division / long-division table with coefficients \(1,\ -6,\ 11,\ -6\) and trial divisors \(1,2,3\), confirming the roots. The table is an auxiliary check and its individual layout is not transcribed.

---

## Page 12 — A repeated-eigenvalue example: characteristic equation and \(\lambda=1\)

**Source: PDF page 12**

**Q.** Find eigen values and eigen vectors of

\[
A=\begin{bmatrix}
4&6&6\\
1&3&2\\
-1&-5&-2
\end{bmatrix}
\]

**Sol.** The characteristic equation is

\[
\begin{vmatrix}
4-\lambda&6&6\\
1&3-\lambda&2\\
-1&-5&-2-\lambda
\end{vmatrix}=0
\]

\[
\lambda^3-S_1\lambda^2+S_2\lambda-|A|=0
\]

\[
\lambda^3-5\lambda^2+8\lambda-4=0
\]

\[
\lambda=1,2,2
\]

Beside the working:

\[
S_1=5
\]

\[
\begin{aligned}
S_2&=(-6+10)+(-8+6)+(2-6)\\
&=4-2+6=8
\end{aligned}
\]

\[
\begin{aligned}
|A|&=4(-6+10)-6(-2+2)+6(-5+3)\\
&=16+0-12=4
\end{aligned}
\]

**i) For \(\lambda=1\),** \([A-\lambda_1 I]x=0\) gives

\[
\begin{bmatrix}
3&6&6\\
1&2&2\\
-1&-5&-3
\end{bmatrix}
\begin{bmatrix}x_1\\x_2\\x_3\end{bmatrix}
=
\begin{bmatrix}0\\0\\0\end{bmatrix}
\]

\[
\text{By }R_{12}
\]

\[
\begin{bmatrix}
1&2&2\\
3&6&6\\
-1&-5&-3
\end{bmatrix}
\begin{bmatrix}x_1\\x_2\\x_3\end{bmatrix}
=
\begin{bmatrix}0\\0\\0\end{bmatrix}
\]

\[
R_2\to R_2-3R_1,\qquad R_3\to R_3+R_1
\]

\[
\begin{bmatrix}
1&2&2\\
0&0&0\\
0&-3&-1
\end{bmatrix}
\begin{bmatrix}x_1\\x_2\\x_3\end{bmatrix}
=
\begin{bmatrix}0\\0\\0\end{bmatrix}
\]

\[
R_{23}
\]

\[
\begin{bmatrix}
1&2&2\\
0&-3&-1\\
0&0&0
\end{bmatrix}
\begin{bmatrix}x_1\\x_2\\x_3\end{bmatrix}
=
\begin{bmatrix}0\\0\\0\end{bmatrix}
\]

\[
\therefore x_1+2x_2+2x_3=0
\]
\[
-3x_2-x_3=0
\]

Put \(x_3=3t\);

\[
\therefore x_2=-t
\]

\[
x_1=-2x_3-2x_2=-6t+2t=-4t
\]

\[
\therefore X=\begin{bmatrix}x_1\\x_2\\x_3\end{bmatrix}
=
\begin{bmatrix}-4t\\-t\\3t\end{bmatrix}
=
(-t)\begin{bmatrix}4\\1\\-3\end{bmatrix}
\]

\[
\therefore \text{corresponding to }\lambda=1,\ \text{eigen vector }
\begin{bmatrix}4\\1\\-3\end{bmatrix}
\]

Beside the working:

\[
\left.
\begin{aligned}
r&=2,\ n=3\\
n-r&=3-2=1
\end{aligned}
\right\}
\text{(linearly independent sol.)}
\]

**ii) For \(\lambda=2\),** \([A-\lambda_2 I]x=0\) gives [continues on PDF page 13]

> **Transcription note (PDF page 12).** The third bracket in \(S_2\) is written \((2-6)\), although the next line uses \(4-2+6=8\) and the correct minor is \(12-6=6\). The handwriting does not clearly show a leading “1”. Reproduced exactly as written.

---

## Page 13 — \(\lambda=2\); Cayley–Hamilton statement and first verification

**Source: PDF page 13**

\[
\begin{bmatrix}
2&6&6\\
1&1&2\\
-1&-5&-4
\end{bmatrix}
\begin{bmatrix}x_1\\x_2\\x_3\end{bmatrix}
=
\begin{bmatrix}0\\0\\0\end{bmatrix}
\]

By \(R_{12}\),

\[
\begin{bmatrix}
1&1&2\\
2&6&6\\
-1&-5&-4
\end{bmatrix}
\begin{bmatrix}x_1\\x_2\\x_3\end{bmatrix}
=
\begin{bmatrix}0\\0\\0\end{bmatrix}
\]

\[
R_2\to R_2-2R_1,\qquad R_3\to R_3+R_1
\]

\[
\begin{bmatrix}
1&1&2\\
0&4&2\\
0&-4&-2
\end{bmatrix}
\begin{bmatrix}x_1\\x_2\\x_3\end{bmatrix}
=
\begin{bmatrix}0\\0\\0\end{bmatrix}
\]

\[
R_3\to R_3+R_2
\]

\[
\begin{bmatrix}
1&1&2\\
0&4&2\\
0&0&0
\end{bmatrix}
\begin{bmatrix}x_1\\x_2\\x_3\end{bmatrix}
=
\begin{bmatrix}0\\0\\0\end{bmatrix}
\]

\[
\frac{1}{2}R_2
\]

\[
\begin{bmatrix}
1&1&2\\
0&2&1\\
0&0&0
\end{bmatrix}
\begin{bmatrix}x_1\\x_2\\x_3\end{bmatrix}
=
\begin{bmatrix}0\\0\\0\end{bmatrix}
\]

\[
\therefore x_1+x_2+2x_3=0
\]
\[
2x_2+x_3=0
\]

Put \(x_3=2t\),

\[
\therefore x_2=-t
\]

\[
x_1=-x_2-2x_3=t-4t=-3t
\]

\[
\therefore X=\begin{bmatrix}-3t\\-t\\2t\end{bmatrix}
=
(-t)\begin{bmatrix}3\\1\\-2\end{bmatrix}
\]

Hence corresponding to \(\lambda=2\), the eigen vector is

\[
\begin{bmatrix}3\\1\\-2\end{bmatrix}
\]

Beside the working:

\[
\left.
\begin{aligned}
r&=2,\ n=3\\
n-r&=3-2=1
\end{aligned}
\right\}
\text{independent sol.}
\]

## Cayley–Hamilton Theorem

Every square matrix satisfies its characteristic equation.

**Q.** Verify Cayley–Hamilton theorem for the matrix

\[
A=\begin{bmatrix}
3&2&1\\
1&2&2\\
3&2&1
\end{bmatrix}
\]

**Sol.** The characteristic equation is

\[
|A-\lambda I|=0
\]

\[
\lambda^3-S_1\lambda^2+S_2\lambda-|A|=0
\]

\[
\lambda^3-6\lambda^2+2\lambda-0=0
\]

Beside the working:

\[
S_1=6
\]
\[
|A|=3(-2)-2(-5)+1(-4)=-6+10-4=0
\]
\[
S_2=-2+0+4=2
\]

Cayley Hamilton theorem states that this equation is satisfied by \(A\) i.e.

\[
A^3-6A^2+2A-0I=0 \tag{1}
\]

---

## Page 14 — Cayley–Hamilton verification completed; second example begins

**Source: PDF page 14**

\[
A^2=A\cdot A=
\begin{bmatrix}
3&2&1\\
1&2&2\\
3&2&1
\end{bmatrix}
\begin{bmatrix}
3&2&1\\
1&2&2\\
3&2&1
\end{bmatrix}
\]

\[
=
\begin{bmatrix}
9+2+3&6+4+2&3+4+1\\
3+2+6&2+4+4&1+4+2\\
9+2+3&6+4+2&3+4+1
\end{bmatrix}
=
\begin{bmatrix}
14&12&8\\
11&10&7\\
14&12&8
\end{bmatrix}
\]

\[
A^3=
\begin{bmatrix}
14&12&8\\
11&10&7\\
14&12&8
\end{bmatrix}
\begin{bmatrix}
3&2&1\\
1&2&2\\
3&2&1
\end{bmatrix}
\]

\[
=
\begin{bmatrix}
78&68&46\\
64&56&38\\
78&68&46
\end{bmatrix}
\]

Now,

\[
A^3-6A^2+9A-3I \quad [\text{terms }9A\text{ and }3I\text{ are struck through}]
\]

\[
=
\begin{bmatrix}
78&68&46\\
64&56&38\\
78&68&46
\end{bmatrix}
-
\begin{bmatrix}
84&72&48\\
66&60&42\\
84&72&48
\end{bmatrix}
+
\begin{bmatrix}
9&6&3\\
3&6&6\\
9&6&3
\end{bmatrix}
-
\begin{bmatrix}
3&0&0\\
0&3&0\\
0&0&3
\end{bmatrix}
+
\begin{bmatrix}
6&4&2\\
2&4&4\\
6&4&2
\end{bmatrix}
\]

\[
=
\begin{bmatrix}
0&0&0\\
0&0&0\\
0&0&0
\end{bmatrix}
\]

Hence Cayley Hamilton theorem verified.

> **Transcription note (PDF page 14).** The heading line is written as \(A^3-6A^2+9A-3I\), with \(9A\) and \(3I\) struck out, and \(+2A\) appended; the matrices for \(3A\) and \(3I\) are nevertheless still written in the working and then struck through. The surviving calculation is \(A^3-6A^2+2A=0\). Reproduced exactly, including the cancelled terms.

**Q.** Verify Cayley Hamilton theorem for the matrix \(A\) and hence find \(A^{-1}\) and \(A^4\), where

\[
A=\begin{bmatrix}
1&2&3\\
2&-1&4\\
3&1&-1
\end{bmatrix}
\]

**Sol.** The characteristic equation is

\[
|A-\lambda I|=0
\]

\[
\lambda^3-S_1\lambda^2+S_2\lambda-|A|=0
\]

\[
\lambda^3+\lambda^2-18\lambda-40=0
\]

Beside the working:

\[
S_1=-1
\]
\[
S_2=-3-10-5=-18
\]
\[
|A|=40
\]

Cayley Hamilton theorem states that

\[
A^3+A^2-18A-40I=0 \tag{1}
\]

---

## Page 15 — Second Cayley–Hamilton verification; \(A^{-1}\) and \(A^4\)

**Source: PDF page 15**

Now,

\[
A^2=
\begin{bmatrix}
1&2&3\\
2&-1&4\\
3&1&-1
\end{bmatrix}
\begin{bmatrix}
1&2&3\\
2&-1&4\\
3&1&-1
\end{bmatrix}
=
\begin{bmatrix}
14&3&8\\
12&9&-2\\
2&4&14
\end{bmatrix}
\]

\[
A^3=
\begin{bmatrix}
14&3&8\\
12&9&-2\\
2&4&14
\end{bmatrix}
\begin{bmatrix}
1&2&3\\
2&-1&4\\
3&1&-1
\end{bmatrix}
=
\begin{bmatrix}
44&33&46\\
24&13&74\\
52&14&8
\end{bmatrix}
\]

\[
\therefore A^3+A^2-18A-40I
\]

\[
=
\begin{bmatrix}
44&33&46\\
24&13&74\\
52&14&8
\end{bmatrix}
+
\begin{bmatrix}
14&3&8\\
12&9&-2\\
2&4&14
\end{bmatrix}
-
\begin{bmatrix}
18&36&54\\
36&-18&72\\
54&18&-18
\end{bmatrix}
-
\begin{bmatrix}
40&0&0\\
0&40&0\\
0&0&40
\end{bmatrix}
\]

\[
=
\begin{bmatrix}
0&0&0\\
0&0&0\\
0&0&0
\end{bmatrix}
\]

Thus Cayley Hamilton theorem verified.

Now, multiplying (1) by \(A^{-1}\), we get

\[
A^2+A-18I-40A^{-1}=0
\]

\[
\therefore A^{-1}=\frac{1}{40}\left\{A^2+A-18I\right\}
\]

\[
=\frac{1}{40}\left\{
\begin{bmatrix}
14&3&8\\
12&9&-2\\
2&4&14
\end{bmatrix}
+
\begin{bmatrix}
1&2&3\\
2&-1&4\\
3&1&-1
\end{bmatrix}
-
\begin{bmatrix}
18&0&0\\
0&18&0\\
0&0&18
\end{bmatrix}
\right\}
\]

\[
=\frac{1}{40}
\begin{bmatrix}
-3&5&11\\
14&-10&2\\
5&5&-5
\end{bmatrix}
\]

Further, multiplying (1) by \(A\), we get

\[
A^4+A^3-18A^2-40A=0
\]

\[
\therefore A^4=40A+18A^2-A^3
\]

\[
=
\begin{bmatrix}
40&80&120\\
80&-40&160\\
120&40&-40
\end{bmatrix}
+
\begin{bmatrix}
252&54&144\\
216&162&-36\\
36&72&252
\end{bmatrix}
-
\begin{bmatrix}
44&33&46\\
24&13&74\\
52&14&8
\end{bmatrix}
\]

\[
=
\begin{bmatrix}
248&101&218\\
272&109&50\\
104&98&204
\end{bmatrix}
\]

---

## Page 16 — Similarity and diagonalisability

**Source: PDF page 16**

## Similarity of Matrices

If \(A\) and \(B\) are any two square matrices of order \(n\), then \(B\) is said to be similar to \(A\), if there exists a non-singular matrix \(M\) such that

\[
B=M^{-1}AM.
\]

## Diagonalisable matrix:

If all eigen values are distinct, the matrix is diagonalisable.

**Theorem.** A square non-singular matrix \(A\) whose eigen values are distinct can be diagonalised by a similarity transformation

\[
D=M^{-1}AM,
\]

where \(M\) is matrix whose columns are the eigen vectors of \(A\) and \(D\) is diagonal matrix whose diagonal elements are eigen values of \(A\).

### Note:

i) If all eigen values of \(A\) are repeated, then \(A\) may be diagonalisable or \(A\) may not be diagonalisable.

ii) If the algebraic multiplicity and geometric multiplicity of a repeated values are equal then \(A\) is diagonalisable.

iii) If algebraic multiplicity \(\neq\) algebraic multiplicity then \(A\) is not diagonalisable.

iv) If an eigen value \(\lambda\) repeated ‘\(t\)’ times then its algebraic multiplicity is \(t\).

v) If corresponding to an eigen value \(\lambda\), there are \(s\) linearly independent eigen vectors then \(s\) is called algebraic multiplicity of \(\lambda\).

> **Transcription notes (PDF page 16).** In note (iii) the words “algebraic multiplicity” are written twice; the intended comparison is normally algebraic versus geometric multiplicity. In note (v) the number of linearly independent eigenvectors is normally called the *geometric* multiplicity, but the teacher writes “algebraic”. Both are reproduced exactly.

---

## Page 17 — Diagonalisation example: statement and \(\lambda=0\)

**Source: PDF page 17**

**Q.** Show that the matrix

\[
A=\begin{bmatrix}
8&-6&2\\
-6&7&-4\\
2&-4&3
\end{bmatrix}
\]

is diagonalisable. Find the transforming matrix and the diagonal matrix.

**Sol.** The characteristic equation is

\[
|A-\lambda I|=0
\]

or

\[
\lambda^3-S_1\lambda^2+S_2\lambda-|A|=0
\]

\[
\lambda^3-18\lambda^2+45\lambda=0
\]

\[
\lambda(\lambda^2-18\lambda+45)=0
\]

\[
\lambda=0,3,15
\]

Beside the working:

\[
S_1=18
\]
\[
S_2=45
\]
\[
|A|=8(5)+6(-10)+2(10)=40-60+20=0
\]

\(\therefore\) all eigen values are distinct, the matrix \(A\) is diagonalisable.

**i) For \(\lambda=0\),** \([A-\lambda_1 I]x=0\) gives

\[
\begin{bmatrix}
8&-6&2\\
-6&7&-4\\
2&-4&3
\end{bmatrix}
\begin{bmatrix}x_1\\x_2\\x_3\end{bmatrix}
=
\begin{bmatrix}0\\0\\0\end{bmatrix}
\]

First two rows gives,

\[
8x_1-6x_2+2x_3=0
\]
\[
-6x_1+7x_2-4x_3=0
\]

By Cramer's rule,

\[
\frac{x_1}{\begin{vmatrix}-6&2\\7&-4\end{vmatrix}}
=
\frac{-x_2}{\begin{vmatrix}8&2\\-6&-4\end{vmatrix}}
=
\frac{x_3}{\begin{vmatrix}8&-6\\-6&7\end{vmatrix}}
\]

or

\[
\frac{x_1}{10}=\frac{x_2}{20}=\frac{x_3}{20}
\]

or

\[
\frac{x_1}{1}=\frac{x_2}{2}=\frac{x_3}{2}
\]

\(\therefore\) corresponding to eigen value \(0\), the eigen vector is

\[
[1\ 2\ 2]'
\quad \text{or} \quad
\begin{bmatrix}1\\2\\2\end{bmatrix}
\]

---

## Page 18 — Diagonalisation example continued; transforming and diagonal matrices

**Source: PDF page 18**

**ii) For \(\lambda=3\),** \([A-3I]x=0\) gives

\[
\begin{bmatrix}
5&-6&2\\
-6&4&-4\\
2&-4&0
\end{bmatrix}
\begin{bmatrix}x_1\\x_2\\x_3\end{bmatrix}
=
\begin{bmatrix}0\\0\\0\end{bmatrix}
\]

The first two rows gives,

\[
5x_1-6x_2+2x_3=0
\]
\[
-6x_1+4x_2-4x_3=0
\]

By Cramer's rule,

\[
\frac{x_1}{\begin{vmatrix}6&2\\4&-4\end{vmatrix}}
=
\frac{-x_2}{\begin{vmatrix}5&2\\-6&-4\end{vmatrix}}
=
\frac{x_3}{\begin{vmatrix}5&-6\\-6&4\end{vmatrix}}
\]

or

\[
\frac{x_1}{16}=\frac{x_2}{8}=\frac{x_3}{-16}
\]

or

\[
\frac{x_1}{2}=\frac{x_2}{1}=\frac{x_3}{-2}
\]

\(\therefore\) corresponding to eigen value \(3\), the eigen vector

\[
[2\ 1\ -2]'
\quad \text{or} \quad
\begin{bmatrix}2\\1\\-2\end{bmatrix}
\]

**iii) For \(\lambda=15\),** \([A-15I]x=0\) gives

\[
\begin{bmatrix}
-7&-6&2\\
-6&-8&-4\\
2&-4&-12
\end{bmatrix}
\begin{bmatrix}x_1\\x_2\\x_3\end{bmatrix}
=
\begin{bmatrix}0\\0\\0\end{bmatrix}
\]

The first two rows gives,

\[
-7x_1-6x_2+2x_3=0
\]
\[
-6x_1-8x_2-4x_3=0
\]

By Cramer's rule,

\[
\frac{x_1}{\begin{vmatrix}-6&2\\-8&-4\end{vmatrix}}
=
\frac{-x_2}{\begin{vmatrix}-7&2\\-6&-4\end{vmatrix}}
=
\frac{x_3}{\begin{vmatrix}-7&-6\\-6&-8\end{vmatrix}}
\]

or

\[
\frac{x_1}{40}=\frac{x_2}{-40}=\frac{x_3}{20}
\]

or

\[
\frac{x_1}{2}=\frac{x_2}{-2}=\frac{x_3}{1}
\]

\(\therefore\) corresponding to eigen value \(15\), the eigen vector is

\[
[2\ -2\ 1]'
\quad \text{or} \quad
\begin{bmatrix}2\\-2\\1\end{bmatrix}
\]

\[
\therefore D=M^{-1}AM
\]

The matrix

\[
A=\begin{bmatrix}
8&-6&2\\
-6&7&-4\\
2&-4&3
\end{bmatrix}
\]

is diagonalised to diagonal matrix

\[
D=\begin{bmatrix}
0&0&0\\
0&3&0\\
0&0&15
\end{bmatrix}
\]

by transforming matrix

\[
M=\begin{bmatrix}
1&2&2\\
2&1&-2\\
2&-2&1
\end{bmatrix}
\]

> **Transcription note (PDF page 18).** In the \(\lambda=3\) Cramer line the first determinant is written with \(+6\) in the top-left corner, whereas the coefficient matrix has \(-6\). The subsequent value \(16\) corresponds to \(\begin{vmatrix}-6&2\\4&-4\end{vmatrix}=24-8=16\). The reading \(+6\) is likely a slip; it is preserved and flagged.

---

## Page 19 — Repeated-eigenvalue diagonalisation example; \(\lambda=-1\)

**Source: PDF page 19**

**Q.** Show that

\[
A=\begin{bmatrix}
-9&4&4\\
-8&3&4\\
-16&8&7
\end{bmatrix}
\]

is diagonalisable. Find diagonal matrix and diagonalising matrix.

**Sol.** The characteristic equation is

\[
|A-\lambda I|=0 \quad \text{gives}
\]

or

\[
\lambda^3-S_1\lambda^2+S_2\lambda-|A|=0
\]

\[
\lambda^3-\lambda^2-5\lambda-3=0
\]

\[
\lambda=-1,-1,3
\]

Beside the working:

\[
S_1=1
\]
\[
S_2=-11+1+5=-5
\]
\[
|A|=-9(-11)-4(8)+4(-16)=3
\]

\(\therefore\) eigen values not distinct then it may or may not be diagonalisable.

**i) For \(\lambda=-1\),** \([A-\lambda_1 I]x=0\) gives

\[
\begin{bmatrix}
-8&4&4\\
-8&4&4\\
-16&8&8
\end{bmatrix}
\begin{bmatrix}x_1\\x_2\\x_3\end{bmatrix}
=
\begin{bmatrix}0\\0\\0\end{bmatrix}
\]

\[
R_2\to R_2-R_1
\]
\[
R_3\to R_3-2R_1
\]

\[
\begin{bmatrix}
-8&4&4\\
0&0&0\\
0&0&0
\end{bmatrix}
\begin{bmatrix}x_1\\x_2\\x_3\end{bmatrix}
=
\begin{bmatrix}0\\0\\0\end{bmatrix}
\]

\[
\frac{1}{4}R_1
\]

\[
\begin{bmatrix}
-2&1&1\\
0&0&0\\
0&0&0
\end{bmatrix}
\begin{bmatrix}x_1\\x_2\\x_3\end{bmatrix}
=
\begin{bmatrix}0\\0\\0\end{bmatrix}
\]

\[
-2x_1+x_2+x_3=0
\]

Put \(x_3=2t,\ x_2=2s\).

\[
\therefore 2x_1=2s+2t
\]
or
\[
x_1=s+t
\]

\[
\therefore X=
\begin{bmatrix}s+t\\2s+0t\\0s+2t\end{bmatrix}
=
s\begin{bmatrix}1\\2\\0\end{bmatrix}
+t\begin{bmatrix}1\\0\\2\end{bmatrix}
\]

\(\therefore\) corresponding to eigen value \(-1\), we get eigen vectors

\[
\begin{bmatrix}1\\2\\0\end{bmatrix}
\quad \text{and} \quad
\begin{bmatrix}1\\0\\2\end{bmatrix}
\]

\[
\therefore
\left.
\begin{aligned}
\text{Algebraic multiplicity of }-1&=2\\
\text{geometric multiplicity of }-1&=2
\end{aligned}
\right\}
\tag{1}
\]

Beside the working:

\[
\left.
\begin{aligned}
r&=1\\
n&=3\\
n-r&=3-1=2
\end{aligned}
\right\}
\text{no. of independent sol.}=2
\]

---

## Page 20 — Example concluded: \(\lambda=3\), diagonal matrix and transforming matrix

**Source: PDF page 20**

**ii) For \(\lambda=3\),** \([A-3I]x=0\) gives

\[
\begin{bmatrix}
-12&4&4\\
-8&0&4\\
-16&8&4
\end{bmatrix}
\begin{bmatrix}x_1\\x_2\\x_3\end{bmatrix}
=
\begin{bmatrix}0\\0\\0\end{bmatrix}
\]

By \(\frac{1}{4}R_1,\ \frac{1}{4}R_2,\ \frac{1}{4}R_3\),

\[
\begin{bmatrix}
-3&1&1\\
-2&0&1\\
-4&2&1
\end{bmatrix}
\begin{bmatrix}x_1\\x_2\\x_3\end{bmatrix}
=
\begin{bmatrix}0\\0\\0\end{bmatrix}
\]

\[
R_1\to R_1-R_3
\]

\[
\begin{bmatrix}
1&-1&0\\
-2&0&1\\
-4&2&1
\end{bmatrix}
\begin{bmatrix}x_1\\x_2\\x_3\end{bmatrix}
=
\begin{bmatrix}0\\0\\0\end{bmatrix}
\]

\[
R_2\to R_2+2R_1
\]
\[
R_3\to R_3+4R_1
\]

\[
\begin{bmatrix}
1&-1&0\\
0&-2&1\\
0&-2&1
\end{bmatrix}
\begin{bmatrix}x_1\\x_2\\x_3\end{bmatrix}
=
\begin{bmatrix}0\\0\\0\end{bmatrix}
\]

\[
R_3-R_2
\]

\[
\begin{bmatrix}
1&-1&0\\
0&-2&1\\
0&0&0
\end{bmatrix}
\begin{bmatrix}x_1\\x_2\\x_3\end{bmatrix}
=
\begin{bmatrix}0\\0\\0\end{bmatrix}
\]

\[
\therefore x_1-x_2=0
\]
\[
-2x_2+x_3=0
\]

Put \(x_3=2t\),

\[
\therefore x_2=t
\]
\[
\therefore x_1=t
\]

\[
\therefore X=\begin{bmatrix}t\\t\\2t\end{bmatrix}=t\begin{bmatrix}1\\1\\2\end{bmatrix}
\]

\[
\therefore \text{corresponding to }\lambda=3,\ \text{the eigen vector is }
\begin{bmatrix}1\\1\\2\end{bmatrix}
\]

\[
\left.
\begin{aligned}
\text{For }\lambda=3,\ \text{algebraic multiplicity is }1\\
\text{and geometric multiplicity }=1
\end{aligned}
\right\}
\tag{2}
\]

Beside the working:

\[
\left.
\begin{aligned}
r&=2,\ n=3\\
n-r&=3-2=1
\end{aligned}
\right\}
\therefore \text{no. of independent solution is }1
\]

From (1) & (2), we can prove that \(A\) is diagonalisable.

Thus \(A\) is diagonalised to

\[
D=\begin{bmatrix}
-1&0&0\\
0&-1&0\\
0&0&3
\end{bmatrix}
\]

by transforming matrix

\[
M=\begin{bmatrix}
1&1&1\\
2&0&1\\
0&2&2
\end{bmatrix}
\]

and

\[
M^{-1}AM=D
\]

\[
\left[\therefore
\begin{array}{l}
\text{geometric multiplicity of each eigen value}\\
=\text{algebraic multiplicity of each eigen value}
\end{array}
\right]
\]

---

## End-of-document verification summary

| Check | Result |
|---|---|
| Pages transcribed | 20 of 20 |
| Matrices checked with SymPy | All matrices and characteristic polynomials verified |
| Eigenvalues checked | All examples agree with SymPy |
| Eigenvectors checked | All eigenvectors agree up to non-zero scalar multiples |
| Cayley–Hamilton identities checked | Both verifications are correct |
| Known teacher slips | 6 flagged inline (pages 3, 4, 12, 14, 16, 18) |
| Silent corrections | None |

Full details of uncertainties, teacher slips and verification results are in `04_OCR_Reports/OCR_Review_Report.md`.
