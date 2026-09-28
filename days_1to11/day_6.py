### Day 6 - 30DaysOfPythonChallenge

## Exercises: Level 1

## 1. Create an empty tuple

tpl = tuple()

## 2. Create a tuple containing names of your sisters and your brothers
# (imaginary siblings are fine)

siblings = ('Gabby', 'Josiah', 'Abby', 'Serena', 'Nadan', 'Luka')

## 3. Join brothers and sisters tuples and assign it to siblings (redundant)

## 4. How many siblings do you have?

print(len(siblings))

## 5. Modify the siblings tuple and add the name of your father and mother and assign
# it to family_members

family_members = list(siblings)
family_members.append('Gordan')
family_members.append('Tiffany')
family_tpl = tuple(family_members)

## Exercises: Level 2

## 1. Unpack sibling and parents from family_members

slbing = family_tpl[0:5]
parents = family_tpl[6:]

## 2. Create fruits, vegetables and animal products tuples. Join the three tuples and
# assign it to a variable called food_stuff_tp

fruits = ('Orange', 'Apple', 'Kiwi', 'Canteloupe')
vegetables = ('Cucumber', 'Tomato', 'Lettuce', 'Spinach')
animal_products = ('Meat', 'Poultry', 'Fish', 'Eggs')

food_stuff_tp = fruits + vegetables + animal_products

## 3. Change the about food_stuff_tp tuple into a food_stuff_lt list

food_stuff_lt = list(food_stuff_tp)

## 4. Slice out the middle term or items from the food_stuff_tp tuple or food_stuff_lt list.

food_stuff_tp = food_stuff_tp[0:3] + food_stuff_tp[6:]

## 5. Slice out the first three items and the last three items from food_stuff_lt list.

food_stuff_lt = food_stuff_lt[3:len(food_stuff_lt) - 4]

## 6. Delete the food_stuff_tp tuple completely

del food_stuff_tp

## 7. Check if an item exists in tuple:

nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')

# - Check if 'Estonia' is a nordic country

print('Estonia' in nordic_countries)

# - Check if 'Iceland' is a nordic country

print('Iceland' in nordic_countries)