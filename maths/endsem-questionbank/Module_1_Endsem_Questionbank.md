# Start here

**Mathematics for Computer Engineering (2023111)** · University of Mumbai · B.E. CSE (AI &amp; ML) · Semester III · NEP 2020

This page teaches **Module I, Part 1: eigenvalues and eigenvectors** from zero, then walks you through every question from the supplied question bank, one at a time, with the full working.

## How the page works

You do not have to finish it in one sitting. It is cut into **7 short sections**. Each one takes about 5–15 minutes and ends with a *Check yourself* box and a **Mark section done** button. Your ticks are saved in this browser, so you can stop after any section and carry on later.

| Section | What you will be able to do | Time |
|---|---|---|
| 1 · The big idea | Say what an eigenvector and an eigenvalue are, and test one | 8 min |
| 2 · Finding the eigenvalues | Build and solve the characteristic equation | 12 min |
| 3 · Finding the eigenvectors | Row-reduce and read off the vectors, including repeated roots | 15 min |
| 4 · Exam toolkit | Spot the question type, check any answer in 10 seconds, avoid the usual slips | 8 min |
| 5 · Practice 1 | Four questions where all eigenvalues are different | 30 min |
| 6 · Practice 2 | Four questions with a repeated eigenvalue | 35 min |
| 7 · One-page revision | Everything on one screen for the night before | 5 min |

> **In plain words.** If you are short on time, finish Sections 1–4 first. They give you the whole method. Sections 5 and 6 are just that method used on the real questions.

## How to use a practice question

Every question starts under a **black bar** so you always know where one ends and the next begins. Try it on paper first. When you are done, open **Show the full solution** and compare. Each solution is built from the same numbered steps, so you can see exactly where a slip happened.

## Difficulty labels

- **Basic**: the idea in its simplest form.
- **Exam-level**: the standard University standard for this topic.
- **Challenging**: longer arithmetic or a trap.

---

# Section 1 · The big idea

**Goal of this section:** know what an eigenvector and an eigenvalue are, and be able to test whether a given vector is one.

## 1.1 Warm-up: a matrix moves a vector

A **matrix** is a grid of numbers. A **column vector** is a list of numbers stacked vertically, such as \(X=\begin{bmatrix}1\\0\end{bmatrix}\). Multiplying a matrix by a vector gives a new vector, which we write \(AX\).

To do it, take each *row* of \(A\), multiply it entry by entry with the vector, and add:

\[
\begin{bmatrix}4&1\\2&3\end{bmatrix}\begin{bmatrix}1\\0\end{bmatrix}
=\begin{bmatrix}4\cdot1+1\cdot0\\2\cdot1+3\cdot0\end{bmatrix}
=\begin{bmatrix}4\\2\end{bmatrix}
\]

You can picture \(AX\) as the matrix **moving** the arrow \(X\) to a new place: it can stretch it, shrink it, turn it, or flip it.

## 1.2 The special arrows

For most arrows, the move **changes their direction**. But for a few special arrows, the move only **stretches or shrinks them along the same line**. Compare the two cases for the same matrix \(A=\begin{bmatrix}4&1\\2&3\end{bmatrix}\):

<figure class="fig">
<div class="fig-row">
<svg viewBox="0 0 250 250" role="img" aria-label="The vector (1,0) is moved to (4,2), which points in a different direction">
<defs><marker id="a1" markerWidth="8" markerHeight="8" refX="6" refY="4" orient="auto"><path d="M0,0 L8,4 L0,8 z" fill="#0a0a0a"/></marker><marker id="a2" markerWidth="8" markerHeight="8" refX="6" refY="4" orient="auto"><path d="M0,0 L8,4 L0,8 z" fill="#1d4ed8"/></marker></defs>
<line x1="30" y1="220" x2="240" y2="220" stroke="#999" stroke-width="1"/>
<line x1="30" y1="220" x2="30" y2="20" stroke="#999" stroke-width="1"/>
<line x1="30" y1="220" x2="66" y2="220" stroke="#0a0a0a" stroke-width="3" marker-end="url(#a1)"/>
<line x1="30" y1="220" x2="178" y2="144" stroke="#1d4ed8" stroke-width="3" marker-end="url(#a2)"/>
<text x="38" y="238">X = (1, 0)</text>
<text x="112" y="128" class="blue">AX = (4, 2)</text>
<text x="38" y="38" class="bold">Direction changed ✗</text>
</svg>
<svg viewBox="0 0 250 250" role="img" aria-label="The vector (1,1) is moved to (5,5), which lies on the same line and is five times longer">
<defs><marker id="a3" markerWidth="8" markerHeight="8" refX="6" refY="4" orient="auto"><path d="M0,0 L8,4 L0,8 z" fill="#0a0a0a"/></marker><marker id="a4" markerWidth="8" markerHeight="8" refX="6" refY="4" orient="auto"><path d="M0,0 L8,4 L0,8 z" fill="#1d4ed8"/></marker></defs>
<line x1="30" y1="220" x2="240" y2="220" stroke="#999" stroke-width="1"/>
<line x1="30" y1="220" x2="30" y2="20" stroke="#999" stroke-width="1"/>
<line x1="30" y1="220" x2="212" y2="38" stroke="#1d4ed8" stroke-width="3" marker-end="url(#a4)"/>
<line x1="30" y1="220" x2="64" y2="186" stroke="#0a0a0a" stroke-width="4" marker-end="url(#a3)"/>
<text x="74" y="212">X = (1, 1)</text>
<text x="120" y="170" class="blue">AX = (5, 5) = 5·X</text>
<text x="38" y="38" class="bold">Same line, 5× longer ✓</text>
</svg>
</div>
<figcaption>Left: an ordinary arrow gets turned. Right: <b>(1, 1) is an eigenvector</b> of this matrix, and the stretch factor <b>5</b> is its eigenvalue.</figcaption>
</figure>

\[
A\begin{bmatrix}1\\1\end{bmatrix}=\begin{bmatrix}4+1\\2+3\end{bmatrix}=\begin{bmatrix}5\\5\end{bmatrix}=5\begin{bmatrix}1\\1\end{bmatrix}
\]

> **In plain words.** An **eigenvector** is an arrow the matrix does not turn. The **eigenvalue** is the number by which the matrix stretches it. The German word *eigen* means "own": these are the matrix's own special directions.

## 1.3 The definition

> **Definition.** Let \(A\) be an \(n\times n\) (square) matrix. A **non-zero** column vector \(X\) is an **eigenvector** of \(A\) if
> \[AX=\lambda X\]
> for some number \(\lambda\). That number \(\lambda\) (Greek *lambda*) is the **eigenvalue** belonging to \(X\).

Reading it symbol by symbol:

- \(A\): a square matrix. Eigenvalues only exist for square matrices.
- \(X\): the special arrow, a column with \(n\) entries.
- \(\lambda\): one ordinary number (it can be positive, negative or zero). The stretch factor.
- \(AX=\lambda X\): "moving \(X\) gives the same arrow, just scaled".

**Why \(X\) must not be the zero vector.** If \(X=0\), then \(A\cdot0=\lambda\cdot0\) is true for *every* \(\lambda\), so every number would be an eigenvalue of every matrix, which says nothing. So the definition rules zero out.

**Other names your exam may use.** Eigenvalues are also called *characteristic roots*, *latent roots*, *characteristic values* or *proper values*. All mean the same thing.

> **Remember.** Any non-zero multiple of an eigenvector is again an eigenvector: \((1,1)\), \((2,2)\) and \((-3,-3)\) all point along the same line. So an answer like \((1,1)^T\) and an answer like \((2,2)^T\) are the same eigenvector.

## Check yourself: Section 1

<details class="check">
<summary>Try these three, then open to compare</summary>

**(a)** For \(A=\begin{bmatrix}2&0\\0&3\end{bmatrix}\) and \(X=\begin{bmatrix}1\\0\end{bmatrix}\), compute \(AX\). Is \(X\) an eigenvector? What is \(\lambda\)?

**(b)** Is \((1,1)^T\) an eigenvector of \(A=\begin{bmatrix}2&1\\0&3\end{bmatrix}\)?

**(c)** Why is the zero vector never called an eigenvector?

> **Answers.**
> (a) \(AX=(2,0)^T=2X\). Yes, \(\lambda=2\).
> (b) \(A(1,1)^T=(2+1,\,0+3)^T=(3,3)^T=3\,(1,1)^T\). Yes, with \(\lambda=3\).
> (c) \(A\cdot0=\lambda\cdot0\) holds for every \(\lambda\), so it would tell us nothing.

</details>

---

# Section 2 · Finding the eigenvalues

**Goal of this section:** given a matrix, write its characteristic equation and solve it for \(\lambda\).

## 2.1 The idea: turn it into an equation we can solve

We want every \(\lambda\) for which \(AX=\lambda X\) has a non-zero solution \(X\). The unknown \(X\) appears on both sides, so move everything to one side:

\[
AX-\lambda X=0\quad\Longrightarrow\quad(A-\lambda I)X=0
\]

Here \(I\) is the **identity matrix** (1s on the diagonal, 0s elsewhere). We need it because you cannot subtract a plain number from a matrix: \(\lambda I\) is the matrix with \(\lambda\) down the diagonal.

Now the key fact. The system \((A-\lambda I)X=0\) has a non-zero solution **only when** the matrix \(A-\lambda I\) is *singular*, which means its **determinant is zero**. That gives the central equation of this module:

> **Characteristic equation.** \(\;|A-\lambda I|=0\)
> - \(A-\lambda I\) is the **characteristic matrix**.
> - Expanding \(|A-\lambda I|\) gives the **characteristic polynomial**.
> - Its roots are the **eigenvalues**.

**How many eigenvalues?** A \(2\times2\) matrix gives a degree-2 equation, so 2 eigenvalues. A \(3\times3\) matrix gives a degree-3 equation, so 3 eigenvalues (some may repeat).

## 2.2 Example: a 2×2 matrix

Take the same matrix as before, \(A=\begin{bmatrix}4&1\\2&3\end{bmatrix}\). Subtract \(\lambda\) from the diagonal and take the determinant (a \(2\times2\) determinant is *main diagonal product minus other diagonal product*):

\[
\begin{vmatrix}4-\lambda&1\\2&3-\lambda\end{vmatrix}=(4-\lambda)(3-\lambda)-(1)(2)=\lambda^{2}-7\lambda+10=0
\]

Factorise: two numbers that multiply to 10 and add to 7 are 5 and 2.

\[
(\lambda-5)(\lambda-2)=0\quad\Longrightarrow\quad\lambda=5\ \text{ or }\ \lambda=2
\]

The 5 matches what we found in Section 1. The matrix has a second special stretch, 2.

## 2.3 The teacher's shortcut (use this for every 3×3)

Expanding a \(3\times3\) determinant with \(\lambda\) in it is slow and error-prone. Your teacher's notes use a formula that skips it:

\[
\boxed{\;\lambda^{3}-S_1\lambda^{2}+S_2\lambda-|A|=0\;}
\]

| Symbol | What it is | How to get it |
|---|---|---|
| \(S_1\) | **Sum of the diagonal** (the trace) | \(a_{11}+a_{22}+a_{33}\) |
| \(S_2\) | **Sum of the three diagonal minors** | Cross out row 1 and column 1, take the \(2\times2\) determinant that is left. Repeat for row 2 / column 2, then row 3 / column 3. Add the three. |
| \(\lvert A\rvert\) | The determinant of \(A\) | Expand along any row |

For a \(2\times2\) matrix the same idea is \(\lambda^{2}-S_1\lambda+|A|=0\). Check it on our example: \(S_1=4+3=7\) and \(|A|=12-2=10\), which gives \(\lambda^2-7\lambda+10\). ✓

<figure class="fig">
<div class="flow">
<span>Matrix \(A\)</span><i>→</i><span>\(S_1,\ S_2,\ |A|\)</span><i>→</i><span>Equation \(\lambda^3-S_1\lambda^2+S_2\lambda-|A|=0\)</span><i>→</i><span>Roots \(\lambda_1,\lambda_2,\lambda_3\)</span>
</div>
<figcaption>The whole eigenvalue step in one line.</figcaption>
</figure>

## 2.4 Solving the cubic

Your cubic will almost always have whole-number roots. Try \(\lambda=\pm1,\pm2,\pm3,\dots\), numbers that divide the last term. If \(\lambda=a\) makes the polynomial zero, then \((\lambda-a)\) is a factor. Divide it out and you are left with a quadratic.

**Example.** \(\lambda^3-6\lambda^2+11\lambda-6\). Try \(\lambda=1\): \(1-6+11-6=0\) ✓. Divide by \((\lambda-1)\):

\[
\lambda^3-6\lambda^2+11\lambda-6=(\lambda-1)(\lambda^2-5\lambda+6)=(\lambda-1)(\lambda-2)(\lambda-3)
\]

So \(\lambda=1,2,3\).

## 2.5 The two free checks

If the roots are \(\lambda_1,\lambda_2,\lambda_3\), then **always**

\[
\lambda_1+\lambda_2+\lambda_3=S_1,\qquad\lambda_1\lambda_2\lambda_3=|A|
\]

For \(1,2,3\): sum \(=6=S_1\) and product \(=6=|A|\) ✓. If your roots fail either check, the equation is wrong. Do this every time; it takes ten seconds and saves whole questions.

## Check yourself: Section 2

<details class="check">
<summary>Try these, then open to compare</summary>

**(a)** For the triangular matrix \(A=\begin{bmatrix}3&1\\0&2\end{bmatrix}\), find the eigenvalues using \(S_1\) and \(|A|\).

**(b)** A \(3\times3\) matrix has \(S_1=6\), \(S_2=11\), \(|A|=6\). Write its characteristic equation and say why \(\lambda=1\) is a root.

> **Answers.**
> (a) \(S_1=5\), \(|A|=6\), so \(\lambda^2-5\lambda+6=0\), giving \(\lambda=2,3\). (For a triangular matrix the eigenvalues are just the diagonal entries.)
> (b) \(\lambda^3-6\lambda^2+11\lambda-6=0\). At \(\lambda=1\): \(1-6+11-6=0\).

</details>

---

# Section 3 · Finding the eigenvectors

**Goal of this section:** for each eigenvalue, find its eigenvector(s) by row reduction, and know how many to expect.

## 3.1 The recipe

Once \(\lambda\) is known, its eigenvectors are the non-zero solutions of \((A-\lambda I)X=0\). The teacher's seven steps, with the reasons:

1. **Write the characteristic equation** \(|A-\lambda I|=0\) (Section 2).
2. **Solve it** to get the eigenvalues.
3. **Pick one eigenvalue** and write \((A-\lambda I)X=0\): subtract \(\lambda\) from the diagonal.
4. **Row-reduce.** Only three moves are allowed: swap two rows, multiply a row by a non-zero number, add a multiple of one row to another. Aim for as many zero rows as you can get.
5. **Count the free parameters.** If there are \(n\) unknowns and \(r\) rows survive (the **rank**), there are \(n-r\) free parameters.
6. **Cramer's rule** can be quicker for small systems (see Example B for the idea).
7. **Read off the vectors.** Give each free parameter the value 1 in turn (the others 0).

<figure class="fig">
<div class="flow">
<span>Eigenvalue \(\lambda\)</span><i>→</i><span>Form \(A-\lambda I\)</span><i>→</i><span>Row-reduce</span><i>→</i><span>Count \(n-r\)</span><i>→</i><span>Eigenvectors</span>
</div>
<figcaption>Repeat this once for every different eigenvalue.</figcaption>
</figure>

## 3.2 How many eigenvectors does a root give?

This is the step beginners skip. It decides everything.

| Rank \(r\) of \(A-\lambda I\) (3×3) | Free parameters \(n-r\) | Independent eigenvectors |
|---|---|---|
| 2 | 1 | **1** (the usual case) |
| 1 | 2 | **2** (the equations collapse to a single one) |
| 0 | 3 | 3 (only when \(A=\lambda I\)) |

**Example of reading it off.** Suppose row reduction gives \(\begin{bmatrix}1&0&-1\\0&1&2\\0&0&0\end{bmatrix}\). Two rows survive, so \(r=2\) and \(n-r=1\). The equations say \(x_1=x_3\) and \(x_2=-2x_3\), so every eigenvector is a multiple of \((1,-2,1)^T\). Listing two "different" vectors here would be a mistake, because they would point the same way.

## 3.3 Example A: finish the 2×2 matrix

In Section 2 we found \(\lambda=5\) and \(\lambda=2\) for \(A=\begin{bmatrix}4&1\\2&3\end{bmatrix}\).

#### Step 1 · Eigenvector for \(\lambda=5\)

Subtract 5 from the diagonal:

\[
A-5I=\begin{bmatrix}-1&1\\2&-2\end{bmatrix}\quad\Longrightarrow\quad -x_1+x_2=0,\quad 2x_1-2x_2=0
\]

The second row is just \(-2\times\) the first, so only **one** equation survives: \(x_2=x_1\). Rank \(r=1\), so \(n-r=2-1=1\) free parameter. Put \(x_1=t\), then \(x_2=t\):

\[
X_1=t\begin{bmatrix}1\\1\end{bmatrix}\quad\text{take }t=1:\ X_1=(1,1)^T
\]

#### Step 2 · Eigenvector for \(\lambda=2\)

\[
A-2I=\begin{bmatrix}2&1\\2&1\end{bmatrix}\quad\Longrightarrow\quad 2x_1+x_2=0\ \Rightarrow\ x_2=-2x_1
\]

Again one free parameter: \(X_2=t(1,-2)^T\), so take \(X_2=(1,-2)^T\).

#### Step 3 · Verify by substitution

This is not optional: it is the only real proof the answer is right.

\[
A\begin{bmatrix}1\\1\end{bmatrix}=\begin{bmatrix}5\\5\end{bmatrix}=5\begin{bmatrix}1\\1\end{bmatrix}\ \checkmark\qquad
A\begin{bmatrix}1\\-2\end{bmatrix}=\begin{bmatrix}2\\-4\end{bmatrix}=2\begin{bmatrix}1\\-2\end{bmatrix}\ \checkmark
\]

> **Answer.**
>
> | Eigenvalue \(\lambda\) | Eigenvector \(X\) |
> |---|---|
> | 5 | \((1,1)^T\) |
> | 2 | \((1,-2)^T\) |

## 3.4 Example B: a 3×3 matrix with a repeated eigenvalue

> **Question.** Find the eigenvalues and eigenvectors of \(A=\begin{bmatrix}0&1&1\\1&0&1\\1&1&0\end{bmatrix}\).

#### Step 1 · The three numbers

\[
S_1=0+0+0=0,\qquad
S_2=\begin{vmatrix}0&1\\1&0\end{vmatrix}+\begin{vmatrix}0&1\\1&0\end{vmatrix}+\begin{vmatrix}0&1\\1&0\end{vmatrix}=-1-1-1=-3
\]

Expanding \(|A|\) along the first row: \(|A|=0-1(0-1)+1(1-0)=1+1=2\).

#### Step 2 · Equation and roots

\[
\lambda^{3}-3\lambda-2=0
\]

Try \(\lambda=2\): \(8-6-2=0\) ✓, so \((\lambda-2)\) is a factor:

\[
\lambda^3-3\lambda-2=(\lambda-2)(\lambda+1)^2\quad\Longrightarrow\quad\lambda=2,\ -1,\ -1
\]

Check: \(2-1-1=0=S_1\) ✓ and \(2\cdot(-1)(-1)=2=|A|\) ✓.

#### Step 3 · Eigenvector for \(\lambda=2\)

\[
A-2I=\begin{bmatrix}-2&1&1\\1&-2&1\\1&1&-2\end{bmatrix}
\]

Subtract row 2 from row 1: \(-3x_1+3x_2=0\), so \(x_1=x_2\). Put that in row 3: \(2x_1-2x_3=0\), so \(x_3=x_1\). All three entries are equal. Rank 2, one parameter: \(X=(1,1,1)^T\).

#### Step 4 · Eigenvectors for \(\lambda=-1\) (the repeated root)

\[
A+I=\begin{bmatrix}1&1&1\\1&1&1\\1&1&1\end{bmatrix}\ \longrightarrow\ \begin{bmatrix}1&1&1\\0&0&0\\0&0&0\end{bmatrix}
\]

Every row says the same thing: \(x_1+x_2+x_3=0\). Rank 1, so \(n-r=3-1=2\) free parameters, which means **two** independent eigenvectors. Solve \(x_1=-x_2-x_3\) and give the free parameters the values (1, 0) and (0, 1):

- \(x_2=1,\ x_3=0\ \Rightarrow\ x_1=-1\): \((-1,1,0)^T\)
- \(x_2=0,\ x_3=1\ \Rightarrow\ x_1=-1\): \((-1,0,1)^T\)

#### Step 5 · Verify

\[
A\begin{bmatrix}-1\\1\\0\end{bmatrix}=\begin{bmatrix}1\\-1\\0\end{bmatrix}=-1\begin{bmatrix}-1\\1\\0\end{bmatrix}\ \checkmark\quad
A\begin{bmatrix}-1\\0\\1\end{bmatrix}=\begin{bmatrix}1\\0\\-1\end{bmatrix}\ \checkmark\quad
A\begin{bmatrix}1\\1\\1\end{bmatrix}=\begin{bmatrix}2\\2\\2\end{bmatrix}=2\begin{bmatrix}1\\1\\1\end{bmatrix}\ \checkmark
\]

> **Answer.**
>
> | Eigenvalue \(\lambda\) | Eigenvectors |
> |---|---|
> | 2 | \((1,1,1)^T\) |
> | \(-1\) (repeated) | \((-1,1,0)^T\) and \((-1,0,1)^T\) |

> **What this example teaches.** A repeated eigenvalue is *not* automatically a problem. Here the rank dropped to 1, which gave two vectors, as many as the repeat count. A matrix like \(B=\begin{bmatrix}3&1&0\\0&3&0\\0&0&5\end{bmatrix}\) has \(\lambda=3\) twice, but \(B-3I\) has rank 2, so it gives only one eigenvector for that value. That gap is what "not diagonalisable" means later (Part 4).

## Check yourself: Section 3

<details class="check">
<summary>Try these, then open to compare</summary>

**(a)** A \(3\times3\) matrix has \(A-\lambda I\) of rank 1. How many independent eigenvectors does that \(\lambda\) have?

**(b)** Row reduction of \(A-\lambda I\) gives the single equation \(x_1+x_2+x_3=0\). Write two independent eigenvectors.

**(c)** After finding a vector \(X\), what is the one check that proves it is correct?

> **Answers.**
> (a) \(n-r=3-1=2\).
> (b) For example \((-1,1,0)^T\) and \((-1,0,1)^T\). Any two independent solutions are fine.
> (c) Compute \(AX\) and confirm it equals \(\lambda X\).

</details>

---

# Section 4 · Exam toolkit

**Goal of this section:** recognise the type of question straight away, check any answer in ten seconds, and dodge the common slips.

## 4.1 The four types

Your teacher sorts every question with two yes/no tests: is the matrix **symmetric** (\(A=A^T\), the grid is a mirror image across the diagonal), and are the eigenvalues **distinct or repeated**? The method never changes. Only the number of eigenvectors for a repeated root changes.

| | **Non-symmetric** | **Symmetric** |
|---|---|---|
| **All eigenvalues distinct** | **Type I** · one vector per root | **Type II** · one vector per root; vectors of different roots are perpendicular |
| **A repeated eigenvalue** | **Type III** · a repeated root may give 1 or 2 vectors: compute \(n-r\) | **Type IV** · a repeated root always gives 2 vectors |

Section 5 uses Types I and II. Section 6 uses Types III and IV.

## 4.2 Checking an answer in ten seconds

1. **Substitute.** Compute \(AX\) for each vector. It must equal \(\lambda X\).
2. **Add the roots.** They must equal the trace \(S_1\).
3. **Multiply the roots.** They must equal \(|A|\).
4. **Triangular matrix?** If everything above or below the diagonal is zero, the eigenvalues are the diagonal entries, with no determinant needed.
5. **\(|A|=0\)?** Then at least one eigenvalue is \(0\). That is a real answer, not an error.

## 4.3 Common mistakes

| Mistake | What it looks like | The fix |
|---|---|---|
| Sign slip | \(\lambda^2-7\lambda-10\) instead of \(+10\) | Check sum and product of roots against \(S_1\) and \(|A|\) |
| Wrong \(S_2\) | Adding all nine minors | Only the **three diagonal** \(2\times2\) minors |
| Stopping at one vector | One vector for a root with rank 1 | Compute \(n-r\); if it is 2, give two vectors |
| Listing the same direction twice | \((1,1,1)\) and \((2,2,2)\) as a pair | Use independent parameters |
| Zero vector as an answer | "\(X=0\)" | Eigenvectors are never zero |
| Dividing by something that might be 0 | Cancelling a symbol | Only divide by known non-zero numbers |

## 4.4 Which method for which question?

| If the question gives… | Do this |
|---|---|
| a \(2\times2\) matrix | \(\lambda^2-S_1\lambda+|A|=0\), then one row reduction per root |
| a \(3\times3\) with distinct roots | \(S_1,S_2,|A|\), factor, one row reduction per root |
| a \(3\times3\) with a repeated root | Same, then compute \(n-r\) for the repeated root |
| a triangular matrix | Diagonal gives the eigenvalues |
| an expression such as \(A^2-2A+I\) | Do not multiply matrices. This is Part 2 (not yet written) |

## Check yourself: Section 4

<details class="check">
<summary>Try these, then open to compare</summary>

**(a)** Write down the eigenvalues of \(\begin{bmatrix}3&5&7\\0&-2&4\\0&0&6\end{bmatrix}\) and their product.

**(b)** Is \(\begin{bmatrix}2&2&1\\1&3&1\\1&2&2\end{bmatrix}\) symmetric?

> **Answers.**
> (a) Triangular, so \(\lambda=3,-2,6\). Product \(=-36=|A|\).
> (b) No: the entry in row 1, column 2 is 2 but in row 2, column 1 it is 1. It is a non-symmetric matrix (Type I or III).

</details>

---

# Section 5 · Practice 1: all eigenvalues different

**Goal of this section:** solve four full questions where the three eigenvalues are distinct, so every root gives exactly one eigenvector.

**Source:** `musa-question-bank-2026.pdf`, page 1, "MODULE 1 → Eigen Value and Eigen Vector", Q.1. The bank prints no marks, so none are invented.

> **Numbering note.** The bank prints the sixth matrix as "v)" a second time. It is a printing slip in the source, not a merged question. Both matrices are kept and each has its own question here.

## Question 1 · Bank Q.1 i) · Type I · Basic

> **Find the eigenvalues and eigenvectors of** \(A=\begin{bmatrix}2&-1&1\\1&2&-1\\1&-1&2\end{bmatrix}\)

> **What to expect.** Non-symmetric with distinct eigenvalues, so three roots and one vector each. This is exactly the teacher's own worked example (notes pp. 2–4).

<details class="solution">
<summary>I have tried it on paper: show the full solution</summary>

#### Step 1 · Characteristic equation

\[
S_1=2+2+2=6,\qquad S_2=(4-1)+(4-1)+(4+1)=3+3+5=11,\qquad |A|=6
\]
\[
\lambda^{3}-6\lambda^{2}+11\lambda-6=0
\]

#### Step 2 · Roots

\(\lambda=1\) works (\(1-6+11-6=0\)), so

\[
(\lambda-1)(\lambda-2)(\lambda-3)=0\quad\Longrightarrow\quad\lambda=1,\,2,\,3
\]

Check: \(1+2+3=6=S_1\) ✓ and \(1\cdot2\cdot3=6=|A|\) ✓.

#### Step 3 · Eigenvectors

**For \(\lambda=1\):**
\[
A-I=\begin{bmatrix}1&-1&1\\1&1&-1\\1&-1&1\end{bmatrix}\xrightarrow{R_2-R_1}\begin{bmatrix}1&-1&1\\0&2&-2\\0&0&0\end{bmatrix}
\]
\(2x_2-2x_3=0\) gives \(x_2=x_3\). Then \(x_1-x_2+x_3=0\) gives \(x_1=0\). Take \(x_3=1\): \(X_1=(0,1,1)^T\).

**For \(\lambda=2\):**
\[
A-2I=\begin{bmatrix}0&-1&1\\1&0&-1\\1&-1&0\end{bmatrix}\longrightarrow\begin{bmatrix}1&0&-1\\0&-1&1\\0&0&0\end{bmatrix}
\]
\(x_1=x_3\) and \(x_2=x_3\). Take \(x_3=1\): \(X_2=(1,1,1)^T\).

**For \(\lambda=3\):**
\[
A-3I=\begin{bmatrix}-1&-1&1\\1&-1&-1\\1&-1&-1\end{bmatrix}\longrightarrow\begin{bmatrix}1&1&-1\\0&-2&0\\0&0&0\end{bmatrix}
\]
\(x_2=0\), then \(x_1=x_3\). Take \(x_3=1\): \(X_3=(1,0,1)^T\).

#### Step 4 · Verify

\[
A\begin{bmatrix}0\\1\\1\end{bmatrix}=\begin{bmatrix}0\\1\\1\end{bmatrix}\ \checkmark\qquad
A\begin{bmatrix}1\\1\\1\end{bmatrix}=\begin{bmatrix}2\\2\\2\end{bmatrix}\ \checkmark\qquad
A\begin{bmatrix}1\\0\\1\end{bmatrix}=\begin{bmatrix}3\\0\\3\end{bmatrix}\ \checkmark
\]

> **Answer.**
>
> | Eigenvalue \(\lambda\) | Eigenvector \(X\) |
> |---|---|
> | 1 | \((0,1,1)^T\) |
> | 2 | \((1,1,1)^T\) |
> | 3 | \((1,0,1)^T\) |

</details>

## Question 2 · Bank Q.1 v) · Type II · Exam-level

> **Find the eigenvalues and eigenvectors of** \(A=\begin{bmatrix}8&-6&2\\-6&7&-4\\2&-4&3\end{bmatrix}\)

> **What to expect.** Symmetric with distinct eigenvalues (Type II, the teacher's own example). Here \(|A|=0\), so one eigenvalue will be **0**. Do not panic: zero is a perfectly good eigenvalue.

<details class="solution">
<summary>I have tried it on paper: show the full solution</summary>

#### Step 1 · Characteristic equation

\[
S_1=8+7+3=18,\qquad S_2=(56-36)+(24-4)+(21-16)=20+20+5=45,\qquad |A|=0
\]
\[
\lambda^{3}-18\lambda^{2}+45\lambda=0
\]

#### Step 2 · Roots

Take out a common \(\lambda\): \(\lambda(\lambda^2-18\lambda+45)=\lambda(\lambda-3)(\lambda-15)\), so \(\lambda=0,\,3,\,15\).

Check: \(0+3+15=18=S_1\) ✓ and \(0\cdot3\cdot15=0=|A|\) ✓.

#### Step 3 · Eigenvectors

**For \(\lambda=0\)** (use \(A\) itself):
\[
\begin{bmatrix}8&-6&2\\-6&7&-4\\2&-4&3\end{bmatrix}\longrightarrow\begin{bmatrix}1&0&-1/2\\0&1&-1\\0&0&0\end{bmatrix}
\]
\(x_1=\tfrac12x_3\) and \(x_2=x_3\). Take \(x_3=2\): \(X_1=(1,2,2)^T\).

**For \(\lambda=3\):**
\[
A-3I=\begin{bmatrix}5&-6&2\\-6&4&-4\\2&-4&0\end{bmatrix}\longrightarrow\begin{bmatrix}1&0&1\\0&1&1/2\\0&0&0\end{bmatrix}
\]
\(x_1=-x_3\) and \(x_2=-\tfrac12x_3\). Take \(x_3=-2\): \(X_2=(2,1,-2)^T\).

**For \(\lambda=15\):**
\[
A-15I=\begin{bmatrix}-7&-6&2\\-6&-8&-4\\2&-4&-12\end{bmatrix}\longrightarrow\begin{bmatrix}1&0&-2\\0&1&2\\0&0&0\end{bmatrix}
\]
\(x_1=2x_3\) and \(x_2=-2x_3\). Take \(x_3=1\): \(X_3=(2,-2,1)^T\).

#### Step 4 · Verify

\[
A\begin{bmatrix}1\\2\\2\end{bmatrix}=\begin{bmatrix}0\\0\\0\end{bmatrix}=0\cdot X\ \checkmark\qquad
A\begin{bmatrix}2\\1\\-2\end{bmatrix}=\begin{bmatrix}6\\3\\-6\end{bmatrix}=3X\ \checkmark\qquad
A\begin{bmatrix}2\\-2\\1\end{bmatrix}=\begin{bmatrix}30\\-30\\15\end{bmatrix}=15X\ \checkmark
\]

> **Bonus check (Type II only).** In a symmetric matrix the eigenvectors of different eigenvalues are perpendicular. For example \((1,2,2)\cdot(2,1,-2)=2+2-4=0\). If this fails for a symmetric matrix, you have a slip.

> **Answer.**
>
> | Eigenvalue \(\lambda\) | Eigenvector \(X\) |
> |---|---|
> | 0 | \((1,2,2)^T\) |
> | 3 | \((2,1,-2)^T\) |
> | 15 | \((2,-2,1)^T\) |

</details>

## Question 3 · Bank Q.1 v) printed a second time · Type II · Exam-level

> **Find the eigenvalues and eigenvectors of** \(A=\begin{bmatrix}1&0&0\\0&3&-1\\0&-1&3\end{bmatrix}\)

> **What to expect.** Symmetric with distinct roots. The first row and column hold only a single 1, so the matrix splits into a \(1\times1\) block and a \(2\times2\) block. That makes this one quick.

<details class="solution">
<summary>I have tried it on paper: show the full solution</summary>

#### Step 1 · Characteristic equation

\[
S_1=1+3+3=7,\qquad S_2=(3-0)+(3-0)+(9-1)=3+3+8=14,\qquad |A|=1\cdot(9-1)=8
\]
\[
\lambda^{3}-7\lambda^{2}+14\lambda-8=0
\]

#### Step 2 · Roots

\(\lambda=1\) works (\(1-7+14-8=0\)), leaving \(\lambda^2-6\lambda+8=(\lambda-2)(\lambda-4)\):

\[
\lambda=1,\,2,\,4
\]

Check: \(1+2+4=7=S_1\) ✓ and \(1\cdot2\cdot4=8=|A|\) ✓.

#### Step 3 · Eigenvectors

**For \(\lambda=1\):** \(A-I=\begin{bmatrix}0&0&0\\0&2&-1\\0&-1&2\end{bmatrix}\). The first row is all zeros, so \(x_1\) is free. The other two rows force \(2x_2-x_3=0\) and \(-x_2+2x_3=0\), whose only solution is \(x_2=x_3=0\). So \(X_1=(1,0,0)^T\).

**For \(\lambda=2\):** \(A-2I=\begin{bmatrix}-1&0&0\\0&1&-1\\0&-1&1\end{bmatrix}\) gives \(x_1=0\) and \(x_2=x_3\). So \(X_2=(0,1,1)^T\).

**For \(\lambda=4\):** \(A-4I=\begin{bmatrix}-3&0&0\\0&-1&-1\\0&-1&-1\end{bmatrix}\) gives \(x_1=0\) and \(x_2=-x_3\). So \(X_3=(0,1,-1)^T\).

#### Step 4 · Verify

\[
A\begin{bmatrix}1\\0\\0\end{bmatrix}=\begin{bmatrix}1\\0\\0\end{bmatrix}\ \checkmark\qquad
A\begin{bmatrix}0\\1\\1\end{bmatrix}=\begin{bmatrix}0\\2\\2\end{bmatrix}=2X\ \checkmark\qquad
A\begin{bmatrix}0\\1\\-1\end{bmatrix}=\begin{bmatrix}0\\4\\-4\end{bmatrix}=4X\ \checkmark
\]

> **Answer.**
>
> | Eigenvalue \(\lambda\) | Eigenvector \(X\) |
> |---|---|
> | 1 | \((1,0,0)^T\) |
> | 2 | \((0,1,1)^T\) |
> | 4 | \((0,1,-1)^T\) |

</details>

## Question 4 · Practice paper (Winter 2025) Q.4 b) · Type II · Exam-level · 5 marks

> **Find the eigenvalues and eigenvectors of** \(A=\begin{bmatrix}3&-1&1\\-1&5&-1\\1&-1&3\end{bmatrix}\)

> **What to expect.** Symmetric with distinct roots. This is from the **2025 practice paper**, not the 2026 bank, and it prints 5 marks. Give it about 8 minutes.

<details class="solution">
<summary>I have tried it on paper: show the full solution</summary>

#### Step 1 · Characteristic equation

\[
S_1=3+5+3=11,\qquad S_2=(15-1)+(9-1)+(15-1)=14+8+14=36,\qquad |A|=36
\]
\[
\lambda^{3}-11\lambda^{2}+36\lambda-36=0
\]

#### Step 2 · Roots

\(\lambda=2\) works (\(8-44+72-36=0\)), leaving \(\lambda^2-9\lambda+18=(\lambda-3)(\lambda-6)\):

\[
\lambda=2,\,3,\,6
\]

Check: \(2+3+6=11=S_1\) ✓ and \(2\cdot3\cdot6=36=|A|\) ✓.

#### Step 3 · Eigenvectors

**For \(\lambda=2\):**
\[
A-2I=\begin{bmatrix}1&-1&1\\-1&3&-1\\1&-1&1\end{bmatrix}\longrightarrow\begin{bmatrix}1&-1&1\\0&2&0\\0&0&0\end{bmatrix}
\]
\(x_2=0\), then \(x_1=-x_3\). Take \(x_3=-1\): \(X_1=(1,0,-1)^T\) (or \((-1,0,1)^T\); same direction).

**For \(\lambda=3\):**
\[
A-3I=\begin{bmatrix}0&-1&1\\-1&2&-1\\1&-1&0\end{bmatrix}\longrightarrow\begin{bmatrix}1&0&-1\\0&1&-1\\0&0&0\end{bmatrix}
\]
\(x_1=x_3\) and \(x_2=x_3\). So \(X_2=(1,1,1)^T\).

**For \(\lambda=6\):**
\[
A-6I=\begin{bmatrix}-3&-1&1\\-1&-1&-1\\1&-1&-3\end{bmatrix}\longrightarrow\begin{bmatrix}1&0&-1\\0&1&2\\0&0&0\end{bmatrix}
\]
\(x_1=x_3\) and \(x_2=-2x_3\). So \(X_3=(1,-2,1)^T\).

#### Step 4 · Verify

\[
A\begin{bmatrix}1\\0\\-1\end{bmatrix}=\begin{bmatrix}2\\0\\-2\end{bmatrix}=2X\ \checkmark\qquad
A\begin{bmatrix}1\\1\\1\end{bmatrix}=\begin{bmatrix}3\\3\\3\end{bmatrix}=3X\ \checkmark\qquad
A\begin{bmatrix}1\\-2\\1\end{bmatrix}=\begin{bmatrix}6\\-12\\6\end{bmatrix}=6X\ \checkmark
\]

> **Answer.**
>
> | Eigenvalue \(\lambda\) | Eigenvector \(X\) |
> |---|---|
> | 2 | \((1,0,-1)^T\) |
> | 3 | \((1,1,1)^T\) |
> | 6 | \((1,-2,1)^T\) |

</details>

> **Source note on the practice paper.** Its printed instructions say "Attempt any three questions from Q.2 to Q.5", but the paper also contains a Q.6, and the official pattern is three answers out of six questions with Q.1 compulsory. This is recorded, not silently corrected.

## Check yourself: Section 5

<details class="check">
<summary>Open when you have finished all four questions</summary>

- Did you check **sum of roots = trace** and **product = determinant** *before* row-reducing?
- In Question 2, did you expect a zero eigenvalue as soon as you saw \(|A|=0\)?
- In Question 3, did you notice the matrix splits into blocks, so the first eigenvector is just \((1,0,0)^T\)?
- Did you substitute at least one vector back into \(AX=\lambda X\)?

If any answer is "no", redo that part of the question once. That habit is worth more marks than any shortcut.

</details>

---

# Section 6 · Practice 2: a repeated eigenvalue

**Goal of this section:** solve four questions where one eigenvalue appears twice, and decide whether that root gives one vector or two.

> **The rule that decides everything.** For a repeated root, compute \(n-r\) from the rank of \(A-\lambda I\). In every question below the rank drops to **1**, so the repeated root gets **two** independent eigenvectors and the equations collapse to a single equation.

## Question 5 · Bank Q.1 ii) · Type III · Exam-level

> **Find the eigenvalues and eigenvectors of** \(A=\begin{bmatrix}2&2&1\\1&3&1\\1&2&2\end{bmatrix}\)

> **What to expect.** Non-symmetric with a repeated root (the teacher's Type III example, notes pp. 7–8).

<details class="solution">
<summary>I have tried it on paper: show the full solution</summary>

#### Step 1 · Characteristic equation

\[
S_1=2+3+2=7,\qquad S_2=(6-2)+(4-1)+(6-2)=4+3+4=11,\qquad |A|=5
\]
\[
\lambda^{3}-7\lambda^{2}+11\lambda-5=0
\]

#### Step 2 · Roots

\(\lambda=1\) works (\(1-7+11-5=0\)), leaving \(\lambda^2-6\lambda+5=(\lambda-1)(\lambda-5)\):

\[
(\lambda-5)(\lambda-1)^{2}=0\quad\Longrightarrow\quad\lambda=5,\ 1,\ 1
\]

Check: \(5+1+1=7=S_1\) ✓ and \(5\cdot1\cdot1=5=|A|\) ✓.

#### Step 3 · Eigenvectors

**For \(\lambda=5\):**
\[
A-5I=\begin{bmatrix}-3&2&1\\1&-2&1\\1&2&-3\end{bmatrix}\longrightarrow\begin{bmatrix}1&-2&1\\0&-4&4\\0&4&-4\end{bmatrix}
\]
Rank 2, one parameter. \(x_2=x_3\) and \(x_1=2x_2-x_3=x_2\). So \(X_3=(1,1,1)^T\).

**For \(\lambda=1\) (repeated):**
\[
A-I=\begin{bmatrix}1&2&1\\1&2&1\\1&2&1\end{bmatrix}\longrightarrow\begin{bmatrix}1&2&1\\0&0&0\\0&0&0\end{bmatrix}
\]
Three identical rows, so rank 1 and \(n-r=2\): **two** eigenvectors. The one equation is \(x_1+2x_2+x_3=0\).

- \(x_2=1,\ x_3=0\ \Rightarrow\ x_1=-2\): \(X_1=(-2,1,0)^T\)
- \(x_2=0,\ x_3=1\ \Rightarrow\ x_1=-1\): \(X_2=(-1,0,1)^T\)

#### Step 4 · Verify

\[
A\begin{bmatrix}1\\1\\1\end{bmatrix}=\begin{bmatrix}5\\5\\5\end{bmatrix}\ \checkmark\qquad
A\begin{bmatrix}-2\\1\\0\end{bmatrix}=\begin{bmatrix}-2\\1\\0\end{bmatrix}\ \checkmark\qquad
A\begin{bmatrix}-1\\0\\1\end{bmatrix}=\begin{bmatrix}-1\\0\\1\end{bmatrix}\ \checkmark
\]

> **Answer.**
>
> | Eigenvalue \(\lambda\) | Eigenvectors |
> |---|---|
> | 5 | \((1,1,1)^T\) |
> | 1 (repeated) | \((-2,1,0)^T\) and \((-1,0,1)^T\) |

</details>

## Question 6 · Bank Q.1 iii) · Type III · Exam-level

> **Find the eigenvalues and eigenvectors of** \(A=\begin{bmatrix}2&1&1\\2&3&2\\3&3&4\end{bmatrix}\)

> **What to expect.** Non-symmetric with a repeated root. Note the three rows of \(A-I\) are multiples of each other, which is how you can spot rank 1 at a glance.

<details class="solution">
<summary>I have tried it on paper: show the full solution</summary>

#### Step 1 · Characteristic equation

\[
S_1=2+3+4=9,\qquad S_2=(6-2)+(8-3)+(12-6)=4+5+6=15,\qquad |A|=7
\]
\[
\lambda^{3}-9\lambda^{2}+15\lambda-7=0
\]

#### Step 2 · Roots

\(\lambda=1\) works (\(1-9+15-7=0\)), leaving \(\lambda^2-8\lambda+7=(\lambda-1)(\lambda-7)\):

\[
(\lambda-7)(\lambda-1)^{2}=0\quad\Longrightarrow\quad\lambda=7,\ 1,\ 1
\]

Check: \(7+1+1=9=S_1\) ✓ and \(7\cdot1\cdot1=7=|A|\) ✓.

#### Step 3 · Eigenvectors

**For \(\lambda=7\):**
\[
A-7I=\begin{bmatrix}-5&1&1\\2&-4&2\\3&3&-3\end{bmatrix}\longrightarrow\begin{bmatrix}1&0&-1/3\\0&1&-2/3\\0&0&0\end{bmatrix}
\]
\(x_1=\tfrac13x_3\) and \(x_2=\tfrac23x_3\). Take \(x_3=3\): \(X_3=(1,2,3)^T\).

**For \(\lambda=1\) (repeated):**
\[
A-I=\begin{bmatrix}1&1&1\\2&2&2\\3&3&3\end{bmatrix}\longrightarrow\begin{bmatrix}1&1&1\\0&0&0\\0&0&0\end{bmatrix}
\]
Rank 1, so two eigenvectors. The equation is \(x_1+x_2+x_3=0\).

- \(x_2=1,\ x_3=0\): \(X_1=(-1,1,0)^T\)
- \(x_2=0,\ x_3=1\): \(X_2=(-1,0,1)^T\)

#### Step 4 · Verify

\[
A\begin{bmatrix}1\\2\\3\end{bmatrix}=\begin{bmatrix}7\\14\\21\end{bmatrix}=7X\ \checkmark\qquad
A\begin{bmatrix}-1\\1\\0\end{bmatrix}=\begin{bmatrix}-1\\1\\0\end{bmatrix}\ \checkmark\qquad
A\begin{bmatrix}-1\\0\\1\end{bmatrix}=\begin{bmatrix}-1\\0\\1\end{bmatrix}\ \checkmark
\]

> **Answer.**
>
> | Eigenvalue \(\lambda\) | Eigenvectors |
> |---|---|
> | 7 | \((1,2,3)^T\) |
> | 1 (repeated) | \((-1,1,0)^T\) and \((-1,0,1)^T\) |

</details>

## Question 7 · Bank Q.1 iv) · Type IV · Exam-level

> **Find the eigenvalues and eigenvectors of** \(A=\begin{bmatrix}6&-2&2\\-2&3&-1\\2&-1&3\end{bmatrix}\)

> **What to expect.** Symmetric with a repeated root (Type IV). For a symmetric matrix a repeated root *always* gives the full number of vectors, so you can be confident you need two.

<details class="solution">
<summary>I have tried it on paper: show the full solution</summary>

#### Step 1 · Characteristic equation

\[
S_1=6+3+3=12,\qquad S_2=(18-4)+(18-4)+(9-1)=14+14+8=36,\qquad |A|=32
\]
\[
\lambda^{3}-12\lambda^{2}+36\lambda-32=0
\]

#### Step 2 · Roots

\(\lambda=2\) works (\(8-48+72-32=0\)), leaving \(\lambda^2-10\lambda+16=(\lambda-2)(\lambda-8)\):

\[
(\lambda-8)(\lambda-2)^{2}=0\quad\Longrightarrow\quad\lambda=8,\ 2,\ 2
\]

Check: \(8+2+2=12=S_1\) ✓ and \(8\cdot2\cdot2=32=|A|\) ✓.

#### Step 3 · Eigenvectors

**For \(\lambda=8\):**
\[
A-8I=\begin{bmatrix}-2&-2&2\\-2&-5&-1\\2&-1&-5\end{bmatrix}\longrightarrow\begin{bmatrix}1&1&-1\\0&-3&-3\\0&0&0\end{bmatrix}
\]
\(x_2=-x_3\) and \(x_1=-x_2+x_3=2x_3\). Take \(x_3=1\): \(X_3=(2,-1,1)^T\).

**For \(\lambda=2\) (repeated):**
\[
A-2I=\begin{bmatrix}4&-2&2\\-2&1&-1\\2&-1&1\end{bmatrix}\longrightarrow\begin{bmatrix}2&-1&1\\0&0&0\\0&0&0\end{bmatrix}
\]
Rank 1, two eigenvectors. The equation is \(2x_1-x_2+x_3=0\).

- \(x_1=1,\ x_2=2\ \Rightarrow\ x_3=0\): \(X_1=(1,2,0)^T\)
- \(x_1=1,\ x_2=0\ \Rightarrow\ x_3=-2\): \(X_2=(1,0,-2)^T\)

#### Step 4 · Verify

\[
A\begin{bmatrix}2\\-1\\1\end{bmatrix}=\begin{bmatrix}16\\-8\\8\end{bmatrix}=8X\ \checkmark\qquad
A\begin{bmatrix}1\\2\\0\end{bmatrix}=\begin{bmatrix}2\\4\\0\end{bmatrix}=2X\ \checkmark\qquad
A\begin{bmatrix}1\\0\\-2\end{bmatrix}=\begin{bmatrix}2\\0\\-4\end{bmatrix}=2X\ \checkmark
\]

> **Answer.**
>
> | Eigenvalue \(\lambda\) | Eigenvectors |
> |---|---|
> | 8 | \((2,-1,1)^T\) |
> | 2 (repeated) | \((1,2,0)^T\) and \((1,0,-2)^T\) |

</details>

## Question 8 · Bank Q.1 vii) · Type III · Exam-level

> **Find the eigenvalues and eigenvectors of** \(A=\begin{bmatrix}-2&2&-3\\2&1&-6\\-1&-2&0\end{bmatrix}\)

> **What to expect.** Non-symmetric with a repeated root, and negative numbers everywhere. The classic trap here is pairing the wrong minors in \(S_2\).

<details class="solution">
<summary>I have tried it on paper: show the full solution</summary>

#### Step 1 · Characteristic equation

\[
S_1=-2+1+0=-1
\]

> **Careful.** The three diagonal minors are
> \(\begin{vmatrix}-2&2\\2&1\end{vmatrix}=-2-4=-6\),
> \(\begin{vmatrix}-2&-3\\-1&0\end{vmatrix}=0-3=-3\),
> \(\begin{vmatrix}1&-6\\-2&0\end{vmatrix}=0-12=-12\).
> So \(S_2=-6-3-12=-21\).

\[
|A|=-2(0-12)-2(0-6)+(-3)(-4+1)=24+12+9=45
\]
\[
\lambda^{3}+\lambda^{2}-21\lambda-45=0
\]

#### Step 2 · Roots

\(\lambda=5\) works (\(125+25-105-45=0\)), leaving \(\lambda^2+6\lambda+9=(\lambda+3)^2\):

\[
(\lambda-5)(\lambda+3)^{2}=0\quad\Longrightarrow\quad\lambda=5,\ -3,\ -3
\]

Check: \(5-3-3=-1=S_1\) ✓ and \(5\cdot(-3)(-3)=45=|A|\) ✓.

#### Step 3 · Eigenvectors

**For \(\lambda=5\):**
\[
A-5I=\begin{bmatrix}-7&2&-3\\2&-4&-6\\-1&-2&-5\end{bmatrix}\longrightarrow\begin{bmatrix}1&0&1\\0&1&2\\0&0&0\end{bmatrix}
\]
\(x_1=-x_3\) and \(x_2=-2x_3\). Take \(x_3=-1\): \(X_3=(1,2,-1)^T\).

**For \(\lambda=-3\) (repeated):**
\[
A+3I=\begin{bmatrix}1&2&-3\\2&4&-6\\-1&-2&3\end{bmatrix}\longrightarrow\begin{bmatrix}1&2&-3\\0&0&0\\0&0&0\end{bmatrix}
\]
Rank 1, two eigenvectors. The equation is \(x_1+2x_2-3x_3=0\).

- \(x_2=1,\ x_3=0\ \Rightarrow\ x_1=-2\): \(X_1=(-2,1,0)^T\)
- \(x_2=0,\ x_3=1\ \Rightarrow\ x_1=3\): \(X_2=(3,0,1)^T\)

#### Step 4 · Verify

\[
A\begin{bmatrix}1\\2\\-1\end{bmatrix}=\begin{bmatrix}5\\10\\-5\end{bmatrix}=5X\ \checkmark\qquad
A\begin{bmatrix}-2\\1\\0\end{bmatrix}=\begin{bmatrix}6\\-3\\0\end{bmatrix}=-3X\ \checkmark\qquad
A\begin{bmatrix}3\\0\\1\end{bmatrix}=\begin{bmatrix}-9\\0\\-3\end{bmatrix}=-3X\ \checkmark
\]

> **Answer.**
>
> | Eigenvalue \(\lambda\) | Eigenvectors |
> |---|---|
> | 5 | \((1,2,-1)^T\) |
> | \(-3\) (repeated) | \((-2,1,0)^T\) and \((3,0,1)^T\) |

</details>

## Check yourself: Section 6

<details class="check">
<summary>Open when you have finished all four questions</summary>

- In each question, did you compute \(n-r\) for the repeated root *before* writing vectors?
- Did you give **two different** vectors for the repeated root (not a vector and its multiple)?
- Could you tell from the three rows of \(A-\lambda I\) alone that the rank was 1?

All four repeated roots here had rank 1. Part 4 shows what happens when a repeated root gives fewer vectors than its repeat count.

</details>

---

# Section 7 · One-page revision

**Goal of this section:** have everything on one screen for the night before the exam.

## The method

1. \(S_1=\) sum of diagonal. \(S_2=\) sum of the three diagonal \(2\times2\) minors. \(|A|=\) determinant.
2. \(\lambda^{3}-S_1\lambda^{2}+S_2\lambda-|A|=0\) (for \(2\times2\): \(\lambda^2-S_1\lambda+|A|=0\)).
3. Try small whole numbers to find one root, divide, and solve the quadratic.
4. **Check:** sum of roots \(=S_1\), product of roots \(=|A|\).
5. For each \(\lambda\): form \(A-\lambda I\), row-reduce, count \(n-r\), read off the vectors.
6. **Check:** \(AX=\lambda X\).

## Facts to know

- \(AX=\lambda X\) with \(X\neq0\). Any non-zero multiple of an eigenvector is an eigenvector.
- Triangular matrix: eigenvalues are the diagonal entries.
- \(|A|=0\) means one eigenvalue is 0.
- Rank 2 gives 1 vector; rank 1 gives 2 vectors (for a \(3\times3\)).
- Symmetric matrix: eigenvectors of different eigenvalues are perpendicular.

## The four types

| | **Non-symmetric** | **Symmetric** |
|---|---|---|
| **Distinct** | Type I | Type II |
| **Repeated** | Type III | Type IV |

## Your results from this page

| Question | Source | Eigenvalues |
|---|---|---|
| 1 | Bank Q.1 i) | \(1,2,3\) |
| 2 | Bank Q.1 v) | \(0,3,15\) |
| 3 | Bank Q.1 v) again | \(1,2,4\) |
| 4 | Practice paper Q.4 b) | \(2,3,6\) |
| 5 | Bank Q.1 ii) | \(5,1,1\) |
| 6 | Bank Q.1 iii) | \(7,1,1\) |
| 7 | Bank Q.1 iv) | \(8,2,2\) |
| 8 | Bank Q.1 vii) | \(5,-3,-3\) |

---

# About the sources

## What is on this page, and what is not

| Block | Source | Status |
|---|---|---|
| Module I, eigenvalues and eigenvectors | MUSA 2026 bank, page 1, Q.1 (i)–(vii), plus practice paper Q.4 b) | **Complete** (this page) |
| Module I, eigenvalues of matrix expressions | MUSA 2026 bank, Q.2 (i)–(ii) | Planned, Part 2 |
| Module I, Cayley–Hamilton theorem | MUSA 2026 bank, Q.1–Q.8 | Planned, Part 3 |
| Module I, diagonalisation | MUSA 2026 bank, Q.1–Q.6 | Planned, Part 4 |
| Modules II, III, V, VI | MUSA 2026 bank and practice paper | Not started |
| Module IV, Fourier series | Existing Module 4 guide | Will be reconciled, not duplicated |

Nothing marked "planned" or "not started" has been written yet. An empty section is never shown as finished.

## Where every question comes from

- **The question bank controls the wording and the numbers.** Every matrix was read from the scanned page at 200–400 dpi and compared against a second enlarged crop.
- **The solutions booklet is a secondary source.** It was treated as a claim to check, not as an answer key. Every Module I eigenvalue answer in it agrees with the solutions here, up to a scalar multiple of an eigenvector (which is still the same eigenvector).
- **Every answer is independently verified** with SymPy 1.14 using exact rational arithmetic, and every eigenvector is checked by substitution into \(AX=\lambda X\).

<details>
<summary>Source files and checksums</summary>

| Source | File on the project machine | SHA-256 (verified 16 November 2026) |
|---|---|---|
| MUSA question bank, Winter Session 2026 (9 pages) | `musa-question-bank-2026.pdf` | `1c24161e4d16e5c3624f610e56ee2034a705475b604a2d39f16849eb921a89f2` |
| MUSA solutions booklet (108 pages) | `maths-question-bank-solutions.pdf` | `523d42600fc54da00b87702edd6ea17dafd8469e286046a4e9ee0e7ffcc404c2` |
| MUSA practice paper, Set-I, Winter 2025 (3 pages) | `musa-practice-paper-set1-w2025.pdf` | `17fb8559daa4f7dec2ac625dc2053c56ab691ef7894650707c048f3ee125d404` |

</details>

*The teacher's method comes from the handwritten Module 1 notes (PDF pages 1–11). For a second view of the geometric picture, see Margalit and Rabinoff, [Interactive Linear Algebra, §5.1](https://textbooks.math.gatech.edu/ila/eigenvectors.html) (Georgia Tech, GNU Free Documentation License). The compact offline answer key is `Module_1_Endsem_Answer_Key.md`.*
