# 1부터 n까지의 곱을 구하는 함수

def factorial(n):
    
    fact = 1 # 곱을 구하기 위한 변수s (시작값을 1으로 지정)
 
    for x in range(1,n+1): # range...로 1,2,...n까지 반복합니다
        
        fact = fact * x

    return fact


print(factorial(5))
print(factorial(10))
