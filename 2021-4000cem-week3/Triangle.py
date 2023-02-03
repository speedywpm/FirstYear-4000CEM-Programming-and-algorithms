# See Week 3 Lab 2 Slides for study of this script.

from math import sqrt

def distance(x1,y1,x2,y2):
    """Function to find length of line between two points"""
    dx = x2 - x1
    dy = y2 - y1
    d = sqrt(dx**2 + dy**2)
    return d

def areaTriangle(x1,y1,x2,y2,x3,y3):
    """Function to find area of triangle defined by 3 points"""
    # This uses Heron's Formula - Google it if you want to know more
    side1 = distance(x1,y1,x2,y2)
    side2 = distance(x2,y2,x3,y3)
    side3 = distance(x3,y3,x1,y1)
    p = (side1 + side2 + side3)/2
    t1 = p-side1
    t2 = p-side2
    t3 = p-side3
    if t1==0 or t2==0 or t3==0:
        print("Does not form a triangle")
        return None
    area = sqrt( p*(p-side1)*(p-side2)*(p-side3) )
    return(area)

ans = areaTriangle(0,0, 0,2, 2,0)
print(ans)
