import random
import time


w_list = ["cat", "dog", "rabbit", "lion", "monkey", "puppy", "tiger"]


print("타자게임 준비되면 Enter!! : ")

input()
st = time.time()

num =1

qword = random.choice(w_list)


while num <= 5:

    print("타자게임",num,"번째 문제 ", qword)
    uword = input()
    
    if qword == uword:
        print("통과")
        num = num+1
        qword = random.choice(w_list)

    else:
         print("오타!다시 ",qword)
        # input() xxx
         


et = time.time()

endtime = format(et-st,".2f")

print("걸린시간은 ",endtime,"초 입니다")
