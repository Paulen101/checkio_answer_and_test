'''
In this mission you need to create a password verification function.

The verification conditions are:

the length should be bigger than 6;
should contain at least one digit, but it cannot consist of just digits;
if the password is longer than 9 - previous rule (about one digit), is not required.
Input: A string (str).

Output: A logic value (bool).

'''



def is_acceptable_password(password): 
    empty = [] 
    for i in password: 
        empty.append(i)
    if len(empty) > 9: 
        return True
    elif len(empty) > 6 and any(i.isdigit() for i in empty) and any(i.isalpha() for i in empty): 
        return True
    else: 
        return False