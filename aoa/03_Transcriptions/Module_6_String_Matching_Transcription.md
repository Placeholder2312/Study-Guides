# Module VI — String Matching Algorithms — Transcription

**Source:** `C:\Users\Harsh\Downloads\AOA\01_Original_Notes\Module_6\Module VI String Matching-Algorithms.pptx.pdf`
**Method:** text-layer extraction with PyMuPDF (no raster OCR required — the PDF is a slide export, not a scan).
**Pages:** 17 · **Extracted characters:** 5,635 · **Extraction date:** 2026-11-20

The text below preserves the slide wording. Figure labels are transcribed in reading order; matrix-style slide content (the naïve alignment drawings) is reconstructed as labelled sequences because the PDF stores every character and index as a separate text object.

---

## Slide 1

Module VI
String Matching Algorithms

- The Naïve string-matching algorithm
- The Rabin Karp algorithm
- The Knuth-Morris-Pratt algorithm

## Slide 2

String Matching Algorithms

- A string-searching algorithm, sometimes called a string-matching algorithm, is an important class of string algorithms that try to find a place where one or several strings (also called patterns) are found within a larger string or text.
- Applications: DNA analysis, plagiarism detection, and cybersecurity threat identification.

## Slide 3

String Matching Algorithms

- The Naïve string-matching algorithm
- The Rabin Karp algorithm
- The Knuth-Morris-Pratt algorithm

## Slide 4

The Naïve string-matching algorithm

- Naïve algorithm is an exact string matching algorithm (finding one or all exact occurrences of a pattern in a text).
- This algorithm is helpful for smaller texts.
- It does not need any pre-processing phases.
- We can find a substring by checking once for the string.
- It also does not occupy extra space to perform the operation.

## Slide 5

The Naïve string-matching algorithm

Text `T` of window size 9: `a b a a a b c c b` with indices `0 1 2 3 4 5 6 7 8`.
Pattern `P` of window size 4: `a a b c` with indices `0 1 2 3`.

## Slide 6

The Naïve string-matching algorithm

Text and pattern as on slide 5. Caption: "At shift S=0".

## Slide 7

The Naïve string-matching algorithm

Same text and pattern. Caption: "At shift S=1".

## Slide 8

The Naïve string-matching algorithm

Same text and pattern. Caption: "At shift S=2".

## Slide 9

The Naïve string-matching algorithm

Same text and pattern. Caption: "At shift S=3".

"Pattern P is found in the Text T at shift S=3. It is a valid shift."

## Slide 10

The Naïve string-matching algorithm

Same text and pattern. Caption: "At shift S=4".

## Slide 11

The Naïve string-matching algorithm

Same text and pattern. Caption: "At shift S=5".

"How many number of shifts we need to do? 9 − 4 = 5."

## Slide 12

The Naïve string-matching algorithm

```
Step 1. n ← length [T]   9
Step 2. m ← length [P]   4
Step 3. for (i = 0; i <= n - m; i++)          // this is for shift
            for (int j = 0; j < m; j++)       // this is for matching pattern with text
                if (T.charAt(i + j) != P.charAt(j))
                    break
            if (j == m)
                println("Pattern found")
```

## Slide 13

The Naïve string-matching algorithm

- Show the comparisons the naïve string matcher makes for the pattern `P = 0001` in the text `T = 000010001010001`.

## Slide 14

The Rabin Karp algorithm

- Calculate hash value for the pattern.
- The characters in the pattern are assigned integers and then some mathematical operations are performed on them to produce a single number (the hash value).
- The exact operations used will depend on the hash function being used.
- Scan the text one character at a time, starting from the first character.
- At each position in the text, it calculates the hash value for the substring of the text that is the same length as the pattern.
- If the hash value for the substring of the text matches the hash value for the pattern, the algorithm compares the substring to the pattern character by character to see if they are an exact match.
- If the substring and the pattern are not an exact match, the algorithm continues scanning the text, calculating new hash values for the substrings as it goes.
- If the substring and the pattern are an exact match, the algorithm reports that the pattern has been found in the text at the current position.

## Slide 15

Algorithm for Rabin-Karp

```
n = T.length
m = P.Length
hP = Hash(P[...])       // P mod q where q is a random prime number
hT = Hash(T[...])       // T mod q
for S = 0 to n-m
    if (hP == hT)
        if (P[0...m-1] = T[S+0, ..., S+m-1])   // matching all characters of P and T
            Print "Pattern found with Shift S"
    if (S < n-m)
        hT = Hash(T(S+1, ..., S+m))
```

## Slide 16

Example:

```
T = 2 3 5 9 0 2 3 1 4 1 5 2 6 7 3 9 9 2 1
P = 3 1 4 1 5        q = 13
Find Hash Value: P mod q = 31415 mod 13 = 7
23590 MOD 13 = 8          35902 MOD 13 = 9
59023 MOD 13 = 3          90231 MOD 13 = 11
02314 MOD 13 = 0          23141 MOD 13 = 1
31415 MOD 13 = 7  Valid Hit
14152 MOD 13 = 8          41526 MOD 13 = 4
15267 MOD 13 = 5          52673 MOD 13 = 10
26739 MOD 13 = 11         67399 MOD 13 = 7  spurious hits
73992 MOD 13 = 9          39921 MOD 13 = 11
```

## Slide 17

```
T = 3 1 4 1 5 9 2 6 5 3 5 8 9 7 9 3
P = 2 6        q = 11
Find Hash Value: P mod q = 26 mod 11 = 4
Find hash value for text: 3 1 4 1 5 9 2 6 5 3 5 8 9 7 9 3
31 MOD 11 = 9        53 MOD 11 = 9
14 MOD 11 = 3        35 MOD 11 = 2
41 MOD 11 = 8        58 MOD 11 = 3
15 MOD 11 = 4  spurious hits
59 MOD 11 = 4  spurious hits
92 MOD 11 = 4  spurious hits
26 MOD 11 = 4  Valid Hit
65 MOD 11 = 10       89 MOD 11 = 1
97 MOD 11 = 9        79 MOD 11 = 2
93 MOD 11 = 5
```

---

## Assignment 6 — transcription

**Assignment 6**

1. Explain naïve string matching algorithm. Show the steps and find number of shifts to find the Pattern "aab" in the Text String "abaabcab".
2. List any four advantages of KMP over other string matching algorithms.

---

## Coverage note

The deck ends at slide 17. **There are no KMP slides**, although the KMP algorithm is prescribed by the syllabus. The KMP section of the study guide is therefore built from standard textbook material and is labelled *Supplementary section*.
