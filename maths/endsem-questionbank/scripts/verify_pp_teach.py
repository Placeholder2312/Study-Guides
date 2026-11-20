from sympy import Matrix, factor, symbols, nsimplify

lam = symbols("lam")


def show(name, A):
    print("=" * 60)
    print(name, A.tolist())
    print("char:", factor(A.charpoly(lam).as_expr()), "| trace:", A.trace(), "| det:", A.det())
    for val, mult, vecs in A.eigenvects():
        for v in vecs:
            # clear denominators to a primitive integer vector
            den = 1
            for e in v:
                den = den * e.q if hasattr(e, "q") else den
            w = Matrix([e * den for e in v])
            from sympy import gcd
            g = 0
            for e in w:
                g = gcd(g, abs(int(e)))
            w = Matrix([int(e) // g for e in w]) if g else w
            print(f"  lam={val}  v={w.T.tolist()}   A*v={(A * w).T.tolist()}")


show("PP-Q4b", Matrix([[3, -1, 1], [-1, 5, -1], [1, -1, 3]]))
show("TEACH-2x2", Matrix([[4, 1], [2, 3]]))
show("TEACH-3x3", Matrix([[0, 1, 1], [1, 0, 1], [1, 1, 0]]))
