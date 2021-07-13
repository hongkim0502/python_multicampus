def sumAll(*a) :
    sum = 0
    for i in range(len(a)) :
        if type(a[i]) == int:
            sum += a[i]
    if sum == 0 :
        return None
    return sum

print(sumAll('a','b'))