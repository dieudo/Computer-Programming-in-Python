# post_test2.py
def main():
    while True:
        number = eval(input("Enter a positive number:"))
        if number > 0: 
            break    # Exit loop if number is valid

    print("The positive number is", number)
    
main()
