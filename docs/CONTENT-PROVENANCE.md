# Content provenance and verification

This document records how selected guides were prepared, what source material they use, and what the verification does and does not establish.

## Mathematics Module 1 — Linear Algebra: Theory of Matrices

The guide at [`maths/modules/module-1.html`](../maths/modules/module-1.html) is the most heavily engineered part of the project. It was produced by AI agents working in structured, rule-bound sessions, with the student supplying the source material and teaching requirements. It followed a pipeline in which each stage left evidence that can be audited.

### Source library

Three originals were collected and left unmodified, each identified by SHA-256 hash in [`maths/Source_Index.md`](../maths/Source_Index.md):

| Source | Form |
|---|---|
| Official syllabus, 72 pages | Born-digital PDF (Mathematics pages 16–18 used) |
| Teacher's Module 1 notes, 20 pages | Scanned cursive handwriting with matrices |
| Tutorial 1 | Word document with 7 embedded Equation Editor objects |

The written project charter, [`maths/AGENTS.md`](../maths/AGENTS.md), governs every session. Its rules include: originals are evidence and are never edited, a missing symbol is never guessed, teacher slips are reproduced as written and flagged, and every result is verified symbolically.

### Tool investigation

Several OCR and math-recognition options were evaluated on the actual documents rather than assumed to work. RapidOCR was installed and tested, and it returned noise on the handwriting. Tesseract, PaddleOCR and pix2tex were investigated and rejected, because they are built for printed text or formulas. The agent's native image input was tested against a handwritten matrix and confirmed by an independent calculation before it was relied on. No paid service was used. The full reasoning is in [`maths/OCR_Review_Report.md`](../maths/OCR_Review_Report.md).

### Transcription

- All **20 handwritten pages** were rendered at 150 dpi and transcribed, with every section citing its original page.
- All **5 tutorial questions** were recovered. The embedded equations do not appear in plain-text extraction, so they were recovered from the document's vector previews rather than reconstructed from context.
- No expression was left unreadable.
- **Six teacher slips** (pages 3, 4, 12, 14, 16 and 18) were preserved exactly as written and flagged in place, never silently corrected. None changes a final answer.

See [`maths/Module_1_Transcription.md`](../maths/Module_1_Transcription.md) and [`maths/Tutorial_1_Transcription.md`](../maths/Tutorial_1_Transcription.md).

### Symbolic verification

Every matrix, characteristic polynomial, eigenvalue, eigenvector, Cayley–Hamilton identity and diagonalisation in the transcribed material was recomputed with SymPy. All matched. The verification tables are in section 6 of the OCR report.

### Authoring the guide

The study guide was written from the verified transcription under the charter's teaching rules: intuition first, every symbol defined, worked examples with all arithmetic shown, and a separate answer key kept apart from the questions. The published guide contains:

- the syllabus wording and the official examination pattern,
- concept-by-concept teaching that keeps the teacher's method and notation,
- Module 1 questions taken from two university papers, with their provenance stated,
- the four self-learning topics, labelled as enrichment from open textbooks,
- **29 practice questions worth 143 marks**, graded basic, exam-level and challenging,
- an answer key, a common-mistakes section, and a source list with exact sections and links.

Every numerical answer in the guide was checked with SymPy. SymPy proves a computation correct; it does not show that a question is typical or likely to appear. The guide therefore makes no frequency claims.

### Publication

The guide was converted to a self-contained HTML page and added to this site. A browser pass checked that the formulas render and that the page works at phone width.

The aim was a guide that can be trusted. Handwriting was read directly instead of through unreliable OCR. Uncertainty is recorded rather than hidden. For example, one matrix entry on notes page 11 is read as 4 with high confidence but not certainty, and that reading is documented. Machine verification stands behind the arithmetic, and the original notes remain the authority wherever a guide and a transcription disagree.

## DSGT guides

Modules 4 (Counting) and 5 (Algebraic Structures) are self-contained guides built from the course question bank, the teacher's slides and past end-semester questions. Teacher material and additions are labelled in the text, for example "Teacher's framing" and "Added for exam use: standard result". Worked examples were re-checked, and arithmetic errors found in the first drafts were corrected. Module 4 also includes diagrams (Venn, pigeonhole). These were subsequently audited against the syllabus.

## Sources, limitations and disclosure

- **AI-assisted content.** These guides were produced with AI agents and checked with symbolic computation and manual review. They are study aids, not official University of Mumbai material. Where a guide and the teacher's notes disagree, follow the teacher, and report the difference.
- **What verification covers.** SymPy confirms arithmetic and identities. It does not establish what will be examined. The Mathematics guide uses only two past papers and makes no claims about question frequency.
- **Known uncertainties** for Mathematics Module 1 are listed in section 9.6 of the guide. They include one handwriting reading, the course-code mismatch between the tutorial and the syllabus, and the teacher's slips.
- **Source documents and redistribution.** The Mathematics workspace states in `maths/README.md` that its original source PDFs and DOCX are not included. The current BEEE tree, however, also tracks course source material: syllabus and examination PDFs under `beee/00_University_Syllabus/`, and assignments, practice material and slide decks under `beee/01_Original_Notes/`. Therefore the public repository is not limited to derived transcriptions and guides. These files were left untouched by the organization cleanup; confirm redistribution rights or deliberately change their availability before describing the entire repository as derived-only. Open textbooks used for enrichment are cited with licences in the relevant guide.
- **Not affiliated** with the University of Mumbai.

For BEEE, DSGT and AOA, see the subject-specific `README.md` and `AGENTS.md` files for their course context, module coverage, source handling and working conventions.
