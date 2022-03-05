#소인수분해 2로나누고 안나눠지면 3으로 나눠줌


while True :
    
    x = int(input("소인수분해 할 숫자? : "))

    d = 2


    while d <= x:
        if x % d == 0:
            print(d)

            x = x/d

        else:
            d = d+1
