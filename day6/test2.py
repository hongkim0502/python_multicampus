
def star(sum) :
    sum =0
    height = int(input("height : "))
    for i in range (1, height+1) :
        sum += i
        for j in range (i) :
            print("*",end = '')

        print()
    return sum

print('별의 갯수 : ',star(sum))