x = int(input("enter a number: "))
sq = x*x
len=len(str(x))
if sq%(10**len) == x:
    print("automorphic")
else:
    print("not automorphic")