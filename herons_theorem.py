# Compute the area of a triangle (using Heron's formula),
# given its side lengths.
import math
###################################################
# Triangle area (Heron's) formula
# Student should enter function on the next lines.
# Hint:  Also define point_distance as use it as a helper function.
def point_distance(x_point1, x_point2, y_point1, y_point2):
    return math.sqrt((x_point1 - x_point2)**2 + (y_point1 - y_point2)**2)


def semi_perimeter(a, b, c):
    return (a + b + c) / 2.0

def triangle_area(x0, y0, x1, y1, x2, y2):
    a = point_distance(x0, x1, y0, y1)
    b = point_distance(x1, x2, y1, y2)
    c = point_distance(x0, x2, y0, y2)
    s = semi_perimeter(a, b, c)
    return math.sqrt(s*(s - a)*(s - b)*(s - c))

###################################################
# Tests
# Student should not change this code.

def test(x0, y0, x1, y1, x2, y2):
    print "A triangle with vertices (" + str(x0) + "," + str(y0) + "),",
    print "(" + str(x1) + "," + str(y1) + "), and",
    print "(" + str(x2) + "," + str(y2) + ") has an area of",
    print str(triangle_area(x0, y0, x1, y1, x2, y2)) + "."

test(0, 0, 3, 4, 1, 1)
test(-2, 4, 1, 6, 2, 1)
test(10, 0, 0, 0, 0, 10)


###################################################
# Expected output
# Student should look at the following comments and compare to printed output.

#A triangle with vertices (0,0), (3,4), and (1,1) has an area of 0.5.
#A triangle with vertices (-2,4), (1,6), and (2,1) has an area of 8.5.
#A triangle with vertices (10,0), (0,0), and (0,10) has an area of 50.