import pymupdf, os, sys
jobs=[
 ('source/COA/Musa COA/COA - MUSA Question Bank 2026.pdf','musa_qb'),
 ('source/COA/Musa COA/COA Paper Set - 1.pdf','musa_paper'),
 ('source/COA/Musa COA/COA - MUSA QB Solution 2026.pdf','musa_sol'),
]
for path,tag in jobs:
    doc=pymupdf.open(path)
    for i,page in enumerate(doc):
        pix=page.get_pixmap(dpi=150)
        out=f'render/{tag}_p{i+1}.png'
        os.makedirs('render',exist_ok=True)
        pix.save(out)
        print(out, pix.width, pix.height)
