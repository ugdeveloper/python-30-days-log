## Statistics, day 24

## NumPy

import numpy as np

print('numpy:', np.__version__)

print(dir(np))

## numpy arrays

pythin_list = [1,2,3,4,5]

# Checking types

print('Type:', type(pythin_list))

print(pythin_list)

two_dim = [[0,1,2],[3,4,5],[6,7,8]]

print(two_dim)

# Numpy array from py list

numpy_array = np.array(pythin_list)
print(type (numpy_array))
print(numpy_array)

# float numpy arrays

numpy_array2 = np.array(pythin_list, dtype=float)

# boolean numpy arrays

numpy_array3 = np.array(pythin_list, dtype=bool)

# multi dim numpy array

numpy_two_dim = np.array(two_dim)

# converting numpy array to list

np_to_list =numpy_array.tolist()

# numpy array from tuple

py_tup = (1,2,3,4,5)

np_from_tup = np.array(py_tup)

# shape of numpy array returns an (x1, x2, x3, x4..... xn)

nums = np.array([1,2,3,4,5])
print(nums.shape) # (5, )
print(numpy_two_dim.shape) # (3, 3)

numpy_three_dim = np.array(
    [[[1,2,3],[4,5,6],[7,8,9]],
     [[11,12,13],[14,15,16],[17,18,19]],
     [[20,21,22],[23,24,25],[26,27,28]]]
    )

print(numpy_three_dim.shape) # (3, 3, 3)

# data type numpy array

print(numpy_array.dtype) # int64
print(numpy_array2.dtype) # float64

# size of numpy array

numpy_array_from_list = np.array([1, 2, 3, 4, 5])
two_dimensional_list = np.array([[0, 1, 2],
                                 [3, 4, 5],
                                 [6, 7, 8]])

print('The size:', numpy_array_from_list.size) # 5
print('The size:', two_dimensional_list.size)  # 3

# Math operations using numpy
''' 
    Addition (+)
    Subtraction (-)
    Multiplication (*)
    Division (/)
    Modules (%)
    Floor Division(//)
    Exponential(**)
'''

# addition, adds to all values in array

numpy_array_from_list = np.array([1,2,3,4,5])
ten_plus_original = numpy_array_from_list + 10 # [11,12,13,14,15]

# subtraction, subtracts from all values in array

numpy_array_from_list = np.array([1,2,3,4,5])
ten_minus_original = numpy_array_from_list - 10 # [-9, -8, -7, -6, -5]

# multiplication, multiplies by all values in array

numpy_array_from_list = np.array([1,2,3,4,5])
ten_times_original = numpy_array_from_list * 10 # [10, 20, 30, 40, 50]

# division, divides by all values in array

numpy_array_from_list = np.array([1,2,3,4,5])
original_divide_ten = numpy_array_from_list / 10# [0.1, 0.2, 0.3, 0.4, 0.5]

# modulus, remainer from all values

numpy_array_from_list = np.array([1,2,3,4,5])
modulo_original= numpy_array_from_list % 3 # [1, 2, 0, 1, 2]

# Floor division, divison without remainder (round to floor)

numpy_array_from_list = np.array([1,2,3,4,5])
original_divide_tofloor = numpy_array_from_list // 10 # [0, 0, 0, 0, 0]

# exponential, every value in array to exponent

numpy_array_from_list = np.array([1,2,3,4,5])
original_power_2 = numpy_array_from_list ** 2

## Checking data types

# .dtype method

# converting types

# 1. Int to Float

numpy_int_arr = np.array([1,2,3,4], dtype=float)

# 2. Float to int

numpy_int_arr = np.array([1., 2., 3., 4.], dtype=int)

# 3. int to bool

numpy_int_arr = np.array([1,2,3,4], dtype=bool) # returns ints != 0 as True

# 4. Int to str

numpy_int_arr = np.array([1,2,3,4], dtype=float)

numpy_int_arr.astype('int').astype('str') # array(['1','2','3'], dtype='<U21)

# multi dim arrays

# 2 Dimension Array
two_dimension_array = np.array([(1,2,3),(4,5,6), (7,8,9)])
print(type (two_dimension_array))
print(two_dimension_array)
print('Shape: ', two_dimension_array.shape)
print('Size:', two_dimension_array.size)
print('Data type:', two_dimension_array.dtype)

'''
output:     <class 'numpy.ndarray'>
            [[1 2 3]
            [4 5 6]
            [7 8 9]]
            Shape:  (3, 3)
            Size: 9
            Data type: int64
'''

# getting items from numpy array

# 2 Dimension Array
two_dimension_array = np.array([[1,2,3],[4,5,6], [7,8,9]])
first_row = two_dimension_array[0]
second_row = two_dimension_array[1]
third_row = two_dimension_array[2]
print('First row:', first_row)
print('Second row:', second_row)
print('Third row: ', third_row)

'''
output:     First row: [1 2 3]
            Second row: [4 5 6]
            Third row:  [7 8 9]

'''

first_column= two_dimension_array[:,0]
second_column = two_dimension_array[:,1]
third_column = two_dimension_array[:,2]
print('First column:', first_column)
print('Second column:', second_column)
print('Third column: ', third_column)
print(two_dimension_array)

'''
output:         First column: [1 4 7]
                Second column: [2 5 8]
                Third column:  [3 6 9]
                [[1 2 3]
                 [4 5 6]
                 [7 8 9]]
'''

## Slicing numpy array

# similar to slicing python list

two_dimension_array = np.array([[1,2,3],[4,5,6], [7,8,9]])
first_two_rows_and_columns = two_dimension_array[0:2, 0:2]
print(first_two_rows_and_columns)

# reverse rows and whole array

two_dimension_array = np.array([[1,2,3],[4,5,6], [7,8,9]])
two_dimension_array[::-1,::-1]

'''
output:      array([[9, 8, 7],
                    [6, 5, 4],
                    [3, 2, 1]])

'''

# how to fill cells

two_dimension_array[1,1] = 55
two_dimension_array[1,2] = 44
print(two_dimension_array)

# numpy zeros

numpy_zeros = np.zeroes((3,3),dtype=int,order='C')

'''
output:          array([[0, 0, 0],
                        [0, 0, 0],
                        [0, 0, 0]])
'''

# numpy ones

numpy_ones = np.ones((3,3),dtype=int,order='C')

'''
output:             [[1 1 1]
                     [1 1 1]
                     [1 1 1]]
'''

# create an array of any number

twoes = numpy_ones * 2

# ns = numpy_ones * n

# reshape, can take an array and reshape it duuduh

first_shape  = np.array([(1,2,3), (4,5,6)])
print(first_shape)
reshaped = first_shape.reshape(3,2)
print(reshaped)

'''
Output:             [[1 2 3]
                    [4 5 6]]
                    -> .reshape()
                    [[1 2]
                    [3 4]
                    [5 6]]
'''

flattened = reshaped.flatten()
print(flattened)

'''
Output:             array([1, 2, 3, 4, 5, 6])
'''

## horizontal append

np_list_one = np.array([1,2,3])
np_list_two = np.array([4,5,6])

print(np.hstack((np_list_one, np_list_two)))

'''
Output: [1, 2, 3, 4, 5, 6]
'''

## vertical append

print('Vertical Append:', np.vstack((np_list_one, np_list_two)))

'''
Output: [[1, 2, 3]
         [4, 5, 6]]
'''

## Generating random numbers

# random float
random_float = np.random.random()

# random numpy array of floats
random_floats = np.random.random(5)

# random ints between 0 and 10
random_int = np.random.randint(0,11)

# random numpy array of lists from 2 to 11 (one row array)
random_ints = np.random.randint(2, 10, size=4)

# two row random
random_int = np.random.randint(2,10, size=(3,3))

# random normal array
normal_array = np.random.normal(79, 15, 80)

## Numpy and statistics

import matplotlib.pyplot as plt
import seaborn as sns

normal_array = np.random.normal(79, 15, 80)

sns.set_theme()
plt.hist(normal_array, color="grey", bins=50)

## matrix in numpy

four_by_four_matrix = np.matrix(np.ones((4,4), dtype=float))

'''
output:     matrix([[1., 1., 1., 1.],
                    [1., 1., 1., 1.],
                    [1., 1., 1., 1.],
                    [1., 1., 1., 1.]])
'''

np.asarray(four_by_four_matrix)[2] = 2

'''
Output:     matrix([[1., 1., 1., 1.],
                    [1., 1., 1., 1.],
                    [2., 2., 2., 2.],
                    [1., 1., 1., 1.]])
'''

# numpy arrange

# create values that are evenly spaced within a defined interval, similar to range()

whole_numbers = np.arrange(0, 20, 1)

'''
Output: array([ 0,  1,  2,  3,  4,  5,  6,  7,  8,  9, 10, 11, 12, 13, 14, 15, 16,
           17, 18, 19])
'''

natural_nums = np.arrange(1, 20, 1)
odd_nums = np.arrange(1,20,2)
even_nums = np.arrange(2,20,2)

## Createing sequence using linspace

evenly_spaced = np.linspace(1.0, 5.0, num=10)

# not including last value

evenly_spaced_not_including_last = np.linspace(1.0, 5.0, num=10, endpoint=False)

## Creating sequence using logspace

# returns even spaced numbers ona a log scale. (magnitudes of 10)

mags_ten_spaced = np.logspace(2.0, 4.0, num=4)

# to get from 10**2 to 10**4, create a evenly spaced sequence 4 nums long

## Complex numbers type

x = np.array([1,2,3], dtype=np.complex128)

print(x.itemsize) # 16 ? what lol

## numpy statistical functions with example

# numpy has some useful statistical functions:

'''
Numpy Functions

    Min np.min()
    Max np.max()
    Mean np.mean()
    Median np.median()
    Variance
    Percentile
    Standard deviation np.std()
'''

np_normal_dis = np.random.normal(5, 0.5, 100)
np_normal_dis
## min, max, mean, median, sd
print('min: ', two_dimension_array.min())
print('max: ', two_dimension_array.max())
print('mean: ',two_dimension_array.mean())
# print('median: ', two_dimension_array.median())
print('sd: ', two_dimension_array.std())

# to find the row/column holding a min or max

# == Column ==, axis=0
print(np.amin(two_dimension_array, axis=0))
print(np.amax(two_dimension_array, axis=0))

# == Row ==, axis=1
print(np.amin(two_dimension_array, axis=1))
print(np.amax(two_dimension_array, axis=1))

## how to create repeating sequences

a = [1,2,3]

# repeat whole of a twice
print(np.tile(a,2))

# repeat each element of a twice
print(np.repeat(a,2))

## how to generate random choices

print(np.random.choice(['a', 'e', 'i', 'o', 'u'], size=10))

# randn goes based off gaussian distribution, mean of u, std of 1. likely to generate numbers closer to zero but from -inf to +inf

print(np.random.randn(2,3))

## new python random
# numpy generator api

rng = np.random.default_rng()

# replacement for random.rand()/random.random()
uniform_array = rng.random((2,3))

# replacement for random.randn()
normal_array = rng.standard_normal((2,3))

## SciPy
from scipy import stats

np_normal_dis = rng.standard_normal(5, 0.5, 100)

plt.hist(np_normal_dis, color="grey", bins=21)
plt.show() #wow this is cool

## linear algebra

# 1. dot product

f = np.array([1,2,3])
g = np.array([4,5,3])
np.dot(f, g)  # 23

# matrix multiplication

h = [[1,2],[3,4]]
i = [[5,6],[7,8]]
### 1*5+2*7 = 19
np.matmul(h, i)

## linear equations

temp = np.array([1,2,3,4,5])
pressure = temp * 2 + 5

plt.plot(temp, pressure)
plt.xlabel('Temperature in degrees C')
plt.ylabel('Pressure in atmospheres')
plt.title('Temperature vs Pressure')
plt.xticks(np.arange(0, 6, step=0.5))
plt.show()

## gaussian distribution

mu_or_mean = 28
sigma_or_std = 15
samples = 10000

x = np.random.normal(mu_or_mean, sigma_or_std, samples)
ax = sns.displot(x)
ax.set(xlabel="x", ylabel="y")
plt.show()

### SUMMARY

# numpy supports

# 1. vecotrized operations
# 2. immutable lists
# 3. homogenous typed lists
# 4. smaller 2d array compared to list of list
# 5. boolean indexing
