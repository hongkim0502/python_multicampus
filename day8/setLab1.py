import random
a = set()
b = set()

for i in range(0,10):
    a.update([random.randint(1,20)])
    b.update([random.randint(1,20)])

print(a)
print(b)
print(a&b)
print(a|b)
print(a-b)
print(b-a)
print(a,b)