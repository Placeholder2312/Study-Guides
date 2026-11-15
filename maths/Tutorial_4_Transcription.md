# Tutorial 4 — Transcription

**Original source:** `02_Tutorials/Tutorial 4.docx`
**Document:** Word document, 1 page, Department of Engineering Science and Humanities
**Subject heading in document:** MATHEMATICS FOR COMPUTER ENGG. (2023111)
**Class heading in document:** SE-CSE
**Title:** TUTORIAL 4

**Recovery method:** the five questions each contain **two embedded Microsoft Equation Editor 3.0 objects** — one for the function, one for the interval — giving **ten objects in total**. Plain text extraction returns only the surrounding prose ("Expand Fourier series for … in …"), which is why the rendered page appears to be missing the mathematics. Every expression below was recovered from the object's vector WMF preview (rendered at 1400 px wide) and cross-checked against the OLE object order in `word/document.xml`. Nothing was inferred from context, and no question was invented.

---

## Document header

> DEPARTMENT OF ENGINEERING SCIENCE AND HUMANITIES
>
> MATHEMATICS FOR COMPUTER ENGG. (2023111)
>
> SE-CSE
>
> **TUTORIAL 4**

> **Note on the course code:** this tutorial prints **2023111**, which agrees with the official syllabus (PDF page 16). Tutorial 1 printed 2163111; that discrepancy is recorded in `04_OCR_Reports/OCR_Review_Report.md` and is not repeated here.

---

## The five questions

**1.** Expand Fourier series for \(f(x)=x^2\) in \((0,2)\).

**2.** Expand Fourier series for \(f(x)=x^2\) in \((0,2\pi)\).

**3.** Expand Fourier series for \(f(x)=x\) in \((-\pi,\pi)\).

**4.** Expand Fourier series for \(f(x)=x\) in \((0,2\pi)\).

**5.** Expand Fourier series for \(f(x)=\left(\dfrac{\pi-x}{2}\right)^2\) in \((0,2\pi)\).

No marks, hints, deductions or instructions to "hence prove" appear on the sheet. Each question asks only for the expansion.

---

## Embedded-equation map

| Q | Object (function) | Preview file | Recovered | Object (interval) | Preview file | Recovered |
|---|---|---|---|---|---|---|
| 1 | `oleObject1.bin` (`rId9`) | `image1.wmf` (`rId8`) | \(f(x)=x^2\) | `oleObject2.bin` (`rId11`) | `image2.wmf` (`rId10`) | \((0,2)\) |
| 2 | `oleObject3.bin` (`rId12`) | `image1.wmf` (**reused**) | \(f(x)=x^2\) | `oleObject4.bin` (`rId14`) | `image3.wmf` (`rId13`) | \((0,2\pi)\) |
| 3 | `oleObject5.bin` (`rId16`) | `image4.wmf` (`rId15`) | \(f(x)=x\) | `oleObject6.bin` (`rId18`) | `image5.wmf` (`rId17`) | \((-\pi,\pi)\) |
| 4 | `oleObject7.bin` (`rId20`) | `image6.wmf` (`rId19`) | \(f(x)=x\) | `oleObject8.bin` (`rId22`) | `image7.wmf` (`rId21`) | \((0,2\pi)\) |
| 5 | `oleObject9.bin` (`rId24`) | `image8.wmf` (`rId23`) | \(f(x)=\left(\dfrac{\pi-x}{2}\right)^2\) | `oleObject10.bin` (`rId25`) | `image7.wmf` (**reused**) | \((0,2\pi)\) |

Two previews are shared because the equations are byte-identical: \(f(x)=x^2\) appears in Q1 and Q2, and the interval \((0,2\pi)\) appears in Q2, Q4 and Q5. Word stores one WMF per distinct display and links it from each object. This is why the document contains **10 OLE objects but only 8 WMF previews** — not a sign of missing content.

`word/media/image9.jpg` is the college letterhead graphic, not mathematical content.

---

## Recovery status

| Item | Result |
|---|---|
| Questions on the sheet | 5 |
| Embedded equation objects | 10 of 10 recovered |
| Preview files available | 8 of 8 rendered successfully (GDI+ vector rendering) |
| Expressions that had to be guessed | **0** |
| Content genuinely absent from the file | **none** |

**Conclusion:** Tutorial 4's mathematics is **fully recoverable** from the original DOCX. The apparent gap in a plain-text or quick visual render is an artefact of Equation Editor 3.0 embedding, exactly as in Tutorial 1. Nothing is awaiting source clarification.

---

## Relation to the teacher's notes

Every Tutorial 4 question is one of the teacher's worked examples:

| Tutorial | Teacher's notes | Teacher's page |
|---|---|---|
| Q1 \(x^2\) on \((0,2)\) | Example 1 | 3 |
| Q2 \(x^2\) on \((0,2\pi)\) | Example 6 | 7 |
| Q3 \(x\) on \((-\pi,\pi)\) | Example 4 | 5 |
| Q4 \(x\) on \((0,2\pi)\) | Example 2 | 3–4 |
| Q5 \(\left(\frac{\pi-x}{2}\right)^2\) on \((0,2\pi)\) | Example 7 | 7–8 |

This is useful: the tutorial is a **rehearsal of the six classroom examples**, so a student who can do Tutorial 4 unaided can do every technique the module requires.

---

## Verification performed

Each question was expanded independently with SymPy and compared with the transcription and with the teacher's answer (`_work/verify_m4.py`, `_work/verify_m4b.py`).

| Q | Symbolic check | Result |
|---|---|---|
| 1 | \(a_0=\frac43,\ a_n=\frac{4}{n^2\pi^2},\ b_n=-\frac{4}{n\pi}\) on \((0,2)\) | ✅ matches |
| 2 | \(a_0=\frac{4\pi^2}{3},\ a_n=\frac{4}{n^2},\ b_n=-\frac{4\pi}{n}\) on \((0,2\pi)\) | ✅ matches |
| 3 | \(a_0=a_n=0,\ b_n=\frac{2(-1)^{n+1}}{n}\) on \((-\pi,\pi)\) | ✅ matches |
| 4 | \(a_0=\pi,\ a_n=0,\ b_n=-\frac2n\) on \((0,2\pi)\) | ✅ matches |
| 5 | \(a_0=\frac{\pi^2}{12},\ a_n=\frac1{n^2},\ b_n=0\) on \((0,2\pi)\) | ✅ matches |

Worked answers are in the study guide (§6.4).
