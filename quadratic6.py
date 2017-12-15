# quadratic6.py
import math 
def main():
    print("Find the real solutions to a quadratic.")
    try:
        a, b, c = eval(input("Enter the coefs (a, b, c):"))
        discRoot = math.sqrt(b * b - 4 * a * c)
        root1 = (-b + discRoot) / (2 * a)
        root2 = (-b - discRoot) / (2 * a)
        print("The solutions are:", root1, root2 )
    except ValueError as excObj:
        if str(excObj) == "math domain error":
            print("VE: No Real Roots")
        else:
            print("VE: You didn't give me the right number of coefs.")
    except NameError:
        print("NE: A variable is not defined.")
    except TypeError:
        print("TE: Your inputs were not all numbers.")
    except SyntaxError:
        print("SE: Inputs were not in the correct form.")
    except:
        print("Something went wrong, sorry!")
main()
