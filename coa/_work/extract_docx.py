import sys, zipfile, re
from xml.etree import ElementTree as ET

W = '{http://schemas.openxmlformats.org/wordprocessingml/2006/main}'
M = '{http://schemas.openxmlformats.org/officeDocument/2006/math}'

def text_of(el):
    out = []
    for node in el.iter():
        if node.tag == W+'t' or node.tag == M+'t':
            out.append(node.text or '')
        elif node.tag == W+'tab':
            out.append('\t')
        elif node.tag == W+'br':
            out.append('\n')
    return ''.join(out)

def walk(body):
    lines = []
    for child in body:
        if child.tag == W+'p':
            t = text_of(child).strip()
            if t:
                lines.append(t)
        elif child.tag == W+'tbl':
            lines.append('')
            lines.append('[TABLE]')
            for tr in child.findall(W+'tr'):
                cells = []
                for tc in tr.findall(W+'tc'):
                    cells.append(' '.join(text_of(p).strip() for p in tc.findall(W+'p')).strip())
                lines.append(' | '.join(cells))
            lines.append('[/TABLE]')
            lines.append('')
    return '\n'.join(lines)

for path in sys.argv[1:]:
    with zipfile.ZipFile(path) as z:
        xml = z.read('word/document.xml')
        root = ET.fromstring(xml)
        body = root.find(W+'body')
        print('\n\n========== ' + path + ' ==========\n')
        print(walk(body))
