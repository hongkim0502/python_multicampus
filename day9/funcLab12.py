def myprint(*a,**b):
    s = {}
    y = ()
    if a == y and len(b) == len(s) :
        print('Hello Python')
    elif b.get('deco'and'sep'):
        print(end=b['deco'])
        print(*a,end=b['deco'],sep=b['sep'])
        print(end='\n')
    elif b.get('deco'):
        print(end=b['deco'])
        print(*a,end=b['deco'])
        print(end='\n')
    elif b.get('sep'):
        print(*a,sep=b['sep'])
        print(end='\n')
    elif a != y and len(b) == len(s) :
        print(end='**')
        print(*a,end='**',sep=',')
        print(end='\n')

myprint(10,20,30,deco='@',sep='-')
myprint('python','javascript','R',deco='$')
myprint('가','나','다')
myprint(100)
myprint(True,111,False,'abc',deco='&',sep="")
myprint()