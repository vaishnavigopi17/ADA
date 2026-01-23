a=int(input("enter first number"))
b=int(input("enter second number"))
while b!=0:
    r=a%b
    a=b
    b=r
print("gcd is:",a)