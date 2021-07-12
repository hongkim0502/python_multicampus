#def a(n) :
    #sum = 0
    #for num in range (n + 1):
     #   sum += num
    #print(n , sum)

#a(4)
#a(10)

def b(x,y) :
    a1 = x + y
    a2 = x - y
    a3 = x * y
    a4 = x / y

    return a1,a2,a3,a4

t, s, m, d = b(10, 20)

print(t)
print(s)
print(m)
print(d)
