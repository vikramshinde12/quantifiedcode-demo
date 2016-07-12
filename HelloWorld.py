
def helloWorld(myString):
 """ Displays Hello World """
    print("Hello : "+myString)
    my_name = input("What is your name?")
    print(my_name)
    my_var = input("Enter the number:")

    if my_name == "Vikram" and my_var == 0:
        print("Vikram Is Great !!")
    elif(my_name == 'Shinde'):
        print("you are also Great !!")
    else:
        print("hello world")

helloWorld('Vikram')