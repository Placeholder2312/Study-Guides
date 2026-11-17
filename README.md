# Study Guides

A mobile-first study library for B.E. Computer Science and Engineering (Artificial Intelligence and Machine Learning) at the University of Mumbai. The site currently includes subject pages from Semesters I, II and III.

**Live site:** <https://study-guides-placeholder.vercel.app>

Choose a subject from the [homepage](https://study-guides-placeholder.vercel.app/). Each subject page lists its modules; published guides are linked from the relevant module list.

## Subjects

- **Semester I:** [Applied Physics](/applied-physics), [Engineering Mechanics](/engineering-mechanics), [Basic Electrical and Electronics Engineering](/beee)
- **Semester II:** [Applied Mathematics-II](/applied-mathematics-ii), [Semiconductor Physics](/semiconductor-physics)
- **Semester III:** [Discrete Structures and Graph Theory](/dsgt), [Mathematics for Computer Engineering](/maths), [Analysis of Algorithm](/aoa), [Computer Organization and Architecture](/coa)

The Semester III readiness snapshot is:

| Subject | Course | Published modules |
|---|---:|---|
| Discrete Structures and Graph Theory (DSGT) | 2023112 | 4 and 5 |
| Mathematics for Computer Engineering | 2023111 | 1 and 4 |
| Analysis of Algorithm | 2023113 | None yet |
| Computer Organization and Architecture | 2023114 | None yet |

Check the live subject pages for the current module list. This project does not cover every Semester I–III course or laboratory.

## Reading experience

- Mobile-first static HTML pages, with light mode by default and an optional dark theme.
- Consistent typography, colours and square-corner visual language across subjects.
- Inline SVG diagrams, section progress navigation and print styles where a guide uses them.
- No site build step. The Mathematics guides use MathJax and a Markdown renderer from a CDN for formula rendering, so those pages need an internet connection for the formulas.

## Repository map

- `assets/`: shared CSS, accessibility styles and theme script.
- `scripts/`: site-maintenance scripts.
- Subject folders: `beee/`, `dsgt/`, `maths/`, `aoa/`, and the additional Semester I–II subject pages.
- `docs/`: repository structure, site-maintenance instructions, and content provenance.

See [Repository structure](docs/REPOSITORY-STRUCTURE.md) before moving files, [Maintaining the site](docs/MAINTAINING-THE-SITE.md) when adding subjects or modules, and [Content provenance](docs/CONTENT-PROVENANCE.md) for the source and verification practices used by the guides.

## Content integrity

Original course materials remain the authority. Transcriptions preserve the teacher's wording and notation; uncertain readings are flagged instead of guessed. Study guides are learning aids, not official University of Mumbai material. Where a guide and teacher material disagree, follow the teacher and report the difference.

The guides are AI-assisted and checked through manual review and, where appropriate, symbolic computation. Those checks validate the calculations they cover; they do not predict examination questions. This project is not affiliated with the University of Mumbai.
