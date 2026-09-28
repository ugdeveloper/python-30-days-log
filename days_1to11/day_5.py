### Day 5 - 30DaysOfPythonChallenge

## Excercises: Level 1

## 1. Declare an empty list

newlist = []

## 2. Declare a list with more than 5 items

newlist = [1, 2, 3, 4, 5]

## 3. Find the length of your list

print(len(newlist))

## 4. Get the first term, the middle item and the last item of the list

print(f"{newlist[0]}, {newlist[len(newlist)/2 - 1]}, {newlist[-1]}")

## 5. Declare a list called mixed_data_types, put your (name, age, height, marital status, address)

mixed_data_types = ['Mijo', 17, 189, False, "6060 Snowy Owl Cres."]

## 6. Declare a list variable named it_companies and assign initial values Facebook, Google,
# Microsoft, Apple, IBM, Oracle and Amazon.

it_companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']

## 7. Print the list using print()

print(it_companies)

## 8. Print the number of companies in the list

print(len(it_companies))

## 9. Print the first, middle, and last company

print(f"{it_companies[0]}, {it_companies[len(it_companies)/2 - 1]}, {it_companies[-1]}")

## 10. Print the list after modifying one of the companies

it_companies[0] = 'The Linux Foundation'
print(it_companies)

## 11. Add an IT company to it_companies

it_companies.append('Nothing')

## 12. Insert an IT company in the middle of the companies list

it_companies.insert(len(it_companies)/2 - 1, 'Xiaomi')

## 13. Change one of the it_companies names to uppercase (IBM excluded!)

it_companies[0] = it_companies[0].upper()

## 14. Join the it_companies with string '#; '

joined = '#; '.join(it_companies)

## 15. Check if a certain company exist in the it_companies list.

print('IMB' in it_companies)

## 16. Sort the list using sort() method.

it_companies.sort()

## 17. Reverse the list in descending order using reverse() method.

it_companies.sort(reverse=True)

## 18. Slice out the first 3 companies from the list.

it_companies = it_companies[3:]

## 19. Slice out the last 3 companies from the list.

it_companies = it_companies[-4::-1]

## 20. Slice out the middle IT company or companies from the list.

it_companies = it_companies[0:3].extend(it_companies[4:])

## 21. Remove the first IT company from the list.

it_companies.pop(0)

## 22. Remove the middle IT company from the list.

it_companies.pop(len(it_companies)/2 - 1)

## 23. Remove the last IT company from the list.

it_companies.pop()

## 24. Remove all IT companies from the list.

it_companies = []

## 25. Destroy the IT companies list.

del it_companies

## 26. Join the following lists:

front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express', 'MongoDB']

front_end.extend(back_end)

## 27. After joining the lists in question 26, copy the joined list and assign it to
# a variable full_stack then insert Python and SQL after Redux.

full_stack = front_end.copy()
full_stack.insert(4, "Python")
full_stack.insert(5, "SQL")

## Exercises: Level 2

## 1. The following is a list of 10 students ages:

ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]

# - Sort the list and find the min and max age.

ages.sort()
min, max = ages[0], ages[-1]

# - Add the min age and max age again to the list

ages.append(min)
ages.append(max)

# - Find the median age (one middle item or two middle items divided by two)

median = (ages[len(ages)/2 - 1] + ages[len(ages)/2]) / 2

# - Find the average age (sum of all items divided by their number)

a, b, c, d, e, f, g, h, i, j, k, l, m, n = ages
avg = (a + b + c + d + e + f + g + h + i + j + k + l + m + n)/14

# - Find the range of ages (max minus min)

range = max - min

# - Compare the value of (min - average) and (max - average), use abs() method.

print(abs(min - avg) > abs(max - avg))

## 2. Find the middle country(ies) in the countries list

countries = ['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']
middle = countries[len(countries)/ 2 - 1]

## 3. ['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']. 
# Unpack the first three countries and the rest as scandic countries.

china, russia, usa, *scandic = countries