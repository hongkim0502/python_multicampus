import random
i = 0
while True :
    i += 1
    Num = random.randint(0,30)
    if Num <= 26 and Num != 0:
        print(chr(64+Num),"(",Num,")")
    else :
        print("수행횟수는 ",i," 번 입니다")
        break
