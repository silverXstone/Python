a=int(input("Enter first value:-"))
b = int(input("Enter second value:-"))
a=(a&b)+(a|b)
b = a+(~b)+1
a=a+(~b)+1
print("first value after swapping:-",a)
print("second value after swapping :-",b)
