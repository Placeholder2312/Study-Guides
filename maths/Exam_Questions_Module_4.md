# Module 4 examination questions — source extraction

**Purpose:** an exact record of every Module 4 (Fourier series) question in the three supplied examination documents, with original wording, function, interval, marks where printed, and page reference. Only Module 4 items are recorded; all other modules are excluded.

**Provenance warning.** None of these documents is a University of Mumbai question paper.

| ID | Document | What it actually is |
|---|---|---|
| **MUSA-PP-2025** | `_work/sources/musa-practice-paper-set1-w2025.pdf` (3 pages) | *MUSA (Mumbai University Students Association) — Practice Paper Set-I of Mathematics for Computer Engineering*, S.E. Sem-III, NEP Scheme, **Winter Session 2025**, 2 hours, 60 marks. The paper itself states: *"This is the test paper for practice purpose"* and *"Numerical values may change in the exam, but the type of questions will remain the same."* |
| **MUSA-QB-2026** | `_work/sources/musa-question-bank-2026.pdf` (9 pages) | *MUSA Question Bank of Mathematics for Computer Engineering*, S.E. Sem-III, NEP 2020, **Winter Session 2026**, Regular & KT batches. A topic-wise question bank, not a paper. |
| **SOL-M4** | `_work/sources/maths-question-bank-solutions.pdf` (108 pages; Module 4 = PDF pages 46–77) | A third-party worked-solution booklet. It has no official standing and was used only as a cross-check. |

---

## 1. MUSA practice paper Set-I (Winter 2025) — Module 4 items

Three questions in the paper belong to Module 4. The paper is organised as Q.1 compulsory plus Q.2–Q.6; "attempt any three questions from Q.2 to Q.5" is printed in the instructions, although a Q.6 also appears.

| Ref | Page | Marks | Exact wording |
|---|---:|---:|---|
| **PP-1** | 2 | **5** | "Find the Fourier series of f(x) = \(x^2\), \(-\pi\le x\le\pi\), and hence, prove that \(\dfrac{\pi^2}{8}=\dfrac{1}{1^2}+\dfrac{1}{3^2}+\dfrac{1}{5^2}+\cdots\)" — printed as **Q.2 b)** |
| **PP-2** | 2 | **6** | "Find Fourier to represent f(x) = \(x^2\) in \((0,2\pi)\) and hence, deduce that: \(\dfrac{\pi^2}{12}=\dfrac{1}{1^2}-\dfrac{1}{2^2}+\dfrac{1}{3^2}-\dfrac{1}{4^2}+\cdots\)" — printed as **Q.3 c)** |
| **PP-3** | 2 | **4** | "Find the Fourier series for \(f(x)=1-x^2\) in \((-1,1)\)" — printed as **Q.5 a)** |

Notes:

- Q.2 also has an "OR" alternative (a Cayley–Hamilton part), Q.3 has "OR" alternatives for parts (a) and (b), and Q.5 is followed by an "OR" on page 3 (a diagonalisation part). The three items above are the only Module 4 parts.
- The phrase "Find Fourier to represent" in PP-2 is reproduced exactly as printed. `[as printed]`
- Marks are printed in the right margin: 5, 6 and 4 respectively.
- No Module 4 content appears on page 1 or page 3.

---

## 2. MUSA question bank (Winter 2026) — Module 4

Module 4 occupies the bottom third of **PDF page 4** and the top two-thirds of **PDF page 5**. Page 6 begins Module 5. The bank groups Module 4 questions under four headings, reproduced verbatim.

### 2.1 "Fourier series (0, 2π)" — page 4 (Q.1–Q.3) and page 5 (Q.4–Q.7)

| Ref | Page | Exact wording |
|---|---:|---|
| **QB-1** | 4 | "Find a Fourier series to represent f(x) = \(x^2\) in \((0,2\pi)\) and hence, deduce that: \(\dfrac{\pi^2}{12}=\dfrac{1}{1^2}-\dfrac{1}{2^2}+\dfrac{1}{3^2}-\dfrac{1}{4^2}+\cdots\)" |
| **QB-2** | 4 | "Find the Fourier series for \(f(x)=\dfrac{3x^2-6\pi x+2\pi^2}{12}\) in \((0,2\pi)\). Hence deduce that \(\dfrac{\pi^2}{6}=\dfrac{1}{1^2}+\dfrac{1}{2^2}+\dfrac{1}{3^2}\cdots\)" |
| **QB-3** | 4 | "Find the Fourier series for \(f(x)=x\sin x\) in the interval of \(0\le x\le 2\pi\). Deduce that \(\sum_{n=2}^{\infty}\dfrac{1}{n^2-1}=\dfrac{3}{4}\)." |
| **QB-4** | 5 | "Find the Fourier series for \(f(x)=\frac12(\pi-x)\) in \((0,2\pi)\). Hence deduce that \(\dfrac{\pi}{4}=1-\dfrac13+\dfrac15-\dfrac17+\cdots\)" |
| **QB-5** | 5 | "Find Fourier expansion for \(f(x)=\sqrt{1-\cos x}\) in \((0,2\pi)\). Hence deduce that \(\dfrac12=\sum_{1}^{\infty}\dfrac{1}{4n^2-1}\)." |
| **QB-6** | 5 | "Find Fourier expansion for \(f(x)=\left(\dfrac{\pi-x}{2}\right)^2\) in the interval of \(0\le x\le 2\pi\) and \(f(x+2\pi)=f(x)\). Also deduce that: i) \(\dfrac{\pi^2}{12}=\dfrac{1}{1^2}-\dfrac{1}{2^2}+\dfrac{1}{3^2}-\dfrac{1}{4^2}+\cdots\)  ii) \(\dfrac{\pi^2}{90}=\dfrac{1}{1^4}+\dfrac{1}{2^4}+\dfrac{1}{3^4}+\dfrac{1}{4^4}+\cdots\)d" `[as printed; the trailing "d" is a typo in the bank]` |
| **QB-7** | 5 | "Obtain Fourier Series for the function \(f(x)=\begin{cases}1+\dfrac{2x}{\pi},&-\pi\le x\le 0\\[2mm]1-\dfrac{2x}{\pi},&0\le x\le\pi\end{cases}\)" |

Note on QB-6(ii): as printed the right-hand side is a sum of fourth powers, so the left-hand side must be \(\pi^4/90\). The printed \(\pi^2/90\) is a dimensional misprint; the solution booklet flags the same misprint explicitly (PDF page 57). Recorded, not silently changed. See the OCR report §7.3.

Note on QB-7: filed under "(0, 2π)" in the bank but its interval is \((-\pi,\pi)\). It is an even function. Recorded as printed and placed correctly in the study guide.

### 2.2 "Fourier series (0, 2l)" — page 5

| Ref | Page | Exact wording |
|---|---:|---|
| **QB-8** | 5 | "Find the Fourier series of f(x) = \(x^2\) in (0, a). Hence deduce that: \(\dfrac{\pi^2}{6}=\dfrac{1}{1^2}+\dfrac{1}{2^2}+\dfrac{1}{3^2}+\dfrac{1}{4^2}+\cdots\)" |
| **QB-9** | 5 | "Find the Fourier expansion of \(f(x)=2x-x^2\). Whose period is 3." |
| **QB-10** | 5 | "If \(f(x)=\begin{cases}\pi x,&0\le x\le 1\\ \pi(2-x),&1\le x\le 2\end{cases}\) with the period of 2, Show that \(f(x)=\dfrac{\pi}{2}-\dfrac{4}{\pi}\sum_{n=0}^{\infty}\dfrac{1}{(2n+1)^2}\cos(2n+1)\pi x\)" |
| **QB-11** | 5 | "If \(f(x)=\begin{cases}\pi x,&0<x<1\\ 0,&1<x<2\end{cases}\) with the period of 2." |
| **QB-12** | 5 | "Find the Fourier expansion of f(x) = \(4-x^2\) in the interval (0, 2) Hence deduce that \(\dfrac{\pi^2}{6}=\dfrac{1}{1^2}+\dfrac{1}{2^2}+\dfrac{1}{3^2}+\cdots\)" |

Notes: QB-8 and QB-10 use the letter **a** for the half-period boundary / interval end, not \(l\); QB-9's period 3 means the interval length is 3; QB-11 gives no explicit instruction beyond finding the expansion. In this section the bank numbers **two different questions "Q.2"** (period-3 parabola and the piecewise triangle). Both are recorded; the second is referred to here as QB-10.

### 2.3 "Fourier series of even and odd functions — \((-\pi,\pi)\)" — page 5

| Ref | Page | Exact wording |
|---|---:|---|
| **QB-13** | 5 | "Find the Fourier series of f(x) = \(x^2\), \(-\pi\le x\le\pi\), and hence, prove that \(\dfrac{\pi^2}{8}=\dfrac{1}{1^2}+\dfrac{1}{3^2}+\dfrac{1}{5^2}+\cdots\)" |
| **QB-14** | 5 | "Obtain the Fourier series for the function \(f(x)=\begin{cases}1+\dfrac{2x}{\pi},&-\pi\le x\le-0\\[2mm]1-\dfrac{2x}{\pi},&0\le x\le\pi\end{cases}\) Hence deduce that \(\dfrac{\pi^2}{8}=\dfrac{1}{1^2}+\dfrac{1}{3^2}+\dfrac{1}{5^2}+\cdots\)" |
| **QB-15** | 5 | "Obtain Fourier series \(x\cos x\) in \((-\pi,\pi)\)." |
| **QB-16** | 5 | "Obtain Fourier series for \(f(x)=\begin{cases}x+\dfrac{2x}{\pi},&-\pi<x<-0\\[2mm]\dfrac{\pi}{2}-x,&0<x<\pi\end{cases}\) Hence deduce that \(\dfrac{\pi^2}{8}=\dfrac{1}{1^2}+\dfrac{1}{3^2}+\dfrac{1}{5^2}+\cdots\)" |
| **QB-17** | 5 | "If \(f(x)=x-x^2,\ -\pi<x<\pi\). Hence, deduce that, \(\dfrac{\pi^2}{12}=\dfrac{1}{1^2}-\dfrac{1}{2^2}+\dfrac{1}{3^2}-\dfrac{1}{4^2}+\cdots\)" |
| **QB-18** | 5 | "If \(f(x)=|x|\) in \((-\pi,\pi)\). Hence, deduce that \(\dfrac{\pi^2}{8}=\dfrac{1}{1^2}+\dfrac{1}{3^2}+\dfrac{1}{5^2}+\dfrac{1}{7^2}\cdots\)" |

Note on QB-16: the first branch is printed \(x+\dfrac{2x}{\pi}\), which is neither even nor odd and does **not** produce the stated \(\pi^2/8\) deduction. The intended function — confirmed independently by the solution booklet (PDF page 69) and by the fact that the deduction only works for it — is \(\dfrac{\pi}{2}+x\) on \((-\pi,0)\) together with \(\dfrac{\pi}{2}-x\) on \((0,\pi)\). The printed form is preserved verbatim here; the study guide solves the corrected version and states clearly that it has done so. This is the only place in the supplied sources where a question's data is internally inconsistent.

### 2.4 "\((-l,l)\)" — page 5

| Ref | Page | Exact wording |
|---|---:|---|
| **QB-19** | 5 | "Find the Fourier series for \(f(x)=1-x^2\) in \((-1,1)\)" |
| **QB-20** | 5 | "Obtain the Fourier series of \(x^2\) from \(-l\) to \(x=l\) and hence, deduce that \(\dfrac{\pi^2}{12}=\dfrac{1}{1^2}-\dfrac{1}{2^2}+\dfrac{1}{3^2}-\dfrac{1}{4^2}+\cdots\)" |
| **QB-21** | 5 | "Find Fourier expansion for \(f(x)=x-x^2,\ -1<x<1\)" |
| **QB-22** | 5 | "Find the Fourier expansion of \(f(x)=f(x)=\begin{cases}0,&-2<x<-1\\1+x,&-1<x<0\\1-x,&0<x<1\\0,&1<x<2\end{cases}\)" `[as printed; "f(x) = f(x) =" is duplicated in the bank]` |

---

## 3. Counts and overlap

| Group | Questions |
|---|---:|
| MUSA practice paper Set-I | 3 |
| MUSA question bank | 22 |
| **Total distinct Module 4 questions supplied** | **25** |

Duplicates across sources (not errors — the same function recurs because it is the standard teaching example):

| Function | Appears in |
|---|---|
| \(x^2\) on \((0,2\pi)\), deduce \(\pi^2/12\) | PP-2, QB-1, teacher's page 7 (without deduction) |
| \(x^2\) on \((-\pi,\pi)\), deduce \(\pi^2/8\) (or the full set) | PP-1, QB-13, teacher's pages 5–6 |
| \(1-x^2\) on \((-1,1)\) | PP-3, QB-19 |
| triangular \(1\pm 2x/\pi\) | QB-7, QB-14 |
| piecewise 4-part pulse on \((-2,2)\) | QB-22 (also solved in SOL-M4, PDF p. 75–76) |

---

## 4. What the solution booklet contains

`SOL-M4` covers all 22 bank questions (PDF pages 46–77) plus a formula summary and a deduction table. It uses the \(\frac{a_0}{2}\) convention throughout. It is **not** an official solution key. Every result quoted from it in the study guide was re-derived independently: its summary table agrees with independent derivation throughout, and the two printed errors that do exist are in the question bank itself (the \(\pi^2/90\) misprint and the QB-16 data error), not in the booklet's answers. See `04_OCR_Reports/OCR_Review_Report_Module_4.md` §7.
