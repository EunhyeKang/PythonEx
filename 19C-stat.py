import math

d = [1,2,3,4,5]

print(d)


# 평균

avg = sum(d) / len(d)
print(avg)


# 분산

vsum = 0
for x in d:
    vsum = vsum + (x-avg)**2

var = vsum / len(d)


# 표준편차

std = math.sqrt(var)
print(std)
