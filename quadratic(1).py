# quadratic.py
# Computes the real roots of a quadratic equation.
# Note: It crashes if no real roots.

import math
def main():
    print("Find the real solutions to a quadratic.")
    a, b, c = eval(input("Enter the coefs (a, b, c):"))
    discrim = b * b - 4 * a * c
    discRoot = math.sqrt(discrim)
    root1 = (-b + discRoot) / (2 * a)
    root2 = (-b - discRoot) / (2 * a)
    print("The solutions are:", root1, root2)

main()
