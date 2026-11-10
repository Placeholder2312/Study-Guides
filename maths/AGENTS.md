# AGENTS.md — Mathematics for Computer Engineering (Semester III)

Project instructions for every future OpenCode session in this workspace.

---

## 1. Academic context

- **University:** University of Mumbai
- **Programme:** B.E. — Computer Science and Engineering (Artificial Intelligence and Machine Learning)
- **Year:** Second Year
- **Semester:** III
- **Scheme:** NEP 2020
- **Subject:** Mathematics for Computer Engineering
- **Official course code:** **2023111** (the Tutorial 1 sheet misprints it as 2163111)
- **Teaching scheme:** Theory 2 hours + Tutorial 1 hour per week; 3 credits
- **Assessment:** IAT-I 20 + IAT-II 20 + End-Semester 60 + Term Work 25 = 125 marks
- **Student's starting level:** almost zero mathematical background. Explain from first principles; never assume prior fluency.
- **Preparation window:** 7 days.

The student is learning for understanding and examination performance, not for research mathematics. Every explanation must be usable by someone meeting the topic for the first time.

---

## 2. Source of truth

`00_University_Syllabus/Syllabus_Coverage.md` is the authoritative statement of what is examinable. It was extracted from the official University of Mumbai document in `00_University_Syllabus/Portion (6.21-N-B.E.-AI-ML-sem-III-IV).pdf` (PDF pages 16–18).

Rules:

1. **Never replace the official syllabus with a generic engineering-mathematics syllabus.**
2. If a topic is not in `Syllabus_Coverage.md`, label it clearly as enrichment, not prescribed content.
3. Preserve the official module boundaries, module numbering, teaching hours and CO mapping.
4. Self-learning topics are listed separately in the syllabus and must be treated separately in teaching material.
5. If a new syllabus document is uploaded, re-extract and update `Syllabus_Coverage.md`; do not silently edit the old extraction.
6. Original terminology must be retained. The official document contains the spellings `reminder theorem`, `Eluer's theorem` and `Divisiblility`; keep them when quoting, optionally adding `[sic]`.

### Syllabus at a glance

| Module | Topic | Hours |
|---|---|---:|
| I | Linear Algebra (Theory of Matrices) | 5 |
| II | Linear and Non-Linear Programming Problems | 5 |
| III | Modular Arithmetic | 4 |
| IV | Fourier Series | 4 |
| V | Statistical Techniques | 4 |
| VI | Probability | 4 |

---

## 3. Directory layout and what belongs where

```text
Maths/
├── AGENTS.md                     ← this file
├── 00_University_Syllabus/       ← official syllabus + Syllabus_Coverage.md
├── 01_Original_Notes/
│   ├── Module_1/                 ← original handwritten notes (do not modify)
│   ├── Module_2/ … Module_6/     ← currently empty, awaiting uploads
├── 02_Tutorials/                 ← original tutorial sheets (do not modify)
├── 03_Transcriptions/            ← Markdown/LaTeX transcriptions + Source_Index.md
├── 04_OCR_Reports/               ← OCR review and verification reports
├── 05_Study_Guides/              ← teaching material (future session)
├── 06_Revision/                  ← revision sheets, practice sets, answer keys
├── 07_Unidentified/              ← documents that cannot be confidently classified
└── _work/                        ← audit artefacts: rendered pages, crops, verification scripts
```

`_work/` is scratch material, not study content. It holds the rendered page images used for
vision transcription, the close-up crops used to settle doubtful symbols, the OCR tool tests, and
the SymPy verification scripts. Keep it: every claim in the OCR report can be re-checked from it.

### Current library status

| Item | Location | Status |
|---|---|---|
| Official syllabus PDF (72 pages) | `00_University_Syllabus/` | Present, unmodified |
| Syllabus extraction | `00_University_Syllabus/Syllabus_Coverage.md` | Complete |
| Module 1 handwritten notes (20 pages) | `01_Original_Notes/Module_1/CSE Module 1.pdf` | Present, unmodified |
| Module 1 transcription | `03_Transcriptions/Module_1_Transcription.md` | Complete |
| Tutorial 1 (5 questions, 7 equation objects) | `02_Tutorials/Tutorial 1.docx` | Present, unmodified |
| Tutorial 1 transcription | `03_Transcriptions/Tutorial_1_Transcription.md` | Complete |
| Modules 2–6 notes | `01_Original_Notes/` | **Not yet supplied** |

There are no duplicate source files.

---

## 4. Handling original files

1. **Never edit, rename, delete or overwrite an original.** Originals are evidence.
2. New uploads should be inspected by content, not by filename. Filenames are not reliable.
3. Classify each upload as: syllabus, teacher notes for a specific module, tutorial, or other study material. Move it to the matching folder.
4. If classification is uncertain, place it in `07_Unidentified/` and report it. Do not guess.
5. If duplicates appear, report them and preserve both.
6. Do not move `AGENTS.md`, project configuration, Git files or unrelated project resources.
7. Do not search unrelated directories on the student's computer.

---

## 5. Transcription rules

All mathematical transcriptions live in `03_Transcriptions/`.

1. A transcription is **faithful reproduction**, not a rewrite and not a study guide.
2. Preserve the teacher's ordering, wording, examples, intermediate calculations and notation.
3. Every section must cite its **original PDF page number**.
4. Use clean Markdown with LaTeX (`$...$` inline, `$$...$$` display).
5. Reproduce matrices exactly, including dimensions, signs and zero entries.
6. **Never invent or “fix” a missing expression.** If a symbol or entry is unreadable, write `[UNCLEAR — PDF PAGE X]`.
7. If the teacher makes a mathematical or notational slip, reproduce it **as written** and flag it with a visible transcription note. Never silently correct the teacher.
8. Keep a per-document section in `Source_Index.md` mapping transcription → original file → page numbers.
9. New or changed transcriptions must be checked symbolically with SymPy (or an equivalent exact tool) wherever the mathematics permits.

### Existing transcription conventions

- `λ` is used for the eigenvalue symbol.
- `[as written]` marks the teacher's own oddity.
- `[UNCLEAR — PDF PAGE X]` marks genuinely unreadable content.
- Editorial brackets `[...]` mark additions needed only for readability.

---

## 6. OCR and document-processing rules

1. Prefer **free, open-source, locally running** tools. Do not use paid APIs or subscriptions.
2. Check what is already installed before installing anything.
3. Do not modify global OpenCode settings or install arbitrary plugins.
4. Do not assume the AI model supports images — verify it on an actual page before relying on it.
5. For DOCX files, inspect the OOXML. Mathematical expressions are often embedded objects (Equation Editor 3.0 / OMML) and will not appear in plain text extraction. Recover them from the embedded preview (WMF/EMF) or object stream; never reconstruct them from context.
6. For scanned PDFs, render pages at ≥150 dpi and read them directly; printed-text OCR such as RapidOCR/Tesseract is unreliable on cursive handwriting.
7. Record tool choices, test results and uncertainties in `04_OCR_Reports/OCR_Review_Report.md`.
8. Verified working setup on this machine: Python 3.12, PyMuPDF, python-docx, SymPy, Pillow, RapidOCR (tested, not suitable for handwriting). Tesseract, PaddleOCR and pix2tex are not installed.

---

## 7. Study-guide rules (for the later teaching session)

Study guides go in `05_Study_Guides/`; revision material and answer keys go in `06_Revision/`.

### Teaching style the student wants

- **Beginner-friendly, human explanations.** Start with intuition, then formal definition, then procedure.
- **Assume almost zero prior knowledge.** Define every symbol the first time it appears.
- **Small steps.** Show why each step is allowed, not only what to compute.
- **Worked examples.** At least one fully worked example per concept, with all intermediate arithmetic visible.
- **Independent practice.** End each section with exercises the student attempts alone.
- **Separate answer keys.** Answers must not sit immediately beside the questions; keep them in a distinct file or a clearly separated section at the end.
- **Exam orientation.** Map practice to the Mumbai University pattern: Q1 compulsory, mixed-module questions, 20 marks each, three questions to answer.
- **Honest difficulty labels.** Mark questions as basic / exam-level / challenging.

### Mathematical accuracy requirements

1. Every formula, matrix operation and numerical result must be checked, ideally with SymPy.
2. Never present a guessed value. If a source is uncertain, say so and point to the transcription note.
3. Keep the teacher's original method and notation unless there is a documented reason to add an alternative.
4. Distinguish clearly between:
   - prescribed syllabus content,
   - self-learning topics,
   - enrichment beyond the syllabus.
5. Do not claim a topic is “important” or “frequently asked” without evidence from the supplied syllabus or tutorials.
6. When a study guide and a transcription disagree, the transcription of the original is the authority; investigate before changing either.

### Suggested study-guide structure

1. Why this topic exists (one short, concrete motivation).
2. Prerequisites in plain language.
3. Definitions and notation.
4. Method, as a numbered recipe.
5. Fully worked example(s).
6. Common mistakes.
7. Independent practice (with mark allocations).
8. Answer key in a separate section/file.
9. Syllabus mapping and page references to the original notes.

---

## 8. What not to do in the current phase

The source library has been organised and verified. Study guides were explicitly **not** created in the setup session. Do not treat `05_Study_Guides/` or `06_Revision/` as populated until a teaching session produces content there.

Do not:

- rewrite or “improve” the faithful transcriptions,
- add teaching commentary inside transcription files,
- delete the `_work/` audit artefacts without being asked,
- modify original PDFs or the DOCX,
- claim modules 2–6 have been processed when no notes exist for them.

---

## 9. Quick reference for a new session

1. Read this file and `00_University_Syllabus/Syllabus_Coverage.md`.
2. Check `03_Transcriptions/Source_Index.md` for what has already been transcribed.
3. Check `04_OCR_Reports/OCR_Review_Report.md` for known uncertainties before teaching a topic.
4. Inspect the project root for newly uploaded files; classify by content.
5. Work only inside this project directory.
6. When producing mathematics, verify with SymPy and cite the source page.
