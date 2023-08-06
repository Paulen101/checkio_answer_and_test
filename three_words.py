'''
You are given a string with words and numbers separated by whitespaces (one space). The words contains only letters. You should check if the string contains three words in succession. For example, the string "start 5 one two three 7 end" contains three words in succession.

Input: A string (str) with words.

Output: Logic value (bool).

'''

def checkio(words): 
    words = words.split()
    count = 0
    for i in words:
        if i.isalpha():
            count += 1
            if count == 3:
                return True
        else:
            count = 0
    return False
    ...