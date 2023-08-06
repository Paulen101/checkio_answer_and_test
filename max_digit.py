'''
You have a number and you need to determine which digit in this number is the biggest.

Input: A positive integer (int).

Output: An integer 0-9 (int).
'''

def max_digit(value):
    if 0 <= value < 10: 
        return value
    else:
        return int(max(str(value)))
    ...
print(max_digit(0))