# import my_module.py
import mymodule

print(mymodule.generate_full_name('Mijo', 'Bakalar')) # Mijo Bakalar

# Can import functions independently aswell
from mymodule import generate_full_name

# Can also rename modules as we import (so useful)

from mymodule import generate_full_name as fn

print(fn("bA", "ab"))

# some common imports are: math, datetime, os, sys, random, statistics, collections, json, re

## Os module
# Allow sus to perform os tasks like creating an dhcaing working directory, removing folders, fetching their contents, and changing and identifying the current folder.
import os

# Creating a dir
os.mkdir('dir_name')

# Changing the current dir
os.chdir('path')

# Getting current working dir
os.getcwd()

# removing dir
os.rmdir()

## Sys module
# manipulate parts of py runtime env. sys.argv returns command line arguments pased to a py script.

# ex 
# python script.py Mijo Bakalar

# import sys
#print(sys.argv[0], argv[1],sys.argv[2])  # this line would print out: filename argument1 argument2

# Useful sys commands:

import sys

# exit sys
sys.exit

# to know largest int var.
sys.maxsize

# To know env path
sys.path

# To know py vers.
sys.version

# Statistics Module

# functions for statistics of numerical data.
# mean, mode, median, stdev

from statistics import * # import all

# Math module
# containing math operations and constants

#ex
from math import pi
print(pi)

from math import sqrt, pow, floor, ceil, log10

# can also import everythin

from math import *

# we can also rename as we import

from math import pi as PI

# String module

# many different use cases

import string
print(string.ascii_letters) # abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ
print(string.digits)        # 0123456789
print(string.punctuation)   # !"#$%&'()*+,-./:;<=>?@[\]^_`{|}~

# Random module
# random gives a random number between 0 and 0.9999....
# we can use this to get any random number

from random import random, randint

print(random())
print(randint(5, 20))