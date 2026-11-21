from PIL import Image, ImageDraw
import glob
files=sorted(glob.glob('render/musa_sol_p*.png'), key=lambda s:int(s.split('_p')[1].split('.')[0]))
thumbs=[]
for f in files:
    im=Image.open(f)
    im.thumbnail((300,430))
    canvas=Image.new('RGB',(310,460),'white')
    canvas.paste(im,(5,25))
    d=ImageDraw.Draw(canvas)
    d.text((5,5), f.split('_')[-1].replace('.png',''), fill='red')
    thumbs.append(canvas)
cols=6; rows=(len(thumbs)+cols-1)//cols
sheet=Image.new('RGB',(cols*310, rows*460),'white')
for i,t in enumerate(thumbs):
    sheet.paste(t,((i%cols)*310,(i//cols)*460))
sheet.save('render/contact_sol.png')
print(sheet.size)
