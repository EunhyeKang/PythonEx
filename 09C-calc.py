import random

a = random.randint(1,30)
b = random.randint(1,30)
c = random.randint(1,5)

print(a,"+",b,"-",c,"=")

x = input()
d = int(x)

if a + b - c == d :
    print("good")

else :
    print("bad")
    
