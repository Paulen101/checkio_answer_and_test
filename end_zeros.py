'''
Try to find out how many zeros a given number has at the end.

Input: A non-negative integer (int).

Output: An integer (int).
'''

def end_zeros(value): 
    counter = 0
    for i in str(value)[::-1]: 
        if i == '0': 
            counter += 1
        else: 
            break
    return counter