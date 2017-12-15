# gpa.py
# Program to find student with highest GPA
class Student:
    def __init__(self, name, creds, qpoints):
        self.name = name
        self.creds = float(creds)
        self.qpoints = float(qpoints)

    def getName(self):
        return self.name

    def getCreds(self):
        return self.creds

    def getQPoints(self):
        return self.qpoints

    def gpa(self):
        return self.qpoints/self.creds

def makeStudent(infoStr):
    # infoStr is a tab-separated line: name creds qpoints
    # returns a corresponding Student object
    name, creds, qpoints = infoStr.split("\t")
    return Student(name, creds, qpoints)

def main():
    # open the input file for reading
    filename = input("Enter the name of the grade file: ")
    infile = open(filename, 'r')
    # set best to the record for the first student in the file
    best = makeStudent(infile.readline())
    # process subsequent lines of the file
    for line in infile:
        # turn the line into a student record
        s = makeStudent(line)
        # if this student is best so far, remember it.
        if s.gpa() > best.gpa():
            best = s
    infile.close()
    # print information about the best student
    print("The student with highest GPA:", best.getName())
    print("GPA:", best.gpa())

if __name__ == '__main__':
    main()
