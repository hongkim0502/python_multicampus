def a1(a, *b, **c) :
    print(a)
    print()
    print(b)
    print()
    print(**c)

#a1('aaa' , 35 , addre = 'sad', height = 175, weight = 65)

print('add=',(lambda x, y : x + y)(10, 20))
