# BEEE Study Guides — Modules 1 and 3

## Overview
Source-based study guides for BEEE (ESC102), B.E. CSE (AI & ML), Semester I, NEP 2020:

- **Module 1 — DC Circuits.** Kirchhoff's laws, mesh and nodal analysis, star-delta, superposition, Thevenin, Norton and maximum power transfer.
- **Module 3 — Single Phase Transformer.** Working principle, types, transformation ratio, ideal and practical transformer, losses, efficiency and applications. The syllabus states that numericals are not expected, so the guide is conceptual and symbolic.

## Repository
- `C:\Users\Harsh\Study-Guides\` — Study Guides root
- Branch: `main`
- Commit: `eb8ea09` — BEEE Module 1 DC Circuits study guide

## Folder Structure
```
beee/
├── 00_University_Syllabus/      # Official syllabus PDF, exam papers, coverage map
├── 01_Original_Notes/           # Source materials per module (assignments, slides, practice Qs)
│   ├── Module_1/                # Assignment 1, Assignment 2, Practice Questions
│   ├── Module_2/                # Assignment 6, Unit 2 practice, slides
│   ├── Module_3/                # Unit 3 slides
│   ├── Module_4/                # Unit 4 slides
│   ├── Module_5/                # Unit 5 slides, Assignment 3, resonance notes
│   └── Module_6/                # Unit 6 slides
├── 02_Tutorials/                # Tutorial sheets (empty - none supplied)
├── 03_Transcriptions/           # Markdown transcriptions of source materials
│   ├── Module_1_Transcription.md
│   └── Source_Index.md
├── 04_OCR_Reports/              # OCR quality assessments of scanned papers
│   └── OCR_Review_Report.md
├── 05_Study_Guides/             # Generated study guides (per module)
│   └── Module_1/                # (reserved for future markdown guide)
├── 06_Revision/                 # Revision materials, solved numericals
├── 07_Unidentified/             # Unclassified images/files
├── _work/                       # Build scripts, intermediate assets
│   ├── papers/                  # Exam paper PDFs
│   ├── shots/                   # Screenshots, figure exports
│   └── build_html.py            # Build script
├── modules/                     # Published HTML guides (Vercel deployment)
│   ├── module-1.html            # Module 1 DC Circuits
│   └── module-3.html            # Module 3 Single Phase Transformer
├── AGENTS.md                    # Agent skill configuration
├── index.html                   # Landing page for the six modules
├── OCR_Review_Report.md         # (symlink to 04_OCR_Reports/)
├── README.md                    # This file
├── Module_1_Transcription.md    # (symlink to 03_Transcriptions/)
├── Source_Index.md              # Sources used by the published guides
└── Syllabus_Coverage.md         # (symlink to 00_University_Syllabus/)
```

## Visual Style
DSGT Module 4 reference: Georgia headings, Helvetica body, black/white/grey, blue accent `#1d4ed8`, square corners, thin borders, light default, `sg-theme` localStorage dark mode, print CSS. Module 3 reuses the Module 1 stylesheet and section-progress script unchanged.

## Module 3 — Single Phase Transformer

- **Syllabus:** University of Mumbai, NEP 2020, ESC102, Module III, 4 teaching hours, CO3.
- **Prescribed scope:** working principle, types, transformation ratio, actual (practical) and ideal transformer, transformer losses, efficiency, applications. *"Numerical are not expected."*
- **Page sections:** module overview → fundamentals → construction → working principle and EMF equation → types → transformation ratio → ideal vs practical → losses → efficiency → applications → revision sheet → practice → answer key → references.
- **Visuals:** three inline SVGs — labelled construction, energy-transfer/working principle, and step-up versus step-down comparison.
- **Practice:** conceptual only, labelled as supplementary and kept separate from the answer key. The only verified university questions for this module are June 2025 NEP paper N10415 Q1(d) and Q5(a).
- **Source limitation:** the Unit 3 slide deck is the only course-specific material; no Module 3 assignment, tutorial sheet or practice bank was supplied.

## Syllabus
University of Mumbai, NEP 2020, ESC102 Basic Electrical and Electronics Engineering:
- Module I "DC Circuits", 10 hours, CO1.
- Module III "Single Phase Transformer", 4 hours, CO3.

## Quick Links
- [All BEEE modules](/beee) — landing page with Modules 1–6
- [Study Guides home](/) — subject list
- [Module 1 — DC Circuits](/beee/modules/module-1)
- [Module 3 — Single Phase Transformer](/beee/modules/module-3)
