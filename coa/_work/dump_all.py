import zipfile
from xml.etree import ElementTree as ET
W='{http://schemas.openxmlformats.org/wordprocessingml/2006/main}'
M='{http://schemas.openxmlformats.org/officeDocument/2006/math}'
p='source/COA/Unit 4 problems.docx'
with zipfile.ZipFile(p) as z:
    xml=z.read('word/document.xml').decode('utf-8')
root=ET.fromstring(xml)
body=root.find(W+'body')
def text(el):
    out=[]
    for n in el.iter():
        if n.tag in (W+'t',M+'t'): out.append(n.text or '')
        elif n.tag==W+'tab': out.append('\\t')
        elif n.tag==W+'br': out.append('\\n')
        elif n.tag==M+'f':
            # fraction: num then den
            pass
    return ''.join(out)
i=0
for para in body.iter(W+'p'):
    s=text(para).strip()
    if s:
        print(i, s)
        i+=1
