#-----------------------------------------------
# Title:            My Tools Library for Python Console
# Author:           Clint MacDonald
# Date:             July 17, 2025
# Purpose:          A set of tools to be reused in our console apps
# Modified By:      Matt Salvadori
# Modification Date:July 17, 2025
# ----------------------------------------------

'''
Note that this file does not use print statements 
in the functions meaning it is locked to the console
If you want to use these functions in a GUI, 
you will need to modify the functions to return values instead of printing the.
'''

#region IMPORTS
import random
#endregion

#region USER INPUT FUNCTIONS
def getString(prompt: str):
    '''Obtains a string from the user'''
    return input(prompt).strip()

def getStringLength(prompt: str, minLen: int, maxLen: int):
    '''Obtains a string from the user with length inside the given range'''
    isValid = False
    while not isValid:
        userString = input(prompt).strip
        # validate the length of the string
        if minLen <= len(userString) <= maxLen: return userString

def getInt(prompt: str):
    '''Get an integer from the user'''
    isValid = False
    while not isValid:
        try:
            return int(input(prompt).strip())
        except ValueError as v:
            pass

def getIntRange(prompt: str, min: int, max: int):
    '''get user input and validate for int and range between 1-4'''
    is_valid = False
    while not is_valid:
        try:
            choice = int(input(prompt))
            if choice < min or choice > max:
                raise ValueError
            is_valid = True
        except ValueError as v:
            print("Invalid Entry")
    return choice

def getFloat(prompt: str):
    '''get a float from the user'''
    is_valid = False
    while not is_valid:
        try:
            return float(input(prompt).strip())

        except ValueError as v:
            pass


def getFloatRange(prompt: str, min: int, max: int):
    '''get a float in range from the user'''
    is_valid = False
    while not is_valid:
        try:
            num = float(input(prompt).strip())
            if min <= num <= max: return num

        except ValueError as v:
            pass
#endregion

#region RANDOM NUMBER GENERATIONS
def getRandIntRange(min: int, max: int):
    '''generate a random integer within the specified range'''
    return random.randint(min, max)

def getRandFloatRange(min: float, max: float, numDec: int):
    '''generate a random float within the specified range'''
    rnd = random.randint(min * (10 ** numDec), max * (10 ** numDec)) / (10**numDec)
    return rnd


#endregion

