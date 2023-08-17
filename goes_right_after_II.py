'''
In a given word you need to check if one symbol goes only right after another.

Cases you should expect while solving this challenge:

one of the symbols is not in the given word - your function should return False;
any symbol appears in a word more than once - use only the first one;
two symbols are the same - your function should return False;
the condition is case sensitive, which means 'a' and 'A' are two different symbols.
'''

def goes_after(word, first, second): 
    if first in word and second in word:
        first_index = word.find(first)
        second_index = word.find(second)

        if first_index < second_index: 
            return second_index == first_index + 1
        else: 
            return False
    else: 
        return False
    ...
    
