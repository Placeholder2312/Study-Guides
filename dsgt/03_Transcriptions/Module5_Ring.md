## RING

## INTRODUCTION

Rings are a fundamental concept in algebraic mathematics that consist of a set equipped with two operations, addition and multiplication, that satisfy certain properties.

Rings have wide-ranging applications across different branches of mathematics, including algebraic geometry, number theory, coding theory, and more.

The purpose of this presentation is to provide an overview of the properties and examples of rings, as well as their applications.

The scope of the presentation will include definitions and properties of rings, important examples of rings, and some applications of rings in mathematics.

DEFINITION OF RING

- A ring is a set R equipped with two operations, usually denoted by "+" for addition and "•" for multiplication, such that the following properties are satisfied:

- (R, +) is an abelian group
- Multiplication is associative: a • (b • c) = (a • b) • c for all a, b, c in R
- Multiplication distributes over addition: a • (b + c) = a • b + a • c and (a + b)
- c = a • c + b • c for all a, b, c in R
- There exists an element 0 in R such that a + 0 = a for all a in R
- For all a in R, there exists an element -a in R such that a + (-a) = 0
- The multiplication operation need not have an identity element
- Examples of rings include the integers, polynomial rings, and matrices
- Rings differ from other algebraic structures, such as groups and fields, in that they have two binary operations instead of one, and the multiplication operation need not have an identity element.

## RING PROPERTIES

A ring must satisfy several essential properties, including:

Closure under addition and multiplication: for any elements a and b in the ring, a + b and a • b must also be in the ring

Associativity of addition and multiplication: (a + b) + c = a + (b + c) and (a • b) • c = a • (b • c) for all a, b, and c in the ring

Distributivity of multiplication over addition: a • (b + c) = a • b + a • c and (a + b) • c = a • c + b • c for all a, b, and c in the ring

Existence of additive identity and inverse: there exists an element 0 in the ring such that a + 0 = a for all a in the ring, and for every a in the ring, there exists an element -a in the ring such that a + (-a) = 0

Examples of rings that satisfy these properties include the integers, polynomial rings, and matrices

These properties are important because they allow us to manipulate and solve equations involving elements of the ring, which has numerous applications in mathematics and beyond.

## **COMMUTATIVE RINGS**

A commutative ring is a ring in which the multiplication operation is commutative, meaning that a • b = b • a for all elements a and b in the ring

Commutative rings differ from general rings in that the multiplication operation is commutative, while general rings do not necessarily have commutative multiplication

Examples of commutative rings include the integers, polynomial rings, and fields

Commutativity  is  important  because  it  simplifies  calculations  and  allows  for  the  use  of geometrical interpretations. For example, commutativity of multiplication in a polynomial ring enables us to easily determine the roots of a polynomial, while non-commutativity in matrix rings can have geometric interpretations in terms of rotations and reflections.

## INTEGRAL DOMAINS

An integral domain is a commutative ring in which there are no zero divisors, meaning that if a • b = 0 for elements a and b in the ring, then either a or b must be 0

Integral domains differ from general rings in that they are commutative and do not have zero divisors

Examples of integral domains include the integers, polynomial rings, and fields

Integral domains are important because they ensure unique factorization of elements into primes, which is a fundamental property of numbers. They also enable us to solve equations, such as polynomial equations and Diophantine equations, and have numerous applications in algebraic geometry and number theory.

FIELD

- A  field  is  a  commutative  ring  in  which  every nonzero element has a multiplicative inverse
- Fields  differ  from  general  rings  in  that  every nonzero element has a multiplicative inverse
- Examples of fields include the rational numbers, real numbers, complex numbers, and finite fields
- Fields  are  important  because  they  enable  us  to solve   all   polynomial   equations,   as   every non-constant polynomial with coefficients in a field has a root in an extension field. Fields also provide a foundation for calculus and analysis, as they are the underlying  structure  for  the  real  numbers  and enable us to define limits, derivatives, and integrals.

## SUBRINGS

A subring is a subset of a ring that is itself a ring under the same operations of addition and multiplication

Subrings relate to the concept of a ring because they are a natural way to study properties of smaller rings within larger ones

Examples of subrings include the even integers as a subring of the integers, and the polynomials with integer coefficients as a subring of the polynomial ring with real coefficients

Subrings are important because they enable us to study properties of smaller rings within larger ones, such as proving theorems about the integers using only properties of the even integers as a subring.

They also provide a way to understand the structure of a ring by analyzing its subrings.

RING HOMOMORP

HISMS

- A ring homomorphism is a function between two rings that preserves  the  ring  structure,  meaning  it  preserves  the operations of addition and multiplication
- Ring  homomorphisms  relate  to  the  concept  of  a  ring because  they  provide  a  way  to  study  the  structure  and properties  of  rings  through  maps  that  preserve  their algebraic properties
- Examples of ring homomorphisms include the natural map from the integers to the integers modulo n, which preserves addition and multiplication modulo n
- Ring homomorphisms are important because they enable us to study the structure and properties of rings through maps  that  preserve  their  algebraic  properties,  such  as studying properties of the integers modulo n by studying the natural map from the integers to the integers modulo n. They also provide a way to compare and relate different rings, such as proving that two rings are isomorphic (i.e., structurally equivalent) by finding a ring homomorphism between them.

APPLICATI

ON OF RINGS

- Rings  have  broad  applications  in  mathematics,  including  in areas such as algebraic geometry, number theory, and coding theory.
- In algebraic geometry, rings are used to study algebraic curves and  surfaces.  For  example,  the  ring  of  polynomials  in  two variables is used to study the properties of algebraic curves in the plane.
- In number theory, rings are used to study algebraic integers and their properties, which are important in understanding the behavior of prime numbers and factoring algorithms.
- In coding theory, rings are used to encode and transmit digital information. For example, rings of polynomials are used to create error-correcting  codes  that  can  detect  and  correct  errors  in digital transmissions.
- Other applications of rings include in physics, where rings are used  to  describe  the  symmetries  of  physical  systems, and  in computer science, where rings are used in cryptography and computer algebra systems.

## IF THE ADDITION & MULTIPLICATORS MODULO L0 IS DEFINED ON A SET OF INTEGERS A={0, 2, 4,6.8}. THEN DETERMINE WHETHER THIS ALGEBRAIC SYSTEM IS A RING.

+10

0

2

4

6

8

**0**

0

2

4

6

8

**2**

2

4

6

8

0

**4**

4

6

8

0

2

**6**

6

8

0

2

4

**8**

8

0

2

4

6

multiplication

⋅10

0

2

4

6

8

**0**

0

0

0

0

0

**2**

0

4

8

2

6

**4**

0

8

6

4

2

**6**

0

2

4

6

8

**8**

0

6

2

8

4

**Condition 1: (A,+10) must be an Abelian Group**

**.Closure:** Every entry in the addition table is an element of A={0,2,4,6,8}. So, the set is **closed** under addition modulo 10.

**.Associativity:** Addition of integers modulo n is always associative. This property is inherited from the integers. So, (a+b)+c=a+(b+c) holds.

**.Identity Element:** The row corresponding to 0 is identical to the header row, and the column corresponding to 0 is identical to the header column. Thus, **0 is the additive identity**.

**.Inverse Element:** For every element, we must find another element in the set that adds up to the identity (0).

- Inverse of 0 is 0 (since 0+0=0)
- Inverse of 2 is 8 (since 2+8=10≡0)
- Inverse of 4 is 6 (since 4+6=10≡0)
- Inverse of 6 is 4 (since 6+4=10≡0)
- Inverse of 8 is 2 (since 8+2=10≡0) Every element has an additive inverse in A.

**.Commutativity:** The addition table is symmetric about its main diagonal (e.g., 2+8=0 and 8+2=0). Thus, the operation is commutative.

**Conclusion:** (A,+10) is an abelian group.

**Condition 2: (A,**⋅**10) must be a Semigroup**

**Closure:** Every entry in the multiplication table is an element of A={0,2,4,6,8}. So, the set is **closed** under multiplication modulo 10.

**Associativity:**	Multiplication	of	integers	modulo	n	is	always	associative.	This property is inherited from the integers. So, (a⋅b)⋅c=a⋅(b⋅c) holds.

**Conclusion:** (A,⋅10) is a semigroup.

**Condition 3: Distributive Laws**

Multiplication modulo n distributes over addition modulo n. This is another property that is inherited from the ring of integers.

a⋅10(b+10c)=(a⋅10b)+10(a⋅10c) (b+10c)⋅10a=(b⋅10a)+10(c⋅10a) These laws hold for all elements in A. **Final Verdict**

Since all three conditions are satisfied: (A,+10) is an abelian group.

(A,⋅10) is a semigroup. The distributive laws hold.

**Yes, this algebraic system is a ring.**

## Consider the set of integers B={0,3,6,9} with the operations of addition and multiplication modulo 12. Determine whether this algebraic system, (B,+12,*12), is a ring.

+12

0

3

6

9

**0**

0

3

6

9

**3**

3

6

9

0

**6**

6

9

0

3

**9**

9

0

3

6

**Addition Table for (B,+12)**

⋅12

0

3

6

9

**0**

0

0

0

0

**3**

0

9

6

3

**6**

0

6

0

6

**9**

0

3

6

9

**Multiplication Table for (B,**⋅**12)**

**Condition 1: (B,+12) must be an Abelian Group**

**.Closure:** All results in the addition table are elements of B={0,3,6,9}. The set is **closed** under +12.

**.Associativity:** Integer addition modulo 12 is associative. This property is inherited.

**.Identity Element:** The row and column for the element 0 leave other elements unchanged. So, **0 is the additive identity**.

**.Inverse Element:** We look for the identity element (0) in each row:

- The inverse of 0 is 0 (since 0+0=0).
- The inverse of 3 is 9 (since 3+9=12≡0).
- The inverse of 6 is 6 (since 6+6=12≡0).
- The inverse of 9 is 3 (since 9+3=12≡0).
- Every element has an additive inverse within the set B.

**.Commutativity:** The addition table is symmetric across the main diagonal, so the operation is commutative.

**Conclusion:** (B,+12) is an abelian group.

**Condition 2: (B,**⋅**12) must be a Semigroup**

- **Closure:** All results in the multiplication table are elements of B={0,3,6,9}. The set is

**closed** under ⋅12.

- **Associativity:** Integer multiplication modulo 12 is associative. This property is inherited.

**Conclusion:** (B,⋅12) is a semigroup.

**Condition 3: Distributive Laws**

The distributive laws of multiplication over addition hold for modular arithmetic, as they are inherited from the properties of integers.

**Final Verdict**

Since all three conditions are met, **yes, the algebraic system (B,+12,**⋅**12) is a ring. Further Properties**

- This is a **commutative ring** because the multiplication table is symmetric.
- This ring has a **multiplicative identity (unity)**. If you look at the multiplication table, the element **9** acts as the unity, since for any element x∈B, x⋅129=x.
- This ring has **zero divisors**. For example, 6⋅12 6=0, even though 6 not =0.

## **THANK YOU!**
