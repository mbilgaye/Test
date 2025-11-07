# Program I

def main():
    num = 0

    while num != 100:
        num = int(input("Enter the number: "))
        print("Checking your number: ")
    print("You have entered correct number 100!")

if __name__ =="__main__":
    main()

# Program II
def main():
    s = input("Enter the string characters: ")

    while len(s) < 20:
        print("Check the length of the string....")
        s = input("Enter the string characters again")
    print("You got it!")

if __name__ == "__main__":
    main()

# Program III
def main():
    s = input("Enter correct characters: ")

    while s != "stop" and s != "quit":
        print("Wrong characters entered, try again.....")
        s = input("Enter the characters: ")
    print("Correct and the program ends")

if __name__ == "__main__":
    main()