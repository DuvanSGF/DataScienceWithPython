"""
Numerical Data

We collected 45 U.S. president heights in centimeters in chronological order and stored them in a list, a built-in data type in python
"""
heights = [189, 170, 189, 163, 183, 171, 185, 168, 173, 183, 173, 173, 175, 178, 183, 193, 178, 173, 174, 183, 183, 180, 168, 180, 170, 178, 182, 180, 183, 178, 182, 188, 175, 179, 183, 193, 182, 183, 177, 185, 188, 188, 182, 185, 191]

cnt = 0
for height in heights:
    if height > 188:
        cnt +=1
print(cnt)

#This shows that there are five presidents who are taller than 188 cm

"""
No matter the format of the data, the first step in data science is to transform it into arrays of numbers.
"""
