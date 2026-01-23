a = int(input("enter first number: "))
b = int(input("enter second number: "))

t = min(a, b)

while t > 0:
    if a % t == 0 and b % t == 0:
        print("gcd is", t)
        break
    t -= 1
