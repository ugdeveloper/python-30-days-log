### Day 4 - 30DaysOfPython Challenge

## Excercises - Day 4

## 1. Concatenate the string 'Thirty', 'Days', 'Of', 'Python' to a single string,
# 'Thirty Days Of Python'.

a, b, c, d = 'Thirty', 'Days', 'Of', 'Python'
name = f"{a} {b} {c} {d}"

## 2. Concatenate the string 'Coding', 'For', 'All' to a single string, 'Coding For All'.

words = ['Coding', 'For', 'All']
sentence = ' '.join(words)

## 3. Declare a variable named company and assign it to an initial value "Coding For All".

company = "Coding For All"

## 4. Print the variable using print().

print(company)

## 5. Print the length of the company string using len() method and print()

print(len(company))

## 6. Change all the characters to uppercaes letters using upper() method

company = company.upper()

## 7. Change all the characters to lowercase letters using the lower() method

company = company.lower()

## 8. Use capitalize(), title(), swapcase() methods to format the value of the string
# Coding For All

company = company.capitalize()
company = company.title()
company = company.swapcase()

## 9. Cut(slice) out the first word fo Coding For All String

company = company[7:]

## 10. Check if Coding For All string contains a word Coding using the method index, find
# or other methods.

print(company.find('Coding'))
print(company.index('Coding'))

## 11. Replace the word coding in the string 'Coding For All' to Python

company = "Coding For All"
company = company.replace('Coding', 'Python')

## 12. Change "Python for Everyone" to "Python for All" using the replace method or
# other methods.

pfe = "Python for Everyone"
pfe = pfe.replace('Everyone', 'All')

## 13. Split the string 'Coding For All' Using space as the seperator(split())

wordlist = company.split()

## 14. "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon" split the string at the comma.

companies = "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon".split(', ')

## 15. What is the character at index 0 in the string Coding For All.

print("Coding For All"[0]) #C

## 16. What is the last index of the string Coding For All.

print("Coding For All".rindex('l')) #13

## 17. What character is at index 10 in "Coding For All" string.

print("Coding For All"[10]) #\space

## 18. Create an acronym or an abbreviation for the name 'Python For Everyone'

pfe = "Python For Everyone"
acr = f"{pfe[0]}{pfe[7]}{pfe[11]}"

## 19. Create an acronym or an abbreivation for the name 'Coding For All'

cfe = "Coding For All"
acr2 = f"{cfe[0]}{cfe[7]}{cfe[11]}"

## 20. Use index to determine the position of the first occurance of C in
# Coding For All

index = cfe.index('C')

## 21. Use index to determine the position of the first occurance of F in
# Coding For All

index = cfe.index('F')

## 22. Use rfind to determine the position of the last occurance of l in Coding For All People

cfep = "Coding For All People"
lindex = cfep.rfind('l')

## 23. Use index or find to find the position of the first occurence of the word
# 'because' in the following sentence: "You cannot end a sentence with because because
# because is a conjunction".

sentence = "You cannot end a sentance with because because because is a conjunction"
because = sentence.find('because')
because = sentence.index('because')

## 24. Use rindex to find the position of the last occurence of the word because in the
# following sentence: "You cannot end a sentence with because because because is a conjunction"

because = sentence.rindex('because')

## 25. Slice out the phrase 'because because because' in the following sentence: 'You cannot end
# a sentence with because because because is a conjunction'.

slice = sentence.replace('because because because', '')

## 26 - 27 is a repeat

## 28. Does 'Coding For All' start with a substring Coding?

print('Coding' in 'Coding For All')
print('Coding For All'.index('Coding'))

## 29. Does 'Coding for All' end with a substring coding?
# No, lol.

## 30. '    Coding For All     ', remove the left and right trailing spaces in the given string.

cfe_excess = '    Coding For All  '
cfe_strip = cfe_excess.strip()

## 31. Which of the following variables return True when we use the method isidentifier():
#       - 30DaysOfPython -> returns False
#       - thirty_days_of_python -> returns True

## 32. The following list contains the names of some python libraries: ['Django', 'Flask'
# 'Bottle', 'Pyramid', 'Falcon']. Join the list with a hash with space string.

py_lib = ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']
py_lib_joined =  ('# ').join(py_lib)

## 33. Use the new line escape sequence to separate the following sentences.
#
#      - I am enjoying this challenge
#      - I just wonder what is next.

print("I am enjoying this challenge.\nI just wonder what is next.")

## 34. Use a tab escape sequence to write the following lines.
#
#      - Name   Age     Country     City
#      - Asanebeh  250     Finland    Helenski

print(("Name\tAge\tCountry\tCity\nMijo\t17\tCanada\tToronto").expandtabs(10))

## 35. Use the string formatting method to display the following:
# radius = 10
# area = 3.14 * radius ** 2
# The area of a circle with radius 10 is 314 meters square.

## 36. Make the following using string formatting methods:
#
# 8 + 6 = 14
# 8 - 6 = 2
# 8 * 6 = 48
# 8 / 6 = 1.33
# 8 % 6 = 2
# 8 // 6 = 1
# 8 ** 6 = 262144

print(f"{8} + {6} = {8 + 6}")
print(f"{8} - {6} = {8 - 6}")
print(f"{8} * {6} = {8 * 6}")
print(f"{8} / {6} = {(8/6):.2f}")
print(f"{8} % {6} = {8 % 6}")
print("%d // %d = %d" %(8, 6, (8//6)))
print("{} ** {} = {}".format(8, 6, 8**6))

## yay done 4.