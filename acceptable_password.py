'''
In this mission you need to create a password verification function.

The verification conditions are:

the length should be bigger than 6;
should contain at least one digit.
Input: A string (str).

Output: A logic value (bool).
'''


def is_acceptable_password(password): 
    empty = [] 
    for i in password: 
        empty.append(i)
    if len(empty) > 6 and any(i.isdigit() for i in empty) and any(i.isalpha() for i in empty): 
        return True
    else: 
        return False