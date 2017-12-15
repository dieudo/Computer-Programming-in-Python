# userfile.py
def main():
    print("Create a file of usernames in batch mode.")
    infileName =input("What file are the names in?")
    infile = open(infileName, 'r')
    
    outfileName=input("What file should the usernames go in?")
    outfile = open(outfileName, 'w')
    
    # process each line of the input file
    for line in infile:
        first, last = line.split()
        uname = (first[0]+last[:7]).lower()
        print(uname, file=outfile)
    infile.close()
    outfile.close()
    print("Usernames have been written to", outfileName)

main()
