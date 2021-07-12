def print_gugudan(a) :
    if a != str(a) and 0 < a <= 9 :
        for i in range(1, 10) :
            print(a,"x",i,"=",a*i, end='\t')
    else :
        return a

print_gugudan(2)