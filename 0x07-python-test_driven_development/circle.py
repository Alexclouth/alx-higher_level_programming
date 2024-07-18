from math import pi
def area(radius = 0):
    if type(radius) not in [int, float]:
        raise TypeError("The radius must be a digit!")
    if radius < 0:
        raise ValueError("The radus must be greater than 0!")
    return pi * (radius ** 2)



'''
radii = [2, 0, 3 + 4j, -3, True, "Radius"]
message = "The area of a circle with the radius = {r} is {a}."

for i in radii:
    ar = area(i)
    print(message.format(r=i, a=ar))'''
