# DSGT Exam Essentials — Progress Record

Short checkpoint for the selective Module I–III study material. Exam: 18 November 2026.

**Scope authority:** `00_University_Syllabus/Syllabus_Coverage.md` (Modules I–III only).
**Mission:** three concise but genuinely teachable selective guides. Not full module guides.

| Module | Guide | Markdown master | Status |
|---|---|---|---|
| I — Crisp Set Theory and Logic | `modules/module-1.html` | `Module_1_Exam_Essentials.md` | first pass complete |
| II — Mathematical Relations | `modules/module-2.html` | `Module_2_Exam_Essentials.md` | first pass complete |
| III — Functions | `modules/module-3.html` | `Module_3_Exam_Essentials.md` | first pass complete |

---

## Official syllabus discrepancies — resolved 17 November 2026

The official University of Mumbai syllabus PDF (6.21 (N), B.E. Artificial Intelligence and Machine Learning, Semesters III–IV; Academic Council approval 20 May 2025) resolves both earlier discrepancies. Its detailed-syllabus table on PDF page 19 assigns **7 teaching hours to Module I** and **5 teaching hours to Module IV**. It lists the **Inclusion–Exclusion Principle under Module IV — Counting**, not Module I. The canonical coverage extraction is `00_University_Syllabus/Syllabus_Coverage.md`. Module I now links to Module IV instead of duplicating the lesson; the transferred practice question and Diagram 4 are retained in Module IV.

## Module I — Crisp Set Theory and Logic (7 hours, CO1)

**Covered:** set vocabulary and notation · subsets, proper subsets and power sets · union, intersection,
difference, complement, symmetric difference and the laws of sets · membership tables · Cartesian
product · partitions · three methods for proving set identities · connectives and truth tables ·
converse/inverse/contrapositive · logical equivalence with the Summer 2026 and Winter 2025 proofs ·
tautology, contradiction, contingency · CNF and DNF · predicates, quantifiers, translation patterns and
negation · mathematical induction with the full Summer 2026 question · the other
proof methods (direct, contrapositive, contradiction, cases, counterexample, exhaustion).

**Skipped (deliberate):** Venn-diagram drawing, membership tables for four or more sets, PROLOG/LISP
expert systems, non-classical logics, cardinality of infinite sets, Cantor's theorem, Karnaugh maps,
long exhaustion proofs.

**Worked examples completed:** power set of a three-element set and the edge cases P(∅), P({∅});
De Morgan by membership table and numerically; distributivity by an eight-row membership table;
A − B = A ∩ B′ by element argument; (A ∪ B) ∩ (A ∪ B′) by named laws; A × B, B × A and the 8-pair
difference for A = {1,3,5}, B = {2,3,8}; all five partitions of {1,2,3}; the campus-access translation;
a full eight-row truth table for (p ∨ q) → ¬r; the Summer 2026 equivalence in full with table; the
Winter 2025 equivalence; ¬(p ∨ (¬p ∧ q)) ≡ ¬p ∧ ¬q; the IAT tautology check; the IAT contingency check;
CNF and DNF of [P → (Q ∧ R)] ∧ [¬P → (¬Q ∧ ¬R)] with truth table; the Java sentence and its negation;
the GenAI and class-statement translations; the Summer 2026 induction in
full; the arithmetic series; the four other proof methods.

**Practice:** 11 questions with a separate answer key, full working, and a membership table in Q4.

**Sources:** Module 1 Set and Logic PPT (teacher, 108 slides, slide ranges cited per section);
Summer 2026 Q.1(b), Q.4(b); Winter 2025 Q.1(b) from scanned page 1; IAT1 sample Q7–Q13;
prelim question bank Module 1; official syllabus.

**Verification:** every equivalence and classification checked by exhaustive truth table; the CNF
verified row by row against the original expression; the induction closed form and step checked
symbolically and at n = 1–4; inclusion–exclusion calculations are verified in Module IV; power-set and Cartesian
counts enumerated programmatically. Two source-slide corrections recorded (slide 97 mislabels a
contrapositive proof; slide 104 has a mis-expanded term).

**Published route:** `/dsgt/modules/module-1`
**Deployment status:** see final entry below.

---

## Module II — Mathematical Relations (8 hours, CO2)

**Covered:** relation definition/notation/domain/range/inverse/matrix · reflexive, symmetric,
antisymmetric, transitive · equivalence relations and classes · transitive closure + Warshall ·
partial orders, posets, minimal/maximal, bounds, meet/join, lattice test.

**Skipped (deliberate):** detailed lattice types, sublattice proofs, extended chain/antichain theory,
relation composition beyond Warshall, drawing Hasse diagrams and digraphs, application essays.

**Worked examples completed:** relation + matrix + inverse; relation-on-a-set (teacher 1.12);
equivalence relation A; partial order divisibility; Summer 2026 polygon equivalence (full);
teacher equivalence classes (full); Summer 2026 airline Warshall (all four rounds, 12 pairs);
Summer 2026 divisibility poset (34 pairs, meet/join table, lattice conclusion);
non-lattice counterexample S = {2,3,4,6}.

**Practice:** 10 questions. Separate answer key with full working (Warshall rounds shown as matrices).

**Sources:** Module 2 Relations PPT (teacher, 76 slides); Summer 2026 paper Q.1(a), Q.3(a), Q.3(b);
Winter 2025 paper Q.3(a), Q.3(b), read from scanned page 3; official syllabus.

**Verification:** Warshall recomputed programmatically (Summer closure 12 pairs; Winter closure 13
pairs); all 28 pairs of the divisibility poset checked for gcd/lcm membership in A; classes checked
for disjointness and coverage.

**Published route:** `/dsgt/modules/module-2`
**Deployment status:** see final entry below.

---

## Module III — Functions (3 hours, CO3)

**Covered:** definition, domain, codomain, range, image, preimage, relation vs function ·
injective/surjective/bijective tests · composition and order · inverse by algebra and by reversing
pairs · verification identities · Summer 2026 discount/tax application.

**Skipped (deliberate):** neural networks, insurance, tax brackets, vending machines, advanced
function theory, extra composition variations.

**Worked examples completed:** ordered-pair function tests (teacher examples a–d); x² on Z (not
injective, not surjective); x + 1 on Z (bijective); finite bijection; teacher composition 2x+3 and
3x+2 with numerical check; Summer 2026 discount/tax (Rs. 918, checked two ways); inverse of
2x + 3 with both identities; inverse of a finite set of pairs; non-invertible x² discussion.

**Practice:** 9 questions, answer key with full working.

**Sources:** Module 3 Functions PPT (teacher, 20 slides); Summer 2026 Q.2(b); IAT1 sample; syllabus.

**Verification:** compositions checked numerically (f∘g = 67, g∘f = 71 at x = 10); discount/tax
checked two ways; inverse identities verified symbolically; the "order does not change two
percentage steps" fact stated honestly with a flat-discount counterexample.

**Published route:** `/dsgt/modules/module-3`
**Deployment status:** see final entry below.

---

## Remaining work / exact next action

Modules I, II and III are written, committed, pushed and verified live on production. Nothing is
blocking the 18 November exam.

Optional additions only (not required, and not to be done unless asked):

1. More CNF/DNF drills, deducing the full laws of logic from the three listed ones.
2. Extra induction practice beyond the worked example and quick practice.
3. Module 6 is still "Coming soon" on the index; it is outside this pass.

## Deployment log

- Module II: committed and pushed to `main`.
- Module III: committed and pushed to `main`.
- Module I: committed and pushed to `main` with the `/dsgt/modules/module-1` redirects removed from
  `vercel.json`.
- Production verified after the build reached READY (`dpl_Gp6QFXrUad4dUcxmpH4a41J5uUBV`, commit
  `2fb2ad9`): `/dsgt/modules/module-1` returns **200** (111,117 bytes, title "DSGT Module 1 — Crisp
  Set Theory and Logic"), `/dsgt/modules/module-2` and `/dsgt/modules/module-3` return 200, and
  `/dsgt` lists Module 1 as a link instead of "Coming soon". All three modules are live.


## Module V — Question / Solution / Final Answer formatting

- Latest audited checkpoint: 17 existing worked examples and 4 previous end-semester questions (21 formatting units). No questions have been added or removed.
- **Completed: 21/21 units.** All 17 worked examples and all 4 previous end-semester questions now use the exact Question / Solution / Final Answer markup and CSS from Module IV. Existing wording, workings and conclusions were preserved.
- Module V's equation CSS now matches Module IV's no-wrap rule; long equations scroll horizontally on narrow screens. The mobile `overflow-wrap: anywhere` override was removed.
- **Module V formatting pass complete:** all worked examples and previous end-semester questions use the Module IV Question / Solution / Final Answer structure. Continue with the next DSGT module only after fetching its latest state.


## Module I — Question / Solution / Final Answer formatting

- Repository audit found 29 existing worked-example containers and 3 past-paper question containers (32 formatting units). This is a fresh repository count; the older “30 remaining” note was only a historical agent estimate.
- **Completed: 10/32 units.** Worked Examples 1–5 now use Module IV's exact Question / Solution / Final Answer markup and CSS. All existing explanations, tables and results were retained.
- **Next:** Worked Examples 11–15. Commit and verify after each five units.
