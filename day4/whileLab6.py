while True :
    num = int(input("숫자를 입력 : "))
    if num == 0 :
        print("종료")
        break
    elif -10 > num > 10 :
        continue
    elif 0 < num < 10 :
        print("입력값 : ", num)
        sum = 1
        for i in range(1, num+1) :
            sum *= i
        print(sum)
    elif  -10 < num <= -1 :
        print("입력값(부호변경)",-num)
        sum = 1
        for i in range(1, -num+1) :
            sum *= i
        print(sum)
