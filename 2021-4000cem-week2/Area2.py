import math
def areaCircle(radius):
    """Function to calculate area of circle with given radius"""
    area = math.pi * radius**2
    return(area)
print("Area of a cirlce with radius 3: " + str( areaCircle(3) ) )
