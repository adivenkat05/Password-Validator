# Refer "funcPass.py" to know about the following functions.
from Function import funcPass

password = input("Enter your password to check if it's strong: ")

# all() func returns True if all the conditions is True.
if all([validatePass.check_digit(password),

        validatePass.check_lowerCase(password),

        validatePass.check_upperCase(password),

        validatePass.check_specialChar(password),

        validatePass.check_length(password),

        not validatePass.check_whiteSpace(password)]
       ):

    print("You have entered strong password.")

else:
    print("Your password has not met the following requirement(s): ")

    if not validatePass.check_digit(password):
        print("   [*] Password must contain atleast one digit (0 - 9)!")

    if not validatePass.check_lowerCase(password):
        print(
            "   [*] Password must contain atleast one lower case character (a - z)!")

    if not validatePass.check_upperCase(password):
        print(
            "   [*] Password must contain atleast one upper case character (A - Z)!")

    if not validatePass.check_specialChar(password):
        print("   [*] Password must contain atleast one special character !")

    if validatePass.check_whiteSpace(password):
        print("   [*] Password should not contain whitespace !")

    if not validatePass.check_length(password):
        print("   [*] Password should be greater than 6 digit !")
