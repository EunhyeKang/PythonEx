import time

# 속으로 20초를 세어 맞히는 프로그램

input("엔터누르고10초세라")

start = time.time()

input("10초후에 다시 엔터 눌러라")

end = time.time()


et= end-start

print("걸린시간 : ", et)
print("차이는? : ", abs(10-et))
