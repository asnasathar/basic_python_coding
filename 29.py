x = int(input("enter a number: "))
y = 0
z = x
while z!=0:
    y=y+(((z%10)**3))
    z = z//10
if y==x:
    print("armstrong")
else:
    print("not armstrong")

