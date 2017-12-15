# average2.py

def main():
    sum = 0.0
    count = 0
    moredata = "yes"
    while moredata[0] == "y":
        x = eval(input("Enter a number >>"))
        sum = sum + x
        count = count + 1
        moredata = input("Have more numbers (yes or no)?")
    print("The average of the numbers is", sum / count)

main()
