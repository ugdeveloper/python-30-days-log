## Day 13 - 30DaysOfPython Challenge

# Exercises: Level 1

# 1. Filte ronly negative and zero in the list using list comprehension

numbers = [-4, -3, -2, -1, 0, 2, 4, 6]

only_negative_and_zero = [i for i in numbers if i <= 0]

print(only_negative_and_zero)

# 2. Flatten the following lsit of lissts to a one dimensional line:

list_of_lists =[[1, 2, 3], [4, 5, 6], [7, 8, 9]]

flattened = [num for row in list_of_lists for num in row]
print(flattened)

# 3. Using list comprehension create the following list of tuples:

tuples_list = [(i, 1, i**2, i**3, i**4) for i in range(11)]

print(tuples_list)

# 4. Flatten the following list to a new list:

countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]

flatten = [country.upper() for row in [country for row in countries for country in row] for country in row]

combine = [[flatten[i], flatten[i][0:3], flatten[i + 1]] for i in range(0, len(flatten), 2)]

print(combine)

# 5. Change the following list to a list of dictionaries:

countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]

country_dict = [{'country': i[0][0], 'city': i[0][1]} for i in countries]

print(country_dict)

# 6. Change the following list of lists to a list of concatenated strings:

names = [[('Asabeneh', 'Yetayeh')], [('David', 'Smith')], [('Donald', 'Trump')], [('Bill', 'Gates')]]

full_names = [f"{i[0][0]} {i[0][1]}" for i in names]

print(full_names)

# 7. Write a lambda funciton which can solve a slope or y-intercept of linear functions

x = lambda x1, y1, x2, y2: int((y2 - y1)/(x2-x1))

