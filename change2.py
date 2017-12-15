# change2.py
# A prog to calculate the value of some change in dollars

def main():
    print("Change Counter\n")
    print("Please enter the count of each type of coins.")
    quarters = eval(input("Quarters: "))
    dimes = eval(input("Dimes: "))
    nickels = eval(input("Nickels: "))
    pennies = eval(input("Pennies: "))
    total = quarters * 25 + dimes * 10 + nickels * 5 + pennies

    print("Your change is ${0:0.2f}".format(total/100))

main()
