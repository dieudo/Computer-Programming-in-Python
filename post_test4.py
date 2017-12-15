# post_test4.py
def main():
    while True:
        number = eval(input("Enter a positive number:"))
        if number > 0:
            break  # Loop exit
        print("The number was not positive!")

    print("The positive number is", number)
    
main()
