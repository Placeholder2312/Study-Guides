import re, pathlib, sys

ROOT = pathlib.Path(r"C:\Users\Harsh\Study-Guides")
dsgt = (ROOT / "dsgt/modules/module-4.html").read_text(encoding="utf-8")

head_end = dsgt.index("<body>")
head = dsgt[:head_end]
# scripts after the main wrap closes
body_start = dsgt.index("<body>") + len("<body>")
scripts_start = dsgt.index("<script>\n(function(){\n  var b=document.getElementById('themeToggle')")
scripts = dsgt[scripts_start:]

def build(body_path, out_path, title, description):
    body = pathlib.Path(body_path).read_text(encoding="utf-8")
    h = head.replace("<title>DSGT Module 4 — Study Guide</title>", f"<title>{title}</title>")
    override = (
        '<meta name="description" content="' + description + '">\n'
        "<style>\n"
        "  /* COA overrides: long worked-example equations may wrap, and wide diagrams use the full column. */\n"
        "  .eq { white-space: normal; }\n"
        "  svg, figure svg { max-width: 100%; }\n"
        "</style>\n"
        "</head>"
    )
    h = h.replace("</head>", override)
    html = h + "<body>\n" + body + "\n" + scripts
    pathlib.Path(out_path).write_text(html, encoding="utf-8")
    print(out_path, len(html))

if __name__ == "__main__":
    build(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4])
