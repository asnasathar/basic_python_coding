x = int(input("Enter a number: "))
if x%2 != 0:
    print("WEIRD")
elif x in range (2,6):
    print("NOT WEIRD")
elif x in range(6, 21):
    print(" WEIRD")
else:
    print(" NOT WEIRD")