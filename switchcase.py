print("1. is meter or 2. is feet")
name = int(input("what type of measurement you calculate :- "))


def feet():
    east = float(input("enter the east side on in feet ^ :- "))
    west = float(input("enter the west side on in feet V :- "))
    north = float(input("enter the noth side on in feet < :- "))
    south = float(input("enter the south side on in feet > :- "))

    direction1 = east + west
    direction2 = north + south

    direct1 = direction1 / 2
    direct2 = direction2 / 2

    multiply = direct1 * direct2

    squarefeet = multiply / 436

    kuli = squarefeet / 8

    print("your total cent is :- ", squarefeet)
    print("your total kuli is :- ", kuli)


def kuli():
    east1 = float(input("enter the east side on in feet ^ :- "))
    west1 = float(input("enter the west side on in feet V :- "))
    north1 = float(input("enter the noth side on in feet < :- "))
    south1 = float(input("enter the south side on in feet > :- "))

    east = east1*3.3
    west = west1*3.3
    north = north1*3.3
    south = south1*3.3
 
    direction1 = east + west
    direction2 = north + south

    direct1 = direction1 / 2
    direct2 = direction2 / 2

    multiply = direct1 * direct2

    squarefeet = multiply / 436

    kuli = squarefeet / 8

    print("your total cent is :- ", squarefeet)
    print("your total kuli is :- ", kuli)


switchers = {
    1: feet,
    2: kuli,
}



def switch(dayoftheweeks):
    return switchers.get(dayoftheweeks)()



print(switch(name))




-------------------------------------------------------------------------------------------------------------------------------------------------


print("1 is add or 2 is sub ")

fun = int(input("what type of function you calculate:- "))

def add():
    num1 = int(input("enter the first number:- "))
    num2 = int(input("enter the second number:- "))
    num3 = num1+num2
    print("your answer is :-" , num3)

def sub():
    num1 = int(input("enter the first number:- "))
    num2 = int(input("enter the second number:- "))
    num3 = num1 - num2
    print("your answer is :-", num3)

switcher = {
    1:add,
    2:sub,
}

def switch(addition):
    return switcher.get(addition)()

print(switch(fun))


