def print_triangle(a) :
    if a <= 10 :
        for i in range(0, a + 1):
            for j in range(i):
                print('*',end='')
            print()
    else :
        return a

print_triangle(5)