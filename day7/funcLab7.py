import random
def differtwovalue(a,b) :
    if a != b :
        sum =max(a,b) - min(a,b)
    else :
        sum = 0
    return sum
for i in range (0, 5) :
    a = random.randint(1,30)
    b = random.randint(1,30)
    differtwovalue(a,b)
    print(a, " 와 ", b , " 의 차는 ", differtwovalue(a,b), " 입니다")