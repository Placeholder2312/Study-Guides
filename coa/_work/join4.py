from pathlib import Path

base = Path(__file__).parent
body = (base / "module4_body.html").read_text(encoding="utf-8")
tail = (base / "module4_tail.html").read_text(encoding="utf-8-sig")
(base / "module4_body.html").write_text(body.rstrip() + "\n" + tail, encoding="utf-8")
print("body", len(body), "tail", len(tail))
