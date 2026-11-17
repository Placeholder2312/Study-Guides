# DSGT Exam Essentials — Progress Record

Short checkpoint for the selective Module I–III study material. Exam: 18 November 2026.

**Scope authority:** `00_University_Syllabus/Syllabus_Coverage.md` (Modules I–III only).
**Mission:** three concise but genuinely teachable selective guides. Not full module guides.

| Module | Guide | Markdown master | Status |
|---|---|---|---|
| I — Crisp Set Theory and Logic | `modules/module-1.html` | `Module_1_Exam_Essentials.md` | in progress |
| II — Mathematical Relations | `modules/module-2.html` | `Module_2_Exam_Essentials.md` | first pass complete |
| III — Functions | `modules/module-3.html` | `Module_3_Exam_Essentials.md` | in progress |

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

## Remaining work / exact next action

1. Build Module III first pass (`module-3.html` + `Module_3_Exam_Essentials.md`) and publish.
2. Build Module I first pass (`module-1.html` + `Module_1_Exam_Essentials.md`) and publish.
3. Remove the `/dsgt/modules/module-1` → `/dsgt` redirects from `vercel.json` so the Module 1 page
   is reachable.
4. Verify all three routes and the DSGT landing page on production.
5. Only then consider optional additions (CNF/DNF, more practice).

## Deployment log

- Module II: pending commit.
