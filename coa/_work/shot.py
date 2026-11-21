import subprocess, sys, tempfile, os
from pathlib import Path

CHROME = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
src = Path(sys.argv[1]).resolve()
out = Path(sys.argv[2]).resolve()
offset = int(sys.argv[3]) if len(sys.argv) > 3 else 0
width = int(sys.argv[4]) if len(sys.argv) > 4 else 1400
height = int(sys.argv[5]) if len(sys.argv) > 5 else 1100

html = src.read_text(encoding="utf-8")
inject = f"<script>addEventListener('load',function(){{window.scrollTo(0,{offset});}});</script>\n</body>"
html = html.replace("</body>", inject)
tmp = Path(tempfile.gettempdir()) / f"shot_{offset}.html"
tmp.write_text(html, encoding="utf-8")

subprocess.run([
    CHROME, "--headless=new", "--disable-gpu", "--hide-scrollbars",
    f"--window-size={width},{height}", f"--screenshot={out}",
    "--virtual-time-budget=2500", tmp.as_uri()
], check=True, capture_output=True)
print(out, out.stat().st_size)
