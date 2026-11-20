# Module 4 — Fourier Series: Transcription

**Original source:** `01_Original_Notes/Module_4/Module 4 CSE.pdf`
**Document:** Handwritten teacher notes, scanned, 8 PDF pages, no text layer
**Subject on page 1:** MODULE 4 CSE
**Transcription method:** every page was rendered at 150 dpi and read visually; doubtful symbols were re-cropped at 400–600 dpi and checked. Printed-text OCR (RapidOCR) was not used as an authority — see `04_OCR_Reports/OCR_Review_Report_Module_4.md`.

> **What this file is.** A faithful reproduction of what the teacher wrote: same order, same examples, same notation, same intermediate arithmetic, including the teacher's own slips. It is **not** a study guide. Corrections and explanations live in `05_Study_Guides/Module_4/Module_4_Study_Guide.md`.
>
> Conventions used here: `[as written]` marks a teacher's wording or symbol reproduced without change; `[UNCLEAR — PDF PAGE n]` marks genuinely unreadable content; editorial square brackets `[...]` mark additions needed only for readability.

> **Notation warning (important when reading this file).** The teacher uses the convention
> \[ f(x)=a_0+\sum_{n=1}^{\infty}\left(a_n\cos\frac{n\pi x}{l}+b_n\sin\frac{n\pi x}{l}\right),\qquad a_0=\frac{1}{2l}\int_c^{c+2l}f(x)\,dx, \]
> so the constant term of the series is \(a_0\) itself. Many textbooks and the MUSA solution booklet instead write \(f(x)=\frac{a_0}{2}+\sum(\cdots)\) with \(a_0=\frac{1}{l}\int f\). The two are related by \(a_0^{\text{(teacher)}}=a_0^{\text{(book)}}/2\). This transcription keeps the teacher's convention throughout; the conversion is worked out once in the study guide, §2.4.

---

## Page 1 — heading, syllabus row, Dirichlet's conditions, general interval, \((0,2l)\), \((0,2\pi)\)

**Heading:** `MODULE 4 CSE`

**Printed syllabus row reproduced at the top of the page:**

| IV | Fourier Series | 1. Dirichlet's conditions, Fourier series of periodic function with period \(2\pi\) and \(2l\). 2. Fourier series of even and odd functions. **Self-learning Topics:** Orthogonal and orthonormal set of functions, Complex form of Fourier Series, Half range Sine and Cosine Series. | 4 | CO4 |
|---|---|---|---|---|---|

### Dirichlet's Conditions

> Dirichlet's Conditions:
>
> A function \(f(x)\) defined in the interval \(c_1\le x\le c_2\) can be expressed as Fourier series if in the interval
>
> i) \(f(x)\) and its integrals are finite and single valued.
>
> ii) \(f(x)\) has dis continuities, finite number. `[as written]`
>
> iii) \(f(x)\) has finite number of maxima and minima
>
> These conditions are known as Dirichlet's conditions.

### Fourier series in the interval \((c,\ c+2l)\)

\[
f(x)=a_0+\sum_{n=1}^{\infty}a_n\cos\left(\frac{n\pi x}{l}\right)+\sum_{n=1}^{\infty}b_n\sin\left(\frac{n\pi x}{l}\right)
\]

> where Fourier coefficients
>
> \[
> a_0=\frac{1}{2l}\int_c^{c+2l}f(x)\,dx
> \]
> \[
> a_n=\frac{1}{l}\int_c^{c+2l}f(x)\cos\left(\frac{n\pi x}{l}\right)dx
> \]
> \[
> b_n=\frac{1}{l}\int_c^{c+2l}f(x)\sin\left(\frac{n\pi x}{l}\right)dx
> \]

### Fourier series in the interval \((0,2l)\) — "put \(c=0\)"

\[
f(x)=a_0+\sum_{n=1}^{\infty}a_n\cos\left(\frac{n\pi x}{l}\right)+\sum_{n=1}^{\infty}b_n\sin\left(\frac{n\pi x}{l}\right)
\]
\[
a_0=\frac{1}{2l}\int_0^{2l}f(x)\,dx,\qquad a_n=\frac{1}{l}\int_0^{2l}f(x)\cos\left(\frac{n\pi x}{l}\right)dx
\]
\[
b_n=\frac{1}{l}\int_0^{2l}f(x)\sin\left(\frac{n\pi x}{l}\right)dx
\]

### Fourier series in the interval \((0,2\pi)\) — "put \(c=0,\ l=\pi\)"

\[
f(x)=a_0+\sum_{n=1}^{\infty}a_n\cos nx+\sum_{n=1}^{\infty}b_n\sin nx
\]
\[
a_0=\frac{1}{2\pi}\int_0^{2\pi}f(x)\,dx,\qquad a_n=\frac{1}{\pi}\int_0^{2\pi}f(x)\cos nx\,dx,
\]
\[
b_n=\frac{1}{\pi}\int_0^{2\pi}f(x)\sin nx\,dx
\]

---

## Page 2 — \((-l,l)\), \((-\pi,\pi)\), even and odd functions, two standard integrals

### Fourier series in the interval \((-l,l)\) — "put \(c=-l\)"

\[
f(x)=a_0+\sum_{n=1}^{\infty}a_n\cos\left(\frac{n\pi x}{l}\right)+\sum_{n=1}^{\infty}b_n\sin\left(\frac{n\pi x}{l}\right)
\]
\[
a_0=\frac{1}{2l}\int_{-l}^{l}f(x)\,dx,\qquad a_n=\frac{1}{l}\int_{-l}^{l}f(x)\cos\frac{n\pi x}{l}\,dx,
\]
\[
b_n=\frac{1}{l}\int_{-l}^{l}f(x)\sin\frac{n\pi x}{l}\,dx
\]

### Fourier series in the interval \((-\pi,\pi)\) — "put \(c=-\pi,\ l=\pi\)"

\[
f(x)=a_0+\sum_{n=1}^{\infty}a_n\cos nx+\sum_{n=1}^{\infty}b_n\sin nx
\]
\[
a_0=\frac{1}{2\pi}\int_{-\pi}^{\pi}f(x)\,dx
\]
\[
a_n=\frac{1}{\pi}\int_{-\pi}^{\pi}f(x)\cos nx\,dx,\qquad b_n=\frac{1}{\pi}\int_{-\pi}^{\pi}f(x)\sin nx\,dx
\]

### Even and odd function

> If \(f(-x)=f(x)\), \(f(x)\) is even
>
> If \(f(-x)=-f(x)\), \(f(x)\) is odd

**Property** `[as written — heading reads "Boperty"]`

\[
\int_{-a}^{a}f(x)\,dx=
\begin{cases}
2\displaystyle\int_0^{a}f(x)\,dx, & \text{if } f(x) \text{ is even}\\[2mm]
0, & \text{if } f(x) \text{ is odd}
\end{cases}
\]

### Fourier series of even function

\[
f(x)=a_0+\sum_{n=1}^{\infty}a_n\cos\left(\frac{n\pi x}{l}\right)
\]
\[
a_0=\frac{1}{2l}\int_{-l}^{l}f(x)\,dx=\frac{1}{l}\int_0^{l}f(x)\,dx
\]
\[
a_n=\frac{1}{l}\int_{-l}^{l}f(x)\cos\frac{n\pi x}{l}\,dx=\frac{2}{l}\int_0^{l}f(x)\cos\left(\frac{n\pi x}{l}\right)dx
\]
\[
b_n=0
\]

### Fourier series of odd function

\[
f(x)=\sum_{n=1}^{\infty}b_n\sin\left(\frac{n\pi x}{l}\right)
\]
\[
a_0=0,\qquad a_n=0,\qquad b_n=\frac{1}{l}\int_{-l}^{l}f(x)\sin\frac{n\pi x}{l}\,dx
\]
\[
=\frac{2}{l}\int_0^{l}f(x)\sin\left(\frac{n\pi x}{l}\right)dx
\]

### Some important formula

\[
\int e^{ax}\cos bx\,dx=\frac{e^{ax}}{a^2+b^2}\left(a\cos bx+b\sin bx\right)
\]
\[
\int e^{ax}\sin bx\,dx=\frac{e^{ax}}{a^2+b^2}\left(a\sin bx-b\cos bx\right)
\]

> **Transcription note (page 2).** Both formulas are written correctly (checked by differentiation), but **neither is used** anywhere in the eight pages: every example in this module needs only polynomial × trigonometric integrals. They are reproduced for completeness, not because the module requires them. `[verified]`

---

## Page 3 — trigonometric values, first example \(x^2\) on \((0,2l)\), second example \(x\) on \((0,2\pi)\)

**Top of page:**

> \(\sin n\pi=0,\quad \sin 2n\pi=0,\quad \cos n\pi=(-1)^n,\quad \cos 2n\pi=1\)

### Q. Expand Fourier series for \(f(x)=x^2\) in \((0,2l)\)

`[as written — the interval is written "(0, 2l)"; in the working the teacher immediately sets 2l = 2, i.e. l = 1, which is the interval (0,2). Tutorial 4, Q1 asks for (0,2).]`

**Sol.** Let
\[
f(x)=a_0+\sum_{n=1}^{\infty}a_n\cos\frac{n\pi x}{l}+\sum_{n=1}^{\infty}b_n\sin\frac{n\pi x}{l}
\]

Marginal note: \(\left[(c,c+2l),\ c=0,\ 2l=2\ \therefore l=1\right]\)

\[
a_0=\frac{1}{2l}\int_0^{2}x^2\,dx
\qquad\left[\because\ a_0=\frac{1}{2l}\int_c^{c+2l}f(x)\,dx\right]
\]
\[
=\frac{1}{2}\left[\frac{x^3}{3}\right]_0^{2}=\frac{1}{6}(8-0)=\frac{4}{3}
\]

\[
a_n=\frac{1}{l}\int_0^{2}x^2\cos n\pi x\,dx
\]
\[
=\left[(x^2)\left(\frac{\sin n\pi x}{n\pi}\right)-(2x)\left(\frac{-\cos n\pi x}{(n\pi)^2}\right)+(2)\left(\frac{-\sin n\pi x}{(n\pi)^3}\right)\right]_0^{2}
\]
\[
=\left(0+\frac{4}{n^2\pi^2}-0\right)-\left(0+0-0\right)=\frac{4}{n^2\pi^2}
\]

\[
b_n=\frac{1}{l}\int_0^{2}x^2\sin n\pi x\,dx
\]
\[
=\left[(x^2)\left(\frac{-\cos n\pi x}{n\pi}\right)-(2x)\left(\frac{-\sin n\pi x}{(n\pi)^2}\right)+(2)\left(\frac{\cos n\pi x}{(n\pi)^3}\right)\right]_0^{2}
\]
\[
=\left(-\frac{4}{n\pi}-0+\frac{2}{n^3\pi^3}\right)-\left(0-0+\frac{2}{n^3\pi^3}\right)
\]
\[
=-\frac{4}{n\pi}
\]

\[
\therefore\quad x^2=\frac{4}{3}+\frac{4}{\pi}\sum_{n=1}^{\infty}\frac{\cos n\pi x}{n^2}-\frac{4}{\pi}\sum_{n=1}^{\infty}\frac{\sin n\pi x}{n}
\]

`[as written — see the transcription note below]`

\[
x^2=\frac{4}{3}+\frac{4}{\pi}\left[\frac{\cos \pi x}{1^2}+\frac{\cos 2\pi x}{2^2}+\frac{\cos 3\pi x}{3^2}+\cdots\right]-\frac{4}{\pi}\left[\frac{\sin \pi x}{1}+\frac{\sin 2\pi x}{2}+\frac{\sin 3\pi x}{3}+\cdots\right]
\]

> **Transcription note (page 3, first example).** The coefficients computed on the page are correct: \(a_0=\tfrac43\), \(a_n=\dfrac{4}{n^2\pi^2}\), \(b_n=-\dfrac{4}{n\pi}\). But the closing common factor on the cosine sum is written \(\dfrac{4}{\pi}\), whereas \(a_n=\dfrac{4}{n^2\pi^2}\) requires the common factor \(\dfrac{4}{\pi^2}\). The bracket itself (with \(1^2,2^2,3^2\) in the denominators) is right. So the page contains a factor-of-\(\pi\) slip, not an integration error. Corrected form:
> \[
> x^2=\frac{4}{3}+\frac{4}{\pi^2}\sum_{n=1}^{\infty}\frac{\cos n\pi x}{n^2}-\frac{4}{\pi}\sum_{n=1}^{\infty}\frac{\sin n\pi x}{n}.
> \]
> The slip is reproduced here unchanged and is discussed in the study guide (§2.9, §7.4). `[verified with SymPy]`

### Q. Find Fourier series for the function \(f(x)=x,\ 0<x<2\pi\)

**Sol.** Let
\[
f(x)=a_0+\sum_{n=1}^{\infty}a_n\cos nx+\sum_{n=1}^{\infty}b_n\sin nx
\]

\[
a_0=\frac{1}{2\pi}\int_0^{2\pi}x\,dx
\qquad\left[\because\ a_0=\frac{1}{2\pi}\int_0^{2\pi}f(x)\,dx\right]
\]
\[
=\frac{1}{2\pi}\left[\frac{x^2}{2}\right]_0^{2\pi}=\frac{1}{4\pi}\left(4\pi^2-0\right)=\pi
\]

\[
a_n=\frac{1}{\pi}\int_0^{2\pi}x\cos nx\,dx
\]
\[
=\frac{1}{\pi}\left[(x)\left(\frac{\sin nx}{n}\right)-(1)\left(\frac{-\cos nx}{n^2}\right)\right]_0^{2\pi}
\]
\[
=\frac{1}{\pi}\left[\left(0+\frac{1}{n^2}\right)-\left(0+\frac{1}{n^2}\right)\right]=0
\]

---

## Page 4 — completion of \(x\) on \((0,2\pi)\), third example \(4-x^2\) on \((0,2\pi)\)

\[
b_n=\frac{1}{\pi}\int_0^{2\pi}x\sin nx\,dx
\]
\[
=\frac{1}{\pi}\left[(x)\left(\frac{-\cos nx}{n}\right)-(1)\left(\frac{-\sin nx}{n^2}\right)\right]_0^{2\pi}
\]
\[
=\frac{1}{\pi}\left[\left(-\frac{2\pi}{n}+0\right)-\left(0+0\right)\right]=-\frac{2}{n}
\]

\[
\therefore\quad x=\pi+\sum_{n=1}^{\infty}\left(-\frac{2}{n}\right)\sin nx
\]
\[
=\pi-2\sum_{n=1}^{\infty}\frac{\sin nx}{n}
\]

### Q. Find Fourier expansion for \(f(x)=4-x^2\) in \((0,2\pi)\)

**Sol.** Let
\[
f(x)=a_0+\sum_{n=1}^{\infty}a_n\cos nx+\sum_{n=1}^{\infty}b_n\sin nx
\qquad\left[(c,c+2l),\ c=0,\ l=\pi\right]
\]

\[
a_0=\frac{1}{2\pi}\int_0^{2\pi}\left(4-x^2\right)dx
\]
\[
=\frac{1}{2\pi}\left[4x-\frac{x^3}{3}\right]_0^{2\pi}
\]
\[
=\frac{1}{2\pi}\left\{\left(8\pi-\frac{8\pi^3}{3}\right)-0\right\}=4\left(1-\frac{\pi^2}{3}\right)=4-\frac{4\pi^2}{3}
\]

\[
a_n=\frac{1}{\pi}\int_0^{2\pi}\left(4-x^2\right)\cos nx\,dx
\]
\[
=\frac{1}{\pi}\left[(4-x^2)\left(\frac{\sin nx}{n}\right)-(-2x)\left(-\frac{\cos nx}{n^2}\right)+(-2)\left(-\frac{\sin nx}{n^3}\right)\right]_0^{2\pi}
\]
\[
=\frac{1}{\pi}\left[\left(0-\frac{4\pi}{n^2}+0\right)-\left(0-0+0\right)\right]
\]
\[
=-\frac{4}{n^2}
\]

`[Intermediate note: the upper-limit bracket is written as 0 − 4π/n² + 0. Checked: at x = 2π the term −(−2x)(−cos nx/n²) equals −4π/n², so the line is consistent.]`

\[
b_n=\frac{1}{\pi}\int_0^{2\pi}\left(4-x^2\right)\sin nx\,dx
\]
\[
=\frac{1}{\pi}\left[(4-x^2)\left(-\frac{\cos nx}{n}\right)-(-2x)\left(-\frac{\sin nx}{n^2}\right)+(-2)\left(\frac{\cos nx}{n^3}\right)\right]_0^{2\pi}
\]
\[
=\frac{1}{\pi}\left[\left\{\frac{4\pi^2-4}{n}-0-\frac{2}{n^3}\right\}-\left\{-\frac{4}{n}-0-\frac{2}{n^3}\right\}\right]
\]
\[
=\frac{1}{\pi}\left[\frac{4(\pi^2-1)}{n}+\frac{4}{n}\right]=\frac{1}{\pi}\left[\frac{4\pi^2}{n}-\frac{4}{n}+\frac{4}{n}\right]=\frac{4\pi}{n}
\]

\[
\therefore\quad 4-x^2=4-\frac{4\pi^2}{3}-4\sum_{n=1}^{\infty}\frac{\cos nx}{n^2}+4\pi\sum_{n=1}^{\infty}\frac{\sin nx}{n}
\]

---

## Page 5 — fourth example \(x\) on \((-\pi,\pi)\), fifth example \(x^2\) on \((-\pi,\pi)\)

### Q. Expand Fourier series for \(f(x)=x\) in \((-\pi,\pi)\)

**Sol.**
\[
f(x)=x
\]

Check of parity, `[as written]`:

> \(\therefore f(-x)=-x=-f(x)\)
>
> \(\therefore f(x)\) is odd function

\[
a_0=0,\qquad a_n=0
\]

\[
b_n=\frac{2}{\pi}\int_0^{\pi}x\sin nx\,dx
\]
\[
=\frac{2}{\pi}\left[(x)\left(\frac{-\cos nx}{n}\right)-(1)\left(\frac{-\sin nx}{n^2}\right)\right]_0^{\pi}
\]
\[
=\frac{2}{\pi}\left[\left\{-\frac{\pi(-1)^n}{n}+0\right\}-\left\{0+0\right\}\right]
\]
\[
=2\,\frac{(-1)^{n+1}}{n}
\]

\[
\therefore\quad f(x)=\sum_{n=1}^{\infty}b_n\sin nx
\]
\[
x=2\sum_{n=1}^{\infty}\frac{(-1)^{n+1}}{n}\sin nx
\]
\[
=2\left[\frac{\sin x}{1}-\frac{\sin 2x}{2}+\frac{\sin 3x}{3}-\frac{\sin 4x}{4}+\cdots\right]
\]

### Q. Expand Fourier series for \(f(x)=x^2\) in \((-\pi,\pi)\)

**Sol.**
\[
\because\ f(-x)=(-x)^2=x^2=f(x)
\]
\[
\therefore\ f(x)\ \text{is even}
\]

Let
\[
f(x)=a_0+\sum_{n=1}^{\infty}a_n\cos nx,\qquad \therefore b_n=0
\]

\[
a_0=\frac{1}{2\pi}\int_{-\pi}^{\pi}f(x)\,dx=\frac{2}{2\pi}\int_0^{\pi}x^2\,dx=\frac{1}{\pi}\left[\frac{x^3}{3}\right]_0^{\pi}
\]
\[
=\frac{1}{3\pi}\left(\pi^3-0\right)=\frac{\pi^2}{3}
\]

\[
a_n=\frac{2}{\pi}\int_0^{\pi}x^2\cos nx\,dx
\qquad\left[\because\ a_n=\frac{1}{\pi}\int_{-\pi}^{\pi}f(x)\cos nx\,dx=\frac{2}{\pi}\int_0^{\pi}f(x)\cos nx\,dx\right]
\]
\[
=\frac{2}{\pi}\left[(x^2)\left(\frac{\sin nx}{n}\right)-(2x)\left(\frac{-\cos nx}{n^2}\right)+(2)\left(\frac{-\sin nx}{n^3}\right)\right]_0^{\pi}
\]
\[
=\frac{2}{\pi}\left[\left(0+\frac{2\pi(-1)^n}{n^2}-0\right)-\left(0+0+0\right)\right]=\frac{4}{n^2}(-1)^n
\]

\[
\therefore\quad x^2=\frac{\pi^2}{3}+4\sum_{n=1}^{\infty}\frac{(-1)^n}{n^2}\cos nx
\]

---

## Page 6 — the same \(x^2\) example, restated, with three numerical deductions

### Q. Find Fourier expansion of \(f(x)=x^2,\ -\pi<x<\pi\) and hence prove that

> i) \(\dfrac{\pi^2}{6}=\displaystyle\sum_{n=1}^{\infty}\frac{1}{n^2}\)
>
> ii) \(\dfrac{\pi^2}{12}=\displaystyle\sum_{n=1}^{\infty}\frac{(-1)^{n+1}}{n^2}\)
>
> iii) \(\dfrac{\pi^2}{8}=\dfrac{1}{1^2}+\dfrac{1}{3^2}+\dfrac{1}{5^2}+\cdots\)

**Sol.**
\[
f(x)=a_0+\sum_{n=1}^{\infty}a_n\cos nx,\qquad \therefore f(x)\ \text{is even}
\]
\[
a_0=\frac{1}{\pi}\int_0^{\pi}x^2\,dx=\frac{\pi^2}{3}
\]
\[
a_n=\frac{2}{\pi}\int_0^{\pi}x^2\cos nx\,dx=\frac{4}{n^2}(-1)^n,\qquad b_n=0
\]
\[
\therefore\quad x^2=\frac{\pi^2}{3}+4\sum_{n=1}^{\infty}\frac{(-1)^n}{n^2}\cos nx\qquad\cdots(1)
\]

**i) Put \(x=\pi\) in (1):**
\[
\pi^2=\frac{\pi^2}{3}+4\sum_{n=1}^{\infty}\frac{(-1)^n}{n^2}(-1)^n
\]
\[
\therefore\quad \pi^2-\frac{\pi^2}{3}=4\sum_{n=1}^{\infty}\frac{(-1)^{2n}}{n^2}
\]
\[
\therefore\quad \frac{\pi^2}{6}=\sum_{n=1}^{\infty}\frac{1}{n^2}
\]
Marginal note: \(\left[\because\ (-1)^{2n}=1\right]\)

**ii) Put \(x=0\) in (1):**
\[
0=\frac{\pi^2}{3}+4\sum_{n=1}^{\infty}\frac{(-1)^n}{n^2}
\]
\[
\therefore\quad -\frac{\pi^2}{3}=4\sum_{n=1}^{\infty}\frac{(-1)^n}{n^2}
\]
\[
\therefore\quad \frac{\pi^2}{12}=\sum_{n=1}^{\infty}\frac{(-1)^{n+1}}{n^2}
\]

**iii) Adding (i) and (ii):** `[as written — "Adding (i) & (ii)" refers to the two results just proved]`
\[
\frac{\pi^2}{6}+\frac{\pi^2}{12}=\sum_{n=1}^{\infty}\left[\frac{1}{n^2}+\frac{(-1)^{n+1}}{n^2}\right]
\]
\[
\therefore\quad \frac{\pi^2}{4}=\left(\frac{1}{1^2}+\frac{1}{2^2}+\frac{1}{3^2}+\frac{1}{4^2}+\frac{1}{5^2}+\cdots\right)+\left(\frac{1}{1^2}-\frac{1}{2^2}+\frac{1}{3^2}-\frac{1}{4^2}+\cdots\right)
\]
\[
=2\left(\frac{1}{1^2}+\frac{1}{3^2}+\frac{1}{5^2}+\cdots\right)
\]
\[
\therefore\quad \frac{\pi^2}{8}=\frac{1}{1^2}+\frac{1}{3^2}+\frac{1}{5^2}+\cdots
\]

> **Transcription note (page 6).** All three deductions are correct. Note that \(a_0\) is written as \(\frac{1}{\pi}\int_0^\pi\) here but as \(\frac{1}{2\pi}\int_{-\pi}^{\pi}\) on page 5; the two are equal because \(f\) is even, so there is no inconsistency. `[verified]`

---

## Page 7 — sixth example \(x^2\) on \((0,2\pi)\), seventh example \(\left(\frac{\pi-x}{2}\right)^2\) on \((0,2\pi)\)

### Q. Expand Fourier series expansion for \(f(x)=x^2\) in \((0,2\pi)\)

**Sol.** Let
\[
f(x)=a_0+\sum_{n=1}^{\infty}a_n\cos nx+\sum_{n=1}^{\infty}b_n\sin nx
\]
\[
a_0=\frac{1}{2\pi}\int_0^{2\pi}x^2\,dx=\frac{1}{2\pi}\left[\frac{x^3}{3}\right]_0^{2\pi}
\]
\[
=\frac{1}{2\pi}\left[\frac{8\pi^3}{3}\right]=\frac{4\pi^2}{3}
\]

\[
a_n=\frac{1}{\pi}\int_0^{2\pi}x^2\cos nx\,dx
\]
\[
=\frac{1}{\pi}\left[(x^2)\left(\frac{\sin nx}{n}\right)-(2x)\left(\frac{-\cos nx}{n^2}\right)+(2)\left(\frac{-\sin nx}{n^3}\right)\right]_0^{2\pi}
\]
\[
=\frac{1}{\pi}\left[\left(0+\frac{4\pi}{n^2}-0\right)-\left(0+0+0\right)\right]=\frac{4}{n^2}
\]

\[
b_n=\frac{1}{\pi}\int_0^{2\pi}x^2\sin nx\,dx
\]
\[
=\frac{1}{\pi}\left[(x^2)\left(\frac{-\cos nx}{n}\right)-(2x)\left(\frac{-\sin nx}{n^2}\right)+(2)\left(\frac{\cos nx}{n^3}\right)\right]_0^{2\pi}
\]
\[
=\frac{1}{\pi}\left[\left(-\frac{4\pi^2}{n}-0-\frac{2}{n^3}\right)-\left(0+0-\frac{2}{n^3}\right)\right]
\]
\[
=-\frac{4\pi}{n}
\]

\[
\therefore\quad x^2=\frac{4\pi^2}{3}+4\sum_{n=1}^{\infty}\frac{1}{n^2}\cos nx-4\pi\sum_{n=1}^{\infty}\frac{\sin nx}{n}
\]

### Q. \(f(x)=\left(\dfrac{\pi-x}{2}\right)^2\) in \((0,2\pi)\)

**Sol.** Let
\[
f(x)=a_0+\sum_{n=1}^{\infty}a_n\cos nx+\sum_{n=1}^{\infty}b_n\sin nx
\]
\[
a_0=\frac{1}{2\pi}\int_0^{2\pi}f(x)\,dx=\frac{1}{2\pi}\int_0^{2\pi}\frac{(\pi-x)^2}{4}\,dx
\]
\[
=\frac{1}{8\pi}\left[\frac{(\pi-x)^3}{-3}\right]_0^{2\pi}=-\frac{1}{24\pi}\left(-\pi^3-\pi^3\right)=\frac{\pi^2}{12}
\]

\[
a_n=\frac{1}{\pi}\int_0^{2\pi}\frac{(\pi-x)^2}{4}\cos nx\,dx
\]
\[
=\frac{1}{4\pi}\left[(\pi-x)^2\left(\frac{\sin nx}{n}\right)-2(\pi-x)(-1)\left(\frac{-\cos nx}{n^2}\right)+(-2)(-1)\left(\frac{-\sin nx}{n^3}\right)\right]_0^{2\pi}
\]
\[
=\frac{1}{4\pi}\left[\left(0+\frac{2\pi}{n^2}+0\right)-\left(0-\frac{2\pi}{n^2}-0\right)\right]=\frac{1}{n^2}
\]

---

## Page 8 — completion of the \(\left(\frac{\pi-x}{2}\right)^2\) example

\[
b_n=\frac{1}{\pi}\int_0^{2\pi}\frac{(\pi-x)^2}{4}\sin nx\,dx
\]
\[
=\frac{1}{4\pi}\left[(\pi-x)^2\left(\frac{-\cos nx}{n}\right)-2(\pi-x)(-1)\left(\frac{-\sin nx}{n^2}\right)+(-2)(-1)\left(\frac{\cos nx}{n^3}\right)\right]_0^{2\pi}
\]
\[
=\frac{1}{4\pi}\left[\left\{-\frac{\pi^2}{n}-0+\frac{2}{n^3}\right\}-\left\{-\frac{\pi^2}{n}-0+\frac{2}{n^3}\right\}\right]
\]
\[
=0
\]

\[
\therefore\quad \frac{(\pi-x)^2}{4}=\frac{\pi^2}{12}+\sum_{n=1}^{\infty}\frac{1}{n^2}\cos nx
\]
\[
=\frac{\pi^2}{12}+\frac{\cos x}{1^2}+\frac{\cos 2x}{2^2}+\frac{\cos 3x}{3^2}+\cdots
\]

> **Transcription note (page 8).** The two brackets in \(b_n\) are identical, so \(b_n=0\); this is correct. The final series is correct and is the one used in the MUSA question bank (Q1.6) to deduce \(\pi^2/12\) and \(\pi^4/90\). `[verified]`

---

## Page-level summary

| PDF page | Content | Status |
|---:|---|---|
| 1 | Module heading, syllabus row, Dirichlet's conditions, general interval \((c,c+2l)\), \((0,2l)\), \((0,2\pi)\) | ✅ clear |
| 2 | \((-l,l)\), \((-\pi,\pi)\), even/odd functions, symmetric-limit integral property, even/odd series, two exponential integrals (unused) | ✅ clear |
| 3 | Trig values; \(x^2\) on \((0,2)\): \(a_0,a_n,b_n\); closing series with a \(\tfrac4\pi\) vs \(\tfrac4{\pi^2}\) slip; \(x\) on \((0,2\pi)\): \(a_0,a_n\) | ⚠️ one factor slip, flagged |
| 4 | \(b_n\) for \(x\); \(x=\pi-2\sum\frac{\sin nx}{n}\); \(4-x^2\) on \((0,2\pi)\) complete | ✅ clear |
| 5 | \(x\) on \((-\pi,\pi)\) (odd); \(x^2\) on \((-\pi,\pi)\) (even) to \(a_n\) | ✅ clear |
| 6 | \(x^2\) on \((-\pi,\pi)\) restated; three deductions \(\pi^2/6,\pi^2/12,\pi^2/8\) | ✅ clear |
| 7 | \(x^2\) on \((0,2\pi)\) complete; \(\left(\frac{\pi-x}{2}\right)^2\): \(a_0,a_n\) | ✅ clear |
| 8 | \(\left(\frac{\pi-x}{2}\right)^2\): \(b_n=0\); final series | ✅ clear |

**Unreadable passages:** none. Every formula on the eight pages was legible; the only doubtful readings were the interval label on page 3 ("\((0,2l)\)" while the working uses \(2l=2\)) and the crossed-out denominator in \(a_0\) on page 3. Both are recorded above rather than guessed.

**Teacher slips found:** one (page 3, common factor \(4/\pi\) instead of \(4/\pi^2\)). It is reproduced, flagged, and corrected in the study guide. No other numerical error was found: all six examples and all three deductions are correct.
