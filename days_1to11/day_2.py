# # Day 2 -30DaysOfPython Challenge

### Excercises: Level 1

## 1. Inside 30DaysOfPython create a folder called day_2 (redundant).
#     Inside this folder create a file named variables.py (redundant).

## 2. Write a python comment saying 'Day 2: 30 Days of python programming' (redundant)

## 3. Declare a first name variable and assign a value to it

first_name = 'Mijo'

## 4. Declare a last name variable and assign a value to it

last_name = 'Bakalar'

## 5. Declare a full name variable and assign a value to it

full_name = first_name + " " + last_name

## 6. Declare a country variable and assign a value to it

country = 'Croatia'

## 7. Declare a city variable and assign a value to it

city = 'Sarajevo'

## 8. Declare an age variable and assign a value to it

age = 17

## 9. Declare a year variable and assign a value to it

year = 2008

## 10 - 13. Declare and assign the following on one line.
#           is_married, is_true, is_light_on

is_married, is_true, is_light_on = False, True, True

### Excercises: Level 2

## 1. Check the data type of all your variables using type() built-in function

type(first_name) #str
type(last_name) #str
type(full_name) #str
type(country) #str
type(city) #str
type(age) #int
type(year) #int
type(is_married) #boolean
type(is_true) #boolean
type(is_light_on) #boolean

## 2. Using the len() built-in function, find the length of your first name

len(first_name)

## 3. Compare the length of your first name and last name

print(len(first_name) - len(last_name)) #if > 0, first name is larger and vice versa (if == 0 same length)

## 4. Declare 5 as num_one and 4 as num_two

num_one = 5
num_two = 4

## 5. Add num_one and num_two and assign the value to a variable sum

total = num_one + num_two

## 6. Subtract num_two from num_one and assign the value to a variable diff

diff = num_one - num_two

## 7. Multiply num_two and num_one and assign the value to a variable product

product = num_two * num_one

## 8. Divide num_one by num_two and assign the value to a variable quotient

quotient = num_one / num_two

## 9. Use modulus division to find num_two divided by num_one and assign the value to
#     variable remainder

remainder = num_two % num_one

## 10. Calculate num_one to the power of num_two and assign the vlaue to a variable exp

exp = num_one ** num_two

## 11. Find the flood division of num_one by num_two and assign the value to a variable
#      floor_division

floor_division = num_one // num_two

## 12. The radius of a circle is 30 meters

pi = 3.1415926925

# i. Calculate the area of the circle and assign the value to a variable name of
# area_of_circle

area_of_circle = (pi)(30**2)

# ii. Calculate the circumference of a circle and assign the value to a variable name
#     of circum_of_circle

circum_of_circle = 2(pi)(30)

# iii. Take radius as user input and calculate the area

radius = input('input a radius: ')
variable_aofcircle = (pi)(radius**2)

## 13. Use the built-in input function to get first name, last name, country and
#      age from a user and store the value to their corresponding variable names

first_name = input('Enter your first name: ')
last_name = input('Enter your last name: ')
country = input('Enter your country: ')
age = input('Enter your age: ')

## 14. Run help('keywords') in python shell or in your file to check for the Python
#      reserved words or keywords