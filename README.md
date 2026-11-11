# Study Guides

Exam-focused study guides for **B.E. Computer Science and Engineering (Artificial Intelligence and Machine Learning), Semester III**, University of Mumbai, NEP 2020 (scheme effective 2025–26).

**Live site:** <https://study-guides-placeholder.vercel.app>

The site is a static, mobile-first library: one homepage lists the Semester III subjects, each subject has its own page, and each page lists its modules. Guides are written to be read on a phone, with a light theme by default and an optional dark theme.

---

## Contents

- [Status](#status)
- [Design and features](#design-and-features)
- [How the Mathematics Module 1 guide was built](#how-the-mathematics-module-1-guide-was-built)
- [How the DSGT guides were built](#how-the-dsgt-guides-were-built)
- [Repository structure](#repository-structure)
- [Hosting and routing](#hosting-and-routing)
- [Adding content](#adding-content)
- [Sources, limitations and disclosure](#sources-limitations-and-disclosure)

---

## Status

Subjects and module names follow the official University of Mumbai Semester III syllabus (item 6.21 (N), AC 20/5/2025).

| Subject | Course | Ready | Modules |
|---|---|---|---|
| Discrete Structures and Graph Theory (DSGT) | 2023112 | 2 of 6 | 1 Crisp Set Theory and Logic (soon) · 2 Mathematical Relations (soon) · 3 Functions (soon) · **4 Counting** · **5 Algebraic Structures** · 6 Graph Theory (soon) |
| Mathematics for Computer Engineering | 2023111 | 1 of 6 | **1 Linear Algebra: Theory of Matrices** · 2 Linear and Non-Linear Programming Problems (soon) · 3 Modular Arithmetic (soon) · 4 Fourier Series (soon) · 5 Statistical Techniques (soon) · 6 Probability (soon) |
| Analysis of Algorithm | 2023113 | 0 of 6 | Introduction · Divide and Conquer · Greedy Method · Dynamic Programming · Backtracking and Branch and Bound · String Matching (all soon) |
| Computer Organization and Architecture | 2023114 | 0 of 6 | Computer Fundamentals · ALU Operations · Processor Organization and Control Unit Design · Memory Systems Organization · I/O Organization · Parallel Processing (all soon) |

Labs, the open elective, Full Stack Java, Entrepreneurship Development and Environmental Science are not covered.

---

## Design and features

- **Mobile first.** Every page is checked at phone width. Tables scroll inside their own box rather than stretching the page, and tap targets are at least 44 px.
- **Light by default, dark on request.** A square toggle on each page switches themes. The choice is saved in the browser under the key `sg-theme`. The site does not follow the operating system's dark setting unless the reader chooses it.
- **One visual language.** Black on white, Georgia headings, Helvetica body text, a single blue accent, hairline rules and no rounded corners. Colours are CSS variables, so the dark theme redefines the same names.
- **Real diagrams.** Venn diagrams, a pigeonhole diagram and similar figures are inline SVG that follow the theme and scale to the screen.
- **Print styles.** Pages print in light mode with navigation hidden.
- **No build step.** Plain HTML and CSS with a small amount of inline JavaScript. The Mathematics guide additionally loads MathJax and a Markdown renderer from a CDN, so it needs an internet connection to render formulas.

---

## How the Mathematics Module 1 guide was built

The Linear Algebra guide ([`maths/modules/module-1.html`](maths/modules/module-1.html)) is the most heavily engineered part of the project. It was produced by AI agents working in structured, rule-bound sessions, with the student supplying the source material and the teaching requirements. It was not a single prompt. It followed a pipeline in which every stage left evidence that can be audited.

### 1. Source library

Three originals were collected and left unmodified, each identified by SHA-256 hash in [`maths/Source_Index.md`](maths/Source_Index.md):

| Source | Form |
|---|---|
| Official syllabus, 72 pages | Born-digital PDF (Mathematics pages 16–18 used) |
| Teacher's Module 1 notes, 20 pages | Scanned cursive handwriting with matrices |
| Tutorial 1 | Word document with 7 embedded Equation Editor objects |

A written project charter, [`maths/AGENTS.md`](maths/AGENTS.md), governs every session. Its rules include: originals are evidence and are never edited, a missing symbol is never guessed, teacher slips are reproduced as written and flagged, and every result is verified symbolically.

### 2. Tool investigation

Several OCR and math-recognition options were evaluated on the actual documents rather than assumed to work. RapidOCR was installed and tested, and it returned noise on the handwriting. Tesseract, PaddleOCR and pix2tex were investigated and rejected, because they are built for printed text or formulas. The agent's native image input was tested against a handwritten matrix and confirmed by an independent calculation before it was relied on. No paid service was used. The full reasoning is in [`maths/OCR_Review_Report.md`](maths/OCR_Review_Report.md).

### 3. Transcription

- All **20 handwritten pages** were rendered at 150 dpi and transcribed, with every section citing its original page.
- All **5 tutorial questions** were recovered. The embedded equations do not appear in plain-text extraction, so they were recovered from the document's vector previews rather than reconstructed from context.
- No expression was left unreadable.
- **Six teacher slips** (pages 3, 4, 12, 14, 16 and 18) were preserved exactly as written and flagged in place, never silently corrected. None changes a final answer.

See [`maths/Module_1_Transcription.md`](maths/Module_1_Transcription.md) and [`maths/Tutorial_1_Transcription.md`](maths/Tutorial_1_Transcription.md).

### 4. Symbolic verification

Every matrix, characteristic polynomial, eigenvalue, eigenvector, Cayley–Hamilton identity and diagonalisation in the transcribed material was recomputed with SymPy. All matched. The verification tables are in section 6 of the OCR report.

### 5. Authoring the guide

The study guide was written from the verified transcription under the charter's teaching rules: intuition first, every symbol defined, worked examples with all arithmetic shown, and a separate answer key kept apart from the questions. The published guide contains:

- the syllabus wording and the official examination pattern,
- concept-by-concept teaching that keeps the teacher's method and notation,
- Module 1 questions taken from two university papers, with their provenance stated,
- the four self-learning topics, labelled as enrichment from open textbooks,
- **29 practice questions worth 143 marks**, graded basic, exam-level and challenging,
- an answer key, a common-mistakes section, and a source list with exact sections and links.

Every numerical answer in the guide was checked with SymPy. The guide also states what that does not mean. SymPy proves a computation correct. It does not show that a question is typical or likely to appear, so the guide makes no frequency claims.

### 6. Publication

The guide was converted to a self-contained HTML page and added to this site. A browser pass checked that the formulas render and that the page works at phone width.

### Why this matters

The aim was a guide that can be trusted. Handwriting was read directly instead of through unreliable OCR. Uncertainty is recorded rather than hidden. For example, one matrix entry on notes page 11 is read as 4 with high confidence but not certainty, and that reading is documented. Machine verification stands behind the arithmetic, and the original notes remain the authority wherever a guide and a transcription disagree.

---

## How the DSGT guides were built

Modules 4 (Counting) and 5 (Algebraic Structures) are self-contained guides built from the course question bank, the teacher's slides and past end-semester questions. Teacher material and additions are labelled in the text, for example "Teacher's framing" and "Added for exam use: standard result". Worked examples were re-checked, and arithmetic errors found in the first drafts were corrected. Module 4 also includes diagrams (Venn, pigeonhole). These were subsequently audited against the syllabus.

---

## Repository structure

```text
.
├── index.html                  Subjects homepage
├── vercel.json                 Routing, redirects, clean URLs
├── README.md
├── dsgt/
│   ├── index.html              DSGT module list
│   └── modules/
│       ├── module-4.html       Counting
│       └── module-5.html       Algebraic Structures
├── maths/
│   ├── index.html              Mathematics module list
│   ├── modules/
│   │   └── module-1.html       Linear Algebra: Theory of Matrices
│   ├── AGENTS.md               Project charter for agent sessions
│   ├── README.md               Library overview
│   ├── Syllabus_Coverage.md    Official syllabus extraction
│   ├── Module_1_Transcription.md
│   ├── Tutorial_1_Transcription.md
│   ├── Source_Index.md         Source-to-transcription map with hashes
│   └── OCR_Review_Report.md    Tool tests, flagged readings, SymPy results
├── aoa/index.html              Analysis of Algorithm (coming soon)
└── coa/index.html              Computer Organization and Architecture (coming soon)
```

---

## Hosting and routing

The site is hosted on Vercel and deploys automatically from `main`. The primary address is `study-guides-placeholder.vercel.app`. The older `study-guides-two.vercel.app` redirects to it.

`vercel.json` enables clean URLs, so pages are served without `.html`, for example `/dsgt/modules/module-4`. It also redirects older addresses, including `/modules/module-4` and `/modules/module-5`, to their current locations.

**Links are absolute paths** such as `/maths/modules/module-1`. Relative links break under clean URLs, because `/maths` has no trailing slash and relative paths would resolve against the site root. Keep all internal links absolute.

---

## Adding content

**A new module**

1. Put `module-N.html` in the subject's `modules/` folder.
2. In that subject's `index.html`, change the module's `div.card.soon` into `a.card` with `href="/<subject>/modules/module-N"`.
3. Update the "n of 6 modules ready" line, and the subject's card on the root `index.html`.

**A new subject.** Copy an existing subject folder, replace the title, course code and module names with those from the official syllabus, and add a card to the root `index.html`.

**Conventions.** Reuse the CSS variables rather than hard-coded colours, keep tap targets at least 44 px, make wide tables scroll inside their own container, use absolute internal links, and keep light as the default theme.

---

## Sources, limitations and disclosure

- **AI-assisted content.** These guides were produced with AI agents and checked with symbolic computation and manual review. They are study aids, not official University of Mumbai material. Where a guide and the teacher's notes disagree, follow the teacher, and report the difference.
- **What verification covers.** SymPy confirms arithmetic and identities. It does not establish what will be examined. The Mathematics guide uses only two past papers and makes no claims about question frequency.
- **Known uncertainties** for Mathematics Module 1 are listed in section 9.6 of the guide. They include one handwriting reading, the course-code mismatch between the tutorial and the syllabus, and the teacher's slips.
- **Source documents** are the student's own course materials, namely the syllabus, handwritten notes and tutorial sheets, and they are not redistributed here. The repository is public and contains only derived transcriptions and guides. Open textbooks used for enrichment are cited with licences in the guide.
- **Not affiliated** with the University of Mumbai.
