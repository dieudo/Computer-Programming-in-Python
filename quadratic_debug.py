# quadratic_debug.py
import math  # Makes the math library available.
def main():
    print("Find the real solutions to a quadratic.")
    a, b, c = eval(input("Enter the coef (a, b, c): "))
    discRoot = math.sqrt(b * b - 4 * a * c)
    root1 = -b + discRoot / (2 * a)
    root2 = -b - discRoot / (2 * a)
    print("The solutions are:", root1, root2 )

main()