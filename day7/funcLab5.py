def print_triangle(a) :
    if a <= 10 :
        for i in range(a):
            for j in range (a) :
                if j < i :
                    print('',end='')
                else :
                    print('@',end='')
            print()

    else :
        return a

print_triangle(5)