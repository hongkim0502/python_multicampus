import random

a = []
b = []
for i in range(0,6):
    a.append(random.randint(1,45))
for i in a:
    if i not in b:
        b.append(i)
    elif a != b :
        a.clear()
        for j in range(0,6):
            a.append(random.randint(1,45))
print('행운의 로또번호 : ',a)
