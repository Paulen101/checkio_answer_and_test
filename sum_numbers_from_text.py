'''
In a given text you need to sum the numbers while excluding any digits that form part of a word.

The text consists of numbers, spaces and letters from the English alphabet.

Input: A string (str).

Output: An integer (int).
'''

def sum_numbers(text): 
    text = text.replace(',', ' ').replace('.', ' ').split()
    return sum([int(i) for i in text if i.isdigit()])
    