import math
def areaCircle(radius):
    """Function to calculate area of circle with given radius"""
    area = math.pi * radius**2
    return(area)
v = areaCircle(3)*10
print("Volume of cylinder with radius 3 and height 10: " + str(v) )
