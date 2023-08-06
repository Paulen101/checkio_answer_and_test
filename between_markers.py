'''
You are given a string and two markers (the initial one and final). You have to find a substring enclosed between these two markers. But there are a few important conditions.

The initial and final markers are always different.
The initial and final markers are always 1 char size.
The initial and final markers always exist in a string and go one after another.
Input: Three arguments. All of them are strings (str). The second and third arguments are the initial and final markers.

Output: A string (str).
'''

def between_markers(text, start, end): 
    if start in text and end in text:
        return text[text.find(start)+1:text.find(end)]
    elif start in text and end not in text:
        return text[text.find(start)+1:]
    elif start not in text and end in text:
        return text[:text.find(end)]
    else:
        return text
    ...


