# quadratic2.py
import math
def quadraticSolver(a, b, c):
    disc = math.sqrt(b**2 - 4 * a * c)
    root1 = (-b + disc)/(2*a)
    root2 = (-b - disc)/(2*a)
    return root1, root2

r1, r2 = quadraticSolver(1, 3, 1)
print(r1, r2)
