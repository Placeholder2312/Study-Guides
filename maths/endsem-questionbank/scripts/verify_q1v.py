from sympy import Matrix, eye

A = Matrix([[8, -6, 2], [-6, 7, -4], [2, -4, 3]])
print("A-15I rref:")
print((A - 15 * eye(3)).rref()[0])
print("A-3I rref:")
print((A - 3 * eye(3)).rref()[0])
print("A rref:")
print(A.rref()[0])
