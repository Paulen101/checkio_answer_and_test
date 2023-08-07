'''
You are given a string and you have to find its first word.

The input string consists of only English letters and spaces.
There are not any spaces at the beginning and the end of the string.
Input: A string (str).

Output: A string (str).
'''

'''
You are given a string where you have to find its first word.

When solving a task pay attention to the following points:

There can be dots and commas in a string.
A string can start with a letter or, for example, one/multiple dot(s) or space(s).
A word can contain an apostrophe and it's a part of a word.
The whole text can be represented with one word and that's it.
Input: A string (str).

Output: A string (str).
'''

def first_word(text): 
    text = text.replace('.', ' ').replace(',', ' ').strip()
    return text.split()[0]






