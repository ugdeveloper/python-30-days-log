### Day 8 - 30DaysOfPythonChallenge

## Exercises: Day 8

## 1. Create an empty dictionary called dog.

dog = dict()

## 2. Add name, colour, breed, legs, age to dog dictionary.

dog['name'], dog['colour'], dog['breed'], dog['legs'], dog['age'] = 'gioia', 'white', 'bichon', 4, 8

## 3. Create a student dictionary and add first_name, last_name, gender, age, marital status,
# skills, country, city and address as keys for the dictionary.

student = {'first_name': 'Mijo', 'last_name': 'Bakalar', 'gender': 'Male', 'age': 17, 'marital status': False, 'skills': ['Java', 'Python', 'JS'], 'country': 'Canada', 'city': 'Toronto', 'address': '81 Charles St.'}

## 4. Get the length of the student dictionary

print(len(student))

## 5. Get the value of skills and check the data type, it should be a list.

print(type(student['skills']))

## 6. Modify the skills values by adding one or two skills.

student['skills'].append('Creativity')
student['skills'].append('IQ')

## 7. Get the dictionary keys as a list.

keys = student.keys()

## 8. Get the dictionary values as a list

values = student.values()

## 9. Change the dictionary to a list of tuples using items() method

tpls = student.items()

## 10. Delete one of the items in the dictionary

del student['address']

## 11. Delete one of the dictionaries

del student

## yay