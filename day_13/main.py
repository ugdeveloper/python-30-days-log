## List comprehension

# Essentially shorthand for iterating through a sequence and generating a list

## The syntax is generally as follows

# [i in i for sequence]

# You can do mathematical operations as the list is outputted

[i * i for i in range(11)] # [0, 1, 4, 9,...,100]

# Lists comprehension can also output tuples

[(i, i*i) for i in range(11)] # output nums and their squares from 0 to 10

# List comprehension can be combined with boolean expressions

[i for i in range(21) if i % 2 == 0] # generates even numbers list in range 0 to 20

# An application of this is flattening a two dimensional list

list_of_lists = [[1,2,3],[4,5,6],[7,8,9]]
flattened_list = [number for row in list_of_lists for number in row]

## Lambda function. An anonymous function without a name, can take *args, but only one expression
# we need it when we want to write an anon function inside another function

# Creating lambda function

# use lambda keyword followed by parameter(s) followed by expression

# useful for one time use functions for the purpose of keeping code tidy

x = lambda param1, param2, param3: param1 + param2 + param3

# essentailly a shorthand for function definition

# you can also have a lambda expression invoke itself via

(lambda a, b: a + b)(1, 2)

## can use a lambda function within a function

def power(x):
    return lambda n : x ** n

## calling power() now requires two arguments to run.

cube = power(2)(3)

