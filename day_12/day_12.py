### Day 12 - 30DaysOfPythonChallenge

## Exercises: Level 1

# 1. Write a function which generates a six digit/character random_user_id.

import random as r
from string import ascii_lowercase, digits

def random_user_id():
    ops = ascii_lowercase + digits
    uid = ''
    while(len(uid) < 6):
        uid += r.choice(ops)
    return uid

print(random_user_id())

# 2. Modify previous task to take two inputs, one for length and one for num of ids

import random as r
from string import ascii_lowercase, digits

def user_id_gen_by_user():
    length_id = int(input("Enter the length of the ID's: "))
    num_ids = int(input("Enter the number of ID's you want to output: "))
    ids = []
    ops = ascii_lowercase + digits

    while(len(ids) < num_ids):
        uid = ''
        while(len(uid) < length_id):
            uid += r.choice(ops)
        ids.append(uid)

    return "\n".join(ids)

print(user_id_gen_by_user())

# 3. Write a function named rgb_color_gen. It will generate rgb colours

import random as r

def rgb_colour_gen():
    return f"rgb{(r(0,255), r(0,255), r(0,255))}"

print(rgb_colour_gen())

# Exercises: Level 2

# 1. Write a function list_of_hexa_colors which returns any number of hexadecimal colors in an array.

import random as r

def list_of_hexa_colors(num_coors):
    hexadec = '0123456789abcdef'
    colors = []
    while len(colors) < num_coors:
        colors.append(f"#{r.choice(hexadec)}{r.choice(hexadec)}{r.choice(hexadec)}{r.choice(hexadec)}{r.choice(hexadec)}{r.choice(hexadec)}")
    return colors
# 2. Write a function list_of_rgb_colors which returns any number of RGB colors in a list

def list_of_rgb_colors(num_colors):
    listy = []
    while len(listy) < num_colors:
        listy.append(f"rgb{(r.randint(0,255), r.randint(0,255), r.randint(0,255))}")
    return listy

# 3. Write a function generate_colors which can generate any number of hexa or rgb colors

def generate_colors(choice, num_outputs):

    if choice is 'hexa':
        return list_of_hexa_colors(num_outputs)
    elif choice is 'rgb':
        return list_of_rgb_colors(num_outputs)
    else:
        pass

print(generate_colors('hexa', 3))

# Exercises: level 3

# 1. Call your function shuffle_list, it takes a list as a parameter and return a shuffled list.

def shuffle_list(arg: list) -> list:

    new_list = []

    while len(arg) > 0:
        index = r.randint(0, len(arg) - 1)
        new_list.append(arg.pop(index))

    return new_list

print(shuffle_list([1, 2, 3, 4, 5, 6, 7, 8]))

# 2. Write a function which returns an array of seven random numbers 0 - 9.
# all the numbers must be unique.

def seven_random_nums() -> list:
    nums = [0,1,2,3,4,5,6,7,8,9]
    new_list = []
    while len(new_list) < 7:
        new_list.append(nums.pop(r.randint(0,len(nums)-1)))
    return new_list

print(seven_random_nums())