import fitz, sys, os
for path in sys.argv[1:]:
    doc=fitz.open(path)
    print('\n\n===== '+path+f' | pages={doc.page_count} =====')
    for i,page in enumerate(doc):
        t=page.get_text()
        print(f'\n--- PAGE {i+1} --- chars={len(t.strip())}')
        print(t)
