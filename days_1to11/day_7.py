### Day 7 - 30DaysOfPythonChallenge

## Exercises: Day 7

# sets

it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]

## Exercises: Level 1

## 1. Find the length of set it_companies

print(len(it_companies))

## 2. Add 'Twitter' to it_companies

it_companies.add('Twitter')

## 3. Insert multiple IT companies at once to the set it_companies

more_it = {'Tiktok', 'Rednote', 'Xiaomi'}

it_companies.update(more_it)

## 4. Remove one of the companies from the set it_companies

it_companies.pop()

## 5. What is the difference between remove and discard

# Remove will raise an error if the item isn't in the set,
# discard will not.

## Exercises: Level 2

## 1. Join A and B

A.update(B)

## 2. Find A intersection B

print(A.intersection(B))

## 3. Is A subset of B

print(A.issubset(B)) # True

## 4. Are A and B disjoint sets

print(A.isdisjoint(B)) # False

## 5. Join A with B and B with A

A.union(B); B.union(A)

## 6. What is the symmetric difference between A and B

print(A.symmetric_difference(B))

## 7. Delete the sets completely

del A
del B

## Exercises: Level 3

# 1. Convert the ages to a set and compare the length of the list
# and the set, which one is bigger?

ages_st = set(age)

print(len(age) == len(ages_st)) # True, same size

# 2. Explain the difference between the following data types:
# string, list, tuple, and set.

# == String ==

# A string is a data type which can hold a sequence of characters

# == List ==

# A list is a data type which can hold many different data types at
# particular points within the list called indexes. The data types
# can be different and lists are mutable.

# == Tuple ==

# A tuple is like a list in that it can hold many different data types.
# The data types are held at specific points called indexes, and they don't
# have to be the same kind of data types. Tuple are immutable.

# == Set ==

# Sets are like lists except they can only hold one kind of data type. Sets are unordered and unindexed.

## 3. I am a teacher and I love to inspire and teach people.
# How many unique words have been used in the sentence?

sentence = "I am a teacher and I love to inspire and teach people."
words = sentence.split(' ')
unique_words = set(words)

print(f"There are {len(unique_words)} in the sentence.")