#Write a python program to find the largest from the three numbers 
a = int(input("enter first number:-"))
b = int(input("enter second number:-"))
c = int(input("enter third number:-"))

if (a >= b) and (a >= c):
   largest = a
elif (b >= a) and (b >= c):
   largest = b
else:
   largest = c

print("The largest number is", largest)
