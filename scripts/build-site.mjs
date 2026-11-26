import { cp, mkdir, readdir, stat } from "node:fs/promises";
import path from "node:path";

const root = process.cwd();
const out = path.join(root, "dist");
const subjects = [
  "aoa",
  "applied-mathematics-ii",
  "applied-physics",
  "beee",
  "coa",
  "dsgt",
  "engineering-mechanics",
  "maths",
  "oe",
  "semiconductor-physics",
];

async function copyFile(relativePath) {
  const source = path.join(root, relativePath);
  const target = path.join(out, relativePath);
  await mkdir(path.dirname(target), { recursive: true });
  await cp(source, target);
}

async function copyHtmlDirectory(relativeDir) {
  const sourceDir = path.join(root, relativeDir);
  let entries;
  try {
    entries = await readdir(sourceDir, { withFileTypes: true });
  } catch (error) {
    if (error.code === "ENOENT") return;
    throw error;
  }
  for (const entry of entries) {
    if (!entry.isFile() || !entry.name.endsWith(".html")) continue;
    await copyFile(path.posix.join(relativeDir, entry.name));
  }
}

await mkdir(out, { recursive: true });
for (const file of ["index.html", "404.html", "robots.txt", "sitemap.xml"]) await copyFile(file);
await cp(path.join(root, "assets"), path.join(out, "assets"), { recursive: true });

for (const subject of subjects) {
  await copyFile(path.posix.join(subject, "index.html"));
  await copyHtmlDirectory(path.posix.join(subject, "modules"));
}
await copyFile("maths/endsem-questionbank/index.html");

const total = async (dir) => {
  let bytes = 0;
  for (const entry of await readdir(dir, { withFileTypes: true })) {
    const full = path.join(dir, entry.name);
    if (entry.isDirectory()) bytes += await total(full);
    else bytes += (await stat(full)).size;
  }
  return bytes;
};
console.log("Prepared static site:", (await total(out)).toLocaleString(), "bytes");
