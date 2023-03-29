# 16. Write a function in Python that accepts one numeric parameter. 
# This parameter will be the measure of an angle in radians. 
# The function should convert the radians into degrees and then return that value. 
# Do not use inbuilt functions. 
# Note : Angle in Radians × 180°/π = Angle in Degrees.

def radianToDegree(val):
    degree = val*(180/3.14159)
    return  degree

rad = float(input("Enter the radian value : "))
print(round(radianToDegree(rad),2))
