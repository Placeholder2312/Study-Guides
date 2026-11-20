# Module 4 — Fourier Series: Revision Sheet

**Mathematics for Computer Engineering (2023111)** · B.E. CSE (AI & ML), Semester III · University of Mumbai · NEP 2020
Module IV · 4 teaching hours · CO4 · prepared 14 November 2026

> **What this is.** A compressed, exam-morning version of
> [`Module_4_Study_Guide.md`](../05_Study_Guides/Module_4/Module_4_Study_Guide.md).
> It states results, not full derivations. Every formula and coefficient here is checked with SymPy;
> the full verification log is guide §9.5. The teacher's convention is used throughout:
> the constant term is \(a_0\), not \(a_0/2\).

---

## 1. The prescribed content, in one box

| Prescribed (examined as syllabus content) | Self-learning (syllabus list) | Enrichment (not in the syllabus) |
|---|---|---|
| Dirichlet's conditions | Orthogonal and orthonormal sets of functions | Parseval's identity |
| Fourier series on \((0,2\pi)\) and \((0,2l)\) | Complex form of the Fourier series | — |
| Fourier series on \((-l,l)\) | Half-range sine and cosine series | — |
| Fourier series of even and odd functions | | — |

No supplied Module 4 question asks a self-learning topic. That is an observation about the
25 available questions, not a promise about your paper. Dirichlet's conditions are prescribed
and are a natural short Q1 question even though none of the 25 asks them.

---

## 2. Definitions you must be able to write in one line

| Term | One-line statement |
|---|---|
| \(f\) has period \(2l\) | \(f(x+2l)=f(x)\) for every \(x\) in the domain |
| Dirichlet's conditions | \(f\) is bounded on the period, has finitely many discontinuities (all finite jumps), and finitely many maxima and minima |
| Fourier series on \((c,c+2l)\) | \(\displaystyle f(x)\sim a_0+\sum_{n=1}^{\infty}\left(a_n\cos\frac{n\pi x}{l}+b_n\sin\frac{n\pi x}{l}\right)\) |
| Constant term (teacher) | \(\displaystyle a_0=\frac{1}{2l}\int_c^{c+2l}f(x)\,dx\), the mean value of \(f\) over one period |
| Cosine coefficient | \(\displaystyle a_n=\frac1l\int_c^{c+2l}f(x)\cos\frac{n\pi x}{l}\,dx\) |
| Sine coefficient | \(\displaystyle b_n=\frac1l\int_c^{c+2l}f(x)\sin\frac{n\pi x}{l}\,dx\) |
| Even function | \(f(-x)=f(x)\) for all \(x\); graph symmetric about the \(y\)-axis |
| Odd function | \(f(-x)=-f(x)\) for all \(x\); graph has half-turn symmetry about the origin |
| Dirichlet value at a jump \(x_0\) | \(\displaystyle \frac{f(x_0^-)+f(x_0^+)}{2}\) |
| Half-range sine series | Odd extension of \(f\) from \((0,l)\) to \((-l,l)\); only sines survive |
| Half-range cosine series | Even extension of \(f\) from \((0,l)\) to \((-l,l)\); only cosines survive |

**Dirichlet's theorem, worded for an answer.** If \(f\) satisfies Dirichlet's conditions on
\((c,c+2l)\), its Fourier series converges at every point. At a point where \(f\) is continuous,
it converges to \(f(x)\); at a jump, to the midpoint of the two one-sided limits; at either end
of the interval, to the midpoint of the values approached from inside and outside the period.

---

## 3. The formula sheet

### 3.1 General interval

For \(f\) defined on \((c,\,c+2l)\), so that the interval has length \(2l\),

\[
\boxed{\;f(x)=a_0+\sum_{n=1}^{\infty}\left(a_n\cos\frac{n\pi x}{l}+b_n\sin\frac{n\pi x}{l}\right)\;}
\]

\[
a_0=\frac{1}{2l}\int_c^{c+2l}f(x)\,dx,\qquad
a_n=\frac1l\int_c^{c+2l}f(x)\cos\frac{n\pi x}{l}\,dx,\qquad
b_n=\frac1l\int_c^{c+2l}f(x)\sin\frac{n\pi x}{l}\,dx .
\]

The divisor in \(a_0\) is \(2l\), the full length. The divisor in \(a_n,b_n\) is \(l\), half the length.
This asymmetry is the single most common source of lost marks.

### 3.2 The four intervals that actually appear

| Interval | \(l\) | Argument | \(a_0\) | \(a_n,b_n\) |
|---|---:|---|---:|---|
| \((0,2\pi)\) | \(\pi\) | \(nx\) | \(\frac{1}{2\pi}\int_0^{2\pi}f\) | \(\frac1\pi\int_0^{2\pi}\) |
| \((-\pi,\pi)\) | \(\pi\) | \(nx\) | \(\frac{1}{2\pi}\int_{-\pi}^{\pi}f\) | \(\frac1\pi\int_{-\pi}^{\pi}\) |
| \((0,2)\) | \(1\) | \(n\pi x\) | \(\frac12\int_0^2f\) | \(\int_0^2\) |
| \((-1,1)\) | \(1\) | \(n\pi x\) | \(\frac12\int_{-1}^{1}f\) | \(\int_{-1}^{1}\) |

For a general \((0,a)\): the length is \(a=2l\), so \(l=a/2\) and the argument is
\(\frac{2n\pi x}{a}\). Then

\[
a_0=\frac1a\int_0^a f,\qquad
a_n=\frac2a\int_0^a f\cos\frac{2n\pi x}{a},\qquad
b_n=\frac2a\int_0^a f\sin\frac{2n\pi x}{a}.
\]

### 3.3 Even and odd shortcuts (only on a symmetric interval)

On \((-l,l)\), with the argument \(\frac{n\pi x}{l}\):

\[
\text{even }f:\quad b_n=0,\qquad
a_0=\frac1l\int_0^l f,\qquad
a_n=\frac2l\int_0^l f\cos\frac{n\pi x}{l}.
\]

\[
\text{odd }f:\quad a_0=a_n=0,\qquad
b_n=\frac2l\int_0^l f\sin\frac{n\pi x}{l}.
\]

The factor \(2\) appears because the integral over \((-l,l)\) is twice the integral over \((0,l)\).
The shortcut is invalid on \((0,2\pi)\): that interval is not symmetric about \(0\).

### 3.4 Half-range series on \((0,l)\) — self-learning

\[
\text{sine series:}\quad b_n=\frac2l\int_0^l f(x)\sin\frac{n\pi x}{l}\,dx,
\qquad f(x)=\sum_{n=1}^{\infty}b_n\sin\frac{n\pi x}{l}.
\]

\[
\text{cosine series:}\quad a_0=\frac1l\int_0^l f(x)\,dx,\qquad
a_n=\frac2l\int_0^l f(x)\cos\frac{n\pi x}{l}\,dx,
\qquad f(x)=a_0+\sum_{n=1}^{\infty}a_n\cos\frac{n\pi x}{l}.
\]

Both represent the same \(f\) on \((0,l)\). They differ outside that interval.

### 3.5 Complex form — self-learning

\[
f(x)=\sum_{n=-\infty}^{\infty}c_n e^{in\pi x/l},\qquad
c_n=\frac{1}{2l}\int_{-l}^{l}f(x)e^{-in\pi x/l}\,dx .
\]

On \((-\pi,\pi)\), replace \(l\) by \(\pi\):
\(c_n=\frac{1}{2\pi}\int_{-\pi}^{\pi}f(x)e^{-inx}dx\).
For real \(f\), \(c_{-n}=\overline{c_n}\), and \(c_0=a_0\).

### 3.6 Parseval — enrichment

With the teacher's convention,

\[
\frac{1}{2l}\int_c^{c+2l}\lvert f(x)\rvert^2\,dx
=a_0^2+\frac12\sum_{n=1}^{\infty}\left(a_n^2+b_n^2\right).
\]

This is the only route to \(\sum 1/n^4=\pi^4/90\); no single substitution produces it.

---

## 4. The integrals and values you should not have to look up

\[
\int x\cos kx\,dx=\frac{x\sin kx}{k}+\frac{\cos kx}{k^2},\qquad
\int x\sin kx\,dx=-\frac{x\cos kx}{k}+\frac{\sin kx}{k^2},
\]

\[
\int x^2\cos kx\,dx=\frac{x^2\sin kx}{k}+\frac{2x\cos kx}{k^2}-\frac{2\sin kx}{k^3},
\]

\[
\int x^2\sin kx\,dx=-\frac{x^2\cos kx}{k}+\frac{2x\sin kx}{k^2}+\frac{2\cos kx}{k^3}.
\]

\[
\sin n\pi=0,\qquad \sin 2n\pi=0,\qquad
\cos n\pi=(-1)^n,\qquad \cos 2n\pi=1.
\]

Two consequences used constantly:

\[
1-\cos n\pi=1-(-1)^n=
\begin{cases}0,&n\text{ even},\\ 2,&n\text{ odd},\end{cases}
\qquad
(-1)^n(-1)^n=1.
\]

The last identity is what turns the \(x=\pi\) substitution into a numerical series.

---

## 5. Results worth memorising

### 5.1 The five teacher examples

| Function and interval | \(l\) | Constant term | Cosine coefficient | Sine coefficient |
|---|---:|---:|---|---|
| \(x^2\) on \((0,2)\) | \(1\) | \(\frac43\) | \(\frac{4}{n^2\pi^2}\) | \(-\frac{4}{n\pi}\) |
| \(x\) on \((0,2\pi)\) | \(\pi\) | \(\pi\) | \(0\) | \(-\frac2n\) |
| \(4-x^2\) on \((0,2\pi)\) | \(\pi\) | \(4-\frac{4\pi^2}{3}\) | \(-\frac4{n^2}\) | \(\frac{4\pi}{n}\) |
| \(x^2\) on \((-\pi,\pi)\) | \(\pi\) | \(\frac{\pi^2}{3}\) | \(\frac{4(-1)^n}{n^2}\) | \(0\) |
| \(\left(\frac{\pi-x}{2}\right)^2\) on \((0,2\pi)\) | \(\pi\) | \(\frac{\pi^2}{12}\) | \(\frac1{n^2}\) | \(0\) |

The corresponding series:

\[
x^2=\frac43+\frac{4}{\pi^2}\sum_{n=1}^{\infty}\frac{\cos n\pi x}{n^2}
-\frac4\pi\sum_{n=1}^{\infty}\frac{\sin n\pi x}{n},\qquad 0<x<2.
\]

\[
x=\pi-2\sum_{n=1}^{\infty}\frac{\sin nx}{n},\qquad 0<x<2\pi.
\]

\[
4-x^2=4-\frac{4\pi^2}{3}-4\sum_{n=1}^{\infty}\frac{\cos nx}{n^2}
+4\pi\sum_{n=1}^{\infty}\frac{\sin nx}{n},\qquad 0<x<2\pi.
\]

\[
x^2=\frac{\pi^2}{3}+4\sum_{n=1}^{\infty}\frac{(-1)^n\cos nx}{n^2},\qquad -\pi<x<\pi.
\]

\[
\left(\frac{\pi-x}{2}\right)^2
=\frac{\pi^2}{12}+\sum_{n=1}^{\infty}\frac{\cos nx}{n^2},\qquad 0<x<2\pi.
\]

**Teacher's slip, notes page 3.** The notes print \(\frac4\pi\) in front of the cosine sum for \(x^2\)
on \((0,2)\). The correct factor is \(\frac4{\pi^2}\). The coefficients themselves are correct; only
that printed factor is wrong. Never copy it.

### 5.2 Even/odd classics

| Function on \((-\pi,\pi)\) | \(a_0\) | \(a_n\) | \(b_n\) |
|---|---:|---|---:|
| \(x\) | \(0\) | \(0\) | \(\frac{2(-1)^{n+1}}{n}\) |
| \(x^2\) | \(\frac{\pi^2}{3}\) | \(\frac{4(-1)^n}{n^2}\) | \(0\) |
| \(\lvert x\rvert\) | \(\frac{\pi}{2}\) | \(-\frac{4}{\pi n^2}\) for odd \(n\), \(0\) for even \(n\) | \(0\) |
| \(\frac{\pi}{2}-\lvert x\rvert\) | \(0\) | \(\frac{4}{\pi n^2}\) for odd \(n\), \(0\) for even \(n\) | \(0\) |
| \(1-\frac{2\lvert x\rvert}{\pi}\) | \(0\) | \(\frac8{\pi^2n^2}\) for odd \(n\), \(0\) for even \(n\) | \(0\) |
| \(\lvert\sin x\rvert\) | \(\frac{2}{\pi}\) | \(-\frac{4}{\pi(4m^2-1)}\) at \(n=2m\); \(0\) for odd \(n\) | \(0\) |
| \(x\cos x\) | \(0\) | \(0\) | \(b_1=-\frac12\); \(b_n=\frac{2n(-1)^n}{n^2-1}\) for \(n\ge2\) |

**Functions on \((0,2\pi)\) are not covered by these shortcuts.** Two that appear in the question
bank still need all three coefficients:

| Function on \((0,2\pi)\) | \(a_0\) | \(a_n\) | \(b_n\) |
|---|---:|---|---:|
| \(x\sin x\) | \(-1\) | \(-\frac12\) at \(n=1\); \(\frac{2}{n^2-1}\) for \(n\ge2\) | \(b_1=\pi\); \(b_n=0\) for \(n\ge2\) |
| \(\sqrt{1-\cos x}\) | \(\frac{2\sqrt2}{\pi}\) | \(-\frac{4\sqrt2}{\pi(4n^2-1)}\) | \(0\) |

The second row looks even as a formula, but \((0,2\pi)\) is not symmetric about \(0\). Parity alone
does not justify dropping \(b_n\); only the calculation does.

### 5.3 Numerical series and where they come from

| Series | Value | Standard route |
|---|---:|---|
| \(\sum_{n\ge1}\frac1{n^2}\) | \(\frac{\pi^2}{6}\) | \(x^2\) on \((-\pi,\pi)\) at \(x=\pi\); or \(x^2\) on \((0,2\pi)\) at the jump \(x=0\) |
| \(\sum_{n\ge1}\frac{(-1)^{n+1}}{n^2}\) | \(\frac{\pi^2}{12}\) | \(x^2\) on \((-\pi,\pi)\) at \(x=0\); or \(x^2\) on \((0,2\pi)\) at \(x=\pi\) |
| \(\sum_{n\text{ odd}}\frac1{n^2}\) | \(\frac{\pi^2}{8}\) | add the first two, or use \(\lvert x\rvert\) at \(x=0\) |
| \(\sum_{n\ge1}\frac1{n^4}\) | \(\frac{\pi^4}{90}\) | Parseval on \(x^2\) over \((-\pi,\pi)\) |
| \(1-\frac13+\frac15-\cdots\) | \(\frac{\pi}{4}\) | \(x\) on \((-\pi,\pi)\) at \(x=\frac{\pi}{2}\) |
| \(\sum_{n\ge2}\frac1{n^2-1}\) | \(\frac34\) | \(x\sin x\) at \(x=0\) |
| \(\sum_{n\ge1}\frac1{4n^2-1}\) | \(\frac12\) | \(\sqrt{1-\cos x}\) at \(x=0\) |

**Warning.** The point that works on one interval may not work on another. On \((-\pi,\pi)\),
\(x=\pi\) gives \(\pi^2/6\). On \((0,2\pi)\), \(x=\pi\) gives \(\pi^2/12\) and the jump \(x=0\)
gives \(\pi^2/6\). Recompute the status of the point; never transplant a deduction.

---

## 6. The method, as a checklist

### 6.1 Expanding a function

1. **Read the interval.** Write its length and \(l=\frac12\)(length).
2. **Write the argument** \(\frac{n\pi x}{l}\) explicitly.
3. **Check parity** only if the interval is \((-l,l)\). Then choose the shortcut or the full formulas.
4. **Compute \(a_0\)** from the average. Check its sign against the graph.
5. **Compute \(a_n,b_n\)** by parts. For \(x^2\), two integrations by parts.
6. **Apply the four trig values.** All \(\sin n\pi\), \(\sin 2n\pi\) must disappear.
7. **Assemble** and take out common factors. Keep \((-1)^n\) visible.
8. **Sanity-check** the decay: a jump gives coefficients \(\sim1/n\); a continuous periodic extension gives \(\sim1/n^2\).

### 6.2 Deducing a numerical series

1. Choose \(x\) so that \(\cos nx=\pm1\) or \(0\), and \(\sin nx=0\).
2. Decide whether the periodic extension is continuous at that \(x\).
3. Continuous: set the series equal to \(f(x)\). Jump or endpoint: set it equal to the midpoint.
4. Simplify, then check the identity is numerically plausible.
5. If the target is a fourth-power sum, use Parseval instead.

### 6.3 Common exam traps

| Trap | Fix |
|---|---|
| Using \(\frac1l\) for \(a_0\) | \(a_0\) uses \(\frac{1}{2l}\) (teacher convention) |
| Using the even/odd shortcut on \((0,2\pi)\) | The interval must be symmetric about \(0\) |
| Forgetting the factor \(2\) on \((-l,l)\) | Even: \(a_n=\frac2l\int_0^l\); odd: \(b_n=\frac2l\int_0^l\) |
| Substituting \(x=0\) when the extension jumps | Use \(\frac{f(0^+)+f(2l^-)}{2}\) |
| Writing \((-1)^n(-1)^n=-1\) | It equals \((-1)^{2n}=1\) |
| Losing the sign of an alternating sum | \(\sum(-1)^n/n^2=-\pi^2/12\); with \((-1)^{n+1}\) it is \(+\pi^2/12\) |
| Quoting \(\pi^2/90\) for a fourth-power sum | The correct value is \(\pi^4/90\) |
| Mixing the teacher's \(a_0\) with a book's \(a_0/2\) | Convert once: \(a_0^{\text{teacher}}=a_0^{\text{book}}/2\) |

---

## 7. Ten-minute self-test

Cover the right-hand column.

1. State Dirichlet's conditions. What does the series equal at a jump?
2. On \((0,2\pi)\), write \(a_0,a_n,b_n\) with the correct divisors.
3. Expand \(f(x)=x\) on \((-\pi,\pi)\). Which coefficients survive, and why?
4. Expand \(f(x)=x^2\) on \((-\pi,\pi)\). Then deduce \(\pi^2/6\) and \(\pi^2/12\).
5. Expand \(f(x)=x^2\) on \((0,2\pi)\). Which substitution gives \(\pi^2/6\) and why is it a jump?
6. Write the half-range sine and cosine formulas on \((0,l)\). Which is the odd extension?
7. Write the complex Fourier coefficient \(c_n\) on \((-\pi,\pi)\). How does \(c_0\) relate to \(a_0\)?
8. State Parseval's identity in the teacher's convention. Which series does it evaluate?
9. Why can you not use \(b_n=0\) for \(4-x^2\) on \((0,2\pi)\)?
10. What is wrong with the printed cosine factor in the notes' \(x^2\) example on \((0,2)\)?

**Answers** are collected at the end of this sheet (§10), so you can attempt all ten first.

---

## 8. Last-five-minutes page

- \(l=\frac12\)(interval length); argument \(=\frac{n\pi x}{l}\).
- \(a_0=\frac1{2l}\int\); \(a_n=\frac1l\int f\cos\); \(b_n=\frac1l\int f\sin\).
- Symmetric interval: odd → only \(b_n\); even → only \(a_0,a_n\); both with \(\frac2l\int_0^l\).
- \(\sin n\pi=\sin2n\pi=0\); \(\cos n\pi=(-1)^n\); \(\cos2n\pi=1\).
- At a jump, the series equals the midpoint.
- \(x^2\) on \((-\pi,\pi)\): \(x=\pi\Rightarrow\pi^2/6\), \(x=0\Rightarrow\pi^2/12\).
- \(x^2\) on \((0,2\pi)\): \(x=\pi\Rightarrow\pi^2/12\), \(x=0\Rightarrow\pi^2/6\).
- Fourth powers: Parseval; value \(\pi^4/90\).
- The teacher's one slip: \(\frac4\pi\) should be \(\frac4{\pi^2}\) in the \(x^2\) example on \((0,2)\).

---

## 9. Where to go next

| If you need… | Open |
|---|---|
| A concept explained from zero | Guide §2.1–2.7 |
| A fully worked example | Guide §2.8–2.13 |
| The 25 supplied questions, with provenance | Guide §3 and `03_Transcriptions/Exam_Questions_Module_4.md` |
| Self-learning topics | Guide §4 |
| Graded practice and Tutorial 4 | Guide §5 |
| Full solutions | Guide §6 |
| The teacher's page-by-page wording | `03_Transcriptions/Module_4_Transcription.md` |
| Source and verification details | Guide §9 and `04_OCR_Reports/OCR_Review_Report_Module_4.md` |

All Module 4 material in this project is student study material. The MUSA practice paper and
question bank are student-association documents, **not** University of Mumbai question papers.

---

## 10. Self-test answers

1. Bounded, finitely many finite jumps, finitely many maxima and minima; at a jump the series equals the midpoint of the one-sided limits.
2. \(a_0=\frac1{2\pi}\int_0^{2\pi}f\), \(a_n=\frac1\pi\int_0^{2\pi}f\cos nx\), \(b_n=\frac1\pi\int_0^{2\pi}f\sin nx\).
3. Odd, so \(a_0=a_n=0\); \(b_n=\frac2\pi\int_0^\pi x\sin nx\,dx=\frac{2(-1)^{n+1}}{n}\).
4. \(x^2=\frac{\pi^2}{3}+4\sum\frac{(-1)^n}{n^2}\cos nx\). At \(x=\pi\): \(\pi^2/6\). At \(x=0\): \(\pi^2/12\).
5. \(x^2=\frac{4\pi^2}{3}+4\sum\frac{\cos nx}{n^2}-4\pi\sum\frac{\sin nx}{n}\). At \(x=0\) the extension jumps from \(4\pi^2\) to \(0\), so the midpoint \(2\pi^2\) gives \(\pi^2/6\).
6. Sine: \(b_n=\frac2l\int_0^l f\sin\frac{n\pi x}{l}\); cosine: \(a_0=\frac1l\int_0^l f\), \(a_n=\frac2l\int_0^l f\cos\frac{n\pi x}{l}\). The sine series is the odd extension.
7. \(c_n=\frac1{2\pi}\int_{-\pi}^{\pi}f(x)e^{-inx}dx\); \(c_0=a_0\).
8. \(\frac1{2l}\int\lvert f\rvert^2=a_0^2+\frac12\sum(a_n^2+b_n^2)\); it gives \(\sum1/n^4=\pi^4/90\).
9. The interval \((0,2\pi)\) is not symmetric about \(0\), so parity gives no shortcut; \(b_n\ne0\).
10. The notes print \(\frac4\pi\); the correct factor is \(\frac4{\pi^2}\).
