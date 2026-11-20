"""QA: every intermediate (row-reduced) matrix printed in Part 1 must have the
same null space as the matrix it came from, and every claim about rank or
non-diagonalisability must be true."""

from sympy import Matrix, eye, factor, symbols

lam = symbols("lam")
ok = True


def same_null(A, R, note):
    global ok
    nA = A.nullspace()
    nR = R.nullspace()
    # both are bases of the same subspace iff ranks and mutual containment hold
    good = (len(nA) == len(nR)) and all(
        A * v == Matrix([0] * A.rows) for v in nR) and all(
        R * v == Matrix([0] * R.rows) for v in nA)
    print(f"{'OK ' if good else 'BAD'} {note}: nullspace dim {len(nA)}")
    ok &= good


print("--- M1-EV-Q1-i ---")
A = Matrix([[2, -1, 1], [1, 2, -1], [1, -1, 2]])
same_null(A - 1 * eye(3), Matrix([[1, -1, 1], [0, 2, -2], [0, 0, 0]]), "lam=1")
same_null(A - 2 * eye(3), Matrix([[1, 0, -1], [0, -1, 1], [0, 0, 0]]), "lam=2")
same_null(A - 3 * eye(3), Matrix([[1, 1, -1], [0, -2, 0], [0, 0, 0]]), "lam=3")

print("--- M1-EV-Q1-ii ---")
A = Matrix([[2, 2, 1], [1, 3, 1], [1, 2, 2]])
same_null(A - 5 * eye(3), Matrix([[1, -2, 1], [0, -4, 4], [0, 4, -4]]), "lam=5")
same_null(A - 1 * eye(3), Matrix([[1, 2, 1], [0, 0, 0], [0, 0, 0]]), "lam=1")

print("--- M1-EV-Q1-iii ---")
A = Matrix([[2, 1, 1], [2, 3, 2], [3, 3, 4]])
same_null(A - 7 * eye(3), Matrix([[1, 0, "-1/3"], [0, 1, "-2/3"], [0, 0, 0]]), "lam=7")
same_null(A - 1 * eye(3), Matrix([[1, 1, 1], [0, 0, 0], [0, 0, 0]]), "lam=1")

print("--- M1-EV-Q1-iv ---")
A = Matrix([[6, -2, 2], [-2, 3, -1], [2, -1, 3]])
same_null(A - 8 * eye(3), Matrix([[1, 1, -1], [0, -3, -3], [0, 0, 0]]), "lam=8")
same_null(A - 2 * eye(3), Matrix([[2, -1, 1], [0, 0, 0], [0, 0, 0]]), "lam=2")

print("--- M1-EV-Q1-v ---")
A = Matrix([[8, -6, 2], [-6, 7, -4], [2, -4, 3]])
same_null(A - 15 * eye(3), Matrix([[1, 0, -2], [0, 1, 2], [0, 0, 0]]), "lam=15")
same_null(A - 3 * eye(3), Matrix([[1, 0, 1], [0, 1, "1/2"], [0, 0, 0]]), "lam=3")
same_null(A, Matrix([[1, 0, "-1/2"], [0, 1, -1], [0, 0, 0]]), "lam=0")

print("--- M1-EV-Q1-vi ---")
A = Matrix([[1, 0, 0], [0, 3, -1], [0, -1, 3]])
same_null(A - 1 * eye(3), Matrix([[0, 0, 0], [0, 2, -1], [0, -1, 2]]), "lam=1")
same_null(A - 2 * eye(3), Matrix([[-1, 0, 0], [0, 1, -1], [0, -1, 1]]), "lam=2")
same_null(A - 4 * eye(3), Matrix([[-3, 0, 0], [0, -1, -1], [0, -1, -1]]), "lam=4")

print("--- M1-EV-Q1-vii ---")
A = Matrix([[-2, 2, -3], [2, 1, -6], [-1, -2, 0]])
same_null(A - 5 * eye(3), Matrix([[1, 0, 1], [0, 1, 2], [0, 0, 0]]), "lam=5")
same_null(A + 3 * eye(3), Matrix([[1, 2, -3], [0, 0, 0], [0, 0, 0]]), "lam=-3")

print("--- PP25-Q4-b ---")
A = Matrix([[3, -1, 1], [-1, 5, -1], [1, -1, 3]])
same_null(A - 2 * eye(3), Matrix([[1, -1, 1], [0, 2, 0], [0, 0, 0]]), "lam=2")
same_null(A - 3 * eye(3), Matrix([[1, 0, -1], [0, 1, -1], [0, 0, 0]]), "lam=3")
same_null(A - 6 * eye(3), Matrix([[1, 0, -1], [0, 1, 2], [0, 0, 0]]), "lam=6")

print("--- teaching example B ---")
A = Matrix([[0, 1, 1], [1, 0, 1], [1, 1, 0]])
same_null(A - 2 * eye(3), Matrix([[-2, 1, 1], [1, -2, 1], [1, 1, -2]]), "lam=2 (unreduced)")
same_null(A + eye(3), Matrix([[1, 1, 1], [0, 0, 0], [0, 0, 0]]), "lam=-1")

print("--- claim: B is not diagonalisable ---")
B = Matrix([[3, 1, 0], [0, 3, 0], [0, 0, 5]])
print("B char poly:", factor(B.charpoly(lam).as_expr()))
print("B eigenvalues:", B.eigenvals())
print("rank(B-3I):", (B - 3 * eye(3)).rank(), "-> geometric multiplicity",
      3 - (B - 3 * eye(3)).rank())
print("B diagonalisable:", B.is_diagonalizable())
ok &= (B.is_diagonalizable() is False)

print()
print("ALL INTERMEDIATE-STEP CHECKS PASSED:", ok)
