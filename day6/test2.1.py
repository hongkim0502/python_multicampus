def test(a) :
    a = int(input("숫자입력 : "))
    sum = 0
    for i in range(0,a+1) :
        print('*' * i )
        sum += i
    return sum
print('별의 갯수 : ', test(sum))
