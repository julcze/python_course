from math import *
# 1

print("X:")
X = int(input())
print("Y:")
Y = int(input())

P_x= 2 * pi *X
F_x= pi * X **2

P_y= 2 * pi *Y
F_y= pi * Y **2

print ("First circle: ", P_x, F_x)
print("Second circle: ", P_y, F_y)

#2
xIsDivisbley = X%Y == 0
xyIsEven= X%2 == 0 and Y%2==0
Isboth = "true" if xIsDivisbley and xyIsEven else "false"
print(Isboth)

#3
xisdivisiblebyy = X%Y == 0
xisdivisiblebyycheck = "X is divisible by Y"if xisdivisiblebyy else "X isn't divisible by y"
print(xisdivisiblebyycheck)
