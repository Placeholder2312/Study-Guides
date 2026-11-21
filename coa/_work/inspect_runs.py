import zipfile, re
from xml.etree import ElementTree as ET
W='{http://schemas.openxmlformats.org/wordprocessingml/2006/main}'
M='{http://schemas.openxmlformats.org/officeDocument/2006/math}'
p='source/COA/Unit 4 problems.docx'
with zipfile.ZipFile(p) as z:
    xml=z.read('word/document.xml').decode('utf-8')
root=ET.fromstring(xml)
body=root.find(W+'body')
paras=[]
for para in body.iter(W+'p'):
    s=''
    for r in para.iter(W+'r'):
        t=''.join(x.text or '' for x in r.iter(W+'t'))
        rpr=r.find(W+'rPr')
        va=''
        if rpr is not None:
            v=rpr.find(W+'vertAlign')
            if v is not None: va='['+v.get(W+'val')+']'
        if t: s+=va+t
    for mt in para.iter(M+'t'):
        pass
    if s.strip(): paras.append(s)
for i,s in enumerate(paras):
    if 'AMAT' in s or 'EAT' in s or '0.9' in s or '0.05' in s or '2A35' in s or '3A5' in s:
        print(i, repr(s))
