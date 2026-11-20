"""Check every eigenvector that will be published in Part 1, exactly.

Exact linear algebra with SymPy: for each matrix we print the characteristic
polynomial, the teacher's coefficients S1 (trace) and S2 (sum of the three
principal 2x2 minors), the determinant, and then verify A*v = lam*v for every
eigenvector that appears in the published answer key.

Run:  python _work/endsem/verify_part1_vectors.py
"""

from sympy import Matrix, factor, symbols, simplify, gcd

lam = symbols("lam")


def s2(A):
    """Sum of the principal 2x2 minors (the teacher's S2)."""
    n = A.rows
    if n == 2:
        return A.det()
    return sum(A.extract([i, j], [i, j]).det() for i, j in [(0, 1), (0, 2), (1, 2)])


CASES = {
    "M1-EV-Q1-i": (
        Matrix([[2, -1, 1], [1, 2, -1], [1, -1, 2]]),
        [(1, Matrix([0, 1, 1])), (2, Matrix([1, 1, 1])), (3, Matrix([1, 0, 1]))],
    ),
    "M1-EV-Q1-ii": (
        Matrix([[2, 2, 1], [1, 3, 1], [1, 2, 2]]),
        [(5, Matrix([1, 1, 1])), (1, Matrix([-2, 1, 0])), (1, Matrix([-1, 0, 1]))],
    ),
    "M1-EV-Q1-iii": (
        Matrix([[2, 1, 1], [2, 3, 2], [3, 3, 4]]),
        [(7, Matrix([1, 2, 3])), (1, Matrix([-1, 1, 0])), (1, Matrix([-1, 0, 1]))],
    ),
    "M1-EV-Q1-iv": (
        Matrix([[6, -2, 2], [-2, 3, -1], [2, -1, 3]]),
        [(8, Matrix([2, -1, 1])), (2, Matrix([1, 2, 0])), (2, Matrix([-1, 0, 2]))],
    ),
    "M1-EV-Q1-v": (
        Matrix([[8, -6, 2], [-6, 7, -4], [2, -4, 3]]),
        [(15, Matrix([2, -2, 1])), (3, Matrix([-2, -1, 2])), (0, Matrix([1, 2, 2]))],
    ),
    "M1-EV-Q1-vi": (
        Matrix([[1, 0, 0], [0, 3, -1], [0, -1, 3]]),
        [(1, Matrix([1, 0, 0])), (2, Matrix([0, 1, 1])), (4, Matrix([0, -1, 1]))],
    ),
    "M1-EV-Q1-vii": (
        Matrix([[-2, 2, -3], [2, 1, -6], [-1, -2, 0]]),
        [(5, Matrix([-1, -2, 1])), (-3, Matrix([-2, 1, 0])), (-3, Matrix([3, 0, 1]))],
    ),
    "PP-Q4b": (
        Matrix([[3, -1, 1], [-1, 5, -1], [1, -1, 3]]),
        [(2, Matrix([-1, 0, 1])), (3, Matrix([1, 1, 1])), (6, Matrix([1, -2, 1]))],
    ),
    "TEACH-2x2": (
        Matrix([[4, 1], [2, 3]]),
        [(5, Matrix([1, 1])), (2, Matrix([1, -2]))],
    ),
    "TEACH-3x3": (
        Matrix([[0, 1, 1], [1, 0, 1], [1, 1, 0]]),
        [(2, Matrix([1, 1, 1])), (-1, Matrix([-1, 1, 0])), (-1, Matrix([-1, 0, 1]))],
    ),
}

ok = True
for name, (A, pairs) in CASES.items():
    print("=" * 68)
    print(name, A.tolist())
    print("  char poly :", factor(A.charpoly(lam).as_expr()))
    print("  S1:", A.trace(), "| S2:", s2(A), "| det:", A.det())
    print("  eigenvals :", A.eigenvals())
    for val, v in pairs:
        res = A * v
        good = simplify(res - val * v) == Matrix([0] * v.rows)
        print(f"  lam={val:<3} v={str(v.T.tolist()):<14} A*v={str(res.T.tolist()):<14} OK={good}")
        ok &= good
    print("  diagonalisable:", A.is_diagonalizable())

print("=" * 68)
print("ALL EIGENVECTOR CHECKS PASSED:", ok)
