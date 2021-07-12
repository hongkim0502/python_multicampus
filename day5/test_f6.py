def a(**a1):
    begin = a1['begin']
    end = a1['end']
    step = a1['step']

    sum = 0
    for num in range(begin, end + 1, step):
        sum += num
    return sum

print(a(begin = 3,step= 1, end = 5))