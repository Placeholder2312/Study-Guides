import pathlib, re, sys
from lxml import html as LH


def text_of(el):
    out = []

    def walk(node):
        if node.text:
            out.append(node.text)
        for ch in node:
            tag = ch.tag.lower() if isinstance(ch.tag, str) else ""
            inner = []
            def collect(n):
                if n.text:
                    inner.append(n.text)
                for c in n:
                    collect(c)
                    if c.tail:
                        inner.append(c.tail)
            collect(ch)
            s = "".join(inner)
            if tag in ("strong", "b"):
                out.append("**" + s.strip() + "**")
            elif tag in ("em", "i"):
                out.append("*" + s.strip() + "*")
            elif tag == "code":
                out.append("`" + s.strip() + "`")
            elif tag == "sup":
                out.append("^(" + s.strip() + ")")
            elif tag == "sub":
                out.append("_(" + s.strip() + ")")
            elif tag == "br":
                out.append("  \n")
            elif tag == "a":
                href = ch.get("href", "")
                out.append(s if href.startswith("#") else "[" + s.strip() + "](" + href + ")")
            elif tag == "span":
                out.append("`" + s.strip() + "`" if "kbd" in ch.get("class", "") else s)
            elif tag in ("svg", "script", "style"):
                pass
            else:
                out.append(s)
            if ch.tail:
                out.append(ch.tail)
    walk(el)
    t = "".join(out)
    t = re.sub(r"[ \t]+", " ", t)
    t = re.sub(r" *\n *", "\n", t)
    return t.strip()


def table_md(tbl):
    rows, header = [], None
    for tr in tbl.xpath("./tr|./thead/tr|./tbody/tr"):
        vals = [text_of(c).replace("|", "\\|").replace("\n", " ") for c in tr.xpath("./th|./td")]
        if header is None and tr.xpath("./th"):
            header = vals
        else:
            rows.append(vals)
    if header is None:
        header = rows.pop(0) if rows else []
    width = len(header)
    lines = ["| " + " | ".join(header) + " |", "|" + "|".join([" --- "] * width) + "|"]
    for r in rows:
        r = r + [""] * (width - len(r))
        lines.append("| " + " | ".join(r[:width]) + " |")
    return "\n".join(lines)


def list_md(el):
    ordered = el.tag.lower() == "ol"
    n = int(el.get("start", "1")) if ordered else 1
    lines = []
    for li in el.xpath("./li"):
        main = text_of(li).strip()
        parts = [p.strip() for p in main.split("\n")]
        marker = f"{n}. " if ordered else "- "
        lines.append(marker + parts[0])
        for extra in parts[1:]:
            if extra:
                lines.append("   " + extra)
        n += 1
    return "\n".join(lines)


def blocks(el):
    out = []
    for ch in el:
        if not isinstance(ch.tag, str):
            continue
        tag = ch.tag.lower()
        cls = ch.get("class", "")
        if tag in ("svg", "script", "style"):
            continue
        if tag in ("h2", "h3", "h4"):
            level = {"h2": "##", "h3": "###", "h4": "####"}[tag]
            out.append(f"{level} {text_of(ch)}")
        elif tag == "p":
            out.append(text_of(ch))
        elif tag == "div" and "eq" in cls.split():
            out.append("> **" + text_of(ch) + "**")
        elif tag == "div" and "example" in cls.split():
            title = ch.xpath('.//div[contains(@class,"example-title")]')
            if title:
                out.append("**" + text_of(title[0]) + "**")
                title[0].getparent().remove(title[0])
            out.extend(blocks(ch))
        elif tag == "div" and "theory" in cls.split():
            srcs = ch.xpath('.//span[contains(@class,"source")]')
            if srcs:
                out.append("*" + text_of(srcs[0]) + "*")
                srcs[0].getparent().remove(srcs[0])
            for p in ch.xpath("./p"):
                out.append(text_of(p))
        elif tag == "div" and "qa-question" in cls.split():
            for lab in ch.xpath('.//div[contains(@class,"qa-label")]'):
                lab.getparent().remove(lab)
            out.append("**Question.** " + text_of(ch))
        elif tag == "div" and "qa-solution" in cls.split():
            for lab in ch.xpath('.//div[contains(@class,"qa-label")]'):
                lab.getparent().remove(lab)
            out.append("**Solution.**")
            out.extend(blocks(ch))
        elif tag == "div" and "qa-final" in cls.split():
            for lab in ch.xpath('.//div[contains(@class,"qa-label")]'):
                lab.getparent().remove(lab)
            out.append("**Final Answer:** " + text_of(ch))
        elif tag == "div" and "exam-q" in cls.split():
            title = ch.xpath('.//div[contains(@class,"exam-q-title")]')
            srcs = ch.xpath('.//div[contains(@class,"exam-source")]')
            if title:
                out.append("**" + text_of(title[0]) + "**")
            if srcs:
                out.append("*" + text_of(srcs[0]) + "*")
            for p in ch.xpath("./p"):
                out.append("> " + text_of(p))
        elif tag == "pre":
            code = ch.text_content().rstrip("\n")
            out.append("```asm\n" + code + "\n```")
        elif tag == "table":
            out.append(table_md(ch))
        elif tag in ("ol", "ul"):
            out.append(list_md(ch))
        elif tag == "figure":
            cap = ch.xpath(".//figcaption")
            if cap:
                out.append("> *" + text_of(cap[0]) + "*")
        elif tag in ("div", "main", "section", "article", "blockquote"):
            out.extend(blocks(ch))
    return out


src = pathlib.Path(sys.argv[1]).read_text(encoding="utf-8")
out_path = pathlib.Path(sys.argv[2])
wrap = LH.fromstring(src).xpath('//div[contains(@class,"wrap")]')[0]

head = []
h1 = wrap.xpath('.//header//h1')
sub = wrap.xpath('.//header//p[contains(@class,"subtitle")]')
meta = wrap.xpath('.//header//div[contains(@class,"meta")]')
if h1:
    head.append("# " + text_of(h1[0]))
if sub:
    head.append("*" + text_of(sub[0]) + "*")
if meta:
    head.append(text_of(meta[0]))

body = []
for el in wrap:
    if not isinstance(el.tag, str):
        continue
    tag = el.tag.lower()
    cls = el.get("class", "")
    if tag == "header" or "topbar" in cls.split() or "toc" in cls.split() or cls == "nav":
        continue
    if tag in ("h2", "h3", "h4", "p", "table", "figure", "ol", "ul", "pre", "div"):
        holder = LH.Element("div")
        holder.append(el)
        body.extend(blocks(holder))
    else:
        body.extend(blocks(el))

md = "\n\n".join(head + body)
md = re.sub(r"\n{3,}", "\n\n", md).strip() + "\n"
out_path.parent.mkdir(parents=True, exist_ok=True)
out_path.write_text(md, encoding="utf-8")
print(out_path, len(md), "chars", md.count("\n"), "lines")
