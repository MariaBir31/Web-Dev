import math

a = int(input())
b = int(input())

for (x in range (a, b + 1)):
    if x >= 0:
        root = int(math.sqrt(x))
        if root * root == x:
            print(x)
