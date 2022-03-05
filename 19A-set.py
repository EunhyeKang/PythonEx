a = {1,2,3,4}
b = {3,4,5,6}

print(a)
print(b)


print(1 in a)
print(6 in a)
print(len(a)) # 집합a의 원소 개수

print(a|b) #합집합
print(a&b) # 교집합
print(a-b) #차집합

c = {x for x in range(1,11)}
d = {x for x in range(1,11) if x %3 == 0}

print(c)
print(d)

print(c<d)
print(c>d)

