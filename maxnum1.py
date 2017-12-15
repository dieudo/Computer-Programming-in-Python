# maxnum1.py
# Find the maximum of a series of numbers

def main():
    x1,x2,x3 = eval(input("Enter three values:"))
    max = x1
    if x2 > max:
        max = x2
    if x3 > max:
        max = x3
    print("The largest value is", max)

main()
