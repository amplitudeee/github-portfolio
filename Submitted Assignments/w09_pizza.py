# ----------------------------
# Title:        COSC1100- Week 9 Guess the Number
# Name:         Matt Salvadori
# Date:         July 10, 2025
# Purpose:      Showing how to integrate functions into programs
# ----------------------------

#region DECLARATIONS

PI = 3.14159
WELCOME_MESSAGE = '''
---------------------------------
Welcome to my Pizza Calc Program
---------------------------------'''

#endregion

def getIntFromUser(prompt):
    '''gets interger from user and validate return diameter'''
    is_valid = False
    while not is_valid:
        try:
            num = int(input(prompt))

            if num < 8 or num > 24 :
                print('Please enter a valid whole number between 8" - 24"')
                raise ValueError
            is_valid = True
        except ValueError as v:
            print('Invalid Input')
    return num

def calcSlices(diameter):
    '''returns possible slices using diameter input'''
    if 8 <= diameter < 10:
        return [6]
    elif 10 <= diameter < 14:
        return [6,8]
    elif 14 <= diameter < 16:
        return [6,8,10]
    elif 16 <= diameter < 20:
        return [6,8,10,12]
    elif 20 <= diameter <= 24:
        return [6,8,10,12,16]

def calcSliceArea(diameter, slices):
    '''calculates the area of slice using slices'''
    return ((diameter / 2) ** 2 * PI) / slices

def printMenu(diameter, sliceQuant):
    '''prints the pizzas diameter, and a line for every cut scenario with corresponding slice areas'''
    print('\n------------------------------------------------------------------------\n')
    print('\nPizza Diameter: %.1f"\n' % diameter)
    for slices in sliceQuant:
        sliceArea = calcSliceArea(diameter, slices)
        print("Cut in %i slices results in an area of %.2fper slice\n" % (slices, sliceArea))
    print('\n------------------------------------------------------------------------')


# main
print(WELCOME_MESSAGE)
diameter_of_pizza = getIntFromUser("\nPlease enter the diameter of pizza between 8 - 24 (0 to end program): ")
slice_quantity = calcSlices(diameter_of_pizza)
printMenu(diameter_of_pizza, slice_quantity)

