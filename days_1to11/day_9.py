### Day 9 - 30DaysOfPython

## Exercises: Level 1

## 1. Get user input using input(“Enter your age: ”). If user is 18 or older, 
# give feedback: You are old enough to drive. If below 18 give feedback to wait 
# for the missing amount of years. Output:

# Enter your age: 30
# You are old enough to learn to drive.
# Output:
# Enter your age: 15
# You need 3 more years to learn to drive.

age = int(input('Enter your age:'))

if age >= 18:
    print('You are old enough to learn to drive.')
else:
    print(f"You need {18 - age} more years to learn to drive")

## 2. Compare the values of my_age and your_age using if … else. 
# Who is older (me or you)? Use input(“Enter your age: ”) to get the age as input.
# You can use a nested condition to print 'year' for 1 year difference in age, 
# 'years' for bigger differences, and a custom text if my_age = your_age. 
# Output:

# Enter your age: 30
# You are 5 years older than me.

my_age = 25
your_age = int(input("Enter your age:"))

if (your_age > my_age):
    print(f"You are {your_age - my_age} years older than me.")
elif (my_age > your_age):
    print(f"I am {my_age - your_age} years older than you.")
else:
    print("We are the same age")

## 3. Get two numbers from the user using input prompt.
# If a is greater than b return a is greater than b, 
# if a is less b return a is smaller than b, 
# else a is equal to b. Output:

a = int(input("Enter number one: "))
b = int(input("Enter number two: "))

if (a > b):
    print(f"{a} is greater than {b}")
elif (b < a):
    print(f"{a} is less than {b}")
else:
    print(f"{a} is equal to {b}")

## Exercises: Level 2

## 1. Write a code which gives grade to students according to their scores:

score = int(input('Enter a grade: '))
grade = ''

if (90 <=  grade <= 100):
    grade = 'A'
elif (80 <= grade <= 89):
    grade = 'B'
elif (70 <= grade <= 79):
    grade = 'C'
elif(60 <= grade <= 69):
    grade = 'D'
elif(0 <= grade <= 59):
    grade = 'F'
else:
    print("Invalid input")

## 2. Get the month from user input then check if the season is Autumn, Winter, Sprint
# or Summer. If the user input is: September, October or November, the season is Autumn.
# December, January or Februrary, the season is Winter. March, April or May, the season is
# Spring. June, July, or August, the season is summer.

month = int(input('Enter the numerical value of a month:'))
season = ''

if (month == 12 or month < 3):
    season = 'winter.'
elif(2 < month < 6):
    season = 'spring.'
elif(5 < month < 9):
    season = 'summer.'
else:
    season = 'fall.'

print(f"The season is {season}")

## 3. The following list contains some fruits:

fruits = ['banana', 'orange', 'mango', 'lemon'] 

# if a fruit doesn't exist in the list add the fruit to the list and print the modified list.
# If the fruit exists print('That fruit already exists in the list')

fruit_add = input('Enter the name of a fruit:').lower()

if (fruit_add not in fruits):
    fruits.append(fruit_add)
else:
    print('That fruit already exists in the list')

## Exercises: Level 3

# 1. Here we have a perosn dictionary. Feel Free to modify it!

person = {
    'first_name': 'Mijo',
    'last_name': 'Bakalar',
    'age': 6969,
    'country': 'Canada',
    'is_married': False,
    'skills': ['Java', 'Python', 'HTML', 'Analysis'],
    'address': {
        'street': 'Snowy Own Cres.',
        'zip_code': 'L5N 7K3'
    }
}

#  * Check if the person dictionary has skills key, if so print out the middle skill in the skills list.

if ('skills' in person):
    print(person['skills'][1])
else:
    print('diedieide')

#  * Check if the person dictionary has skills key, if so check if the person has 'Python' skill and print out the result.

if ('skills' in person):
    if ('Python' in person['skills']):
        print(True)
    else:
        print(False)
else:
    print(False)

#  * If a person skills has only JavaScript and React, print('He is a front end developer'), 
# if the person skills has Node, Python, MongoDB, print('He is a backend developer'), 
# if the person skills has React, Node and MongoDB, Print('He is a fullstack developer'), 
# else print('unknown title') - for more accurate results more conditions can be nested!

if ('skills' in person):
    if (('JavaScript' or 'React') in person['skills']):
        if (('Node' or 'Python' or 'MongoDB') in person['skills']):
            print("He is a full_stack developer")
        else:
            print("He is a front_end developer")

    elif(('Node' or 'Python' or 'MongoDB') in person['skills']):
        print("He is a back_end developer")
    else:
        print("unknown title")


#  * If the person is married and if he lives in Finland, print the information in the following format:

#     Asabeneh Yetayeh lives in Finland. He is married.

if ((person['is_married'] == False) and (person['country'] == 'Canada')):

    print(f"\t{person['first_name']} {person['last_name']} lives in {person['country']}. He is not married")

## CONGRATULATIONS!!! WOWOW