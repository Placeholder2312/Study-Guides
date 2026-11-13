#!/usr/bin/env python3
"""One-time accessibility pass for the module pages. Safe to re-run.

Run from the repo root:  python3 scripts/patch-modules.py
Then review `git diff`, commit, and delete this script.

Older-template modules (dsgt module-4/5, beee module-1) get: a skip link, a <main>
landmark, labelled <nav>s, th scope="col", a reduced-motion guard for smooth
scrolling, and a theme button that stays hidden until JS runs. The maths module
already has the landmarks; it only gets th scope="col" after render.
"""
import re, sys, pathlib

OLD = ["dsgt/modules/module-4.html", "dsgt/modules/module-5.html", "beee/modules/module-1.html"]
MATHS = "maths/modules/module-1.html"

def once(s, old, new, label, report):
    n = s.count(old)
    if n != 1:
        report.append(f"  ! {label}: expected 1 match, found {n} (skipped)")
        return s
    report.append(f"  ok {label}")
    return s.replace(old, new, 1)

def th_scopes(s):
    def row(m):
        r = m.group(0)
        th = len(re.findall(r"<th[\s>]", r)); td = len(re.findall(r"<td[\s>]", r))
        if th and not td:
            return re.sub(r"<th(?=[\s>])(?![^>]*\bscope=)", '<th scope="col"', r)
        return r  # body rows / mixed rows left alone
    return re.sub(r"<tr[^>]*>.*?</tr>", row, s, flags=re.S)

def patch_old(s):
    rep = []
    if "skip-link" in s:
        return s, ["  (already patched)"]
    s = once(s, "html { scroll-behavior: smooth; }",
             "@media (prefers-reduced-motion: no-preference) { html { scroll-behavior: smooth; } }",
             "reduced-motion guard", rep)
    s = once(s, "</head>", '<link rel="stylesheet" href="/assets/a11y.css">\n</head>', "link a11y.css", rep)
    m = re.search(r"<body[^>]*>", s)
    if m:
        s = s[:m.end()] + '\n<a class="skip-link" href="#main">Skip to content</a>' + s[m.end():]; rep.append("  ok skip link")
    s = once(s, "</header>", '</header>\n\n  <main id="main" tabindex="-1">', "open <main>", rep)
    s = once(s, "<footer>", "</main>\n\n  <footer>", "close <main>", rep)
    s, n = re.subn(r'<div class="toc">(\s*<ol>.*?</ol>\s*)</div>',
                   r'<nav class="toc" aria-label="Table of contents">\1</nav>', s, count=1, flags=re.S)
    rep.append("  ok toc -> labelled <nav>" if n == 1 else "  ! toc not converted")
    s = once(s, '<nav class="nav">', '<nav class="nav" aria-label="Jump to section">', "label section nav", rep)
    before = s.count('scope="col"'); s = th_scopes(s)
    added = s.count('scope="col"') - before
    rep.append("  ok th scope=col on %d header cells" % added)
    s = once(s, 'id="themeToggle"></button>', 'id="themeToggle" hidden></button>', "hide toggle until JS runs", rep)
    s = once(s, "function paint(){var d=dark();", "function paint(){b.hidden=false;var d=dark();", "unhide toggle in paint()", rep)
    return s, rep

def patch_maths(s):
    if "setAttribute('scope', 'col')" in s:
        return s, ["  (already patched)"]
    anchor = "if (t.tHead && !t.tHead.textContent.trim()) t.tHead.style.display = 'none';"
    add = anchor + "\n      Array.prototype.forEach.call(t.querySelectorAll('thead th'), function (th) { th.setAttribute('scope', 'col'); });"
    rep = []
    s = once(s, anchor, add, "th scope=col after render", rep)
    return s, rep

for f in OLD + [MATHS]:
    p = pathlib.Path(f); s = p.read_text(encoding="utf-8")
    new, rep = (patch_maths if f == MATHS else patch_old)(s)
    print(f); print("\n".join(rep))
    if new != s: p.write_text(new, encoding="utf-8")
