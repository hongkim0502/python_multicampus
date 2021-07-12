def a1(*a):
    sum = 0
    print(a)
    for num in a:
        sum += num
    return sum

print(a1(1,2,3))
print(a1(5,7,9,11,13))
print(a1(8,9,6,2,9,7,8))