import sys
from html.parser import HTMLParser
from pathlib import Path

VOID = {"area","base","br","col","embed","hr","img","input","link","meta","param","source","track","wbr","path","rect","line","text","circle","marker","defs","g","svg","title","desc","polygon","polyline","ellipse"}

TRACK = {"div","p","span","strong","em","ol","ul","li","table","tr","td","th","section","header","footer","nav","figure","figcaption","h1","h2","h3","h4","a","button","code","sub","sup"}

class Check(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.stack = []
        self.errors = []
        self.ids = set()
        self.hrefs = []
        self.classes = set()

    def handle_starttag(self, tag, attrs):
        d = dict(attrs)
        if "id" in d:
            self.ids.add(d["id"])
        if tag == "a" and d.get("href", "").startswith("#"):
            self.hrefs.append(d["href"][1:])
        if "class" in d:
            self.classes.update(d["class"].split())
        if tag in TRACK and tag not in VOID:
            self.stack.append((tag, self.getpos()))

    def handle_startendtag(self, tag, attrs):
        d = dict(attrs)
        if "id" in d:
            self.ids.add(d["id"])
        if "class" in d:
            self.classes.update(d["class"].split())

    def handle_endtag(self, tag):
        if tag not in TRACK:
            return
        if not self.stack:
            self.errors.append(f"stray </{tag}> at {self.getpos()}")
            return
        open_tag, pos = self.stack.pop()
        if open_tag != tag:
            self.errors.append(f"</{tag}> at {self.getpos()} closes <{open_tag}> opened at {pos}")

p = Path(sys.argv[1])
html = p.read_text(encoding="utf-8")
c = Check()
c.feed(html)
for t, pos in c.stack:
    c.errors.append(f"unclosed <{t}> at {pos}")
missing = sorted({h for h in c.hrefs if h and h not in c.ids})
print("file:", p, "size:", len(html))
print("errors:", len(c.errors))
for e in c.errors[:20]:
    print("  ", e)
print("broken anchors:", missing if missing else "none")
print("ids:", len(c.ids))
