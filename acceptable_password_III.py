'''
In this mission you need to create a password verification function.

The verification conditions are:

the length should be bigger than 6;
should contain at least one digit, but it cannot consist of just digits;
having numbers or containing just numbers does not apply to the password longer than 9;
a string should not contain the word "password" in any case.
Input: A string (str).

Output: A logic value (bool)
'''
def acceptable_password(password): 
    empty = [] 
    if password.lower().find('password') != -1:
        return False
    for i in password: 
        empty.append(i)
    if len(empty) > 9: 
        return True
    elif len(empty) > 6 and any(i.isdigit() for i in empty) and any(i.isalpha() for i in empty): 
        return True
    else: 
        return False