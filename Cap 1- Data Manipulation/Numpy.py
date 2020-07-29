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
