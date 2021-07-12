while True :
    user = int(input("숫자를 입력 :"))
    if 1 <= user <= 12 :
        if 12 or 1 or 2 :
            print(user,"월은 겨울")
        elif 3 or 4 or 5 :
            print(user,"월은 봄")
        elif 6 or 7 or 8 :
            print(user,"월은 여름")
        elif 9 or 10 or 11 :
            print(user,"월은 가을")
    else :
        print("1~12 사이의 값을 입력하세요!")
        break