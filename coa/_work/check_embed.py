import zipfile
p='source/COA/Unit 4 problems.docx'
with zipfile.ZipFile(p) as z:
    print([n for n in z.namelist() if 'embed' in n or 'media' in n or 'ole' in n.lower()])
