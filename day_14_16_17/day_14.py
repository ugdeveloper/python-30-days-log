### Day 14 - 30DaysOfPython Challenge

countries = ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland']
names = ['Asabeneh', 'Lidiya', 'Ermias', 'Abraham']
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

## Exercises: Level 1

# 1. map vs filter vs reduce

# map takes function and iterable, returns iterable
# filter takes boolean and iterable, returns iterable
# reduce takes functio and iterable, returns single value

# 2. higher order function vs closure vs decorator

# higher order function is a function that takes 1 or more function as args
# closures are functions wiht nested functions that are returned
# decorators are design patterns that allow users to add new funcitonality to existing objects
# without changing its structure

## Exercises: Level 2

# 1. Use map to create a new list by changing each country to uppercase in the countries list

def change_to_upper(name):
    return name.upper()

new_list = map(change_to_upper, countries)

# 2. Use map to create a new list by changing each number to its square in the numbers list

def square(num):
    return num**2

new_list = map(square, numbers)

# 3. Use map to change each name to uppercaes in the names list

new_list = map(change_to_upper, names)

# 4. Use filter to filter out countries containing land

def contains_land(country):
    return True if 'land' in country else False

new_list = filter(contains_land, countries)

# 5. Use filter to filter out countries having exactly six characters

def contains_six(country):
    return True if len(country) is 6 else False

new_list = filter(contains_six, countries)

# 6. Use filter to filter out countries containing six letters and more in the country list

def more_than_six(country):
    return True if len(country) > 6 else False

new_list = filter(more_than_six, countries)

# 7. Use filter to filter out countries strating with an 'E'

def starts_with_E(country):
    return True if country[0] is 'E' else False

new_list = filter(starts_with_E, countries)

# 8. Chain two or more list iterators

new_list = map(change_to_upper, countries).filter(starts_with_E, countries)

# 9. Declare a function called get_string_lists which takes a list as a parameter and then returns a list containing only string items

def is_string(y: str) -> bool:
    return True if y is str else False

def get_string_lists(x: list) -> list:
    return filter(is_string, x)

# 10. Use reduce ot sum all the numbers in the numbers list.

from functools import reduce

def add_two_nums(x: int, y: int) -> int:
    return x + y

sum_of_all = reduce(add_two_nums, numbers)

# 11. Use reduce to concatenate all the countries and to produce this sentence: Estonia, Finland, Sweden, Denmark, Norway, and Iceland are north European countries

def concatenate(l: list) -> str:

    return [s + ", " for s in l]

# 13. Function returns dictionary, keys are first letters, values are num appearances of letter

def num_appearances(l: list) -> dict:

    dict1 = {}

    for i in l:

        if i in dict:
            dict[i] += 1

        else:

            dict[i] = 1

    return dict1


