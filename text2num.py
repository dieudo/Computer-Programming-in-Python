# text2num.py
def main():
    print("This program converts texts to numbers.")
    message = input("Enter the text: ")
    print("Here are the Unicode codes:")
    for ch in message:
        print(ord(ch),  end=" ")

main()
