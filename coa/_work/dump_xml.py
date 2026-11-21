import zipfile
p='source/COA/Unit 4 problems.docx'
with zipfile.ZipFile(p) as z:
    xml=z.read('word/document.xml').decode('utf-8')
for key in ['AMAT','EAT=0.95','0.95+0.15']:
    idx=xml.find(key)
    print('KEY',key,idx)
    if idx>0:
        start=xml.rfind('<w:p ',0,idx)
        end=xml.find('</w:p>',idx)
        print(xml[start:end+6][:6000])
        print('\n---\n')
