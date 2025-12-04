x =input("Enter a string:")
r = x[::-1]
print("reversed string",x[::-1])
if x.lower()==r.lower():
    print("palindrome")
else:
    print("not palindrome")
