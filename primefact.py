n=int(input("enter a num:"))
i=2
print("prime factors are:")
while n>1:
    while n%i==0:
        print(i)
        n//=i
    i+=1