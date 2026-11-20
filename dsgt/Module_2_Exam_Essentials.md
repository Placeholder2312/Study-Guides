# DSGT Module 2 — Mathematical Relations (Selective Exam Essentials)

**Course:** Discrete Structures and Graph Theory (2023112) · B.E. CSE (AI & ML) · Sem III · NEP 2020
**Module II · 8 teaching hours · CO2**
**Status:** selective coverage — not a complete module guide.

This guide teaches a deliberately small set of Module 2 topics properly. Everything is prescribed
syllabus content unless labelled as practice.

**Covered:** relation definition and representation · the four properties · equivalence relations
and equivalence classes · transitive closure and Warshall's algorithm · partial orders, posets,
meet and join, and how to decide whether a poset is a lattice.

**Deliberately skipped:** detailed types of lattices (bounded, complemented, distributive proofs) ·
sublattice proofs · extended chain/antichain theory · relation composition beyond Warshall ·
drawing Hasse diagrams and digraphs (separate diagram task) · real-world application essays.

---

## 1. Relations: definition, notation, representation

**Teacher's definition (Module 2 PPT, slide 8).** A relation in mathematics is a subset of the
Cartesian product of two sets. If X and Y are sets, X × Y is the set of all ordered pairs (x, y)
with x ∈ X and y ∈ Y. A relation R from X to Y is any subset of X × Y.

**Simple meaning.** A relation is a rule that links elements of one set to elements of another set
(or of the same set). Each link is recorded as an **ordered pair**. Order matters: (1, 2) ≠ (2, 1).

**Formal definition.** A binary relation R from A to B is a subset of A × B. If (a, b) ∈ R we write
**a R b** and say "a is related to b".

**Notation.**

| Symbol | Read as | Meaning |
|---|---|---|
| A × B | A cross B | all ordered pairs (a, b) with a ∈ A, b ∈ B |
| (a, b) ∈ R | the pair belongs to R | the link from a to b is in the relation |
| a R b | a is related to b | the same statement in infix form |
| R ⊆ A × A | R is a relation on A | both coordinates come from A |
| D_R(R) | domain of R | first coordinates that actually occur |
| R_R(R) | range of R | second coordinates that actually occur |
| R⁻¹ | inverse of R | reverse every pair |

**Domain versus range — the trap.** The domain is not automatically A and the range is not
automatically B. They are only the coordinates that actually occur. If A = {1, 2, 3} and
R = {(1, 5)}, the domain is {1}, not A.

**Four ways to write the same relation**

- **Roster form:** list the pairs.
- **Set-builder form:** state the rule, e.g. R = {(a, b) : b = 2a}.
- **Matrix form:** rows are elements of A, columns are elements of B; write 1 where the pair is in R.
- **Digraph:** vertices are elements, arrows are pairs. You should be able to read one; drawing one
  belongs to the separate diagram task.

### Worked example — relation, domain, range, inverse, matrix

Let A = {1, 2, 3}, B = {2, 4, 6}, and R = {(a, b) : b = 2a}.

1. Build the pairs by computing 2a for each a: **R = {(1, 2), (2, 4), (3, 6)}**.
2. Domain = first coordinates = {1, 2, 3}. Range = second coordinates = {2, 4, 6}.
3. Inverse = reverse each pair: **R⁻¹ = {(2, 1), (4, 2), (6, 3)}**.
4. Matrix: rows 1, 2, 3; columns 2, 4, 6.

| M_R | 2 | 4 | 6 |
|---|---|---|---|
| **1** | 1 | 0 | 0 |
| **2** | 0 | 1 | 0 |
| **3** | 0 | 0 | 1 |

### Worked example — a relation on one set (teacher's Example 1.12)

A = {1, 2, 3, 4}, R = {(a, b) : a divides b}. Go through each a and keep its multiples in A:

**R = {(1,1), (1,2), (1,3), (1,4), (2,2), (2,4), (3,3), (4,4)}.**

Every element divides itself, so all four diagonal pairs occur. This is the standard partial order.

### Common mistakes

- Writing the domain as A without checking.
- Reversing only some pairs when forming R⁻¹.
- Forgetting that a relation on A is a subset of A × A.
- Reading matrix columns as A; rows are the first set, columns the second.

**Quick check 1.** A = {2, 3, 4}, B = {4, 6, 8}, R = {(a, b) : b = 2a}. Write R, its domain,
range, inverse and matrix. *(Answer Q1.)*

---

## 2. Properties of relations

From here R is a relation **on a set A**, so R ⊆ A × A.

**Teacher's definitions (slides 35, 41, 52, 53, 54).**

- **Reflexive:** (a, a) ∈ R for every a ∈ A.
- **Symmetric:** (a, b) ∈ R ⇒ (b, a) ∈ R for all a, b ∈ A.
- **Antisymmetric:** (a, b) ∈ R and (b, a) ∈ R ⇒ a = b for all a, b ∈ A.
- **Transitive:** (a, b) ∈ R and (b, c) ∈ R ⇒ (a, c) ∈ R for all a, b, c ∈ A.

| Property | Formal statement | How to test it | Typical example |
|---|---|---|---|
| Reflexive | (a, a) ∈ R for every a ∈ A | every element must appear as (a, a); one missing loop fails it | "is equal to", ≤, divides |
| Symmetric | (a, b) ∈ R ⇒ (b, a) ∈ R | for every pair look for its reverse; one one-way pair fails it | "is a sibling of", "same age as" |
| Antisymmetric | (a, b), (b, a) ∈ R ⇒ a = b | look for a ≠ b with both directions; one such pair fails it | ≤, divides, "subset of" |
| Transitive | (a, b), (b, c) ∈ R ⇒ (a, c) ∈ R | for every chain a → b → c check the shortcut a → c | ≤, divides, "ancestor of" |

### Symmetric versus antisymmetric

They are **not opposites**.

- **Symmetric** says: whenever a link goes one way, the reverse must exist. It forbids one-way links.
- **Antisymmetric** says: if both directions exist, the endpoints are the same element. It forbids
  two-way links between different elements.
- A relation can be **both**: equality is symmetric and antisymmetric.
- A relation can be **neither**: on {1,2,3}, R = {(1,2), (2,1), (2,3)} is not symmetric (no (3,2))
  and not antisymmetric ((1,2) and (2,1) with 1 ≠ 2).

Remember: *symmetric = both directions always; antisymmetric = both directions only for the same element.*

### Systematic procedure

1. Write R in roster form and list the elements of A.
2. **Reflexive?** Tick off (1,1), (2,2), … for every element; name the first missing loop.
3. **Symmetric?** For each (a, b) with a ≠ b, check whether (b, a) is present.
4. **Antisymmetric?** For each a ≠ b, check both directions do not occur together.
5. **Transitive?** For each (a, b), take every pair starting at b and check the shortcut.
6. **Conclude** with exactly the properties that hold.

### Worked example A — an equivalence relation

A = {1, 2, 3, 4}, R = {(1,1), (1,2), (2,1), (2,2), (3,3), (4,4)}.

- **Reflexive:** all of (1,1), (2,2), (3,3), (4,4) present. ✓
- **Symmetric:** the only off-diagonal pairs are (1,2) and (2,1). ✓
- **Antisymmetric:** (1,2) and (2,1) both present with 1 ≠ 2. ✗
- **Transitive:** (1,2)(2,1) → (1,1) present; (2,1)(1,2) → (2,2) present. ✓

Conclusion: reflexive, symmetric, transitive — an equivalence relation, not antisymmetric.

**Answer-sheet form.** Definition, then a present/absent check, then a one-line conclusion, for each
property. Four short blocks.

### Worked example B — a partial order

A = {1, 2, 3, 6}, x R y means x divides y.

R = {(1,1), (1,2), (1,3), (1,6), (2,2), (2,6), (3,3), (3,6), (6,6)}.

- **Reflexive:** 1|1, 2|2, 3|3, 6|6. ✓
- **Symmetric:** (1,2) ∈ R but (2,1) ∉ R. ✗
- **Antisymmetric:** x|y and y|x force x = y for positive integers. ✓
- **Transitive:** x|y and y|z force x|z; e.g. (1,2)(2,6) → (1,6) present. ✓

Conclusion: reflexive, antisymmetric, transitive — a partial order.

### Common mistakes

- Testing symmetry on (1,1); a diagonal pair proves nothing.
- Claiming "not symmetric, therefore antisymmetric".
- Checking only one chain for transitivity.
- Testing reflexivity only on elements that appear in some pair.

**Quick check 2.** A = {1,2,3,4}, R = {(1,1),(2,2),(3,3),(4,4),(1,3),(3,1)}. Test all four
properties. *(Answer Q2.)*

---

## 3. Equivalence relations and equivalence classes

**Definition (slide 55).** R on A is an **equivalence relation** if it is reflexive, symmetric and
transitive. If R is an equivalence relation and a ∈ A, the **equivalence class** of a is

> [a] = {x ∈ A : (x, a) ∈ R}

Equivalence classes split A into non-overlapping blocks; every element lies in exactly one class.

**Recognition.** "Same number of sides", "same remainder", "same city", "is similar to",
"is congruent to", "same blood group" all signal an equivalence relation. The question asks you to
verify three properties and list classes.

### Verified University question — Summer 2026 Q.1(a), 5 marks

A digital geometry platform groups polygons by number of sides. A is the set of all polygons and
R = {(P₁, P₂) : P₁ and P₂ have the same number of sides}. Analyse whether R is an equivalence
relation, verify the properties, and construct classes for triangles, quadrilaterals and pentagons.

**Solution.**

1. **Reflexive.** Any polygon P has the same number of sides as itself, so (P, P) ∈ R. ✓
2. **Symmetric.** If P₁ and P₂ have the same number of sides, then P₂ and P₁ do too, so
   (P₂, P₁) ∈ R. ✓
3. **Transitive.** If P₁, P₂ have n sides and P₂, P₃ have n sides, then P₁ and P₃ both have n
   sides, so (P₁, P₃) ∈ R. ✓
4. **Conclusion.** Reflexive, symmetric, transitive ⇒ R is an equivalence relation on A.
5. **Classes.** [triangle] = all 3-sided polygons; [quadrilateral] = all 4-sided polygons;
   [pentagon] = all 5-sided polygons.
6. **Interpretation.** The relation turns a messy collection into labelled buckets. The platform can
   compute one number (side count) and use it as a class label. Retrieval is "find the class, then
   search inside it", and no polygon is filed twice.

### Finding classes from a roster

1. Start with the smallest unplaced element of A.
2. Collect every element related to it.
3. That is one class; cross those elements off.
4. Repeat until A is exhausted.
5. Check the classes are disjoint and their union is A.

### Worked example — classes from a finite relation (teacher's example)

A = {1,2,3,4,5,6} and

R = {(1,1),(1,5),(2,2),(2,3),(2,6),(3,2),(3,3),(3,6),(4,4),(5,1),(5,5),(6,2),(6,3),(6,6)}.

- Start at 1: pairs involving 1 are (1,1), (1,5), (5,1), (5,5) ⇒ **[1] = {1, 5}**.
- Next unplaced: 2. Pairs are (2,2), (2,3), (2,6), (3,2), (3,3), (3,6), (6,2), (6,3), (6,6)
  ⇒ **[2] = {2, 3, 6}**, so [3] = [6] = {2, 3, 6}.
- Next unplaced: 4 ⇒ **[4] = {4}**.

> [1] = [5] = {1,5} · [2] = [3] = [6] = {2,3,6} · [4] = {4}

Check: disjoint, and together contain 1…6. There are **three** classes, not six; [2], [3], [6] are
three names for the same class.

### Common mistakes

- "Reflexive because (1,1) is present" while ignoring other elements.
- Confusing the number of classes with the number of elements.
- Listing overlapping classes.
- Omitting the sentence "Hence R is an equivalence relation."

**Quick check 3.** A = {1,…,6}, a R b means a ≡ b (mod 3). Prove R is an equivalence relation and
find all classes. *(Answer Q3.)*

---

## 4. Transitive closure and Warshall's algorithm

**Definitions (slides 63, 73).** R is **transitive** if (a, b) ∈ R and (b, c) ∈ R always force
(a, c) ∈ R. The **transitive closure** of R is the smallest transitive relation containing R —
equivalently, all pairs (a, b) such that a directed path of length ≥ 1 runs from a to b.

The closure of a relation on n elements is an n × n Boolean matrix T with T_ij = 1 if a path runs
from i to j, else 0.

| Term | Plain meaning |
|---|---|
| Path of length 1 | a direct pair (a, b) in R |
| Path of length 2 | a → x → b for some intermediate x |
| Reachability | a path of some length ≥ 1 from a to b |
| Transitive closure R⁺ | all reachable pairs |
| Reflexive–transitive closure R* | R⁺ plus every (a, a) |

### The update rule

> W_ij⁽ᵏ⁾ = W_ij⁽ᵏ⁻¹⁾ ∨ ( W_ik⁽ᵏ⁻¹⁾ ∧ W_kj⁽ᵏ⁻¹⁾ )

W = matrix · i = row (start) · j = column (end) · k = the intermediate vertex currently allowed ·
∨ = OR · ∧ = AND.

Read it as: *i reaches j if it already did, or if i reaches the current intermediate k and k reaches j.*

**What k means.** After round k the matrix records every path whose intermediate vertices come only
from the first k elements. Round 1 allows stopovers at vertex 1 only; round 2 allows vertices 1 and 2;
after n rounds every intermediate is allowed, which is the full closure. That is why the outer loop
must run over all vertices in order.

### Procedure

1. Fix an order for the elements; write W⁽⁰⁾ with 1 for each direct pair.
2. For k = first … last element: find rows i with a 1 in column k and columns j with a 1 in row k;
   put 1 in every (i, j); record the new matrix and the changed entries.
3. After the last round, read the pairs off the final matrix.
4. Sanity-check by tracing two or three actual paths.

### Verified University question — Summer 2026 Q.3(a), 8 marks

V = {a, b, c, d}, R = {(a, b), (b, d), (d, c), (d, a)}. Find the transitive closure.

**W⁽⁰⁾**

| | a | b | c | d |
|---|---|---|---|---|
| **a** | 0 | 1 | 0 | 0 |
| **b** | 0 | 0 | 0 | 1 |
| **c** | 0 | 0 | 0 | 0 |
| **d** | 1 | 0 | 1 | 0 |

**k = a.** Column a has a 1 in row d; row a has a 1 at b ⇒ add (d, b).

| W⁽ᵃ⁾ | a | b | c | d |
|---|---|---|---|---|
| **a** | 0 | 1 | 0 | 0 |
| **b** | 0 | 0 | 0 | 1 |
| **c** | 0 | 0 | 0 | 0 |
| **d** | 1 | 1 | 1 | 0 |

**k = b.** Column b has 1s in rows a, d; row b has a 1 at d ⇒ add (a, d) and (d, d). The (d, d)
entry is the circular route d → a → b → d.

| W⁽ᵇ⁾ | a | b | c | d |
|---|---|---|---|---|
| **a** | 0 | 1 | 0 | 1 |
| **b** | 0 | 0 | 0 | 1 |
| **c** | 0 | 0 | 0 | 0 |
| **d** | 1 | 1 | 1 | 1 |

**k = c.** Column c has a 1 only in row d, and row c has no 1s ⇒ no change. This already shows c is a
dead end.

**k = d.** Column d has 1s in rows a, b, d; row d has 1s in every column ⇒ rows a, b, d become all 1.

| W⁽ᵈ⁾ | a | b | c | d |
|---|---|---|---|---|
| **a** | 1 | 1 | 1 | 1 |
| **b** | 1 | 1 | 1 | 1 |
| **c** | 0 | 0 | 0 | 0 |
| **d** | 1 | 1 | 1 | 1 |

**Final answer.**

> R⁺ = {(a,a),(a,b),(a,c),(a,d),(b,a),(b,b),(b,c),(b,d),(d,a),(d,b),(d,c),(d,d)}

Twelve pairs. Row c is entirely zero: c is related to nothing, not even itself.

**Independent check by paths.** The cycle a → b → d → a lets a, b, d return to themselves, hence the
three self-pairs. From a: a → b → d → c reaches c. From b: b → d → a reaches a; b → d → c reaches c.
From d: d → a → b reaches b. From c: no outgoing edge. All twelve entries are accounted for.

**Direct, layover, circular.** Direct: (a,b), (b,d), (d,c), (d,a). Layover examples: (a,d), (a,c),
(b,a), (b,c), (d,b). Circular: (a,a), (b,b), (d,d).

**Note on the diagonal.** This follows your lecture convention of paths of length ≥ 1. If the matrix
is initialised with 1s on the diagonal instead, (c,c) also appears and every diagonal entry is 1.
State which convention you used; do not mix them.

### Common mistakes

- Using updated values where round k−1 is required.
- Skipping rounds because nothing changes — write the matrix for method marks.
- Adding a pair because a path exists backwards; paths are directed.
- Reading the closure off the original matrix.
- Forgetting that a vertex on a cycle gets a self-pair and a vertex off a cycle does not.

**Quick check 4.** A = {a,b,c,d}, R = {(a,b),(b,a),(b,c),(c,d),(d,a)}. Apply Warshall, showing each
round. *(Answer Q4.)*

---

## 5. Partial orders, posets and lattices

**Definitions.** R on A is a **partial order** if it is reflexive, antisymmetric and transitive; the
pair (A, R) is a **poset**.

- **a ≤ b** means (a, b) ∈ R. Under divisibility, a ≤ b means a divides b.
- **Minimal element:** nothing in A is strictly below it. **Maximal:** nothing strictly above it.
- **Least element:** below every element. **Greatest:** above every element.
- **Lower bound of B:** below every element of B. The largest is the **greatest lower bound (meet, ∧)**.
- **Upper bound of B:** above every element of B. The smallest is the **least upper bound (join, ∨)**.
- **Lattice:** every pair of elements has a meet and a join inside the set.

**Why divisibility is a partial order.** x|x; x|y and y|x ⇒ x = y; x|y and y|z ⇒ x|z. It is only
*partial* because not every pair is comparable: 2 does not divide 3 and 3 does not divide 2.

**Meet and join under divisibility.** When the poset is divisibility on positive integers:

> meet(a, b) = gcd(a, b) · join(a, b) = lcm(a, b)

This is a shortcut, not a definition. If gcd or lcm is not an element of A, that meet or join does not
exist in the poset and the poset is not a lattice.

### Verified University question — Summer 2026 Q.3(b), 7 marks

A = {1, 2, 3, 6, 12, 24, 36, 72} ordered by divisibility.

**Part 1 — all ordered pairs.** For each x, list elements of A divisible by x:

| x | divisible elements | count |
|---|---|---|
| 1 | 1, 2, 3, 6, 12, 24, 36, 72 | 8 |
| 2 | 2, 6, 12, 24, 36, 72 | 6 |
| 3 | 3, 6, 12, 24, 36, 72 | 6 |
| 6 | 6, 12, 24, 36, 72 | 5 |
| 12 | 12, 24, 36, 72 | 4 |
| 24 | 24, 72 | 2 |
| 36 | 36, 72 | 2 |
| 72 | 72 | 1 |

34 pairs in total:

R = {(1,1),(1,2),(1,3),(1,6),(1,12),(1,24),(1,36),(1,72),
(2,2),(2,6),(2,12),(2,24),(2,36),(2,72),
(3,3),(3,6),(3,12),(3,24),(3,36),(3,72),
(6,6),(6,12),(6,24),(6,36),(6,72),
(12,12),(12,24),(12,36),(12,72),
(24,24),(24,72),(36,36),(36,72),(72,72)}.

**Part 2 — Hasse diagram content (described in words, not drawn).** One dot per element; y above x
and joined exactly when y **covers** x (x|y, x ≠ y, no z with x|z|y). Covering pairs:

> 1–2, 1–3, 2–6, 3–6, 6–12, 12–24, 12–36, 24–72, 36–72

Levels: 1 | 2, 3 | 6 | 12 | 24, 36 | 72. A line means "covers", not "divides".

**Part 3 — is it a lattice?**

| Pair | gcd (meet) | in A? | lcm (join) | in A? |
|---|---|---|---|---|
| (2, 3) | 1 | yes | 6 | yes |
| (6, 12) | 6 | yes | 12 | yes |
| (12, 24) | 12 | yes | 24 | yes |
| (12, 36) | 12 | yes | 36 | yes |
| (24, 36) | 12 | yes | 72 | yes |
| (24, 72) | 24 | yes | 72 | yes |
| (2, 72) | 2 | yes | 72 | yes |
| (1, 72) | 1 | yes | 72 | yes |

The critical pair is (24, 36): meet 12, join 72, both in A. Every pair behaves the same way because A
is closed under gcd and lcm for these elements.

**Conclusion.** Every pair has a meet and a join in A ⇒ (A, |) is a lattice. It is bounded: 1 is the
least element, 72 the greatest.

**Justification sentence.** "For (24, 36), meet = gcd(24,36) = 12 ∈ A and join = lcm(24,36) = 72 ∈ A.
Since gcd and lcm of every pair lie in A, the poset is a lattice."

### The counterexample to memorise

S = {2, 3, 4, 6} under divisibility. For (3, 4): gcd = 1 ∉ S and lcm = 12 ∉ S. So (3, 4) has neither
a meet nor a join inside S ⇒ (S, |) is a poset but **not a lattice**. A poset is never automatically a
lattice.

**Chain and antichain.** A **chain** is a subset whose elements are pairwise comparable, e.g.
{1, 2, 6, 12, 24, 72}. An **antichain** is a subset with no two distinct elements comparable, e.g.
{24, 36} or {2, 3}.

### Common mistakes

- Assuming poset ⇒ lattice.
- Computing gcd and lcm but not checking membership in A.
- Confusing minimal with least.
- Drawing an edge for every divisibility pair instead of only covering pairs.
- Omitting diagonal pairs when listing R for a partial order.

**Quick check 5.** (a) A = {1,2,4,8,16} under divisibility: lattice? (b) S = {2,3,4,6}: lattice?
Justify with a meet and a join. *(Answer Q5.)*

---

## Practice questions

**Q1.** A = {2,3,4}, B = {4,6,8}, R = {(a,b) : b = 2a}. Write R, domain, range, R⁻¹ and M_R.

**Q2.** A = {1,2,3,4}, R = {(1,1),(2,2),(3,3),(4,4),(1,3),(3,1)}. Test all four properties.

**Q3.** A = {1,…,6}, a R b iff a ≡ b (mod 3). Prove R is an equivalence relation; list classes.

**Q4.** A = {a,b,c,d}, R = {(a,b),(b,a),(b,c),(c,d),(d,a)}. Apply Warshall; give the closure.

**Q5.** (a) A = {1,2,4,8,16} under divisibility: lattice? (b) S = {2,3,4,6}: lattice? Give reasons.

**Q6.** *(Winter 2025 Q.3(a), 8 marks)* Modules M1…M5 with prerequisite relation
R = {(1,2),(2,3),(3,4),(4,5),(1,1),(3,3),(5,5)}. Apply Warshall, list what each Mi unlocks, and
identify root and terminal modules.

**Q7.** *(Winter 2025 Q.3(b), 7 marks)* S = {1, 2, 4, 8, 16} TB with a | b. List all pairs, state the
covering pairs, check whether S is a lattice, and identify least and greatest elements.

**Q8.** For A = {1,2,3,6,12,24,36,72} under divisibility, find meet and join of (a) 6 and 36,
(b) 24 and 72, (c) explain what happens if you try to use 8, which is not in A.

**Q9.** Explain the difference between symmetric and antisymmetric relations, with one relation on
{1,2,3} that is symmetric but not antisymmetric and one that is antisymmetric but not symmetric.

**Q10.** A = {1,2,3,4,6,12} under divisibility. Find minimal, maximal, least and greatest elements.
Is it a lattice?

---

## Answer key

### Q1

R = {(2,4), (3,6), (4,8)}. Domain {2,3,4}. Range {4,6,8}. R⁻¹ = {(4,2), (6,3), (8,4)}.

| M_R | 4 | 6 | 8 |
|---|---|---|---|
| **2** | 1 | 0 | 0 |
| **3** | 0 | 1 | 0 |
| **4** | 0 | 0 | 1 |

### Q2

Reflexive: yes, all diagonal pairs present. Symmetric: yes, (1,3) and (3,1) occur together.
Antisymmetric: no, because (1,3) and (3,1) occur with 1 ≠ 3. Transitive: yes —
(1,3)(3,1) → (1,1) and (3,1)(1,3) → (3,3), both present.

So R is an equivalence relation with [1] = [3] = {1,3}, [2] = {2}, [4] = {4}.

### Q3

Reflexive: 3 | (a − a) = 0. Symmetric: 3 | (a − b) ⇒ 3 | (b − a). Transitive:
3 | (a − b) and 3 | (b − c) ⇒ 3 | (a − c). Hence an equivalence relation.

Classes: [1] = [4] = {1,4} (remainder 1); [2] = [5] = {2,5} (remainder 2);
[3] = [6] = {3,6} (remainder 0).

### Q4 — Warshall, all four rounds

W⁽⁰⁾:

| | a | b | c | d |
|---|---|---|---|---|
| **a** | 0 | 1 | 0 | 0 |
| **b** | 1 | 0 | 1 | 0 |
| **c** | 0 | 0 | 0 | 1 |
| **d** | 1 | 0 | 0 | 0 |

**k = a:** column a has 1s in rows b, d; row a has a 1 at b ⇒ add (b,b), (d,b).

| W⁽ᵃ⁾ | a | b | c | d |
|---|---|---|---|---|
| **a** | 0 | 1 | 0 | 0 |
| **b** | 1 | 1 | 1 | 0 |
| **c** | 0 | 0 | 0 | 1 |
| **d** | 1 | 1 | 0 | 0 |

**k = b:** column b has 1s in rows a, b, d; row b has 1s in columns a, b, c ⇒ add (a,a), (a,c),
(d,a), (d,c).

| W⁽ᵇ⁾ | a | b | c | d |
|---|---|---|---|---|
| **a** | 1 | 1 | 1 | 0 |
| **b** | 1 | 1 | 1 | 0 |
| **c** | 0 | 0 | 0 | 1 |
| **d** | 1 | 1 | 1 | 0 |

**k = c:** column c has 1s in rows a, b, d; row c has a 1 at d ⇒ add (a,d), (b,d), (d,d).

| W⁽ᶜ⁾ | a | b | c | d |
|---|---|---|---|---|
| **a** | 1 | 1 | 1 | 1 |
| **b** | 1 | 1 | 1 | 1 |
| **c** | 0 | 0 | 0 | 1 |
| **d** | 1 | 1 | 1 | 1 |

**k = d:** column d has 1s in every row; row d has 1s in every column ⇒ row c gains a, b, c.

**Final:** all sixteen pairs. R⁺ = A × A. The relation is strongly connected: a → b → a is already a
two-step cycle, so every element reaches every element including itself.

### Q5

(a) Lattice. For powers of 2, gcd is the smaller and lcm the larger, both in A. Example:
gcd(4,8) = 4, lcm(4,8) = 8. It is a chain, and every chain is a lattice.

(b) Not a lattice. gcd(3,4) = 1 ∉ S and lcm(3,4) = 12 ∉ S, so (3,4) has neither meet nor join in S.

### Q6 — Winter 2025 modules

Chain 1 → 2 → 3 → 4 → 5 with loops at 1, 3, 5. Closure matrix:

| | 1 | 2 | 3 | 4 | 5 |
|---|---|---|---|---|---|
| **1** | 1 | 1 | 1 | 1 | 1 |
| **2** | 0 | 0 | 1 | 1 | 1 |
| **3** | 0 | 0 | 1 | 1 | 1 |
| **4** | 0 | 0 | 0 | 0 | 1 |
| **5** | 0 | 0 | 0 | 0 | 1 |

R⁺ = {(1,1),(1,2),(1,3),(1,4),(1,5),(2,3),(2,4),(2,5),(3,3),(3,4),(3,5),(4,5),(5,5)} — 13 pairs.

Unlocks: M1 → M2, M3, M4, M5. M2 → M3, M4, M5. M3 → M4, M5. M4 → M5. M5 → nothing.
Root: M1. Terminal: M5. M2 and M4 have no self-loop, so (2,2) and (4,4) are absent.

### Q7 — Winter 2025 storage plans

S = {1, 2, 4, 8, 16}. Every smaller power divides every larger one, giving 15 pairs.
Covers: 1–2, 2–4, 4–8, 8–16 (one vertical chain).
Lattice: yes — gcd and lcm of two powers of 2 are the smaller and larger, both in S.
Least 1, greatest 16; bounded.

### Q8

(a) gcd(6,36) = 6, lcm = 36. Meet 6, join 36.
(b) gcd(24,72) = 24, lcm = 72. Meet 24, join 72.
(c) 8 ∉ A, so 8 is not an element of the poset and has no meet or join *in A*. Always check
membership before computing.

### Q9

Symmetric: every one-way link must come back. Antisymmetric: a two-way link forces the endpoints to
be equal. Symmetric forbids one-way links; antisymmetric forbids two-way links between different
elements. Neither implies the other.

Symmetric but not antisymmetric: {(1,1),(1,2),(2,1),(2,2),(3,3)}.
Antisymmetric but not symmetric: {(1,1),(1,2),(2,2),(3,3)} (the "≤" relation).

### Q10

Least = 1, greatest = 12; the only minimal element is 1 and the only maximal is 12.
Lattice: yes — for (4,6), gcd = 2 ∈ A and lcm = 12 ∈ A; for (3,4), gcd = 1 ∈ A and lcm = 12 ∈ A;
all other pairs likewise. Hence every pair has meet and join in A.

---

## Last-minute revision sheet

**Definitions.** Relation = subset of A × B · domain/range = coordinates that occur · reflexive =
(a,a) for all a · symmetric = reverse of every pair · antisymmetric = both directions only for equal
elements · transitive = shortcuts exist · equivalence = reflexive + symmetric + transitive ·
class [a] = all elements related to a · closure = all reachable pairs · partial order = reflexive +
antisymmetric + transitive · poset = set + partial order · lattice = every pair has meet and join.

**Procedures.** Properties: roster → reflexive → symmetric → antisymmetric → transitive → conclude.
Equivalence: three labelled proofs + conclusion. Classes: unplaced element → collect → cross off →
repeat → check disjoint and covering. Warshall: W⁽⁰⁾ → rounds → record changes → read pairs.
Lattice: every pair → gcd and lcm → both in A? → witness if not → conclusion.

**Checks before handing in.** Elements listed before reflexivity? Named counterexample for each
rejected property? A matrix for every k? gcd/lcm checked for membership? Conclusion sentence written?

---

## Sources, verification and coverage

**Teacher material.** Mrs. Shamal Bagal, *Module 2: Mathematical Relations* (PowerPoint, 76 slides):
definitions of relation, binary relation, matrix representation, inverse, the four properties,
equivalence relations, closures, Warshall's algorithm, the equivalence-class example. Teacher's
examples are reproduced from slides 8, 12, 35–54, 55, 62, 72 and 73–76.

**Official scope.** University of Mumbai DSGT (2023112), Module II — Mathematical Relations, 8 hours,
CO2. Prescribed: definition and representation, properties, equivalence relations and classes,
closures, Warshall's algorithm, partial orders, posets, Hasse diagrams, chains and antichains,
lattices, types of lattices, sublattices. Self-learning: applications in databases, economics, social
networks, sports, medical diagnosis and weather.

**Questions.** Summer 2026 Q.1(a), Q.3(a), Q.3(b) — from the supplied paper, data preserved.
Winter 2025 Q.3(a), Q.3(b) — read directly from the scanned paper, page 3 of 4.
Practice Q1–Q5 and Q8–Q10 are written for this guide and are not claimed to be university questions.

**Verification performed.** Every Warshall matrix was recomputed with a Boolean-matrix implementation;
the Summer 2026 closure (12 pairs) and Winter 2025 closure (13 pairs) were checked pair by pair
against explicit paths. All 28 pairs of the divisibility poset were checked programmatically: every
gcd and lcm lies in A, which is why the answer is "lattice". Equivalence classes were re-derived and
checked for disjointness and coverage.

**Not covered.** Types of lattices beyond the one-line "bounded" remark; sublattice proofs; closure
theory other than transitive closure; relation composition beyond Warshall; drawing Hasse diagrams and
digraphs; application essays. Deliberate omissions, not oversights.
