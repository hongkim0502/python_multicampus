import random

while True :
    pairNum1 = random.randint(1, 6)
    pairNum2 = random.randint(1, 6)
    if pairNum1 > pairNum2 :
        print('pairNum1이 pairNum2 보다 크다.')
    elif pairNum1 == pairNum2:
            print("게임 끝")
            break
    else :
        print('pairNum1이 pairNum2 보다 작다.')

