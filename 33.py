import math
a = int(input("enter a number: "))
b = int(input("enter a number: "))
c = int(input("enter a number: "))
D =b**2 - 4*a*c
if D > 0:
    x1 = (-b + math.sqrt(D))/(2*a)
    print("x1 =",x1)
    x2 = (-b - math.sqrt(D))/(2*a)
    print("x2 =",x2)
elif D==0:
    x1 = (-b/(2*a))
    print("x1 =",x1)
    x2 = (-b/(2*a))
    print("x2 =",x2)
elif D<0:
    print("no real root")
