# DSGT Module 1 — Crisp Set Theory and Logic (Selective Exam Essentials)

**Course:** Discrete Structures and Graph Theory (2023112) · B.E. CSE (AI & ML) · Sem III · NEP 2020
**Module I — 7 teaching hours · CO1**
**Status:** selective coverage — not a complete module guide.

Module 1 is the biggest module: set theory, propositional logic, predicate logic and proof technique.
This guide teaches the examinable core in revision order and says plainly what it leaves out.

**Covered:** set vocabulary and notation · subsets and power sets · set operations and laws ·
Cartesian product · partitions · proving set identities · truth tables · logical equivalence with two
full university proof questions · tautology, contradiction, contingency · CNF and DNF · predicates,
quantifiers and their negations · mathematical induction with the whole
Summer 2026 question · a one-page comparison of the other proof methods.

**Deliberately skipped:** Venn-diagram drawing, membership tables for four or more sets, PROLOG/LISP
expert systems, non-classical logics, cardinality of infinite sets, and long proof-by-exhaustion case
lists. These are self-learning or extension material.

---

## 1. Sets: the vocabulary you must have

**Teacher's definitions (Module 1 PPT, slides 4–15).** A **set** is a well-defined collection of
distinct objects, written with members separated by commas inside curly brackets { }. Its objects are
**elements** or members, written with lowercase letters.

If A = {a, b} then a **belongs to** A, written a ∈ A; an element not in A satisfies c ∉ A. The number of
elements is the **cardinality**, written n(A) or |A|. For A = {1,2,3,4}, |A| = 4. The three dots … are an
ellipsis meaning "continue in the same pattern"; C = {a, b, c, …, z} has 26 elements.

**Simple meaning.** A set is a bag with no order and no duplicates. {2,4,6}, {6,2,4} and {2,4,4,6} are
all the same set.

### The three ways to write a set

| Form | What it is | Example (whole numbers below 8) |
|---|---|---|
| Statement / semantic | a sentence describing the members | {the set of whole numbers less than 8} |
| Roster | the members listed inside { } | {0,1,2,3,4,5,6,7} |
| Set-builder | a rule every member satisfies | {x \| x is a whole number and x < 8} |

The vertical bar is read "such that". Many textbooks write a colon instead: {x : x is even}.

### Symbols

| Symbol | Read as | Meaning |
|---|---|---|
| ∈ / ∉ | belongs to / does not belong | a ∈ A: a is an element of A |
| \|A\| or n(A) | cardinality | the number of distinct elements |
| ∅ | empty set | the set with no elements, ∅ = { } |
| U | universal set | everything under discussion |
| A ⊆ B | subset | every element of A is in B |
| A ⊂ B | proper subset | A ⊆ B and A ≠ B |
| A′ | complement | U − A |

**Formal definition — subset.**

> A ⊆ B ⟺ ∀x (x ∈ A → x ∈ B)

A is a **proper subset** of B, written A ⊂ B, when A ⊆ B and at least one element of B is not in A. Two
sets are **equal** when A ⊆ B and B ⊆ A.

That single line does most of the work in this module. "Subset" is a quantified implication, so it is
proved like one and negated like one. To show A ⊄ B you must produce one element in A and not in B.

**Facts worth memorising.**

1. ∅ ⊆ A for every set A, including A = ∅.
2. A ⊆ A for every A.
3. If A ⊆ B and B ⊆ C then A ⊆ C (transitive).
4. ∅ ∈ {∅}, but ∅ ∉ ∅. The empty set contains nothing at all.
5. If |A| = n then A has 2ⁿ subsets.

### Power set

**Definition (asked verbatim in the IAT sample and the prelim bank).** The **power set** of A, written
P(A), is the set of all subsets of A:

> P(A) = { X | X ⊆ A }

Every element of P(A) is itself a set, and |P(A)| = 2ⁿ when |A| = n.

**How to recognise the question.** "Write the power set", "find P(A) and its cardinality", "how many
subsets does A have" — all the same task. The trap is the two forgotten members: ∅ and A itself.

### Worked example — the power set of a three-element set

A = {a, b, c}, so |A| = 3 and P(A) has 8 members. Build them by size so nothing is missed or repeated:

- 0 elements: ∅
- 1 element: {a}, {b}, {c}
- 2 elements: {a,b}, {a,c}, {b,c}
- 3 elements: {a,b,c}

> P(A) = { ∅, {a}, {b}, {c}, {a,b}, {a,c}, {b,c}, {a,b,c} }

Count 1 + 3 + 3 + 1 = 8. ✓

**Exam presentation.** Write 2³ = 8 first, group the subsets by size, then the final set.

### Worked example — the two edge cases

For A = ∅ the only subset is ∅, so P(∅) = {∅} and |P(∅)| = 2⁰ = 1. Note ∅ ≠ {∅}: the left has no
elements, the right has one. For A = {∅}, P({∅}) = {∅, {∅}} and |P({∅})| = 2.

### Common mistakes

- Writing a ∈ A when you mean {a} ⊆ A.
- Using ⊂ when the sets are equal. {1,2} ⊂ {1,2} is false.
- Leaving ∅ out of the power set, or leaving out A itself — that gives 2ⁿ − 2 subsets.
- Saying |∅| = 1. The empty set has zero elements; {∅} has one.
- Confusing equivalent sets (same cardinality) with equal sets (same elements).
- Writing {a, b, a} and calling the cardinality 3. Duplicates collapse.

**Quick check 1.** (a) Write P({a,b,c,d}) and give |P(A)|. *(IAT sample Q10.)*
(b) True or false with a reason: (i) ∅ ∈ {∅}; (ii) ∅ ⊆ {∅}; (iii) {∅} ⊆ ∅; (iv) {1,2} ⊂ {1,2,3}.
(c) Write the even integers between 1 and 11 in roster and set-builder form. *(Answer Q1.)*

---

## 2. Set operations and the laws of sets

**Teacher's definitions (slides 18–19).** **Union** A ∪ B lists every element in A, in B, or both.
**Intersection** A ∩ B lists the common elements. **Difference** A − B lists the elements of A not in B.
**Complement** A′ lists the elements of U not in A. **Symmetric difference** A △ B lists the elements in
exactly one of A and B:

> A △ B = (A ∪ B) − (A ∩ B) = (A − B) ∪ (B − A)

| Operation | Set-builder definition | A = {1,2,3,4}, B = {3,4,5,6} |
|---|---|---|
| A ∪ B | {x \| x ∈ A or x ∈ B} | {1,2,3,4,5,6} |
| A ∩ B | {x \| x ∈ A and x ∈ B} | {3,4} |
| A − B | {x \| x ∈ A and x ∉ B} | {1,2} |
| B − A | {x \| x ∈ B and x ∉ A} | {5,6} |
| A △ B | elements in exactly one of A, B | {1,2,5,6} |
| A′ | {x ∈ U \| x ∉ A} | depends on U |

With U = {1,…,10} and A = {2,3,4,5,6}, A′ = {1,7,8,9,10}. The complement is the one operation that
cannot be computed without knowing U.

**Two words the question bank uses.** A and B are **disjoint** when A ∩ B = ∅ and **overlapping** when
A ∩ B ≠ ∅.

### The laws of set theory

Each law has a union and a dual intersection version, obtained by swapping ∪ with ∩ and ∅ with U.

| Law | Union form | Intersection form |
|---|---|---|
| Idempotent | A ∪ A = A | A ∩ A = A |
| Commutative | A ∪ B = B ∪ A | A ∩ B = B ∩ A |
| Associative | (A ∪ B) ∪ C = A ∪ (B ∪ C) | (A ∩ B) ∩ C = A ∩ (B ∩ C) |
| Distributive | A ∪ (B ∩ C) = (A ∪ B) ∩ (A ∪ C) | A ∩ (B ∪ C) = (A ∩ B) ∪ (A ∩ C) |
| Identity | A ∪ ∅ = A | A ∩ U = A |
| Domination | A ∪ U = U | A ∩ ∅ = ∅ |
| Complementation | A ∪ A′ = U | A ∩ A′ = ∅ |
| Double complement | (A′)′ = A | — |
| De Morgan | (A ∪ B)′ = A′ ∩ B′ | (A ∩ B)′ = A′ ∪ B′ |
| Absorption | A ∪ (A ∩ B) = A | A ∩ (A ∪ B) = A |

Union distributes over intersection **and** intersection distributes over union. Both are true and both
are used in proofs.

### Checking a law: membership tables

A membership table is the set-theory truth table: 1 means "in", 0 means "not in". Two expressions are
equal exactly when their columns match in every row.

### Worked example — De Morgan with a membership table

Claim: (A ∪ B)′ = A′ ∩ B′.

| A | B | A ∪ B | (A ∪ B)′ | A′ | B′ | A′ ∩ B′ |
|---|---|---|---|---|---|---|
| 1 | 1 | 1 | 0 | 0 | 0 | 0 |
| 1 | 0 | 1 | 0 | 0 | 1 | 0 |
| 0 | 1 | 1 | 0 | 1 | 0 | 0 |
| 0 | 0 | 0 | 1 | 1 | 1 | 1 |

The fourth and last columns agree in all four rows, so the sets are equal.

**Exam presentation.** Label columns with expressions, then write one sentence: "columns 4 and 7 agree
in every row, hence the sets are equal". Without it the table proves nothing.

### Worked example — the same law checked numerically

U = {1,…,10}, A = {2,3,4,5,6}, B = {5,6,7}. Then A ∪ B = {2,3,4,5,6,7} and (A ∪ B)′ = {1,8,9,10}.
Also A′ = {1,7,8,9,10}, B′ = {1,2,3,4,8,9,10}, so A′ ∩ B′ = {1,8,9,10}. Same set. A numerical check
never proves a law, but it catches almost every slip.

### Common mistakes

- Treating A − B and B − A as the same. One of them may be empty.
- Writing A − B as A′ − B or A ∩ B. The identity is A − B = A ∩ B′.
- Computing a complement with no universal set stated.
- Reading A △ B as "everything except B". It is exactly one of the two.
- Quoting distributivity in the wrong direction and "simplifying" into a longer expression.
- Forgetting that ∪ and ∩ commute but − does not.

**Quick check 2.** U = {1,…,12}, A = {1,2,3,4,6}, B = {2,4,6,8,10}, C = {3,6,9,12}. Find
(a) A ∪ B, (b) A ∩ B ∩ C, (c) A − C, (d) A △ B, (e) (B ∪ C)′. *(Answer Q2.)*

---

## 3. Cartesian product and partitions

**Definition.** An **ordered pair** (a, b) is determined by its coordinates in order: (a,b) = (c,d)
exactly when a = c and b = d. The **Cartesian product** is the set of all ordered pairs with first
coordinate from A and second from B:

> A × B = { (a, b) | a ∈ A and b ∈ B }

If |A| = m and |B| = n then |A × B| = mn.

**Simple meaning.** Pick one item from the first set, pair it with one from the second, and repeat for
every combination. Round brackets, because order matters inside the pair.

**Properties that get examined.**

1. A × B and B × A have the same size but are different sets unless A = B.
2. A × ∅ = ∅, because there is no second coordinate to choose.
3. A × (B ∪ C) = (A × B) ∪ (A × C), and the same with ∩.
4. A relation from A to B is by definition a subset of A × B.
5. |P(A × B)| = 2^|A||B| — the number of relations from A to B.

### Worked example — A × B, B × A, and their difference (IAT sample Q13)

A = {1,3,5}, B = {2,3,8}. Each product has 9 pairs.

> A × B = {(1,2),(1,3),(1,8), (3,2),(3,3),(3,8), (5,2),(5,3),(5,8)}
> B × A = {(2,1),(2,3),(2,5), (3,1),(3,3),(3,5), (8,1),(8,3),(8,5)}

A pair (x, y) is in both only if x and y are each in A ∩ B = {3}. So the only common pair is (3,3), and

> (A × B) − (B × A) = {(1,2),(1,3),(1,8),(3,2),(3,8),(5,2),(5,3),(5,8)}

That is 9 − 1 = 8 pairs.

**Exam presentation.** Write the two blocks of nine, then cross out the shared pairs visibly.

### Partitions

**Definition.** A **partition** of a non-empty set A is a collection of non-empty subsets of A, called
blocks, such that (i) the blocks are pairwise disjoint — no element is in two of them; and (ii) their
union is all of A.

Two conditions, both required. Missing blocks leave elements unaccounted for; overlapping blocks put an
element in two places.

### Worked example — every partition of {1, 2, 3}

- One block: { {1,2,3} }
- Two blocks: { {1,2},{3} }, { {1,3},{2} }, { {2,3},{1} }
- Three blocks: { {1},{2},{3} }

Five in total. Check { {1,3},{2} }: non-empty blocks, no shared element, union is {1,2,3} — a partition.
But { {1,2},{2,3} } is not, because 2 is in both blocks, and { {1},{2} } is not, because 3 is missing.

**Why partitions matter.** The equivalence classes of an equivalence relation always form a partition,
and every partition comes from exactly one equivalence relation. When Module 2 asks you to verify that
classes partition A, this is the definition you check.

### Common mistakes

- Writing |A × B| = |A| + |B|. It is a product.
- Using curly brackets for an ordered pair: {1,2} destroys the order.
- Assuming A × B = B × A.
- Using ∅ as a block. Blocks must be non-empty.
- Listing subsets of A and calling them a partition. The collection must cover A without overlaps.

**Quick check 3.** (a) A = {p,q}, B = {1,2,3}. Write A × B and |A × B|.
(b) Is { {1,4},{2},{3,5} } a partition of {1,2,3,4,5}? (c) Give a partition of {a,b,c,d} into two blocks.
*(Answer Q3.)*

---

## 4. Proving set identities

| Method | What you do | Best when |
|---|---|---|
| Element argument | take arbitrary x, show x ∈ A ⟺ x ∈ B; often split into two inclusions | the question says "prove" |
| Membership table | list all 2ⁿ cases and compare columns | two or three sets, "verify" |
| Algebraic proof | rewrite one side with the laws of section 2, one law per line | standard laws, or time is short |

### Worked example — element argument for A − B = A ∩ B′

Let x be arbitrary. Then

> x ∈ A − B ⟺ x ∈ A and x ∉ B ⟺ x ∈ A and x ∈ B′ ⟺ x ∈ A ∩ B′

Each step is an equivalence, so the sets are equal. ∎

**Exam presentation.** Start with "let x be arbitrary", chain with ⟺ (not →), and finish with "since x
was arbitrary, A − B = A ∩ B′". The last sentence is part of the proof.

### Worked example — membership table for distributivity

Claim: A ∩ (B ∪ C) = (A ∩ B) ∪ (A ∩ C). Three sets, eight rows.

| A | B | C | B ∪ C | A ∩ (B ∪ C) | A ∩ B | A ∩ C | (A ∩ B) ∪ (A ∩ C) |
|---|---|---|---|---|---|---|---|
| 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 |
| 1 | 1 | 0 | 1 | 1 | 1 | 0 | 1 |
| 1 | 0 | 1 | 1 | 1 | 0 | 1 | 1 |
| 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| 0 | 1 | 1 | 1 | 0 | 0 | 0 | 0 |
| 0 | 1 | 0 | 1 | 0 | 0 | 0 | 0 |
| 0 | 0 | 1 | 1 | 0 | 0 | 0 | 0 |
| 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |

Columns 5 and 8 agree in all eight rows.

### Worked example — algebraic proof

Simplify (A ∪ B) ∩ (A ∪ B′).

> = A ∪ (B ∩ B′)  (distributive law)
> = A ∪ ∅  (complementation)
> = A  (identity law)

Three lines, three named laws — a complete proof.

### Common mistakes

- Proving only A ⊆ B and stopping. Equality needs both inclusions or a chain of ⟺.
- Using ⟹ in a chain of equivalences.
- Manipulating both sides at once without saying so.
- Naming no laws. Unnamed steps are assertions.
- Wrong row count. n sets need 2ⁿ rows.
- Reading a Venn diagram and calling it a proof.

**Quick check 4.** (a) Prove by an element argument that A ∪ (A ∩ B) = A.
(b) Use a membership table to check (A ∩ B)′ = A′ ∪ B′.
(c) Simplify (A ∩ B) ∪ (A ∩ B′) naming each law. *(Answer Q4.)*

---

## 5. Propositional logic and truth tables

**Teacher's definitions (slides 29–39).** A **proposition** is a declarative sentence that is either
true or false, not both. "Delhi is the capital of India" is a proposition; "Sit down!" is not, because a
command has no truth value; "x + 1 = 2" is not, because it needs x fixed first.

A **compound proposition** is built from simpler ones with the connectives ¬, ∧, ∨, →, ↔. The simple
statements inside are **atomic propositions**, written p, q, r, …

**Simple meaning.** Logic is arithmetic on truth values: two values, five operations, a fixed rule each.

| p | q | ¬p | p ∧ q | p ∨ q | p ⊕ q | p → q | p ↔ q |
|---|---|---|---|---|---|---|---|
| T | T | F | T | T | F | T | T |
| T | F | F | F | T | T | F | F |
| F | T | T | F | T | T | T | F |
| F | F | T | F | F | F | T | T |

Two variables give 2² = 4 rows; n variables give 2ⁿ. Keep the row order TT, TF, FT, FF so the marker can
compare tables.

**The five connectives.**

1. **¬p** flips the value; the only unary connective.
2. **p ∧ q** is true only when both are true.
3. **p ∨ q** is true when at least one is true — the inclusive or.
4. **p ⊕ q** is true when exactly one is true.
5. **p → q** is false in exactly one case: p true and q false.

**Implication is the one that trips everyone up.** From a false hypothesis anything follows. "If
1 + 1 = 3 then your grandmother wears combat boots" is a true implication. The connective records only
the truth-value relationship; it does not claim causation.

| English sentence | Symbolic form | Why |
|---|---|---|
| if p, then q | p → q | standard reading |
| q if p | p → q | "if" introduces the hypothesis |
| p only if q | p → q | "only if" marks the conclusion |
| p is sufficient for q | p → q | p is enough to force q |
| q is necessary for p | p → q | no q means no p |
| q unless ¬p | p → q | "unless" hides a negation |
| p if and only if q | p ↔ q | both implications at once |

"p only if q" is the classic trap: it is p → q, not q → p. "You will pass only if you write the exam"
means passing forces writing, not the other way round.

### Converse, inverse, contrapositive

| Name | Form | Equivalent to p → q? |
|---|---|---|
| Converse | q → p | No |
| Inverse | ¬p → ¬q | No |
| Contrapositive | ¬q → ¬p | **Yes** |

The converse and inverse are equivalent to each other, and neither is equivalent to the original.

**Precedence.** ¬ binds tightest, then ∧, then ∨, then →, then ↔. So p ∨ q → ¬r means (p ∨ q) → ¬r.
Bracket everything anyway.

### Worked example — translating an English sentence (slide 53)

"You can access the Internet from campus only if you are a computer science major or you are not a
freshman."

p: you can access the Internet from campus; q: you are a CS major; r: you are a freshman.

> p → (q ∨ ¬r)

Check with q = F, r = T: then q ∨ ¬r = F, so the implication is false when p is true — you cannot access
the system. That matches the English.

### Worked example — full truth table for (p ∨ q) → ¬r

| p | q | r | p ∨ q | ¬r | (p ∨ q) → ¬r |
|---|---|---|---|---|---|
| T | T | T | T | F | F |
| T | T | F | T | T | T |
| T | F | T | T | F | F |
| T | F | F | T | T | T |
| F | T | T | T | F | F |
| F | T | F | T | T | T |
| F | F | T | F | F | T |
| F | F | F | F | T | T |

Rows 7 and 8 matter: when p ∨ q is false the implication is true whatever ¬r is, even in row 7 where ¬r
is also false. That row is the one people mark wrong.

### Common mistakes

- Making p → q false when p is false.
- Translating "p only if q" as q → p.
- Reading ∨ as exclusive or.
- Writing too few rows. Three atoms need eight.
- Treating the converse as equivalent to the original.
- Misplacing a negation in a sub-column.

**Quick check 5.** (a) Which are propositions: (i) 7 + 5 = 12; (ii) Close the door; (iii) n is prime;
(iv) The moon is made of green cheese.
(b) Translate "You will get the scholarship if and only if your attendance is above 75% or you have a
sports quota."
(c) Give the converse, inverse and contrapositive of "if a number is divisible by 4 then it is even".
*(Answer Q5.)*

---

## 6. Logical equivalence

**Teacher's definition (slides 46–47).** Two propositions are **logically equivalent**, written A ≡ B,
when they always have the same truth value. Equivalently, A ≡ B exactly when A ↔ B is a tautology.

**Two ways to prove it.** A truth table proves equivalence by exhaustion; a chain of laws proves it by
derivation. Use the table for at most three atoms when the question says "using truth tables"; use the
laws when it says "using logical equivalences", which the university papers do.

| Law | Form |
|---|---|
| Identity | p ∧ T ≡ p; p ∨ F ≡ p |
| Domination | p ∨ T ≡ T; p ∧ F ≡ F |
| Idempotent | p ∨ p ≡ p; p ∧ p ≡ p |
| Double negation | ¬(¬p) ≡ p |
| Commutative | p ∨ q ≡ q ∨ p; p ∧ q ≡ q ∧ p |
| Associative | (p ∨ q) ∨ r ≡ p ∨ (q ∨ r); same with ∧ |
| Distributive | p ∧ (q ∨ r) ≡ (p ∧ q) ∨ (p ∧ r); p ∨ (q ∧ r) ≡ (p ∨ q) ∧ (p ∨ r) |
| De Morgan | ¬(p ∧ q) ≡ ¬p ∨ ¬q; ¬(p ∨ q) ≡ ¬p ∧ ¬q |
| Absorption | p ∨ (p ∧ q) ≡ p; p ∧ (p ∨ q) ≡ p |
| Implication | p → q ≡ ¬p ∨ q |
| Negation of implication | ¬(p → q) ≡ p ∧ ¬q |
| Contrapositive | p → q ≡ ¬q → ¬p |
| Biconditional | p ↔ q ≡ (p → q) ∧ (q → p) |

Almost every equivalence question starts with the implication law. Whenever the target has no →, convert
every arrow with p → q ≡ ¬p ∨ q first.

### Verified University question — Summer 2026 Q.1(b), 5 marks

Prove that ((p → q) → r) and (p ∧ ¬q) ∨ r are logically equivalent, and interpret how logical
equivalence helps simplify decision rules in software systems.

> (p → q) → r
> ≡ ¬(p → q) ∨ r  (implication law on the outer arrow)
> ≡ ¬(¬p ∨ q) ∨ r  (implication law on p → q)
> ≡ (p ∧ ¬q) ∨ r  (De Morgan, then double negation)

That is the right-hand expression, so they are equivalent. ∎

**Truth-table confirmation.**

| p | q | r | p → q | (p → q) → r | p ∧ ¬q | (p ∧ ¬q) ∨ r |
|---|---|---|---|---|---|---|
| T | T | T | T | T | F | T |
| T | T | F | T | F | F | F |
| T | F | T | F | T | T | T |
| T | F | F | F | T | T | T |
| F | T | T | T | T | F | T |
| F | T | F | T | F | F | F |
| F | F | T | T | T | F | T |
| F | F | F | T | F | F | F |

Columns 5 and 7 match in all eight rows.

**The interpretation part.** The two forms describe the same decision rule, but the right-hand one has no
implication. In a program, (p ∧ ¬q) ∨ r is three basic tests joined by AND, NOT and OR — a direct
branch — whereas nested implications are harder to read and test. Equivalence lets a designer replace a
convoluted rule with a simpler one without changing any outcome, which is what makes a rules engine
auditable.

**Mark split.** Roughly three marks for the derivation, two for the interpretation.

### Verified University question — Winter 2025 Q.1(b)

Prove that (P ∨ Q) → R ≡ (P → R) ∧ (Q → R).

Reduce both sides separately until they meet.

> LHS: (P ∨ Q) → R ≡ ¬(P ∨ Q) ∨ R ≡ (¬P ∧ ¬Q) ∨ R
> RHS: (P → R) ∧ (Q → R) ≡ (¬P ∨ R) ∧ (¬Q ∨ R) ≡ (¬P ∧ ¬Q) ∨ R

Both equal (¬P ∧ ¬Q) ∨ R. ∎

**Why the last step is legitimate.** Distributivity says X ∨ (Y ∧ Z) ≡ (X ∨ Y) ∧ (X ∨ Z). With X = R,
Y = ¬P, Z = ¬Q, read right to left: (¬P ∨ R) ∧ (¬Q ∨ R) ≡ R ∨ (¬P ∧ ¬Q).

**The dual worth knowing.** Swapping ∧ and ∨ gives (P ∧ Q) → R ≡ (P → R) ∨ (Q → R). "If either one
happens, then R" splits into an AND of implications; "if both happen, then R" splits into an OR.

### Worked example — a third equivalence (IAT sample Q11(i))

Prove ¬(p ∨ (¬p ∧ q)) ≡ ¬p ∧ ¬q.

> ≡ ¬p ∧ ¬(¬p ∧ q)  (De Morgan)
> ≡ ¬p ∧ (p ∨ ¬q)  (De Morgan, then double negation)
> ≡ (¬p ∧ p) ∨ (¬p ∧ ¬q)  (distributive)
> ≡ F ∨ (¬p ∧ ¬q)  (complementation)
> ≡ ¬p ∧ ¬q  (identity)

### Common mistakes

- Applying De Morgan to an implication: ¬(p → q) is p ∧ ¬q, not ¬p → ¬q.
- Dropping a negation in the middle of a chain.
- Claiming equivalence from "most rows". All 2ⁿ rows must agree.
- Changing both sides at once and losing track of what has been proved.
- Naming a law that does not apply.
- Answering only the derivation when the question also says "interpret".

**Quick check 6.** (a) Prove p → q ≡ ¬q → ¬p with the laws.
(b) Prove (p ∧ q) ∨ (p ∧ ¬q) ≡ p.
(c) Show with one truth-table row that the converse of p → q is not equivalent to p → q. *(Answer Q6.)*

---

## 7. Tautology, contradiction, contingency — and CNF/DNF

**Teacher's definitions (slides 55–56).** A **tautology** is true for every assignment (p ∨ ¬p). A
**contradiction** is false for every assignment (p ∧ ¬p). A **contingency** is neither (¬p).

| Type | Final column | How to answer |
|---|---|---|
| Tautology | all T | say "tautology", show the column is all T |
| Contradiction | all F | say "contradiction", show the column is all F |
| Contingency | mixed | say "contingency", give one T row and one F row |

Two routes: the truth table always works and is what most questions intend; simplification is faster and
is the only practical route at four or more atoms.

### Worked example — is [(p → r) ∧ (¬q → p) ∧ ¬r] → q a tautology? (IAT sample Q9(i))

Simplify the antecedent first.

> (p → r) ∧ ¬r ≡ (¬p ∨ r) ∧ ¬r ≡ (¬p ∧ ¬r) ∨ (r ∧ ¬r) ≡ ¬p ∧ ¬r

So the antecedent gives both ¬p and ¬r. Also (¬q → p) ≡ q ∨ p. Combining,
(¬p ∧ ¬r) ∧ (q ∨ p) ≡ (¬p ∧ ¬r) ∧ q, since p is false.

With A = ¬p ∧ ¬r ∧ q,

> A → q ≡ ¬A ∨ q ≡ (p ∨ r ∨ ¬q) ∨ q ≡ p ∨ r ∨ T ≡ T

Tautology. ∎

**Faster reading.** The antecedent asserts ¬r and p → r. If p were true then r would be true,
contradicting ¬r, so p is false. With p false, ¬q → p forces ¬q false, so q is true. The antecedent can
only hold when q holds, which is what the implication claims. Write this if the question says "justify".

### Worked example — is (p → q) ∧ ¬q a tautology? (IAT sample Q9(ii))

> ≡ (¬p ∨ q) ∧ ¬q ≡ (¬p ∧ ¬q) ∨ (q ∧ ¬q) ≡ ¬p ∧ ¬q

True when p and q are both false, false otherwise — a **contingency**. It is the first half of modus
tollens; adding the conclusion ¬p gives the tautology (p → q) ∧ ¬q → ¬p.

### Worked example — (p → q) ↔ (¬q → ¬p) is a tautology

By the contrapositive law the two sides are the same proposition, and X ↔ X ≡ T. By table: columns for
p → q and ¬q → ¬p are F, T, T, T, so the biconditional column is all T.

### CNF and DNF

| Term | Meaning | Example |
|---|---|---|
| Literal | a variable or its negation | p, ¬q |
| Clause | literals joined by ∨ | p ∨ ¬q ∨ r |
| Term (minterm) | literals joined by ∧, one per variable | p ∧ ¬q ∧ r |
| **CNF** | conjunction of clauses — AND of ORs | (p ∨ q) ∧ (¬p ∨ r) |
| **DNF** | disjunction of terms — OR of ANDs | (p ∧ q) ∨ (¬p ∧ r) |

The names give the outer operator: **C**NF has the **c**onjunction outside; **D**NF has the
**d**isjunction outside.

**Procedure.**

1. Remove every ↔ using p ↔ q ≡ (p → q) ∧ (q → p).
2. Remove every → using p → q ≡ ¬p ∨ q.
3. Push negations inwards with De Morgan and double negation until ¬ sits only on single variables.
4. CNF: distribute ∨ over ∧. DNF: distribute ∧ over ∨.
5. Drop duplicate literals and clauses, and delete clauses containing q ∨ ¬q (they are T).

### Worked example — CNF and DNF of [P → (Q ∧ R)] ∧ [¬P → (¬Q ∧ ¬R)] (IAT sample Q9(ii))

Remove the arrows:

> P → (Q ∧ R) ≡ ¬P ∨ (Q ∧ R)
> ¬P → (¬Q ∧ ¬R) ≡ P ∨ (¬Q ∧ ¬R)

Negations are already on single variables. Distribute for CNF:

> ¬P ∨ (Q ∧ R) ≡ (¬P ∨ Q) ∧ (¬P ∨ R)
> P ∨ (¬Q ∧ ¬R) ≡ (P ∨ ¬Q) ∧ (P ∨ ¬R)

> **CNF:** (¬P ∨ Q) ∧ (¬P ∨ R) ∧ (P ∨ ¬Q) ∧ (P ∨ ¬R)

For the DNF, read the true rows of the table.

| P | Q | R | P → (Q ∧ R) | ¬P → (¬Q ∧ ¬R) | Whole |
|---|---|---|---|---|---|
| T | T | T | T | T | 1 |
| T | T | F | F | T | 0 |
| T | F | T | F | T | 0 |
| T | F | F | F | T | 0 |
| F | T | T | T | F | 0 |
| F | T | F | T | F | 0 |
| F | F | T | T | F | 0 |
| F | F | F | T | T | 1 |

Only rows 1 and 8 are true, so the DNF has two terms:

> **DNF:** (P ∧ Q ∧ R) ∨ (¬P ∧ ¬Q ∧ ¬R)

Sanity check on the CNF: at P = F, Q = F, R = F all four clauses are true, matching row 8; at P = F,
Q = T, R = F clause 3 is false, matching row 6.

**Note on one bank question.** "(A → B) → (B → C) → (A → C)" has ambiguous brackets as printed. Under
either sensible reading it is a tautology (hypothetical syllogism), so its CNF is simply **true** and its
DNF is the disjunction of all eight minterms. Legitimate but odd; state your reading, prove the
tautology in two lines, then give the forms.

### Common mistakes

- Swapping CNF and DNF. Check which operator is outside.
- Stopping the distribution halfway.
- Leaving a negation over a bracket.
- Converting → to ∧. The law uses ∨.
- Calling a contingency a tautology because most rows are true.
- Reading the final column from the wrong sub-column.
- Forgetting to drop repeated clauses.

**Quick check 7.** (a) Classify: (i) (p ∧ q) → p; (ii) p ↔ ¬p; (iii) (p ∨ q) ∧ ¬p.
(b) Convert (p → q) ∧ (q → r) into CNF. (c) Give the DNF of p ⊕ q. *(Answer Q7.)*

---

## 8. Predicates and quantifiers

**Teacher's definitions (slides 70–82).** A **predicate** (propositional function) is a statement with
variables whose truth depends on their values: P(x) reads "x is greater than 3". P is the predicate
symbol, x the argument, and P(x) is the value of the function at x.

A predicate becomes a proposition in two ways only: replace every variable by a value from the domain,
or bind every variable with a quantifier. The set of allowed values is the **domain** or **universe of
discourse** U.

| Predicate | Read as | Name |
|---|---|---|
| Father(x) | x is a father | unary |
| Brother(x, y) | x is a brother of y | binary |
| Sum(x, y, z) | x + y = z | ternary |
| P(x₁, …, xₙ) | an n-place property | n-ary |

With P(x) meaning "x > 5" and U the integers, P(8) is true and P(5) false. With P(x,y,z) meaning
x + y = z, P(−4,6,2) is true and P(5,2,10) false; P(5,x,7) is still a predicate, because x is free.

| Quantifier | Symbol | Read as | True when |
|---|---|---|---|
| Universal | ∀x P(x) | for all x, P(x) | every element of U satisfies P |
| Existential | ∃x P(x) | there exists x with P(x) | at least one element satisfies P |

**The domain decides the truth value.** With P(x) meaning "x > 0", ∀x P(x) is false over the integers
and true over the positive integers. Always state the domain.

**Finite domains turn quantifiers into connectives.** For U = {1,2,3},

> ∀x P(x) ≡ P(1) ∧ P(2) ∧ P(3)   ∃x P(x) ≡ P(1) ∨ P(2) ∨ P(3)

That is why the translation rules use ∧ with ∃ and → with ∀.

### Translating English into quantifiers

| English shape | Symbolic form | Note |
|---|---|---|
| All S are P | ∀x (S(x) → P(x)) | implication, never ∧ |
| Some S are P | ∃x (S(x) ∧ P(x)) | conjunction, never → |
| No S are P | ∀x (S(x) → ¬P(x)) | "all S are not P" |
| Some S are not P | ∃x (S(x) ∧ ¬P(x)) | negation of "all S are P" |

"All students are friendly" as ∀x(S(x) ∧ F(x)) claims everything in the universe is a student and
friendly, including the examiner's dog. The implication version says: if it is a student, it is
friendly.

### Negating a quantified statement

> ¬∀x P(x) ≡ ∃x ¬P(x)   ¬∃x P(x) ≡ ∀x ¬P(x)

Flip the quantifier and negate the inside. "Not all" becomes "some not"; "none" becomes "all not".

### Worked example — the Java sentence and its negation (slide 86)

Domain: all people. Student(x): x is a student in this class; Taken(x, y): x has taken course y; Java is
a constant.

> ∀x (Student(x) → Taken(x, Java))

Negation:

> ≡ ∃x ¬(Student(x) → Taken(x, Java))
> ≡ ∃x (Student(x) ∧ ¬Taken(x, Java))

"There is at least one student in this class who has not taken Java." The ∧ appears because the negation
of an implication is a conjunction.

### Worked example — two prelim-bank sentences

S(x): x is a student; G(x): x took GenAI; P(x): x passes GenAI.

**(i) Some students took GenAI:** ∃x (S(x) ∧ G(x)).
**(ii) Every student who takes GenAI passes it:** ∀x ((S(x) ∧ G(x)) → P(x)).

The ∧ sits inside the hypothesis because "student who takes GenAI" is one combined condition.

### Worked example — three class statements (slide 87)

S(x): student; M(x): has taken mathematics; G(x): girl student; C(x): in the class; P(x): sports person;
I(x): intelligent; H(x): hardworking.

- All students have taken a course in mathematics: ∀x (S(x) → M(x))
- There is a girl student in a class who is also a sports person: ∃x (G(x) ∧ C(x) ∧ P(x))
- Some students are intelligent, but not hardworking: ∃x (S(x) ∧ I(x) ∧ ¬H(x))

### Two quantifiers in one statement

Order matters. Over the reals:

> ∀x ∃y (x + y = 0) — for every x there is y = −x. **True.**
> ∃y ∀x (x + y = 0) — one fixed y works for every x. **False.**

The first quantifier chooses first; later ones may depend on it.

### Common mistakes

- ∀x (S(x) ∧ P(x)) for "all S are P". Use →.
- ∃x (S(x) → P(x)) for "some S is P". Use ∧.
- Negating ∀x P(x) as ∀x ¬P(x). That negates ∃x P(x).
- Forgetting that ¬(A → B) is A ∧ ¬B.
- Leaving the domain unstated.
- Swapping nested quantifiers.
- Treating a predicate with a free variable as a proposition.

**Quick check 8.** Domain: all people. S(x): student; F(x): friendly; H(x): speaks Hindi; B(x): born in
India. Write in symbols: (i) everyone is friendly; (ii) someone speaks Hindi; (iii) some student was not
born in India. Negate each and translate the negation back. *(Answer Q8.)*

---

## 9. Inclusion–Exclusion is covered in Module IV

The University of Mumbai syllabus places the **Inclusion–Exclusion Principle in Module IV — Counting (5 hours, CO4)**, not Module I. The complete explanation, worked university question, Venn diagram, practice and answer key are in [Module IV, Section 2 — Inclusion–Exclusion](/dsgt/modules/module-4#iep). This guide therefore does not duplicate that topic.

---

## 10. Mathematical induction

**Teacher's definition (slide 101; exam question Summer 2026 Q.4(b)).** If (i) P(1) is true, and
(ii) for every k ≥ 1, P(k) true implies P(k+1) true, then P(n) is true for every n ≥ 1.

**Why it works.** The base starts a chain; the step says each true statement forces the next.

**Template.**

1. State P(n) explicitly.
2. Base case: substitute the starting value, compute both sides, say they are equal.
3. Inductive hypothesis: "assume P(k) for some arbitrary k ≥ 1", and write that equation down.
4. Inductive step: start from the left side at k+1, split off the new last term, replace the rest using
   the hypothesis, reach the right side at k+1.
5. Conclusion: "by the principle of mathematical induction, P(n) holds for all n ≥ 1".

### Verified University question — Summer 2026 Q.4(b), 7 marks

Prove that Σ_{r=1}^{n} r(r + 3) = n(n + 1)(n + 5)/3 for every positive integer n.

**Claim.** P(n): Σ_{r=1}^{n} r(r + 3) = n(n+1)(n+5)/3 for all n ≥ 1.

**Base, n = 1.** Left: 1·(1+3) = 4. Right: 1·2·6/3 = 4. ✓

**Hypothesis.** Assume P(k): Σ_{r=1}^{k} r(r + 3) = k(k+1)(k+5)/3.

**Step.** Split off r = k+1:

> Σ_{r=1}^{k+1} r(r+3) = Σ_{r=1}^{k} r(r+3) + (k+1)(k+4)
> = k(k+1)(k+5)/3 + (k+1)(k+4)
> = (k+1)[ k(k+5)/3 + (k+4) ]
> = (k+1)[ (k² + 5k + 3k + 12)/3 ]
> = (k+1)(k² + 8k + 12)/3
> = (k+1)(k+2)(k+6)/3

Since k² + 8k + 12 = (k+2)(k+6). And the right side at k+1 is
(k+1)(k+2)((k+1)+5)/3 = (k+1)(k+2)(k+6)/3 — the same. ∎

**Conclusion.** P(1) holds and P(k) implies P(k+1) for arbitrary k ≥ 1, so P(n) holds for all n ≥ 1.

**Numerical check.** n = 3: left = 4 + 10 + 18 = 32; right = 3·4·8/3 = 32 ✓. n = 4: left 60; right
4·5·9/3 = 60 ✓.

**Exam presentation.** Six labelled blocks: claim, base, hypothesis, step, "which is P(k+1)", conclusion.

### Worked example — the teacher's arithmetic series (slides 103–105)

Prove 1 + 5 + 9 + … + (4n − 3) = n(2n − 1).

**Base n = 1.** Left 4(1) − 3 = 1; right 1·1 = 1. ✓

**Hypothesis.** 1 + 5 + … + (4k − 3) = k(2k − 1).

**Step.** Add the term 4(k+1) − 3 = 4k + 1:

> = k(2k − 1) + (4k + 1) = 2k² − k + 4k + 1 = 2k² + 3k + 1 = (k+1)(2k+1)
> = (k+1)(2(k+1) − 1)

Hence true for all n ≥ 1. ∎

**A correction to the slide.** Slide 104 writes the expansion of k(2k − 1) as "(2k)² − k + 4k + 1". It
should be 2k² − k + 4k + 1; "(2k)²" means 4k². The final answer on the slide is correct, so it is a
typesetting slip — but copy the correct expansion.

### Common mistakes

- Skipping the base case, or computing only one side of it.
- Never using the inductive hypothesis.
- Proving P(k+1) from first principles instead of from P(k).
- Assuming P(k) for all k, which is what you are proving.
- Not showing the final expression equals P(k+1).
- Factoring slips. Check with n = 3.
- No concluding sentence.

**Quick check 10.** (a) Prove 1 + 4 + 7 + … + (3n − 2) = n(3n − 1)/2.
(b) Prove 2ⁿ > n for all n ≥ 1. *(Answer Q9.)*

---

## 11. The other proof methods in one page

| Method | To prove | You assume | You must reach |
|---|---|---|---|
| Direct | P → Q | P | Q |
| Contrapositive | P → Q | ¬Q | ¬P |
| Contradiction | S | ¬S | any contradiction |
| Cases | S | nothing extra | S in every exhaustive case |
| Counterexample | ¬(∀x P(x)) | nothing | one x with ¬P(x) |
| Exhaustion | S over a finite list | nothing | every case checked |
| Deduction | S | known facts | S by valid steps |

### Direct proof — the sum of two even integers is even (slide 96)

Let x = 2m and y = 2n. Then x + y = 2m + 2n = 2(m + n), and m + n is an integer, so x + y is even. ∎

Same shape for "n odd ⇒ n² odd": n = 2k + 1 gives n² = 4k² + 4k + 1 = 2(2k² + 2k) + 1.

### Contrapositive — if n² is even then n is even

The direct route starts from "n² is even", which says nothing convenient about n. The contrapositive
starts from "n is odd".

**Contrapositive statement.** If n is odd then n² is odd.

**Proof.** Let n = 2k + 1. Then n² = 4k² + 4k + 1 = 2(2k² + 2k) + 1, which is odd. ∎

Since P → Q ≡ ¬Q → ¬P, this proves the original.

**A source correction worth knowing.** Slide 97 presents this argument under the heading "Direct Proof".
It is not direct: it begins by assuming the negation of the conclusion, which makes it a contrapositive
(or a contradiction) proof. The mathematics is right; the label is wrong. Name it "proof by
contrapositive" in the exam.

### Contradiction — √2 is irrational (slide 100)

Suppose √2 = a/b with integers a, b ≠ 0 and no common factor. Squaring: 2b² = a², so a² is even, hence a
is even by the contrapositive result above. Write a = 2k: then 2b² = 4k², so b² = 2k², so b is even.
Then a and b share the factor 2, contradicting the choice that they have none. Hence √2 is irrational. ∎

The contradiction need not be "1 = 0"; any clash with an earlier statement or a known fact closes it.

### Cases — |x| + |x + 1| ≥ 1 for every real x (slide 107)

Split where a term changes sign: x = −1 and x = 0.

- x ≤ −1: both terms negative, sum = −2x − 1 ≥ 1 since −2x ≥ 2.
- −1 < x < 0: sum = −x + (x + 1) = 1 ≥ 1.
- x ≥ 0: sum = 2x + 1 ≥ 1.

All cases give at least 1, and the cases cover every real x. ∎

Requirements: the cases must be **exhaustive** and ideally **mutually exclusive**. Missing a boundary
point is the usual failure.

### Counterexample

"Every prime is odd" fails at 2, which is prime and even. "n² + n + 41 is prime for all n" holds for
n = 1, …, 39 but at n = 41 the value is 41(41 + 1 + 1) = 41 · 43, composite.

One counterexample is a complete disproof of a "for all" statement. It proves nothing else.

### Common mistakes

- Calling a contrapositive proof a "direct proof".
- In a contradiction proof, assuming the negation of the hypothesis instead of the negation of the whole
  statement.
- Cases that miss a case or overlap at a boundary.
- Using one example to "prove" a universal statement.
- Giving a counterexample where the claim happens to hold.
- Ending a contradiction proof without saying what was contradicted.

**Quick check 11.** (a) Prove directly that the product of two odd integers is odd.
(b) Prove by contrapositive: if 3n + 2 is odd then n is odd.
(c) Disprove by counterexample: every odd number is prime. *(Answer Q10.)*

---

## Practice questions

**Q1.** (a) Write P({a,b,c,d}) and state its cardinality. (b) True or false with a reason:
(i) ∅ ∈ {∅}; (ii) ∅ ⊆ {∅}; (iii) {∅} ⊆ ∅; (iv) {1,2} ⊂ {1,2,3}. (c) Write the even integers from 2 to
10 in roster and set-builder form.

**Q2.** U = {1,…,12}, A = {1,2,3,4,6}, B = {2,4,6,8,10}, C = {3,6,9,12}. Find (a) A ∪ B,
(b) A ∩ B ∩ C, (c) A − C, (d) A △ B, (e) (B ∪ C)′.

**Q3.** (a) A = {p,q}, B = {1,2,3}. Write A × B and |A × B|. (b) Is { {1,4},{2},{3,5} } a partition of
{1,2,3,4,5}? (c) Give one partition of {a,b,c,d} into two blocks.

**Q4.** (a) Prove by an element argument that A ∪ (A ∩ B) = A. (b) Use a membership table to verify
(A ∩ B)′ = A′ ∪ B′. (c) Simplify (A ∩ B) ∪ (A ∩ B′) naming each law.

**Q5.** (a) Which are propositions: (i) 7 + 5 = 12; (ii) Close the door; (iii) n is prime; (iv) The moon
is made of green cheese. (b) Translate: "You will get the scholarship if and only if your attendance is
above 75% or you have a sports quota." (c) Give the converse, inverse and contrapositive of "if a number
is divisible by 4 then it is even".

**Q6.** *(IAT sample Q11)* Prove with the laws of logic: (i) p → q ≡ ¬q → ¬p;
(ii) (p ∧ q) ∨ (p ∧ ¬q) ≡ p. Then show by one truth-table row that the converse of p → q is not
equivalent to p → q.

**Q7.** *(IAT sample Q9)* Classify: (i) (p ∧ q) → p; (ii) p ↔ ¬p; (iii) (p ∨ q) ∧ ¬p. Convert
(p → q) ∧ (q → r) into CNF, and give the DNF of p ⊕ q.

**Q8.** *(Prelim bank)* Domain: all people. S(x): student; F(x): friendly; H(x): speaks Hindi;
B(x): born in India. Write in symbols: (i) everyone is friendly; (ii) someone speaks Hindi; (iii) some
student was not born in India. Negate each and translate back.

**Q10.** (a) Prove directly that the product of two odd integers is odd. (b) Prove by contrapositive: if
3n + 2 is odd then n is odd. (c) Disprove by counterexample: every odd number is prime.

**Q11.** *(Prelim bank Q1)* Define with a suitable example: disjoint set, proper subset, Cartesian
product, partition of a set, power set, existential quantifier.

---

## Answer key

### Q1

**(a)** |A| = 4, so 16 subsets: ∅ (1); {a},{b},{c},{d} (4); {a,b},{a,c},{a,d},{b,c},{b,d},{c,d} (6);
{a,b,c},{a,b,d},{a,c,d},{b,c,d} (4); {a,b,c,d} (1). Total 16 ✓.

**(b)** (i) True — {∅} has one element, namely ∅. (ii) True — ∅ is a subset of every set.
(iii) False — {∅} has an element, so it cannot be a subset of the empty set. (iv) True — every element
of {1,2} is in {1,2,3}, and 3 is extra.

**(c)** Roster {2,4,6,8,10}; set-builder {x ∈ {1,…,10} | x is even}.

### Q2

(a) {1,2,3,4,6,8,10}. (b) A ∩ B = {2,4,6}, intersect C gives {6}. (c) {1,2,4}.
(d) (A ∪ B) − (A ∩ B) = {1,3,8,10}. (e) B ∪ C = {2,3,4,6,8,9,10,12}, so the complement is {1,5,7,11}.

### Q3

**(a)** {(p,1),(p,2),(p,3),(q,1),(q,2),(q,3)}, six pairs.
**(b)** Yes — non-empty blocks, no shared element, union {1,2,3,4,5}.
**(c)** { {a,b},{c,d} } (also { {a,c},{b,d} } or { {a,d},{b,c} }).

### Q4

**(a)** x ∈ A ∪ (A ∩ B) ⟺ x ∈ A or (x ∈ A and x ∈ B). If x ∈ A the disjunction holds; if x ∈ A ∩ B then
x ∈ A. So either way x ∈ A. Conversely if x ∈ A then x is in the union. Same elements, so equal. ∎

**(b)**

| A | B | A ∩ B | (A ∩ B)′ | A′ | B′ | A′ ∪ B′ |
|---|---|---|---|---|---|---|
| 1 | 1 | 1 | 0 | 0 | 0 | 0 |
| 1 | 0 | 0 | 1 | 0 | 1 | 1 |
| 0 | 1 | 0 | 1 | 1 | 0 | 1 |
| 0 | 0 | 0 | 1 | 1 | 1 | 1 |

Columns 4 and 7 agree.

**(c)** (A ∩ B) ∪ (A ∩ B′) = A ∩ (B ∪ B′) (distributive) = A ∩ U (complementation) = A (identity).

### Q5

**(a)** (i) Proposition, true. (ii) Not — a command. (iii) Not — n is free. (iv) Proposition, false.

**(b)** p: you get the scholarship; q: attendance above 75%; r: sports quota. Then p ↔ (q ∨ r). The "or"
is inclusive.

**(c)** p → q with p = divisible by 4, q = even. Converse q → p: "if even then divisible by 4" — false
(6). Inverse ¬p → ¬q: "if not divisible by 4 then not even" — false (6). Contrapositive ¬q → ¬p: "if not
even then not divisible by 4" — true.

### Q6

**(i)** p → q ≡ ¬p ∨ q (implication) ≡ q ∨ ¬p (commutative) ≡ ¬(¬q) ∨ ¬p (double negation) ≡ ¬q → ¬p
(implication).

**(ii)** (p ∧ q) ∨ (p ∧ ¬q) ≡ p ∧ (q ∨ ¬q) (distributive) ≡ p ∧ T (complementation) ≡ p (identity).

**Not equivalent.** With p = F, q = T: p → q is T but q → p is F. One differing row is enough. (The
converse is equivalent to the inverse.)

### Q7

**(i) Tautology.** (p ∧ q) → p ≡ ¬(p ∧ q) ∨ p ≡ (¬p ∨ ¬q) ∨ p ≡ (¬p ∨ p) ∨ ¬q ≡ T.

**(ii) Contradiction.** (p → ¬p) ∧ (¬p → p) ≡ (¬p ∨ ¬p) ∧ (p ∨ p) ≡ ¬p ∧ p ≡ F.

**(iii) Contingency.** (p ∨ q) ∧ ¬p ≡ (p ∧ ¬p) ∨ (q ∧ ¬p) ≡ q ∧ ¬p — true when q is true and p is false.

**CNF of (p → q) ∧ (q → r):** (¬p ∨ q) ∧ (¬q ∨ r) — already CNF.

**DNF of p ⊕ q:** (p ∧ ¬q) ∨ (¬p ∧ q).

### Q8

(i) ∀x F(x); negation ∃x ¬F(x) — someone is not friendly.
(ii) ∃x H(x); negation ∀x ¬H(x) — nobody speaks Hindi.
(iii) ∃x (S(x) ∧ ¬B(x)); negation ∀x (¬S(x) ∨ B(x)) — everyone is either not a student or born in
India, that is every student was born in India.

### Q9

**(a)** Base n = 1: left 1, right 1·2/2 = 1 ✓. Assume P(k). Adding 3k + 1:

> k(3k − 1)/2 + (3k + 1) = (3k² − k + 6k + 2)/2 = (3k² + 5k + 2)/2
> = (k + 1)(3k + 2)/2 = (k + 1)(3(k + 1) − 1)/2

which is P(k+1). ∎

**(b)** Base n = 1: 2 > 1 ✓. Assume 2ᵏ > k. Then 2^(k+1) = 2·2ᵏ > 2k ≥ k + 1 for k ≥ 1. ∎

### Q10

**(a)** x = 2m + 1, y = 2n + 1, so xy = 4mn + 2m + 2n + 1 = 2(2mn + m + n) + 1, which is odd. ∎
**(b)** Contrapositive: if n is even, n = 2k, then 3n + 2 = 6k + 2 = 2(3k + 1) is even. So the original
holds. ∎
**(c)** 9 is odd and 9 = 3 × 3, so it is not prime. (15, 21, 25 work too.)

### Q11

- **Disjoint sets:** A ∩ B = ∅. Example {1,2} and {3,4}.
- **Proper subset:** A ⊂ B when A ⊆ B and B has an extra element. Example {1,2} ⊂ {1,2,3}.
- **Cartesian product:** A × B = {(a,b) | a ∈ A, b ∈ B}. Example {1,2} × {x} = {(1,x),(2,x)}.
- **Partition:** non-empty pairwise disjoint blocks whose union is the set. Example { {1,2},{3} } for
  {1,2,3}.
- **Power set:** P(A) = {X | X ⊆ A}, |P(A)| = 2ⁿ. Example P({1,2}) = {∅,{1},{2},{1,2}}.
- **Existential quantifier:** ∃x P(x) is true when at least one x in the domain satisfies P. Example
  over the integers, ∃x (x² = 4) is true.

---

## Last-minute revision sheet

**Definitions.** Subset: ∀x(x ∈ A → x ∈ B) · proper subset: subset and not equal · power set: all subsets,
2ⁿ of them · Cartesian product: all ordered pairs, |A||B| of them · partition: non-empty disjoint blocks
covering the set · proposition: declarative, true or false, not both · tautology/contradiction/
contingency: always true / always false / mixed · logical equivalence: same value in every row · CNF:
AND of ORs · DNF: OR of ANDs · predicate: statement with variables · ∀ / ∃: every element / at least one
· induction: base plus step.

**Formulas.**

- p → q ≡ ¬p ∨ q; ¬(p → q) ≡ p ∧ ¬q; p → q ≡ ¬q → ¬p
- ¬(p ∧ q) ≡ ¬p ∨ ¬q; ¬(p ∨ q) ≡ ¬p ∧ ¬q
- p ↔ q ≡ (p → q) ∧ (q → p)
- ¬∀x P(x) ≡ ∃x ¬P(x); ¬∃x P(x) ≡ ∀x ¬P(x)

**Procedures.** Power set: count 2ⁿ, list by size · set equality: element argument, membership table, or
named laws · truth table: 2ⁿ rows, one column per sub-expression · equivalence proof: start from the
messier side, one law per line, name the law · tautology test: final column all T · CNF: kill ↔, kill →,
push ¬ in, distribute ∨ over ∧ · English to quantifiers: "all S are P" → ∀(S → P), "some S is P" →
∃(S ∧ P) · induction: claim, base, hypothesis, step, "this is P(k+1)", conclusion.

**Checks.** Is U or the domain stated wherever needed? Does every power set contain ∅ and the whole set?
Are there exactly 2ⁿ rows? Is a law named on every derivation line? Does the induction hypothesis
actually appear? Do both sides agree at n = 3? Is there a differing row for every "not equivalent" claim?

---

## Sources, verification and coverage

**Teacher material.** Mrs. Shamal Bagal, *Module 1: Crisp Set Theory and Logic* (PowerPoint, 108 slides).
Sets and notation slides 4–15; set operations 18–19; propositional logic 29–41; truth tables and
equivalence 44–49; tautology, contradiction, contingency and the laws 55–68; predicates 70–75;
quantifiers 76–90; mathematical proof and direct proof 94–98; contradiction 99–100; induction 101–105;
proof by cases 107–108.

**Official scope.** University of Mumbai DSGT (2023112), Module I — Crisp Set Theory and Logic, 7 hours,
CO1. Prescribed: sets, subsets, universal and empty sets, set operations, set representation, laws of set
theory; propositional logic; predicate logic; universal and existential quantifiers; types of
mathematical proof — direct, contradiction, deduction, cases, exhaustion, counterexample, mathematical
induction. Self-learning: PROLOG/LISP expert systems, other types of logic and sets.

**Questions.** Summer 2026 Q.1(b) (5 marks), Q.4(b) (7 marks) — wording condensed,
data, marks and numbers preserved. Winter 2025 Q.1(b), read from scanned page 1. IAT1 sample Q7–Q13.
Prelim question bank Module 1. Practice questions without a badge were written for this guide and are not
claimed to be university questions.

**Verification performed.**

- Every equivalence in section 6 and every classification in section 7 was checked by exhaustive truth
  table over all assignments, not by inspection.
- The Summer 2026 and Winter 2025 derivations were each checked twice: by the laws, and by an eight-row
  truth table.
- The CNF (¬P ∨ Q) ∧ (¬P ∨ R) ∧ (P ∨ ¬Q) ∧ (P ∨ ¬R) was checked against the original expression in all
  eight rows; the DNF was read from the verified table. An earlier draft wrongly assumed the expression
  reduced to P ↔ (Q ∧ R); the table disproved it and the corrected version is what appears above.
- The induction identity Σ r(r+3) = n(n+1)(n+5)/3 was checked in closed form and at n = 1, 2, 3, 4, and
  the step algebra symbolically. The arithmetic series was checked the same way.
- Inclusion–exclusion calculations and Venn regions are verified in the Module IV guide.
- Power-set counts and the |A × B| − |B × A| count were enumerated programmatically.

**Corrections to the source slides.** Slide 97 labels the n² even ⇒ n even argument a "direct proof"; it
is a proof by contrapositive. Slide 104 writes "(2k)² − k + 4k + 1" where the expansion of k(2k − 1) is
2k² − k. The mathematics on both slides is otherwise correct.

**Not covered.** PROLOG/LISP expert systems, non-classical logics (modal, fuzzy, intuitionistic),
cardinality of infinite sets, Cantor's theorem, Venn diagrams and set-operation diagrams, Karnaugh maps,
and proof by exhaustion beyond the definition. Deliberate omissions, not oversights.
