# factorial.py
# Compute the factorial of a number
# Illustrates the for loop with an accumulator
def main():
    n = eval(input("Enter a whole number: "))
    fact = 1
    for i in range(n,1,-1): 
        fact = fact * i
    print("The factorial of", n, "is", fact)

main()
