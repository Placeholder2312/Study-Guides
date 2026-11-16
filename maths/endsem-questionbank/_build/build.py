"""Build maths/endsem-questionbank/index.html from the Markdown masters.

    python maths/endsem-questionbank/_build/build.py

The Markdown files are the masters. The page embeds them in a
<script type="text/markdown"> block, exactly like the existing Module 1 page, so
the HTML can never become a shortened summary of the guide.

The answer key is appended after the teaching and question sections and is
never interleaved with them.
"""

import io
import os

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)

MASTER = os.path.join(ROOT, "Module_1_Endsem_Questionbank.md")
KEY = os.path.join(ROOT, "Module_1_Endsem_Answer_Key.md")
TEMPLATE = os.path.join(HERE, "template.html")
OUT = os.path.join(ROOT, "index.html")

SEP = "\n\n---\n\n"


def read(path):
    with io.open(path, encoding="utf-8") as fh:
        return fh.read().replace("\r\n", "\n")


master = read(MASTER).rstrip()
key = read(KEY).strip()

# Parts that were published as separate files are joined here; the Markdown
# masters stay separate so the answer key can be handed out on its own.
parts = [master, key]
md = SEP.join(parts)

for bad in ("</script", "<!--", "__MARKDOWN__"):
    assert bad not in md, "markdown contains %r, which would break the page" % bad

template = read(TEMPLATE)
assert template.count("__MARKDOWN__") == 1, "template must contain exactly one placeholder"

html = template.replace("__MARKDOWN__", md)

with io.open(OUT, "w", encoding="utf-8", newline="\n") as fh:
    fh.write(html)

print("wrote      :", OUT)
print("markdown   :", len(md.encode("utf-8")), "bytes")
print("html       :", len(html.encode("utf-8")), "bytes")
print("h1 count   :", md.count("\n# ") + md.startswith("# "))
print("display math blocks:", md.count("\\["))
