def a1(name, *score, **option):
    print(name)
    sum = 0
    for s in score :
        sum += s
    print("총점 :", sum)
    if(option['avg'] == True):
        print("평균 :", sum / len(score))

a1("김", 88, 99, 77, avg= True)
