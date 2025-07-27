# ------------------------------------
# Title:    Projectile Motion Calculations
# Author:   Matt Salvadori
# Date:     July 15, 2025
# Purpose:  To calculate the time it takes for a projectile
#           to hit the ground mapping it's location each time interval.
# ------------------------------------

#region IMPORTS
#endregion

#region GLOBAL VARIABLES (CONSTANTS)
# YOU MAY NOT CHANGE ANYTHING IN THIS SECTION
# except for the values of the variables for testing purposes
MIN_PASSWORD_LENGTH = 8
MAX_PASSWORD_LENGTH = 12
ALLOW_SPECIAL_CHARACTERS = True
ALLOWED_SPECIAL_CHARACTERS = "!@#$%^&*"
MUST_HAVE_DIGIT = True
MUST_HAVE_UPPERCASE = True
MUST_HAVE_LOWERCASE = True
ALLOW_SPACES = False
ALPHANUMERIC_CHARACTERS = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
#endregion

#region FUNCTION DEFINITIONS
def getString(prompt):
    '''get string from user'''
    return input(prompt)



def passwordsMatch(str1, str2):
    '''check if passwords match'''
    return str1 == str2


def validatePassword(password):
    '''wrapper function that consolidates all password validation tests'''
    is_valid = True
    if not test_password_length(password):
        is_valid = False

    if not test_password_allowed_characters(password):
        is_valid = False

    if not test_password_must_have_digit(password):
        is_valid = False

    if not test_password_must_have_uppercase(password):
        is_valid = False

    if not test_password_must_have_lowercase(password):
        is_valid = False

    if not test_password_allow_spaces(password):
        is_valid = False
    
    return is_valid


def test_password_length(password: str):
    '''Test if the length of the password is within limits'''
    # return false if password outside of parameters
    return len(password) > MIN_PASSWORD_LENGTH and len(password) < MAX_PASSWORD_LENGTH
    

def test_password_allowed_characters(password: str):
    '''Test if characters in password match string constants'''
    teststring = ALPHANUMERIC_CHARACTERS
    # change test string  to allow special characters if special characters is allowed
    if ALLOW_SPECIAL_CHARACTERS:
        teststring = ALPHANUMERIC_CHARACTERS + ALLOWED_SPECIAL_CHARACTERS
    # test password to see if there are characters not in test string
    for i in password:
        if not i in teststring:
            return False

    return True

def test_password_must_have_digit(password: str):
    '''Test if password has digits'''
    if MUST_HAVE_DIGIT:
        has_digit = False
        # loop through each letter to test for a digit
        for i in password:
            # if digit in password return true
            if i.isdigit():
                has_digit = True
        return has_digit
    else:
        return True


def test_password_must_have_uppercase(password: str):
    '''Test if password has any uppercase'''
    if MUST_HAVE_UPPERCASE:
        has_upper = False
        # loop through each letter to test for uppercase
        for i in password:
            # if uppercase letter in password return true
            if i.isupper():
                has_upper = True
        return has_upper
    else:
        return True
    

def test_password_must_have_lowercase(password: str):
    '''Test in any password has lowercase'''
    if MUST_HAVE_LOWERCASE:
        has_lower = False
        # loop through each letter to test for lowercase
        for i in password:
            # if lowercase letter in password return true
            if i.islower():
                has_lower = True
        return has_lower
    else:
        return True

def test_password_allow_spaces(password: str):
    '''Test if password allows spaces'''
    if not ALLOW_SPACES:
        no_spaces = True
        # loop through each letter to test for spaces
        for i in password:
            # if space in password return false
            if i == ' ':
                no_spaces = False
        return no_spaces
    else:
        return True

#endregion

#region MAIN APPLICATION

# YOU MAY NOT CHANGE ANYTHING IN THIS REGION
print('-'*40)
print("Welcome to the Password Generator")

doContinue = True
while doContinue:
    print('-'*40)

    # input
    password = getString("Enter your password (Q to Quit): ")
    if password.upper() == "Q":
        doContinue = False
        continue

    # have the user re-type the password to confirm
    password2 = getString("Re-enter your password: ")

    # check if the passwords match
    if passwordsMatch(password, password2):

        # check if the password is valid
        if validatePassword(password):    
            print("Password is valid")
        else: 
            print("Passwords are invalid")
    else:
        print("Passwords do not match")

    input("Press Enter to continue...")

print("Goodbye!")
print('-'*40)
exit(0)
#endregion