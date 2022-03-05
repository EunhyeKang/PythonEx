# 1부터 n까지의 합을 구하는 함수

def sum_func(n):
    
    s = 0 # 합을 구하기 위한 변수s (시작값을 0으로 지정)
 
    for x in range(1,n+1): # range...로 1,2,...n까지 반복합니다
        
        s = s+x 

    return s


print(sum_func(10))
print(sum_func(100))
