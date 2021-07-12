def exper(a,b,c=str) :
    if c == '+' :
        sum = a+b

    elif c == '-' :
        sum = a-b

    elif c == '*' :
        sum = a*b

    elif c == '/' :
        sum = a/b
    else :
        sum = 'None'


    return sum

a = exper(int(input("값을 입력 :")),int(input('값을 입력 : ')),input('연산자 입력 : '))
if a == 'None':
    print('수행 불가')
else :
    print('연산결과 : ',a)

