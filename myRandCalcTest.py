# 계산 맞히기 게임
# 간단한 덧셈,뺄셈,곱셈 문제 임의로 보여줌
# -> 사용자가 계산해서 답 입력
# -> 정답/오답 체크 점수매김
# ->5번 반복해서 전체 정답 수 알려주기

import random


def make_question():

    a = random.randint(1,10)
    b = random.randint(1,10)
    
    op = random.randint(1,3)


    tmp = str(a) ########

    if op == 1:
        tmp = tmp + "+"

    if op == 2:
        tmp = tmp + "-"

    if op == 3:
         tmp = tmp + "*"

    tmp = tmp + str(b) #####

    return tmp ######



s1=0
s2=0


for x in range(5):

    
    q= make_question() ##
    print(q)
    
    ans = input("정답은 : ")
    ans = int(ans) ############

    if ans == eval(q): #
        print("정답입니다\n")
        s1 = s1+1

    if ans != eval(q): #
        print("오답입니다\n")
        s2 = s2+1


print("정답의 개수는 ",s1," 오답의 개수는 ",s2," 입니다")









        

