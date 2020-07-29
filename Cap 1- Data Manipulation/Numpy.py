"""
Introduction to Numpy

Numpy (short for Numerical Python) allows us to find the answer to how many presidents are
taller than 188cm with ease. Below we show how to use the library and start with the basic object in numpy.
"""
import numpy as np

#Peso de los 45 presidentes del los Estados Unidos.
heights = [189, 170, 189, 163, 183, 171, 185, 168, 173, 183, 173, 173, 175, 178, 183, 193, 178, 173, 174, 183, 183, 180, 168,
           180, 170, 178, 182, 180, 183, 178, 182, 188, 175, 179, 183, 193, 182, 183, 177, 185, 188, 188, 182, 185, 191]

heights_arr = np.array(heights)
#Imprime 5 que son los mayores de 188.
print((heights_arr > 188).sum())


#Imprime el tamaño del array en este caso es 45
print(heights_arr.size)

#Imprime las dimensiones del array en este caso es (45,)
print(heights_arr.shape)


# Other data we have collected includes the ages of the presidents:
# Reshape
import numpy as np

heights = [189, 170, 189, 163, 183, 171, 185, 168, 173, 183, 173, 173, 175, 178, 183, 193, 178, 173, 174, 183, 183, 180, 168, 180, 170, 178, 182, 180, 183, 178, 182, 188, 175, 179, 183, 193, 182, 183, 177, 185, 188, 188, 182, 185, 191]

ages = [57, 61, 57, 57, 58, 57, 61, 54, 68, 51, 49, 64, 50, 48, 65, 52, 56, 46, 54, 49, 51, 47, 55, 55, 54, 42, 51, 56, 55, 51, 54, 51, 60, 62, 43, 55, 56, 61, 52, 69, 64, 46, 54, 47, 70]

heights_and_ages = heights + ages
# convert a list to a numpy array
heights_and_ages_arr = np.array(heights_and_ages)
print(heights_and_ages_arr.reshape((2,45)))


"""
EXERCISE

Review the code below and reshape the 1darray of shape (45,) to a 2darray with a shape of (5, 9).

"""
#Solution
heights_arr.shape
#(45, )
heights_arr_reshaped = heights_arr.reshape((5, 9))


"""
DATA TYPE
 
Numpy supports several data types such as int (integer), float (numeric floating point), and bool (boolean values, True and False).
The number after the data type, ex. int64, represents the bitsize of the data type.

"""
import numpy as np

heights = [189, 170, 189, 163, 183, 171, 185, 168, 173, 183, 173, 173, 175, 178, 183, 193, 178, 173, 174, 183, 183, 180, 168, 180, 170, 178, 182, 180, 183, 178, 182, 188, 175, 179, 183, 193, 182, 183, 177, 185, 188, 188, 182, 185, 191]

heights_arr = np.array(heights)
print(heights_arr.dtype)
# int64

import numpy as np

heights_float = [189.0, 170, 189, 163, 183, 171, 185, 168, 173, 183, 173, 173, 175, 178, 183, 193, 178, 173, 174, 183, 183, 180, 168, 180, 170, 178, 182, 180, 183, 178, 182, 188, 175, 179, 183, 193, 182, 183, 177, 185, 188, 188, 182, 185, 191]

heights_float_arr = np.array(heights_float)
print(heights_float_arr)
print("\n")
print(heights_float_arr.dtype)
# Float64
