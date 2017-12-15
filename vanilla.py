# vanilla.py
def main():
    answer = input("What flavor do u want [vanilla]?")
    if answer:
        flavor = answer
    else:
        flavor = "vanilla"

    print("The flavor you chose is", flavor)
    
main()
