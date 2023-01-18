import re
# re stands for Regular Expression.
# Refer https://docs.python.org/3/library/re.html to know about search() function.

# check_digit() checks if password contains atleast 1 integer character.

def check_digit(password):
    if re.search(r'[0123456789]', password):
        return True
    else:
        return False

# check_lowerCase() checks if password contains atleast 1 lower case character.


def check_lowerCase(password):
    if re.search(r'[abcdefghijklmnopqrstuvwxyz]', password):
        return True
    else:
        return False

# check_upperCase() checks if password contains atleast 1 upper case character.


def check_upperCase(password):
    if re.search(r'[ABCDEFGHIJKLMNOPQRSTUVWXYZ]', password):
        return True
    else:
        return False

# check_specialChar() checks if password contains atleast 1 special characters.


def check_specialChar(password):
    if re.search(r'[!@#$%^&*()<>?~]', password):
        return True
    else:
        return False

# check_whiteSpace() checks if password contains whitespaces.


def check_whiteSpace(password):
    if re.search(r'[\s]', password):
        return True
    else:
        return False

# check_length() checks the length of password, password must be more than 6 digits.


def check_length(password):
    if 6 <= len(password):
        return True
    else:
        return False
