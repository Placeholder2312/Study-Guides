# Repository structure

This is a static multi-semester study site. Subject folders are the content workspaces; the root contains the shared site shell and deployment configuration.

```text
Study-Guides/
├── index.html                  # Semester/subject homepage
├── 404.html                    # Not-found page
├── robots.txt                  # Crawler policy and sitemap location
├── sitemap.xml                 # Published routes
├── vercel.json                 # Clean URLs and legacy redirects
├── README.md                   # Project entry point
├── .gitignore                  # Local editor/cache/build exclusions
├── assets/                     # Shared CSS, accessibility styles and theme script
├── scripts/                    # Site maintenance scripts
├── docs/                       # Repository and content-maintenance documentation
├── beee/                       # Semester I: Basic Electrical and Electronics Engineering
│   ├── 00_University_Syllabus/
│   ├── 01_Original_Notes/
│   ├── 02_Tutorials/
│   ├── 03_Transcriptions/
│   ├── 04_OCR_Reports/
│   ├── 05_Study_Guides/
│   ├── 06_Revision/
│   ├── 07_Unidentified/
│   ├── _work/
│   ├── modules/                # Published HTML guides
│   ├── index.html
│   ├── README.md
│   └── AGENTS.md
├── applied-physics/             # Semester I subject landing page
├── engineering-mechanics/       # Semester I subject landing page
├── applied-mathematics-ii/      # Semester II subject landing page
├── semiconductor-physics/       # Semester II subject landing page
├── dsgt/                        # Semester III: Discrete Structures and Graph Theory
│   ├── 00_University_Syllabus/ ... 07_Unidentified/
│   ├── _work/
│   ├── modules/
│   ├── index.html
│   ├── README.md
│   └── AGENTS.md
├── maths/                       # Semester III: Mathematics for Computer Engineering
│   ├── endsem-questionbank/     # Separate question-bank page and verification scripts
│   ├── modules/                 # Published HTML guides
│   ├── AGENTS.md, README.md
│   ├── Source_Index.md, Syllabus_Coverage.md
│   ├── transcriptions and OCR review reports
│   └── working source/guide material
├── aoa/                         # Semester III: Analysis of Algorithm
│   ├── 00_University_Syllabus/ ... 07_Unidentified/
│   ├── _work/
│   ├── modules/
│   ├── index.html
│   ├── README.md
│   └── AGENTS.md
├── oe/                          # Semester III: Open Elective - Global and Regional Environmental Issues
│   └── index.html               # 24-question exam bank study guide
└── coa/                         # Semester III: Computer Organization and Architecture landing page
```

The numbered subject folders have consistent roles:

| Folder | Purpose |
|---|---|
| `00_University_Syllabus/` | Official syllabus, coverage map and relevant examination papers |
| `01_Original_Notes/` | Subject/module source library |
| `02_Tutorials/` | Tutorial sheets |
| `03_Transcriptions/` | Page-referenced transcriptions and source indexes |
| `04_OCR_Reports/` | OCR review, uncertain readings and verification reports |
| `05_Study_Guides/` | Working Markdown/HTML guide sources |
| `06_Revision/` | Revision sheets and question banks |
| `07_Unidentified/` | Material not confidently classified yet |
| `_work/` | Scratch and intermediate material; not site navigation |
| `modules/` | Finished HTML guides linked from the subject page |

## Important compatibility notes

- Keep the current subject names and numbered directory convention. It makes the source-to-guide pipeline consistent across courses.
- BEEE currently has some subject-root copies of files that also exist in the numbered canonical folders. They have identical Git blob contents and may be compatibility paths. Do not delete or rename them without checking references first.
- BEEE's `_work/` contains a build script and intermediate assets; it is not safe to ignore or delete the whole folder.
- `maths/endsem-questionbank/` is a distinct published page and tool area, not disposable scratch output.
- The root site is plain static HTML/CSS/JavaScript. Do not add an application bundler solely for organizational reasons.
