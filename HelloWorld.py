
def helloWorld(myString):
    print("Hello : "+myString)
    myName = input("What is your name?")
    print(myName)
    myVar = input("Enter the number:")

    if myName == "Vikram" and myVar == 0:
        print("Vikram Is Great !!")
    elif(myName == 'Shinde'):
        print("you are also Great !!")
    else:
        print("hello world")

helloWorld('Vikram')