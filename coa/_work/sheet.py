from PIL import Image, ImageDraw
import sys
src = Image.open(sys.argv[1])
w, h = src.size
step = int(sys.argv[2]) if len(sys.argv) > 2 else 1500
scale = float(sys.argv[3]) if len(sys.argv) > 3 else 0.4
cols = int(sys.argv[4]) if len(sys.argv) > 4 else 3
slices = []
for y in range(0, h, step):
    s = src.crop((0, y, w, min(y + step, h)))
    s = s.resize((int(w * scale), int((min(y + step, h) - y) * scale)))
    slices.append((y, s))
rows = (len(slices) + cols - 1) // cols
cw, ch = slices[0][1].size
sheet = Image.new("RGB", (cols * (cw + 10) + 10, rows * (ch + 24) + 10), "white")
d = ImageDraw.Draw(sheet)
for i, (y, s) in enumerate(slices):
    x = 10 + (i % cols) * (cw + 10)
    yy = 10 + (i // cols) * (ch + 24)
    sheet.paste(s, (x, yy))
    d.text((x + 4, yy + ch + 4), f"y={y}", fill="black")
out = sys.argv[5] if len(sys.argv) > 5 else "sheet.png"
sheet.save(out)
print(out, sheet.size, len(slices))
