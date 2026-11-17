# Maintaining the Study Guides site

## Hosting and routing

The site is hosted on Vercel and deploys from `main`. The primary address is <https://study-guides-placeholder.vercel.app>. The older `study-guides-two.vercel.app` host redirects to it.

[`vercel.json`](../vercel.json) enables clean URLs, so pages are served without `.html`, for example `/dsgt/modules/module-4`. It also preserves redirects from older module paths.

**Internal site links must be absolute paths**, such as `/maths/modules/module-1`. Relative links break under clean URLs because `/maths` has no trailing slash and relative paths can resolve against the site root.

## Adding a module

1. Put `module-N.html` in the subject's `modules/` folder.
2. In that subject's `index.html`, change the relevant coming-soon card into an anchor with `href="/<subject>/modules/module-N"`.
3. Update the subject's module-ready count and the subject card on the root `index.html`.
4. Update that subject's `README.md` and any applicable syllabus/coverage or source index documents.
5. Check the page at phone width, test its internal links, check dark mode and print styles, and verify that the root and subject module counts agree.

## Adding a subject

1. Start from an existing subject folder whose structure matches the course.
2. Preserve the official syllabus numbering and module titles; do not replace them with a generic syllabus.
3. Keep the numbered source-library folders, transcriptions, OCR reports, study-guide working files, revision material and `_work/` separate.
4. Add the subject landing page at `/<subject>/index.html` and a card to the root `index.html`.
5. Add the subject's `README.md` and `AGENTS.md` with verified course-specific context.
6. Update the root README and sitemap when a published route is added.

## Design and accessibility conventions

- Reuse the CSS variables in `assets/site.css`; do not introduce unrelated hard-coded colours.
- Keep tap targets at least 44 px.
- Make wide tables scroll inside their own container rather than expanding the page.
- Keep light mode as the default and preserve the optional `sg-theme` preference.
- Use inline SVG for diagrams where it fits the existing page style.
- Keep print styles useful with navigation hidden.
- Preserve absolute internal paths and clean-URL conventions.

## Content and source handling

See [Content provenance](CONTENT-PROVENANCE.md) for the Mathematics and DSGT guide workflows. See [Repository structure](REPOSITORY-STRUCTURE.md) before moving source, transcription, guide or scratch files.

Original course documents are not automatically publishable. Respect the existing source-handling rules and each subject's `AGENTS.md`. Do not replace source originals or silently "correct" a faithful transcription.
