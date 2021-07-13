def print_triangle_withdeco(a,b = '%'):

    if 0 < a <= 10 :
        for i in range(a+1):
            for j in range(a,0,-1):
                if j <= i :
                    print(b,end = '')
                else :
                    print(" ",end= '')
            print()
    else :
        return

print(print_triangle_withdeco(5,'*'))