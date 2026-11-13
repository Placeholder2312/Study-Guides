# AGENTS.md - Analysis of Algorithm (Semester III)

Project instructions for OpenCode sessions working on the AOA study guides.

---

## 1. Academic context

- **University:** University of Mumbai
- **Programme:** B.E. - Computer Science and Engineering (Artificial Intelligence and Machine Learning)
- **Semester:** III
- **Scheme:** NEP 2020
- **Subject:** Analysis of Algorithm
- **Official course code:** 2023113
- **Published page:** `aoa/index.html`
- **Guide status:** 0 of 6 modules ready

## 2. Modules

| Module | Topic |
|---|---|
| I | Introduction |
| II | Divide and Conquer Approach |
| III | Greedy Method Approach |
| IV | Dynamic Programming Approach |
| V | Backtracking and Branch and Bound |
| VI | String Matching Algorithms |

## 3. Directory layout

```text
aoa/
├── AGENTS.md                  # this file
├── README.md                  # repository overview
├── index.html                 # published subject landing page
├── 00_University_Syllabus/    # official syllabus, university papers, coverage map
├── 01_Original_Notes/         # source material per module (kept local, not committed)
│   └── Module_1/ ... Module_6/
├── 02_Tutorials/              # tutorial sheets (none supplied yet)
├── 03_Transcriptions/         # Markdown transcriptions and Source_Index.md
├── 04_OCR_Reports/            # OCR review and verification reports
├── 05_Study_Guides/           # generated module guides
├── 06_Revision/               # IAT question banks, revision sheets, answer keys
├── 07_Unidentified/           # material that cannot be confidently classified
└── _work/                     # scratch: rendered pages, papers, shots, sources, wmf
```

## 4. Source rules

1. Original lecture slides, question papers and textbooks stay in the local source
   library (`Downloads/AOA`). Do not commit copyrighted PDFs, slides or books to Git.
2. Treat `00_University_Syllabus/Syllabus_Coverage.md` as authoritative once it exists.
   Do not substitute a generic algorithms syllabus.
3. Keep the official module numbering and titles.
4. Do not invent numerical answers for illegible or ambiguous questions. Record the
   assumption instead.
5. Use the existing Study Guides visual language (Georgia headings, Helvetica body,
   black/white/grey, blue accent `#1d4ed8`, square corners, light theme with optional
   dark mode). Do not introduce a separate design system.

## 5. Working notes

- Published guides live in `aoa/modules/` and are plain static HTML.
- `05_Study_Guides/` is the working library for Markdown/HTML sources; only finished
  guides are linked from `index.html`.
- `_work/` is scratch material and is never linked from the site.
