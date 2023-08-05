'''
You are given a string and you have to find its first word.

The input string consists of only English letters and spaces.
There are not any spaces at the beginning and the end of the string.
Input: A string (str).

Output: A string (str).
'''

def first_word(text): 
    text = text.replace('.', ' ').replace(',', ' ').strip()
    return text.split()[0]

print(first_word("Hello world"))




