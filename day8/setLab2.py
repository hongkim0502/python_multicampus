import random

a = set()
b = set()
for i in range(0,6):
    a.update([random.randint(1,45)])
for i in a:
    if i not in b:
        b.update([i])
    elif a != b :
        a.clear()
        for j in range(0,6):
            a.update[(random.randint(1,45))]

print('행운의 로또번호 : ',a)