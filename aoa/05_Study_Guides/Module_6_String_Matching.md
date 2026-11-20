# AOA — Module 6: String Matching Algorithms

**B.E. Computer Science (AI & ML) · Semester III · Course 2023113 · NEP 2020**
**Module VI · 3 teaching hours**
End-semester paper: 6 questions of 20 marks · Q1 compulsory · answer any 3 · 2 hours

> **Source note.** This guide is built from the Module 6 slide deck (`Module VI String Matching-Algorithms.pptx.pdf`, 17 slides) and `Assignment 6.docx`. The deck covers the naïve algorithm and Rabin–Karp in detail; **it contains no KMP slides**. The KMP section below is written from the prescribed syllabus and standard textbook material, and is marked as supplementary where it goes beyond the deck. The extraction was text-layer based (no scans), so no character-recognition errors are expected; the OCR report records page-by-page character counts.

---

## Syllabus and scope

> **Official syllabus — University of Mumbai, 6.21 (N) B.E. AI & ML, Sem III & IV, 2025–26, page 23.**
> **Module VI — String Matching Algorithms:** The Naïve string-matching algorithm, The Rabin Karp algorithm, The Knuth-Morris-Pratt algorithm.
> **Hours:** 3 · **CO mapping as printed:** CO2.

| Prescribed topic | What you must be able to do | Section |
|---|---|---|
| Naïve string matching | Write the algorithm, trace every alignment, count comparisons, state the worst case. | 2 |
| Rabin–Karp | Compute a hash, use the rolling hash, explain spurious hits, give the expected complexity. | 3 |
| Knuth–Morris–Pratt | Build the prefix (failure) function, run the search without backtracking the text, prove linear time. | 4 |
| Comparison | Choose the right algorithm for a given text, pattern and requirement. | 5 |
| Self-learning | State real-life applications of each algorithm. | 6 |

**Scope warning.** The syllabus prescribes only these three algorithms. Boyer–Moore, Aho–Corasick, suffix arrays and Z-algorithm are useful context but are **not** part of Module VI; do not present them as prescribed topics.

---

## 1 — The string-matching problem

### 1.1 The problem

Given a **text** `T[0…n−1]` and a **pattern** `P[0…m−1]`, with `m ≤ n`, find every **shift** `s` (also called an offset or alignment) such that

```
T[s + j] = P[j]   for every j = 0, 1, …, m − 1
```

Such an `s` is a **valid shift**, and `s` is a **match**. The set of valid shifts is the answer. Usually `m` is much smaller than `n`, and the pattern is fixed while the text is large.

Notation used throughout:

| Symbol | Meaning |
|---|---|
| `n` | length of the text |
| `m` | length of the pattern |
| `s` | shift, `0 ≤ s ≤ n − m` |
| `T[s…s+m−1]` | the window of the text compared with the pattern |
| `n − m + 1` | number of possible shifts (alignments) |

### 1.2 Why it matters

A string-matching algorithm appears wherever a small string must be located inside a large one: searching a document, matching a gene in DNA, detecting a copied assignment, matching a signature in network traffic, or finding a keyword in a log file. The three prescribed algorithms illustrate the three standard strategies:

- **Naïve** — compare every alignment, restart from scratch after a mismatch.
- **Rabin–Karp** — compare cheap **fingerprints** first, and verify only when the fingerprints agree.
- **KMP** — **preprocess the pattern** so that the text never has to be re-read.

### 1.3 Preprocessing versus matching

Every algorithm in this module has two phases:

1. **Preprocessing** — work done once on the pattern (and possibly the text) before searching. Naïve does nothing; Rabin–Karp hashes the pattern; KMP builds the prefix function.
2. **Matching** — scanning the text using the preprocessing.

The total cost is `preprocessing + matching`. This split is the basis of the comparison table in Section 5.

---

## 2 — The naïve string-matching algorithm

### 2.1 The problem

Slide the pattern under the text one position at a time and compare characters until a mismatch is found or the whole pattern matches. It is **exact** matching: only identical characters count, with no tolerance for errors.

### 2.2 The idea

For every shift `s` from `0` to `n − m`:

1. set `j = 0`;
2. while `j < m` and `T[s + j] = P[j]`, increment `j`;
3. if `j = m`, report `s`;
4. otherwise move to `s + 1` and start again from `j = 0`.

The algorithm uses **no preprocessing** and **no extra space** beyond a few counters. That is its main advantage and the reason it is the baseline against which the other two are measured.

### 2.3 How to recognise it

- The question says "naïve", "brute force", "simple", or "compare every shift".
- The text and pattern are short, or the question asks for the number of comparisons.
- The expected answer includes the worst case `T = aaaa…`, `P = aa…a`, where almost every alignment compares almost `m` characters.
- No preprocessing is mentioned.

### 2.4 How it works

1. `n = length(T)`, `m = length(P)`.
2. Repeat for `s = 0, 1, …, n − m`:
   - compare `P[0]` with `T[s]`, then `P[1]` with `T[s+1]`, and so on;
   - stop the comparison at the first mismatch;
   - if all `m` characters matched, output `s`.
3. If no shift matched, report "pattern not found".

### 2.5 Pseudocode

```
NAIVE-STRING-MATCHER(T, P)
  n = length[T]
  m = length[P]
  for s = 0 to n - m:                    // every alignment
      j = 0
      while j < m and T[s + j] == P[j]:  // compare the window
          j = j + 1
      if j == m:
          print "Pattern occurs with shift", s
```

The inner `while` is the comparison loop. The moment `T[s + j] ≠ P[j]`, the algorithm abandons that alignment and moves to the next one; it does **not** remember anything about the characters it has already seen.

### 2.6 Worked example — `P = aab`, `T = abaabcab`

Assignment 6 asks for the pattern `aab` in the text `abaabcab`. Here `n = 8`, `m = 3`, so there are `n − m + 1 = 6` alignments.

| Shift `s` | Window `T[s…s+2]` | Compared characters | Result |
|---|---|---|---|
| 0 | `aba` | `a`=`a`, `a`≠`b` | reject after 2 comparisons |
| 1 | `baa` | `b`≠`a` | reject after 1 comparison |
| 2 | `aab` | `a`=`a`, `a`=`a`, `b`=`b` | **valid shift** |
| 3 | `abc` | `a`=`a`, `b`≠`a` | reject after 2 comparisons |
| 4 | `bca` | `b`≠`a` | reject after 1 comparison |
| 5 | `cab` | `c`≠`a` | reject after 1 comparison |

**Answer:** the pattern `aab` occurs exactly once, at **shift 2** (the substring starting at index 2). The total number of character comparisons is `2 + 1 + 3 + 2 + 1 + 1 = 10`.

Note the phrasing: there are **6 alignments**, which corresponds to **5 shifts** after the initial alignment `s = 0`. A question that asks "how many shifts" may mean either; state which convention you use. In general it is `n − m + 1` alignments.

### 2.7 Worked example — the slide example `P = aabc`, `T = abaaabccb`

This is the trace drawn across slides 5–11. Here `n = 9`, `m = 4`, so there are `9 − 4 + 1 = 6` alignments (`S = 0 … 5`).

| Shift `S` | Window | Outcome |
|---|---|---|
| 0 | `abaa` | mismatch at the second character |
| 1 | `baaa` | mismatch at the first character |
| 2 | `aaab` | mismatch at the third character |
| 3 | `aabc` | **valid shift — pattern found** |
| 4 | `abcc` | mismatch at the second character |
| 5 | `bccb` | mismatch at the first character |

The slide's line "9 − 4 = 5" counts the moves after the first alignment; there are six alignments in total.

### 2.8 Worked example — the comparison-counting exercise

Slides 12–13 pose: show the comparisons the naïve matcher makes for `P = 0001` in `T = 000010001010001`.

`n = 15`, `m = 4`, `n − m + 1 = 12` alignments. The verified trace is:

| Shift | Characters compared | Match? |
|---|---|---|
| 0 | `0001` vs `0000` | no (4 comparisons) |
| 1 | `0001` vs `0001` | **yes** (4 comparisons) |
| 2 | `000` vs `001` | no (3) |
| 3 | `00` vs `01` | no (2) |
| 4 | `0` vs `1` | no (1) |
| 5 | `0001` vs `0001` | **yes** (4) |
| 6 | `000` vs `001` | no (3) |
| 7 | `00` vs `01` | no (2) |
| 8 | `0` vs `1` | no (1) |
| 9 | `00` vs `01` | no (2) |
| 10 | `0` vs `1` | no (1) |
| 11 | `0001` vs `0001` | **yes** (4) |

**Answer:** valid shifts **1, 5 and 11**; **31 comparisons** in total. The varying comparison counts (4,3,2,1) show why the naïve analysis must take the worst case, not the average.

### 2.9 Complexity

Worst case: every alignment compares `m` characters, and there are `n − m + 1` alignments, so

```
O((n − m + 1) · m) = O(nm)
```

The worst case is reached by `T = aaaaa…a` and `P = aaaa…ab`, or by `T = aaaa…` and `P = aaaa…` (all matches, every alignment fully compared). Best case: `O(n)` when the first character of the pattern never occurs in the text. Space: **O(1)** extra. No preprocessing.

### 2.10 Common mistakes

- Reporting the number of comparisons as `n·m` without saying it is the worst case.
- Forgetting the `+1`: the number of alignments is `n − m + 1`, not `n − m`.
- Comparing beyond the end of the text (`s + j ≥ n`).
- Reporting the last compared index instead of the shift `s`.
- Starting the next alignment at `s + j` (that is a different, incorrect optimisation).
- Misreading the slide's "9 − 4 = 5" as the number of alignments.

---

## 3 — The Rabin–Karp algorithm

### 3.1 The problem and the idea

Comparing characters one by one is expensive when many alignments share a long prefix. Rabin–Karp replaces the character comparison with a **numeric fingerprint**: each window is converted to a number modulo a prime `q`, and the numbers are compared first. Only when the fingerprints agree does the algorithm verify the characters.

Because the fingerprint of the next window can be computed from the previous one in constant time (**rolling hash**), the algorithm avoids recomputing the hash of every window from scratch.

### 3.2 Hash function and rolling hash

Treat a window of `m` digits as an `m`-digit number:

```
hash(w) = (w[0]·d^(m−1) + w[1]·d^(m−2) + … + w[m−1]) mod q
```

where `d` is the alphabet size (10 for decimal digits, 256 for bytes, 26 for letters) and `q` is a prime large enough to keep the hash values spread out. The **rolling** step removes the leading digit, shifts the rest left, and appends the new digit:

```
hash(T[s+1 … s+m]) = (d · (hash(T[s … s+m−1]) − T[s]·d^(m−1)) + T[s+m]) mod q
```

If the pattern hash and the window hash differ, the window cannot match, so the characters are skipped. If they agree, the window is either a real match or a **spurious hit** (a collision), and the algorithm verifies it character by character.

### 3.3 How to recognise it

- "Hash", "fingerprint", "rolling hash", "modulo", "spurious hit".
- A numeric text and pattern, and a prime `q` given in the question.
- The question asks for the expected running time or the number of hash comparisons.
- A single pattern is searched in a large text, and preprocessing the pattern is acceptable.

### 3.4 How it works

1. Choose `q`; compute `hP = hash(P)`.
2. Compute the hash of the first window `T[0 … m−1]`.
3. For `s = 0 … n − m`:
   - if `hT = hP`, verify the window character by character and report a match if it agrees;
   - if `s < n − m`, roll the hash to the next window.

### 3.5 Pseudocode

```
RABIN-KARP(T, P, q)
  n = length[T];  m = length[P]
  hP = HASH(P, q)                       // hash of the pattern
  hT = HASH(T[0..m-1], q)               // hash of the first window
  for s = 0 to n - m:
      if hP == hT:
          if P[0..m-1] == T[s..s+m-1]:  // verify the candidate
              print "Pattern found at shift", s
      if s < n - m:
          hT = ROLL(hT, T[s], T[s+m], q) // constant-time update
```

`ROLL` implements the rolling-hash formula above. Verification is essential: the hash equality is necessary but not sufficient.

### 3.6 Worked example — `q = 13`

Slide 16 gives:

```
T = 2 3 5 9 0 2 3 1 4 1 5 2 6 7 3 9 9 2 1
P = 3 1 4 1 5          q = 13
```

Pattern hash: `31415 mod 13 = 7`. Every 5-digit window (slides show them in an interleaved order; the table below is in text order):

| Shift `s` | Window | Value mod 13 | Status |
|---|---|---|---|
| 0 | 23590 | 8 | — |
| 1 | 35902 | 9 | — |
| 2 | 59023 | 3 | — |
| 3 | 90231 | 11 | — |
| 4 | 02314 | 0 | — |
| 5 | 23141 | 1 | — |
| 6 | **31415** | **7** | **valid hit — verify and report** |
| 7 | 14152 | 8 | — |
| 8 | 41526 | 4 | — |
| 9 | 15267 | 5 | — |
| 10 | 52673 | 10 | — |
| 11 | 26739 | 11 | — |
| 12 | **67399** | **7** | **spurious hit — verification fails** |
| 13 | 73992 | 9 | — |
| 14 | 39921 | 11 | — |

The only valid shift is **6**. Shift 12 is a spurious hit: the hash agrees but the characters do not.

### 3.7 Worked example — `q = 11`

Slide 17 gives:

```
T = 3 1 4 1 5 9 2 6 5 3 5 8 9 7 9 3
P = 2 6          q = 11
```

Pattern hash: `26 mod 11 = 4`. The 2-digit windows and their hashes:

| Shift | Window | mod 11 | Status |
|---|---|---|---|
| 0 | 31 | 9 | — |
| 1 | 14 | 3 | — |
| 2 | 41 | 8 | — |
| 3 | 15 | 4 | spurious |
| 4 | 59 | 4 | spurious |
| 5 | 92 | 4 | spurious |
| 6 | **26** | **4** | **valid hit** |
| 7 | 65 | 10 | — |
| 8 | 53 | 9 | — |
| 9 | 35 | 2 | — |
| 10 | 58 | 3 | — |
| 11 | 89 | 1 | — |
| 12 | 97 | 9 | — |
| 13 | 79 | 2 | — |
| 14 | 93 | 5 | — |

The valid shift is **6**. This example shows that a small modulus produces many spurious hits, which erode the speed advantage.

### 3.8 Spurious hits

A **spurious hit** is a window whose hash equals the pattern hash but whose characters differ. It costs a full `m`-character verification and is therefore the main performance risk. The expected number of spurious hits is about `(n − m + 1) / q` if the hashes behave randomly; choosing a large prime `q` reduces them. In the worst case every window collides, and Rabin–Karp degenerates to `O(nm)`, exactly like the naïve algorithm.

### 3.9 Complexity

| Case | Time |
|---|---|
| Preprocessing | `O(m)` to hash the pattern |
| Expected matching | `O(n + m)` for random hashes and a large `q` |
| Worst matching | `O(nm)` (every window is a spurious hit) |
| Space | `O(1)` extra |

### 3.10 Common mistakes

- Reporting only the answer "hash match" without verifying the characters.
- Forgetting to reduce modulo `q` at every step, so the numbers overflow.
- Using `q = 1` or a tiny modulus and then claiming linear time.
- Mixing up the shift index `s` and the window value.
- Forgetting the rolling subtraction of the leading digit.
- Claiming Rabin–Karp is always `O(n + m)`; that is the expected case, not the worst case.

---

## 4 — The Knuth–Morris–Pratt algorithm

> **Supplementary section.** The Module 6 slide deck ends after Rabin–Karp and contains no KMP slides. KMP is prescribed in the syllabus (page 23), so this section supplies the standard treatment. The trace below was verified character by character.

### 4.1 The problem

The naïve algorithm throws away information after a mismatch. If the pattern has a border — a proper prefix that is also a suffix — then the characters just compared already tell us how far the pattern can shift without missing a match. KMP encodes that information once, in the **prefix function**, and uses it to avoid ever moving the text pointer backwards.

### 4.2 The idea

Let `q` be the number of characters of the pattern matched so far, and `i` the current text position.

- If `P[q] = T[i]`, both advance.
- If they differ and `q > 0`, the first `q` characters of the pattern matched; the longest border of `P[0…q−1]` tells us the largest `k < q` such that `P[0…k−1]` is also a suffix of that matched portion. Set `q = π[q−1]` and try again **without moving `i`**.
- If `q = 0`, just advance `i`.

The text pointer `i` never decreases, which is the source of the linear-time guarantee.

### 4.3 The prefix function

For a pattern `P[0…m−1]`, define `π[i]` (also written `f[i]`, `LPS[i]` or "failure function") as the length of the **longest proper prefix** of `P[0…i]` that is also a **suffix** of `P[0…i]`.

```
π[i] = max { k : 0 ≤ k < i+1 and P[0…k−1] = P[i−k+1…i] }
```

`π[0] = 0` always. For `P = ababaca`:

| `i` | 0 | 1 | 2 | 3 | 4 | 5 | 6 |
|---|---|---|---|---|---|---|---|
| `P[i]` | a | b | a | b | a | c | a |
| `π[i]` | 0 | 0 | 1 | 2 | 3 | 0 | 1 |

Read the last row as: after matching `ababa`, the longest border is `aba` (length 3), so a mismatch at `c` can resume with `q = 3` instead of restarting at 0.

### 4.4 Computing the prefix function

```
COMPUTE-PREFIX(P)
  m = length[P]
  pi[0] = 0
  k = 0
  for i = 1 to m - 1:
      while k > 0 and P[i] != P[k]:
          k = pi[k - 1]
      if P[i] == P[k]:
          k = k + 1
      pi[i] = k
```

The `while` loop is what makes the computation linear: `k` can increase at most `m` times and every iteration of the loop decreases it, so the total number of decreases is also bounded by `m`. Hence `O(m)`.

### 4.5 The search

```
KMP-MATCHER(T, P)
  n = length[T];  m = length[P]
  pi = COMPUTE-PREFIX(P)
  q = 0                                  // characters matched so far
  for i = 0 to n - 1:
      while q > 0 and P[q] != T[i]:
          q = pi[q - 1]                  // fall back along the border
      if P[q] == T[i]:
          q = q + 1
      if q == m:
          print "Pattern occurs with shift", i - m + 1
          q = pi[q - 1]                  // continue searching for the next match
```

### 4.6 Worked example — `P = ababaca`, `T = abababacaba`

Prefix function: `π = [0, 0, 1, 2, 3, 0, 1]`.

The verified search trace (`i` is the text index, `q` the matched length before comparing):

| Step | `i` | `T[i]` | `q` before | `P[q]` | Action |
|---|---|---|---|---|---|
| 1 | 0 | a | 0 | a | match, `q = 1` |
| 2 | 1 | b | 1 | b | match, `q = 2` |
| 3 | 2 | a | 2 | a | match, `q = 3` |
| 4 | 3 | b | 3 | b | match, `q = 4` |
| 5 | 4 | a | 4 | a | match, `q = 5` |
| 6 | 5 | b | 5 | c | mismatch, `q = π[4] = 3` |
| 7 | 5 | b | 3 | b | match, `q = 4` (text index did not move) |
| 8 | 6 | a | 4 | a | match, `q = 5` |
| 9 | 7 | c | 5 | c | match, `q = 6` |
| 10 | 8 | a | 6 | a | match, `q = 7 = m` → **match at shift 2**, `q = π[6] = 1` |
| 11 | 9 | b | 1 | b | match, `q = 2` |
| 12 | 10 | a | 2 | a | match, `q = 3` |

**Answer:** the pattern occurs once, at **shift 2** (the window `ababaca`). The text index advanced 11 times and never moved backwards; step 6 is the crucial fallback, where the pattern shifts from its `ababa` border without re-reading `T[0…4]`.

### 4.7 Complexity

| Phase | Time | Space |
|---|---|---|
| Prefix function | `Θ(m)` | `Θ(m)` |
| Search | `Θ(n)` | `Θ(1)` extra |
| Total | `Θ(n + m)` | `Θ(m)` |

The linear bound holds in the **worst case**, not just on average, because `i` only increases and `q` only falls back along borders that were built by previous increases.

### 4.8 Why KMP is preferred

1. **Worst-case linear time** `O(n + m)`, unlike the naïve `O(nm)` and Rabin–Karp's worst case.
2. **The text is read once, left to right** — it never backtracks, so it works on a stream or a file that cannot be rewound.
3. **The prefix function is reusable** when the same pattern is searched in many texts.
4. **No collisions or probabilistic behaviour** — the result is deterministic, unlike hashing.

### 4.9 Common mistakes

- Building the prefix function over the text instead of the pattern.
- Using the prefix value of the wrong index (`π[q]` instead of `π[q−1]`).
- Advancing `i` during a fallback, which breaks correctness.
- Forgetting to reset `q = π[m−1]` after a full match, so later matches are missed.
- Confusing the prefix function with the Z-array.
- Claiming `O(nm)` because of the nested loops; the amortised argument gives `O(n)`.

---

## 5 — Comparing the three algorithms

| | Naïve | Rabin–Karp | KMP |
|---|---|---|---|
| Preprocessing | none | `O(m)` hash of the pattern | `O(m)` prefix function |
| Matching (expected) | `O(nm)` | `O(n + m)` | `O(n + m)` |
| Matching (worst) | `O(nm)` | `O(nm)` | `O(n + m)` |
| Extra space | `O(1)` | `O(1)` | `O(m)` |
| Text backtracking | yes (restarts each shift) | no (windows slide) | no |
| Randomised? | no | yes (collisions) | no |
| Best used when | short text/pattern; teaching baseline | many patterns or a large alphabet; plagiarism and document similarity | large text, repeated searches, streaming, guaranteed performance |

**Choosing in an exam.**

- "Count the comparisons for every shift" → naïve.
- "Use a hash / a prime q / explain spurious hits" → Rabin–Karp.
- "No backtracking / prefix function / linear worst case" → KMP.
- "Search one pattern in a huge text with a guarantee" → KMP.
- "Search many patterns or compare documents by fingerprints" → Rabin–Karp (and note that multi-pattern RK hashes each pattern).

---

## 6 — Self-learning: real-life applications

| Algorithm | Real-life use |
|---|---|
| Naïve | Short searches in a text editor, spreadsheet `FIND`, teaching the baseline, small configuration files |
| Rabin–Karp | Plagiarism detection (winnowing fingerprints), duplicate detection, DNA substring search, spam and malware signature matching, rsync-style block matching |
| KMP | `grep`-style search in large files, network intrusion detection, DNA sequence alignment, streaming log search, finding a motif in a genome |

The syllabus lists "real life applications of all algorithms" as the self-learning topic for Module VI. Two or three concrete examples per algorithm are enough for an examination answer; always name the property that makes the algorithm suitable (hashing, linear time, streaming).

---

## 7 — Practice questions

Attempt these on paper; the worked key follows in Section 8. Provenance is stated for each question.

### Q1 — Naïve matching

*Assignment 6, Q1 (course assignment — not a University paper).* Explain the naïve string-matching algorithm. Show the steps and find the number of shifts needed to find the pattern `aab` in the text `abaabcab`.

### Q2 — KMP advantages

*Assignment 6, Q2 (course assignment — not a University paper).* List any four advantages of KMP over other string-matching algorithms.

### Q3 — Comparison counting

*Module 6 slide deck, slides 12–13 (class exercise).* Show the comparisons the naïve matcher makes for `P = 0001` in `T = 000010001010001`. State all valid shifts and the total number of character comparisons.

### Q4 — Rabin–Karp

*Module 6 slide deck, slide 16 (class example).* For `T = 2359023141526739921`, `P = 31415`, `q = 13`, compute the pattern hash, the hash of every window, and identify the valid hits and the spurious hits.

### Q5 — Rabin–Karp with a small modulus

*Module 6 slide deck, slide 17 (class example).* Repeat Q4 for `T = 3141592653589793`, `P = 26`, `q = 11`. Why are there so many spurious hits?

### Q6 — Prefix function

*Standard textbook exercise (supplementary).* Compute the prefix function for `P = aabaabaaa` and use it to search `T = aabaabaabaabaaa`. Give every match position.

### Q7 — Conceptual

*IAT-style theory question — not a University paper.* (a) Why is the naïve algorithm `O(nm)` in the worst case? (b) What is a spurious hit? (c) State the three phases of KMP and their costs.

---

## 8 — Answer key

### A1 — Naïve matching, `aab` in `abaabcab`

`n = 8`, `m = 3`, so there are `n − m + 1 = 6` alignments (`s = 0 … 5`). The trace is in Section 2.6.

| Shift | Window | Result |
|---|---|---|
| 0 | `aba` | reject (2 comparisons) |
| 1 | `baa` | reject (1) |
| 2 | `aab` | **match** (3) |
| 3 | `abc` | reject (2) |
| 4 | `bca` | reject (1) |
| 5 | `cab` | reject (1) |

**Answer:** one occurrence at **shift 2**, 10 comparisons, 6 alignments (5 shifts after the first).

### A2 — Four advantages of KMP

1. Worst-case **`O(n + m)`** time, against the naïve `O(nm)` and Rabin–Karp's worst case.
2. The text pointer **never moves backwards**, so the text can be streamed or read once.
3. The **prefix function is computed once** and can be reused for many texts.
4. **Deterministic** — no hash collisions or spurious hits, unlike Rabin–Karp.

(Also acceptable: no preprocessing of the text; predictable performance; well suited to large files.)

**Answer:** KMP runs in `O(n + m)` worst-case time, never moves the text pointer backwards, reuses one prefix function across texts, and is deterministic.

### A3 — Comparisons for `0001` in `000010001010001`

12 alignments, **31 comparisons**, valid shifts **1, 5, 11**. The per-shift table is in Section 2.8.

**Answer:** valid shifts **1, 5 and 11**; **31 character comparisons** over 12 alignments.

### A4 — Rabin–Karp, `q = 13`

Pattern hash: `31415 mod 13 = 7`.

| Shift | Window | mod 13 | Status |
|---|---|---|---|
| 0 | 23590 | 8 | — |
| 1 | 35902 | 9 | — |
| 2 | 59023 | 3 | — |
| 3 | 90231 | 11 | — |
| 4 | 02314 | 0 | — |
| 5 | 23141 | 1 | — |
| 6 | 31415 | 7 | **valid** |
| 7 | 14152 | 8 | — |
| 8 | 41526 | 4 | — |
| 9 | 15267 | 5 | — |
| 10 | 52673 | 10 | — |
| 11 | 26739 | 11 | — |
| 12 | 67399 | 7 | spurious |
| 13 | 73992 | 9 | — |
| 14 | 39921 | 11 | — |

**Answer:** valid shift **6**; one spurious hit at shift 12.

### A5 — Rabin–Karp, `q = 11`

Pattern hash: `26 mod 11 = 4`. Windows: `31→9, 14→3, 41→8, 15→4, 59→4, 92→4, 26→4, 65→10, 53→9, 35→2, 58→3, 89→1, 97→9, 79→2, 93→5`.

**Answer:** valid shift **6**; spurious hits at shifts **3, 4, 5**. With only 11 possible hash values and 15 windows, collisions are expected: about `15/11 ≈ 1.4`, and three occurred.

### A6 — Prefix function for `aabaabaaa`

`π = [0, 1, 0, 1, 2, 3, 4, 5, 2]`.

Searching `T = aabaabaabaabaaa` finds the pattern at shift **6** only. Working: the first nine characters `aabaabaab` fail at the last position (`b` where the pattern has `a`); the prefix function allows the scan to resume without re-reading the text. At shift 6 the window `aabaabaaa` matches completely; the fallback `q = π[8] = 2` then lets the scan continue, but no further full match exists.

**Answer:** `π = [0, 1, 0, 1, 2, 3, 4, 5, 2]`; the pattern occurs once, at shift **6**.

### A7 — Conceptual

**(a)** There are `n − m + 1` alignments and each can compare up to `m` characters, giving `O((n−m+1)m) = O(nm)`. The worst case is `T = aaaaa…a`, `P = aaaa…ab`, where every alignment matches `m − 1` characters before failing.

**(b)** A spurious hit is a window whose hash equals the pattern hash but whose characters differ. It must be verified and rejected; too many of them destroy the speed advantage of Rabin–Karp.

**(c)** Preprocessing (`O(m)`, prefix function), matching (`O(n)`), total `O(n + m)`; space `O(m)`.

**Answer:** (a) `n − m + 1` alignments with up to `m` comparisons each gives `O(nm)`; (b) a hash match whose characters differ; (c) `O(m)` preprocessing, `O(n)` matching, `O(n + m)` total, `O(m)` space.

---

## 9 — Common mistakes across the module

| Trap | What the examiner expects |
|---|---|
| Reporting `n − m` alignments | `n − m + 1` alignments; state the convention |
| Saying naïve is `O(n + m)` | Worst case `O(nm)`; best case `O(n)` |
| Skipping Rabin–Karp verification | A hash match must be checked character by character |
| Calling Rabin–Karp linear in the worst case | Expected `O(n + m)`, worst `O(nm)` |
| Using the prefix function of the wrong index | `π[q−1]` on a mismatch |
| Moving the text pointer during a KMP fallback | The text pointer never goes backwards |
| Forgetting to reset `q` after a match | `q = π[m−1]` to keep finding matches |
| Presenting Boyer–Moore as prescribed | Module VI is naïve, Rabin–Karp, KMP only |
| Giving a match index without the shift | Report the shift `s`, not the last compared index |

---

## 10 — Last-minute revision sheet

**Naïve.** Compare all `n − m + 1` alignments; restart at each shift. Time `O(nm)` worst, `O(n)` best; space `O(1)`. `aab` in `abaabcab` → shift **2**. `0001` in `000010001010001` → shifts **1, 5, 11**, 31 comparisons.

**Rabin–Karp.** Hash the pattern, roll the window hash, verify only on equality. Expected `O(n + m)`, worst `O(nm)`, space `O(1)`. `31415 mod 13 = 7`; valid shift **6**; spurious at **12**. `26 mod 11 = 4`; valid shift **6**; spurious at **3, 4, 5**.

**KMP.** Prefix function `π[i]` = longest proper prefix that is also a suffix of `P[0…i]`. `ababaca` → `[0,0,1,2,3,0,1]`. Search is `O(n + m)` worst case, space `O(m)`. Match of `ababaca` in `abababacaba` at shift **2**; the fallback at `q = 5` goes to `q = 3` without moving the text pointer.

**One-line differences.**

- Naïve: compare everything, remember nothing.
- Rabin–Karp: compare fingerprints, verify matches.
- KMP: preprocess the pattern, never re-read the text.

**Numbers to remember:** `n − m + 1` alignments; naïve `O(nm)`; RK expected `O(n+m)`; KMP `O(n+m)`; `π(ababaca) = 0,0,1,2,3,0,1`.

---

## 11 — References and attribution

**Official syllabus.**
University of Mumbai, Faculty of Science and Technology, *6.21 (N) B.E. Artificial Intelligence and Machine Learning, Semester III and Semester IV*, 2025–26, page 23 (Module VI). PDF: `https://mu.ac.in/old/wp-content/uploads/2025/06/6.21-N-B.E.-AI-ML-sem-III-IV.pdf`.

**Course material inspected.**
- `Module VI String Matching-Algorithms.pptx.pdf` — 17 slides; naïve algorithm (slides 4–13) and Rabin–Karp (slides 14–17). Text extracted with a text-layer pass; the deck has no KMP slides.
- `Assignment 6.docx` — naïve question (`aab` in `abaabcab`) and KMP advantages.

**Standard references for further reading (not quoted page-by-page).**
- T. H. Cormen, C. E. Leiserson, R. L. Rivest and C. Stein, *Introduction to Algorithms*, 3rd edition, MIT Press (naïve matching, Rabin–Karp, KMP, prefix function).
- E. Horowitz, S. Sahni and S. Rajasekaran, *Computer Algorithms*, 2nd edition, Universities Press.

**Attribution.** All explanations, tables, pseudocode and traces were written for this guide. Practice questions state their provenance at the question; none is presented as a University examination paper. KMP is marked **Supplementary section** because the provided slide deck does not cover it, although the syllabus prescribes it.
