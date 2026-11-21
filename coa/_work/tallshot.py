import subprocess, sys
from pathlib import Path

CHROME = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
src = Path(sys.argv[1]).resolve()
out = Path(sys.argv[2]).resolve()
height = int(sys.argv[3]) if len(sys.argv) > 3 else 22000
width = int(sys.argv[4]) if len(sys.argv) > 4 else 1400

subprocess.run([
    CHROME, "--headless=new", "--disable-gpu", "--hide-scrollbars",
    f"--window-size={width},{height}", f"--screenshot={out}",
    "--virtual-time-budget=3000", src.as_uri()
], check=True, capture_output=True)
print(out, out.stat().st_size)
