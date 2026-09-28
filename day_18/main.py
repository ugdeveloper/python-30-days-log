## regular expressions, day 18

# RegEx can be used to find patterns in data.

# import the re module to detect or find patterns

import re

# Some methods in re

    # re.match(): searches the beginning of the first line of the string and returns matched objects if found, else returns none.

    # re.searcH: returns a mtach object if ther eis one anyone in the string, including multiline strings.

    # re.findall returns list containing all matches

    # re.split: takes a string and splits it at the match points, returns a list

    # re.sub: replaces one or many matches iwth a string.

# search can be better than match because it searches for the pattern through the text, not just beginning with.

import re

txt = 'I love to teach python and javaScript'
match = re.match('I like to teach', txt, re.I)
print(match)  # None

import re

txt = '''Python is the most beautiful language that a human being has ever created.
I recommend python for a first programming language'''

# It returns an object with span and match
match = re.search('first', txt, re.I)
print(match)  # <re.Match object; span=(100, 105), match='first'>
# We can get the starting and ending position of the match as tuple using span
span = match.span()
print(span)     # (100, 105)
# Lets find the start and stop position from the span
start, end = span
print(start, end)  # 100 105
substring = txt[start:end]
print(substring)       # first

# findall searches for all matches

txt = '''Python is the most beautiful language that a human being has ever created.
I recommend python for a first programming language'''

# It return a list
matches = re.findall('language', txt, re.I)
print(matches)  # ['language', 'language']

txt = '''Python is the most beautiful language that a human being has ever created.
I recommend python for a first programming language'''

matches = re.findall('Python|python', txt)
print(matches)  # ['Python', 'python']

# if not including re.I

matches = re.findall('[Pp]ython', txt)
print(matches)  # ['Python', 'python']


## another case for replacing substrings

txt = '''Python is the most beautiful language that a human being has ever created.
I recommend python for a first programming language'''

match_replaced = re.sub('Python|python', 'JavaScript', txt, re.I)
print(match_replaced)  # JavaScript is the most beautiful language that a human being has ever created.I recommend python for a first programming language
# OR
match_replaced = re.sub('[Pp]ython', 'JavaScript', txt, re.I)
print(match_replaced)  # JavaScript is the most beautiful language that a human being has ever created.I recommend python for a first programming language

# there are many examples that i could continue to look through

# Writing regex patterns

regex_pattern = r'apple' #use r identifier
txt = 'Apple and banana are fruits. An old cliche says an apple a day a doctor way has been replaced by a banana a day keeps the doctor far far away. '
# To make case insensitive adding flag '
matches = re.findall(regex_pattern, txt, re.I)
print(matches)  # ['Apple', 'apple']

# or without the flag

regex_pattern = r'[Aa]pple'
matches = re.findall(regex_pattern ,txt)
print(matches) # same output

# Useful regex info
    # []: A set of characters
    #     [a-c] means, a or b or c
    #     [a-z] means, any letter from a to z
    #     [A-Z] means, any character from A to Z
    #     [0-3] means, 0 or 1 or 2 or 3
    #     [0-9] means any number from 0 to 9
    #     [A-Za-z0-9] any single character, that is a to z, A to Z or 0 to 9

    # \: uses to escape special characters
    #     \d means: match where the string contains digits (numbers from 0-9)
    #     \D means: match where the string does not contain digits
    # . : any character except new line character(\n)
    # ^: starts with
    #     r'^substring' eg r'^love', a sentence that starts with a word love
    #     r'[^abc] means not a, not b, not c.
    # $: ends with
    #     r'substring$' eg r'love$', sentence that ends with a word love
    # *: zero or more times
    #     r'[a]*' means a optional or it can occur many times.
    # +: one or more times
    #     r'[a]+' means at least once (or more)
    # ?: zero or one time
    #     r'[a]?' means zero times or once
    # {3}: Exactly 3 characters
    # {3,}: At least 3 characters
    # {3,8}: 3 to 8 characters
    # |: Either or
    #     r'apple|banana' means either apple or a banana
    # (): Capture and group
