def sumEven1(*a):
    sum = 0
    if len(a) == 0:
        return -1
    for j in range(len(a)) :
        if a[j] % 2 == 0 :
             sum += a[j]
    return sum


print(sumEven1(1,3,5,7))