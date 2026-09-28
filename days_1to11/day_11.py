### Day 11 - 30DaysOfPythonChallenge

## Exercises: Day 11

## Exercises: Level 1

## 1. Declare a function add_two_numbers. It takes two parameters and returns a sum

def add_two_numbers(num1, num2):
    return num1 + num2

## 2. Area of a circle is calculated as follows: : area = π x r x r. Write a function that calculates area_of_circle.

def area_of_circle(radius):
    return (3.14)(radius**2)

## 3. Write a function called add_all_nums which takes arbitrary number of arguments and sums all the arguments. 
# Check if all the list items are number types. If not do give a reasonable feedback.

def add_all_nums(*nums):
    sum = 0
    for num in nums:
        if type(num) is str:
            print("Please pass only numbers to this function")
            break
        else:
            sum += num
    return sum

## 4. Temperature in °C can be converted to °F using this formula: °F = (°C x 9/5) + 32. Write a function which converts °C to °F, convert_celsius_to-fahrenheit.

def convert_celsius_to_fahrenheit(temp_celsius):
    return (temp_celsius * (9/5)) + 32

## 5. Write a function called check_season, it takes a month parameter and returns the season:
# Autumn, Winter, Spring or Summer.

def check_season(month):

    if month is ('December' or 'January' or 'Februrary'):
        return 'Winter'
    elif month is ('March' or 'April' or 'May'):
        return 'Spring'
    elif month is ('June' or 'July' or 'August'):
        return 'Summer'
    elif month is ('September' or 'October' or 'November'):
        return 'Fall'
    else:
        return "invalid month, check spelling"

## 6. Write a function called calculate_slope which returns the slope of a linear equation.

def calculate_slope(x1, y1, x2, y2):

    return (y2 - y1) / (x2 - x1)

## 7. Quadratic equation is calculated as follows: axax² + bx + c = 0. Write a function which calculates solution set of a quadratic equation, solve_quadratic_eqn.

def solve_quadratic_eqn(a, b, c):

    x1 = (-b + (b**2 - 4*a*c)) / 2*a
    x2 = (-b - (b**2 - 4*a*c)) / 2*a

    return x1, x2

## 8. Declare a function named print_list. It takes a list as a parameter and it prints out each element of the list.

def print_list(list_input):

    for list_item in list_input:
        print(list_item)

# 9. Declare a function named reverse_list. It takes an array as a parameter and returns the reverse of the array (use loops)

def reverse_list(list_input):
    pointer_a = list_input[0]; pointer_b = list_input[len(list_input)-1]

    i = 0

    while i <= len(list_input)/2:
        temp = list_input.index(pointer_b)
        list_input[list_input.index(pointer_a)] = pointer_b
        list_input[temp] = pointer_a

        i += 1

        pointer_a = list_input[i]; pointer_b = list_input[len(list_input) - 1 - i]

    return list_input

print(reverse_list([1,2,3,4,5]))

print(reverse_list(['A', 'B', 'C']))

## 10. Declare a function named capitalize_list_items. It takes a list as a parameter and returns a capitalized list of items.

def capitalize_list_items(list_input):

    new_list = []

    for item in list_input:
        new_list.append(item.upper())

    return new_list

print(capitalize_list_items(['hello', 'i am', 'butt']))

## 11. Declare a function named add_item. It takes a list and item parameters. It returns a list with the item added at the end.

def add_item(lis, item):

    return lis.append(item)

## 12. Declare a function named remove_item. It taes a list and a item parameters. It returns a list with the item removed from it

def remove_item(lis, item):

    del lis[lis.index(item)]

    return lis

## 13. Declare a function named sum_of_numbers. It takes a number parameter and it adds all the numbers in that range.

def sum_of_numbers(num_factorial):

    sum = 0

    for i in range(num_factorial + 1):

        sum += i

    return sum

print(sum_of_numbers(5))

## 14. Declare a function named sum_of_odds. It takes a number parameter and it adds all the odd numbers in that range

def sum_of_odds(num_factorial_odds):

    sum = 0

    for i in range(num_factorial_odds + 1):

        if (i % 2 != 0):
            sum += i

    return sum

## 15. Declare a function named sum_of_even. It takes a number parameter and it adds all the even numbers in that rnage.

def sum_of_even(num_factorial_evens):

    sum = 0

    for i in range(num_factorial_evens + 1):

        if (i % 2 == 0):
            sum += i

    return sum

## Exercises: Level 2

## 1. Declare a function named evens_and_odds. It takes a positive integer as parameter and it counts number of evens and odds in the number.

def evens_and_odds(count_up_to):
    odds = 0
    evens = 0

    for num in range(count_up_to + 1):
        if (num % 2 == 0):
            evens += 1
        else:
            odds += 1

    return odds, evens

## 2. Call your function factorial, it takes a whole number as a parameter and returns a factorial of the number (alr did)

## 3. Call your function is_empty. It takes a parameter and checks if it is empty or not.

def is_empty(param):
    if len(param) == 0:
        return True
    else:
        return False

