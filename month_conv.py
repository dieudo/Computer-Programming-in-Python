# month_conv.py
def main():
    months = ["Jan", "Feb", "Mar", "Apr",
              "May", "Jun", "Jul", "Aug",
              "Sep", "Oct", "Nov", "Dec"]   
    n = eval(input("Enter a month number between 1 and 12: "))

    print("The month abbreviation is", months[n-1] + ".")

main()
