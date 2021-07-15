import random
a = []
for i in range(0,10):
    a.append(random.randint(0,100))

a = {i : 'wait' for i in a }
b = {k :'nopass' for k, v in a.items() if k < 60}
c = {k :'pass' for k, v in a.items() if k >= 60}
a = {**b, **c}

print(a)