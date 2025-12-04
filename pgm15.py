x=input("enter a string: ")
y=input("enter a string: ")
if sorted(x.lower()) == sorted(y.lower()):
    print("anagram")
else:
    print("not anagram")
