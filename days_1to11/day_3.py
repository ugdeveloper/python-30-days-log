### Day 3 - 30DaysOfPython Challenge

## Excercises - Day 3

## 1. Declare your age as an integer varible

age = 17

## 2. Declare your height as an integer variable

height = 189

## 3. Declare a variable that stores a complex number

cmplx = 17 + 189j

## 4. Write a script that prompts the user to enter base and height of the triangle
#  and calculate an area of this triangle.

base = int(input("Enter base: "))
height = int(input("Enter height: "))
area = base * height * 0.5
print("The area of the triangle is " + area)

## 5. Write a script that prompts the user to enter side a, side b, and side c of
# the triangle. Calculate the perimeter of the triangle.

side_a, side_b, side_c = int(input("Enter side a: ")), int(input("Enter side b: ")), int(input("Enter side c: "))
perimeter = side_a + side_b + side_c
print("The perimeter of the triangle is " + perimeter)

## 6. Get length and width of a rectangle using prompt. Calculate its area and
# perimeter.

length = int(input("Enter length: "))
width = int(input("Enter width: "))
area = length*width
perimeter = 2 * (length + width)
print(f"The area of the rectangle is {area} and the perimeter is {perimeter}")

## 7. Get radius of a circle using prompt. Calculate area and circumference where
# pi = 3.14

radius = int(input("Enter radius: "))
area = (3.14)*(radius**2)
circumference = 2 * 3.14 * radius

## 8. Calculate the slope, x-intercept and y-intercept of y = 2x - 2

slope = 2
y_intercept = -2
x-intercept = y_intercept / slope

## 9. Slope is (m = y2-y1/x2-x1). Find the slope and Euclidean distance between point
# (2,2) and point (6,10)

x1, y1, x2, y2 = 2, 2, 6, 10
m = (y2-y1)/(x2-x1)
dist = ((y2-y1)*2 + (x2-x1)*2)**0.5

## 10. Compare the values of slopes in tasks 8 and 9
slope > m

## 11. Calculate the value of x-intercepts (y = x^2 + 6x + 9). Try to use different x values
# and figure out at what x value y is going to be 0.

a = 1
b = 6
c = 9

x1, x2 = (-b + (b*2 - 4*a*c)**0.5)/2*a, (-b - (b*2 - 4*a*c)**0.5)/2*a

print(f"The x-intercepts of the quadratic y = x^2 + 6x + 9 are {x1} and {x2}")

## 12. Find the length of 'python' and 'dragon' and make a falsy comparison statement

py_len = len('python')
dra_len = len('dragon')

(py_len > dra_len) == True

## 13. Use and operator to check if 'on' is found in both 'python' and 'dragon'

'on' in 'python' and 'on' in 'dragon'

## 14. I hope this course is not full of jajrgon. Use in operator to check if jargon is
# in the sentence.

'jargon' in "I hope this course is not full of jargon"

## 15. There is no 'on' in both dragon in python

'on' not in 'python' and 'on' not in 'dragon'

## 16. Find the length of the text python and convert the value to float and convert
# it to a string.

pyth_len = len('python')
float_py = float(pyth_len)
string_py = str(float_py)

## 17. Even numbers are divisible by 2 and their remainder is 0. How do you check if
# a number is even or not using python.

number = ("Input a #: ") # take any input of a number from the user

number % 2 == 0 # if this statement returns true, it is even. Else, false.

## 18. Check if the floor divison of 7 by 3 is equal to the int converted value of 
# 2.7

floor_div = 7//3 # assigns a value of 2
int_conv = int(2.7) # assigns a value of 2

# Thus, we can infer that floor divison and integer conversion both work by truncating
# the decimals.

## 19. Check if type of '10' is equal to type of 10

type('10') == type(10) # Returns false, string != int

## 20. Check if int('9.8') is equal to 10

int(9.8) # Returns 9, as per our previous inference.

## 21. Write a script that prompts the user to enter hours and
# rate per hour. Calculate pay of the person.

week_hours, rate = int(input("Enter hours: ")), int(input("Enter rate per hour: "))
weekly_earning = (week_hours * rate)
print(f"Your weekly earning is {weekly_earning}")

## 22. Write a script that prompts the user to enter number of years.
# Calculate the number of seconds a person can live. Assume a person
# can live a hundred years.

years_lived = int(input("Enter the number of years you have lived: "))
seconds_lived = years_lived * (365) * (24) * (3600) # years * days in year * hours in day * seconds in hour
print(f"You have lived for {seconds_lived} seconds")

## 23. Write a python script that displays the following table
# 1 1 1 1 1
# 2 1 2 4 8
# 3 1 3 9 27
# 4 1 4 16 64
# 5 1 5 25 125

print(f"1 1 1 1 1\n2 1 2 4 8\n3 1 3 9 27\n4 1 4 16 64\n5 1 5 25 125")