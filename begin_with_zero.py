'''
You have a string that consist only of digits. You need to find how many zero digits ("0") are at the beginning of the given string.

Input: A string (str), that consists of digits.

Output: An integer (int).
'''

def beginning_zeros(value): 
    
    for i in range(len(value)):
        if value[i] != '0':
            return i 
    return len(value)


