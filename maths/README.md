# Mathematics for Computer Engineering — Semester III

Notes for **2023111 Mathematics for Computer Engineering**, B.E. Computer Science and Engineering
(AI & ML), Semester III, University of Mumbai (NEP 2020).

This folder is the working library: official syllabus scope, faithful transcriptions of the
lecture notes and tutorial sheets, the study guides themselves, and audit reports recording how
each transcription and every computed result was verified.

## Guides

| Guide | Modules covered |
|---|---|
| [`modules/module-1`](modules/module-1.html) | Module 1 — Linear Algebra: Theory of Matrices |
| [`modules/module-4`](modules/module-4.html) | Module 4 — Fourier Series |

Both are single self-contained HTML pages: the guide text is embedded in the page and typeset in
the browser with MathJax, so they need an internet connection for the formulas. The Module 4 text is
also kept as portable Markdown in `Module_4_Study_Guide.md`.

## What's here

| File | Contents |
|---|---|
| `Syllabus_Coverage.md` | Official syllabus extraction — six modules, teaching hours, CO mapping, self-learning topics, textbooks, assessment scheme |
| `Module_1_Transcription.md` | Module 1 (Linear Algebra / Theory of Matrices), 20 handwritten pages, page-referenced |
| `Tutorial_1_Transcription.md` | Tutorial 1, five questions with all embedded equations recovered |
| `Module_4_Study_Guide.md` | Module 4 (Fourier Series) study guide — Dirichlet's conditions, periods 2π and 2l, even and odd functions, worked expansions, graded practice and a separate answer key |
| `Module_4_Transcription.md` | Module 4 notes, 8 handwritten pages, page-referenced |
| `Tutorial_4_Transcription.md` | Tutorial 4, five questions with all ten embedded equations recovered |
| `Exam_Questions_Module_4.md` | 25 Module 4 examination questions with provenance, original wording and a duplicate map |
| `Module_4_Revision_Sheet.md` | Module 4 revision sheet; self-test answers kept in a separate closing section |
| `Source_Index.md` | Maps every transcription back to its source file and page numbers |
| `OCR_Review_Report.md` | Module 1: tools tested, why each was chosen or rejected, unresolved readings, SymPy verification results |
| `OCR_Review_Report_Module_4.md` | Module 4: equation recovery from the tutorial DOCX, page readings, source errata, SymPy verification summary |
| `AGENTS.md` | Conventions for maintaining this library |

## Scope

| Module | Topic | Hours |
|---|---|---:|
| I | Linear Algebra (Theory of Matrices) | 5 |
| II | Linear and Non-Linear Programming Problems | 5 |
| III | Modular Arithmetic | 4 |
| IV | Fourier Series | 4 |
| V | Statistical Techniques | 4 |
| VI | Probability | 4 |

Modules I and IV have been transcribed and written up. Modules II, III, V and VI are extracted in
the syllabus but no lecture notes for them have been supplied yet.

## Transcription policy

These files are **faithful reproductions**, not study guides. They preserve the lecturer's
ordering, wording, notation and arithmetic — including slips, which are flagged in place rather
than silently corrected. Unreadable content is marked `[UNCLEAR — PDF PAGE N]` rather than guessed.

Where a transcription and a study guide disagree, the transcription is the authority.

## Verification

Every matrix, eigenvalue, eigenvector, Cayley–Hamilton identity and diagonalisation in the
transcribed Module 1 material was independently checked with SymPy. Results are recorded in
`OCR_Review_Report.md`, including the six lecturer slips preserved as written and the one
genuinely faint reading.

For Module 4, every Fourier coefficient, series, integration sign and numerical deduction was
checked with SymPy 1.14. `OCR_Review_Report_Module_4.md` records the results, the teacher's one
numerical slip (notes page 3 prints `4/π` where `4/π²` is correct), and two errata in the
student-association question bank.

## Notes on sources

The source PDFs and DOCX are not included here. The syllabus document and the handwritten lecture
notes are not my work, and this repository is public. The transcriptions are derived from them for
personal study.
