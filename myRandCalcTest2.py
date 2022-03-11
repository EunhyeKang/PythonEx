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

    q = str(a) ##

    if op == 1:
        q = q + "+"
    if op == 2:
        q = q + "-"
    if op == 3:
        q = q + "*"

    q = q + str(b) #
    return q #


sum1 = 0
sum2 = 0

for x in range(5): ##

    ans = make_question()
    print("문제 : ", ans , "= ")

    ans_user = input()
    ans_user = int(ans_user) ########
    
    if ans_user == eval(ans):
        print("정답입니다\n")
        sum1 = sum1+1
    
    #if ans_user != eval(ans):
    else:
        print("오답입니다\n")
        sum2 = sum2+1

print("정답 갯수 : " , sum1,"개 오답 갯수 : ",sum2,"개 입니다.")






    

    
