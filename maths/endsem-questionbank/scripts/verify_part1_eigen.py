"""Independent verification for Module I of the MUSA 2026 question bank.

Run:  python _work/endsem/verify_part1_eigen.py
All arithmetic is exact (SymPy), so any output here is a proof of the result
*given* the transcribed matrix. Visual comparison with the scanned page
remains necessary to confirm the matrix itself.
"""

from sympy import Matrix, Rational, eye, factor, symbols, pprint

lam = symbols("lam")

EIGEN = {
    "M1-EV-Q1-i": Matrix([[2, -1, 1], [1, 2, -1], [1, -1, 2]]),
    "M1-EV-Q1-ii": Matrix([[2, 2, 1], [1, 3, 1], [1, 2, 2]]),
    "M1-EV-Q1-iii": Matrix([[2, 1, 1], [2, 3, 2], [3, 3, 4]]),
    "M1-EV-Q1-iv": Matrix([[6, -2, 2], [-2, 3, -1], [2, -1, 3]]),
    "M1-EV-Q1-v": Matrix([[8, -6, 2], [-6, 7, -4], [2, -4, 3]]),
    "M1-EV-Q1-vi": Matrix([[1, 0, 0], [0, 3, -1], [0, -1, 3]]),
    "M1-EV-Q1-vii": Matrix([[-2, 2, -3], [2, 1, -6], [-1, -2, 0]]),
}

for name, A in EIGEN.items():
    print("=" * 70)
    print(name, "  A =", A.tolist())
    cp = A.charpoly(lam).as_expr()
    print("char poly  :", factor(cp))
    print("char eq    : det(A - lam I) = 0   ->", factor(cp), "= 0")
    print("trace      :", A.trace(), "  det:", A.det())
    print("eigenvals  :", A.eigenvals())          # {value: multiplicity}
    print("eigenvects :")
    for val, mult, vecs in A.eigenvects():
        print("   lam =", val, " alg.mult =", mult, " geo.mult =", len(vecs))
        for v in vecs:
            print("      ", v.T.tolist())
    print("diagonalisable:", A.is_diagonalizable())

print("=" * 70)
print("M1-EV-Q2-i   A^3 + 5A + 8I")
A = Matrix([[-1, 2, 3], [0, 3, 5], [0, 0, -2]])
print("A char poly:", factor(A.charpoly(lam).as_expr()))
print("eig(A):", A.eigenvals())
M = A**3 + 5 * A + 8 * eye(3)
print("A^3+5A+8I =", M.tolist())
print("eig of expression, direct  :", M.eigenvals())
print("eig of expression, spectral:", {factor(l**3 + 5 * l + 8): m for l, m in A.eigenvals().items()})

print("=" * 70)
print("M1-EV-Q2-ii   A^2 - 2A + I")
A = Matrix([[2, 3, 4], [0, 4, 2], [0, 0, 3]])
print("A char poly:", factor(A.charpoly(lam).as_expr()))
print("eig(A):", A.eigenvals())
M = A**2 - 2 * A + eye(3)
print("A^2-2A+I =", M.tolist())
print("eig of expression, direct  :", M.eigenvals())
print("eig of expression, spectral:", {factor(l**2 - 2 * l + 1): m for l, m in A.eigenvals().items()})
