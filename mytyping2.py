#타자 게임 동물이름 영어단어 화면/사용자는 타자입력/ 맞으면 다음문제, 틀리면 다시입력받음/5문제 후 시간계산

import random
import time

wordlist = ["cat","bat","rat","pig","dog","lion"]


question = random.choice(wordlist)
num = 1

print("엔터 치면 게임 시작")
input()

st = time.time()

while num<=5 :

    print(num,"번째문제")
    print(question)
    ans = input()

    if question == ans :
        print("완벽해요")
        num = num+1
        #print(question)
        question = random.choice(wordlist) ###### 프린트 하는게 아니라 다시뽑아야한다.


    else :
        print("다시입력,맞출때까지")

et = time.time()

time = format(et-st,".2f")

print("걸린시간은 ",time,"초 입니다")

        
    

