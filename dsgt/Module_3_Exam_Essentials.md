# DSGT Module 3 — Functions (Selective Exam Essentials)

**Course:** Discrete Structures and Graph Theory (2023112) · B.E. CSE (AI & ML) · Sem III · NEP 2020
**Module III · 3 teaching hours · CO3**
**Status:** selective coverage — not a complete module guide.

A compact guide to a three-hour module. It covers the whole prescribed core: what a function is,
the three types, composition and inverses.

**Covered:** definition, domain, codomain, range, image and preimage · injective, surjective and
bijective tests · composition and its order · inverse functions and verification · the Summer 2026
discount-and-tax application.

**Deliberately skipped:** neural networks, insurance risk, tax brackets and vending machines in depth ·
advanced function theory · dozens of composition variations. These are self-learning or extension
material, not core exam method.

---

## 1. Functions: definition and vocabulary

**Teacher's definition (Module 3 PPT, slide 3).** A function f from A to B is defined if for every
element a ∈ A there exists a **unique** element b ∈ B such that f(a) = b, that is (a, b) ∈ f.

A is the **domain**, B is the **codomain**. If f(a) = b, then b is the **image** of a and a is a
**pre-image** of b. The **range** is the set of all images of elements of A. Functions are also called
mappings or transformations, written f : A → B.

**Simple meaning.** A machine with one input slot and one output slot. You put in an element of A and
get back exactly one element of B. No input is left without an output, and no input produces two
different outputs.

**The essential rule — two halves.**

1. **Every** element of the domain must be used. If some a ∈ A has no image, it is not a function
   from A to B.
2. **Exactly one** image per element. If some a has two images, it is not a function.

Different inputs may share an output. That is still a function. "Unique output" does not mean
"different output".

| Term | Meaning | How to find it |
|---|---|---|
| Domain | the set you start from, A | given, or all first coordinates |
| Codomain | the set you map into, B | given in the question |
| Range | outputs that actually occur | collect all f(a); range ⊆ codomain |
| Image of a | the single value f(a) | substitute a |
| Pre-image of b | every a with f(a) = b | solve f(a) = b |

**Relation versus function.** Every function is a relation, but not every relation is a function. A
relation becomes a function when each first coordinate appears exactly once and the domain equals A.

**Testing a set of ordered pairs.**

1. The first coordinates must be exactly the elements of A — none missing.
2. No first coordinate may be repeated with a different second coordinate.
3. If both checks pass it is a function; the range is the set of second coordinates that occur.

### Worked example — is it a function? (teacher's examples)

**(a)** A = {1,2,3}, B = {a,b,c}, f = {(1,a), (2,b), (3,c)}. Every input appears once with one image.
It is a function. Domain = A, range = {a,b,c} = B.

**(b)** A = {1,2,3}, B = {a,b,c}, f = {(1,a), (2,b), (3,a)}. All inputs appear once; 1 and 3 share the
image a, which is allowed. It is a function with range {a,b}.

**(c)** A = {1,2,3,4}, B = {a,b,c}, f = {(1,a), (2,a), (3,b)}. The first coordinates are {1,2,3}, but
A = {1,2,3,4}. Element 4 has no image, so **f is not a function from A to B** (teacher's slide 4).

**(d)** A = {1,2,3}, f = {(1,a), (1,b), (2,c), (3,a)}. Input 1 has two images, so it is not a function.

### Common mistakes

- Saying "not a function" because two inputs share an output — that is allowed.
- Forgetting that every element of A must appear.
- Writing the range as the codomain.
- Confusing the image of a (one value) with the pre-image of b (a set).

**Quick check 1.** A = {1,2,3,4}, B = {p,q,r}. Which are functions from A to B?
(i) f = {(1,p),(2,q),(3,r),(4,p)} (ii) g = {(1,p),(2,p),(3,p)}
(iii) h = {(1,q),(2,r),(3,q),(4,q)} (iv) k = {(1,p),(2,q),(2,r),(3,q),(4,p)} *(Answer Q1.)*

---

## 2. Injective, surjective, bijective

**Teacher's definitions (slides 5, 8, 11, 12).**

- **Injective (one-to-one):** distinct elements of the domain have distinct images.
  > f(a₁) = f(a₂) ⇒ a₁ = a₂
- **Surjective (onto):** for every b ∈ B there is some a ∈ A with f(a) = b. Every codomain element
  has at least one pre-image.
- **Bijective:** both injective and surjective — a one-to-one correspondence.

| Type | Question it answers | Disprove it by finding | Prove it by |
|---|---|---|---|
| Injective | do different inputs give different outputs? | two different inputs with the same output | assuming f(a₁) = f(a₂) and deriving a₁ = a₂ |
| Surjective | does every codomain element get hit? | one codomain element with no pre-image | taking arbitrary b ∈ B and constructing a ∈ A with f(a) = b |
| Bijective | both at once? | either failure above | proving both separately |

**Quick size check for finite sets.** Injective needs |A| ≤ |B|; surjective needs |A| ≥ |B|;
bijective needs |A| = |B|. These are necessary conditions, so a size mismatch is an instant disproof,
but they do not by themselves prove the property for a particular function.

### Worked example 1 — f(x) = x² from Z to Z (teacher's example)

**Injective?** f(1) = 1 and f(−1) = 1. Two different inputs, one output ⇒ **not injective**.

**Surjective?** Take b = 2. No integer squares to 2 (1² = 1, 2² = 4), so 2 has no pre-image ⇒
**not surjective**.

**Bijective?** No.

**Answer-sheet form.** "f(1) = f(−1) = 1 with 1 ≠ −1, hence not injective. 2 ∈ Z has no pre-image in Z,
hence not surjective. Therefore not bijective."

### Worked example 2 — f(x) = x + 1 from Z to Z (teacher's example)

**Injective.** Suppose f(x) = f(y). Then x + 1 = y + 1, so x = y. Hence injective.

**Surjective.** Let b be any integer in the codomain. Choose x = b − 1, which is an integer. Then
f(b − 1) = (b − 1) + 1 = b. Hence surjective.

**Bijective.** Injective and surjective ⇒ bijective.

The injective proof compares two outputs; the surjective proof starts from an arbitrary codomain element
and constructs an input. They are different arguments and both are needed.

### Worked example 3 — finite sets

A = {a,b,c,d}, B = {1,2,3,4}, f = {(a,4),(b,2),(c,1),(d,3)}. The images 4, 2, 1, 3 are all different
⇒ injective. The range is {1,2,3,4} = B ⇒ surjective. Hence bijective.

### Common mistakes

- Proving injectivity by checking a few values; a proof needs the general case.
- Confusing "not injective" with "not a function".
- Checking surjectivity against the range instead of the codomain.
- Forgetting that the domain matters: x² is not injective on Z but is injective on the non-negative
  integers.

**Quick check 2.** Test for injective, surjective, bijective, with a reason:
(i) f : Z → Z, f(x) = 2x (ii) g : Z → Z, g(x) = x − 3 (iii) h : R → R, h(x) = x². *(Answer Q2.)*

---

## 3. Composition of functions

**Teacher's definition (slide 14).** Let f : A → B and g : B → C. The composition of f and g is
denoted g ∘ f : A → C and defined by

> (g ∘ f)(a) = g(f(a))

The composition of functions is not commutative: in general f ∘ g ≠ g ∘ f.

**How to read the symbol.** g ∘ f is "g after f". The function nearest the input is applied first.
In (g ∘ f)(x), compute f(x), then feed that into g.

**Notation warning.** Your slides use both **g ∘ f** and **gof** for the same thing. Some textbooks
write fg instead. The safe rule that never changes: **the inside function runs first.**

**Domain condition.** For g ∘ f to make sense, the range of f must lie inside the domain of g.

**Procedure.** Identify inside and outside → substitute the whole inside formula → expand and
simplify → if asked for both orders, swap and compare.

### Worked example — the teacher's pair (slide 15)

f : Z → Z, f(x) = 2x + 3 and g : Z → Z, g(x) = 3x + 2.

**(f ∘ g)(x) = f(g(x)) = f(3x + 2) = 2(3x + 2) + 3 = 6x + 4 + 3 = 6x + 7.**

**(g ∘ f)(x) = g(f(x)) = g(2x + 3) = 3(2x + 3) + 2 = 6x + 9 + 2 = 6x + 11.**

6x + 7 ≠ 6x + 11, so f ∘ g ≠ g ∘ f: composition is not commutative.

**Numerical check.** At x = 10: g(10) = 32, f(32) = 67 = 6(10) + 7. f(10) = 23, g(23) = 71 = 6(10) + 11. ✓

### Verified University question — Summer 2026 Q.2(b), 7 marks

A shirt costs Rs. 1000. The store gives 15% discount, then applies 8% sales tax to the discounted price.
Develop functions, form the composite, compute the final amount.

**Step 1 — define the functions.** Let p be the marked price.

> d(p) = p − 0.15p = 0.85p · t(p) = p + 0.08p = 1.08p

**Step 2 — choose the order.** The discount happens first, so the discounted price is the input to tax:

> (t ∘ d)(p) = t(d(p)) = t(0.85p) = 1.08(0.85p) = 0.918p

**Step 3 — compute.** (t ∘ d)(1000) = 0.918 × 1000 = **918**.

**Step 4 — check by hand.** 15% of 1000 = 150, discounted price 850. Tax 8% of 850 = 68. Total
850 + 68 = 918. ✓

**Step 5 — interpretation.** The composite collapses a two-step billing rule into one formula, 0.918p.
The software computes the final price in one call, the rule is reusable for any marked price, and the
order of steps is recorded in the composition.

**Honest note about order.** Both steps here are pure percentage multiplications, and
0.85 × 1.08 = 1.08 × 0.85, so reversing the order happens to give the same number. The order still
matters in the definition — tax is computed on the discounted price — and it changes the answer as soon
as a step involves a fixed amount. With a flat Rs. 100 discount, t ∘ d gives 1.08(p − 100) = 972 at
p = 1000, while d ∘ t gives 1.08p − 100 = 980. Do not claim the two orders always differ; check the
actual functions.

### Common mistakes

- Applying the outside function first.
- Substituting only x instead of the whole inner expression.
- Assuming composition is commutative.
- Losing a term in expansion: 2(3x + 2) = 6x + 4, not 6x + 2.

**Quick check 3.** f(x) = x + 1, g(x) = 2x² + 3 on R. Find f ∘ g and g ∘ f; are they equal?
*(Answer Q3.)*

---

## 4. Inverse functions

**Teacher's definition (slides 16–17).** Let f : A → B be bijective with f(a) = b. The inverse is
f⁻¹ : B → A defined by f⁻¹(b) = a, where a ∈ A and b ∈ B. If the inverse can be defined, f is
**invertible**. If f is not bijective, an inverse from the full codomain back to the full domain cannot
be defined.

For a bijection f : A → B:

> (f ∘ f⁻¹)(x) = x for x ∈ B · (f⁻¹ ∘ f)(x) = x for x ∈ A

**Simple meaning.** The inverse undoes the function. If f sends 3 to 7, f⁻¹ sends 7 back to 3.

**Why bijectivity is required.** If f is not injective, two inputs share an output and the reverse rule
cannot decide which to return. If f is not surjective, some codomain element has no pre-image and the
reverse rule has nothing to return. Injectivity gives uniqueness; surjectivity gives coverage.

**Algebraic method.** Write y = f(x) → solve for x in terms of y → swap x and y → verify both identities.

### Worked example — f(x) = 2x + 3, f : R → R (IAT question)

1. y = 2x + 3
2. y − 3 = 2x ⇒ x = (y − 3)/2
3. Swap names: **f⁻¹(x) = (x − 3)/2**

**Verify.** f(f⁻¹(x)) = 2[(x − 3)/2] + 3 = (x − 3) + 3 = x ✓
f⁻¹(f(x)) = [(2x + 3) − 3]/2 = 2x/2 = x ✓

**Numerical check.** f(5) = 13 and f⁻¹(13) = 5 ✓

**Answer-sheet form.** Four steps, then the two verifications under headings, then the boxed answer.
The verification usually carries marks.

### Worked example — inverse of a finite function (teacher's Example 2.19)

A = {a,b,c}, B = {1,2,3}, f = {(a,1), (b,3), (c,2)}. The images 1, 3, 2 are all different ⇒ injective;
every element of B appears ⇒ surjective; hence bijective and invertible. Reverse each pair:

> f⁻¹ = {(1,a), (3,b), (2,c)} = {(1,a), (2,c), (3,b)}

The domain of f⁻¹ is B and its range is A.

### Worked example — when there is no inverse

f : Z → Z, f(x) = x² is neither injective nor surjective, so no f⁻¹ : Z → Z exists. Restrict the domain
to the non-negative integers and the codomain to perfect squares and the same formula becomes bijective,
with inverse the positive square root. The formula did not change; the domain and codomain did.

### Common mistakes

- Writing f⁻¹(x) = 1/f(x). The −1 denotes the inverse function, not a reciprocal.
- Finding a formula but skipping verification.
- Forgetting to swap x and y at the end.
- Claiming an inverse exists for a non-bijective function.
- Reversing pairs without swapping domain and codomain.

**Quick check 4.** (a) f : R → R, f(x) = 5x − 7. Find f⁻¹ and verify both identities.
(b) f = {(1,4),(2,5),(3,6)}. Write f⁻¹. *(Answer Q4.)*

---

## Practice questions

**Q1.** Which of f, g, h, k are functions from A = {1,2,3,4} to B = {p,q,r}? Give each range.
(i) f = {(1,p),(2,q),(3,r),(4,p)} (ii) g = {(1,p),(2,p),(3,p)}
(iii) h = {(1,q),(2,r),(3,q),(4,q)} (iv) k = {(1,p),(2,q),(2,r),(3,q),(4,p)}

**Q2.** Test for injective, surjective, bijective, with reasons:
(i) f : Z → Z, f(x) = 2x (ii) g : Z → Z, g(x) = x − 3 (iii) h : R → R, h(x) = x².

**Q3.** f(x) = x + 1, g(x) = 2x² + 3 on R. Find f ∘ g and g ∘ f; are they equal?

**Q4.** (a) f : R → R, f(x) = 5x − 7. Find f⁻¹ and verify both identities.
(b) f = {(1,4),(2,5),(3,6)}. Write f⁻¹.

**Q5.** Define function, domain, codomain and range in one line each. Give a relation on {1,2,3} that is
not a function.

**Q6.** *(IAT sample)* A = {2,4,6}, B = {a,b,c,d}, f = {(2,b),(4,a),(6,d)}. Show f is one-to-one.
Is it onto? Is it bijective?

**Q7.** *(Summer 2026 Q.2(b) style)* An item costs Rs. 2000. A 20% discount is applied, then 5% tax on
the discounted price. Define the functions, form the composite, compute the final price. Then repeat
with a flat Rs. 200 discount and say whether order now matters.

**Q8.** f : R → R, f(x) = x³ and g : R → R, g(x) = x^(1/3). Show they are inverses.

**Q9.** For f(x) = 3x − 4 on R, find f⁻¹, verify, and explain why f is invertible.

---

## Answer key

### Q1

**f** is a function (all four inputs once); range {p,q,r}.
**g** is not a function from A to B: 4 has no image.
**h** is a function; range {q,r}.
**k** is not a function: input 2 has two images, q and r.

### Q2

**(i) f(x) = 2x on Z.** Injective: 2x = 2y ⇒ x = y. Not surjective: 3 has no integer pre-image
(2x = 3 gives x = 1.5). Not bijective.

**(ii) g(x) = x − 3 on Z.** Injective: x − 3 = y − 3 ⇒ x = y. Surjective: for b ∈ Z take x = b + 3 ∈ Z.
Bijective.

**(iii) h(x) = x² on R.** Not injective: h(2) = h(−2) = 4. Not surjective onto R: −1 has no real
pre-image. Not bijective.

### Q3

f(g(x)) = (2x² + 3) + 1 = **2x² + 4**.
g(f(x)) = 2(x + 1)² + 3 = 2(x² + 2x + 1) + 3 = **2x² + 4x + 5**.
Not equal (at x = 0: 4 vs 5). Composition is not commutative.

### Q4

**(a)** y = 5x − 7 ⇒ x = (y + 7)/5 ⇒ **f⁻¹(x) = (x + 7)/5**.
f(f⁻¹(x)) = 5[(x + 7)/5] − 7 = (x + 7) − 7 = x ✓
f⁻¹(f(x)) = [(5x − 7) + 7]/5 = 5x/5 = x ✓

**(b)** f⁻¹ = {(4,1), (5,2), (6,3)}.

### Q5

A function f : A → B assigns to every a ∈ A exactly one f(a) ∈ B. Domain = A; codomain = B;
range = outputs that occur, a subset of B.
Not a function: {(1,2), (1,3), (2,1), (3,1)} (input 1 has two images), or {(1,2), (2,3)} (3 has no image).

### Q6

Images are b, a, d — all different ⇒ injective. The codomain is {a,b,c,d} and c has no pre-image, so it
is **not onto**; range {a,b,d} ≠ B. Hence **not bijective**. (Also |A| = 3 < |B| = 4, so onto is
impossible.)

### Q7

20% discount: d(p) = 0.80p. 5% tax: t(p) = 1.05p. Final = t(d(p)) = 1.05 × 0.80p = 0.84p.
At p = 2000: 0.84 × 2000 = **Rs. 1680**. Check: discount 400, price 1600, tax 80, total 1680 ✓

Flat Rs. 200 discount: d(p) = p − 200, so t(d(p)) = 1.05(p − 200) = 1.05p − 210 = **1890** at p = 2000.
The reversed order gives 1.05p − 200 = 1900. Order matters now because one step is a fixed amount.

### Q8

(f ∘ g)(x) = (x^(1/3))³ = x. (g ∘ f)(x) = (x³)^(1/3) = x. Both compositions are the identity, so
g = f⁻¹ and f = g⁻¹.

### Q9

y = 3x − 4 ⇒ x = (y + 4)/3 ⇒ **f⁻¹(x) = (x + 4)/3**.
f(f⁻¹(x)) = 3[(x + 4)/3] − 4 = x ✓ ; f⁻¹(f(x)) = [(3x − 4) + 4]/3 = x ✓
f is invertible because it is bijective: 3x − 4 = 3y − 4 ⇒ x = y (injective), and for any b ∈ R,
x = (b + 4)/3 is real with f(x) = b (surjective).

---

## Last-minute revision sheet

**Definitions.** Function: every input has exactly one image · domain/codomain/range: inputs/target/
outputs that occur · image f(a) / pre-image every a with f(a) = b · injective: f(a₁) = f(a₂) ⇒ a₁ = a₂ ·
surjective: every codomain element is hit · bijective: both · composition: (g ∘ f)(x) = g(f(x)),
inside first · inverse: f⁻¹(b) = a exactly when f(a) = b, exists only for bijections.

**Procedures.** Is it a function? all inputs used once · injective? assume equal outputs, derive equal
inputs · surjective? take arbitrary b and construct a · compose? substitute whole inner formula, expand ·
inverse? y = f(x) → solve → swap → verify both identities.

**Checks.** Domain and codomain stated? Counterexample for every "not"? Inside function first?
Both inverse identities verified? Answer written in x, not y?

---

## Sources, verification and coverage

**Teacher material.** Mrs. Shamal Bagal, *Module 3: Functions* (PowerPoint, 20 slides): function
definition, domain, codomain, image, pre-image, range; injective, surjective, bijective definitions and
examples; composition; inverse function and the two identities; the finite inverse example. Teacher's
examples are from slides 3–19.

**Official scope.** University of Mumbai DSGT (2023112), Module III — Functions, 3 hours, CO3.
Prescribed: injective, surjective, bijective functions, composition, inverse functions, real-life
applications. Self-learning: neural networks, insurance risk factors, taxes and tax brackets, vending
machines.

**Questions.** Summer 2026 Q.2(b) — discount and tax, data preserved (Rs. 1000, 15%, 8%); an extra flat
discount variation was added as Q7. IAT sample — f(x) = 2x + 3 inverse and the one-to-one ordered-pair
question, adapted as Q6. Q1–Q5 and Q7–Q9 are written for this guide and are not claimed to be university
questions.

**Verification performed.** Compositions checked algebraically and numerically (at x = 10, f ∘ g = 67,
g ∘ f = 71). Discount/tax checked two ways: 0.918 × 1000 = 918 and 850 + 68 = 918. Both inverse
identities verified symbolically for 2x + 3, 5x − 7 and 3x − 4. The claim that order does not change a
two-percentage computation was checked and stated honestly rather than presented as a general rule.

**Not covered.** Neural networks, insurance and taxation case studies, vending machines, advanced
abstract function theory, large sets of composition variations. Deliberate omissions, not oversights.
