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



    if op == 1:
        print(a,"+",b," = ")

    if op == 2:
        print(a,"-",b," = ")

    if op == 3:
        print(a,"*",b," = ")



sc1 = 0
sc2 = 0


for x in range(5):

    q = make_question()
    print(q)

    answer = input("=")
    r = int(answer)


    if eval(q) == r :
        print("정답입니다")

    else :
        print("오답입니다")


















    
