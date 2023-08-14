'''
Stephen's speech module is broken. 
This module is responsible for his number pronunciation. 
He has to click to input all of the numerical digits in a figure, so when there are big numbers it can take him a long time. 
Help the robot to speak properly and increase his number processing speed by writing a new speech module for him. 
All the words in the string must be separated by exactly one space character. Be careful with spaces - it's hard to see if you place two spaces instead one.

Input: An integer (int).

Output: A string (str).
'''


FIRST_TEN = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
SECOND_TEN = [
    "ten",
    "eleven",
    "twelve",
    "thirteen",
    "fourteen",
    "fifteen",
    "sixteen",
    "seventeen",
    "eighteen",
    "nineteen",
]
OTHER_TENS = [
    "twenty",
    "thirty",
    "forty",
    "fifty",
    "sixty",
    "seventy",
    "eighty",
    "ninety",
]
HUNDRED = "hundred"
def speech_module(value):
    ...
    if value < 10:
        return FIRST_TEN[value - 1]
    elif value < 20:
        return SECOND_TEN[value - 10]
    elif value < 100:
        return OTHER_TENS[value // 10 - 2] + (" " + FIRST_TEN[value % 10 - 1] if value % 10 else "")
    elif value < 1000:
        return FIRST_TEN[value // 100 - 1] + " " + HUNDRED + (" " + speech_module(value % 100) if value % 100 else "")
    else:
        return speech_module(value // 1000) + " thousand" + (" " + speech_module(value % 1000) if value % 1000 else "")