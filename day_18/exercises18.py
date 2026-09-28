### day 18, regular expressions - 30daysofpythonchallenge

# Exercises

# 1. What is the most frequence word in the following paragraph?

import re

paragraph = 'I love teaching. If you do not love teaching what else can you love. I love Python if you do not love something which can give you all the capabilities to develop an application what else can you love.'

def pack_paragraph(paragraph: str) -> list:

    pack = re.findall(r'\w+', paragraph.lower())

    counts = {}

    for word in pack:
        counts[word] = counts.get(word, 0) + 1


    return [(count, word) for word, count in counts.items()]

print(pack_paragraph(paragraph))

# 2. The position of particles on horizontal axis is:

points = ['-12', '-4', '-3', '-1', '0', '4', '8']

sorted = [int(i) for i in points].sort()

distance = sorted[len(sorted) - 1] - sorted[0]

# 3. Write a pattern which identifies if a string is a valid python variable

import keyword

def is_valid_var(arg: str) -> bool:

    reg = r'^[a-zA-Z_][a-zA-Z0-9_]*$'

    if arg.isidentifier():
        return False
    elif re.match(arg, reg):
        return True
    else:
        return False

# 4. Clean the following text. After cleaning, count three most frequent words in the string

import re

sentence = '''%I $am@% a %tea@cher%, &and& I lo%#ve %tea@ching%;. There $is nothing; &as& mo@re rewarding as educa@ting &and& @emp%o@wering peo@ple. ;I found tea@ching m%o@re interesting tha@n any other %jo@bs. %Do@es thi%s mo@tivate yo@u to be a tea@cher!?'''

sentence = re.sub(r'[^\w\s]+', '', sentence)

list_words = re.findall(r'\w+', sentence)

dict = {}

for word in list_words:
    dict[word] = dict.get(word, 0) + 1

nums = list(dict.values())
nums.sort(reverse=True)
print(nums[0:3])

# BOOOM