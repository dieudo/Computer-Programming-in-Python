# printfile.py
# Prints a file to the screen.
def main():
    fname = input("Enter filename: ")
    file1 = open(fname,'r')
    data = file1.read()
    print(data)
    file1.close()
main()
