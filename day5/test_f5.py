def calcstep(begin, end, step):
    sum = 0
    for num in range(begin, end + 1 , step):
        sum += num
    return sum

print(calcstep(1,10,2))