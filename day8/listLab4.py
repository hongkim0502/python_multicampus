import random
a = []
listnum = a
for i in range(0, 10) :
    listnum.append(random.randint(1,50))

print(listnum)
for i in range(len(listnum)) :
    if listnum[i] < 10 :
        listnum[i] = 100

print(listnum)
print(listnum[1])
print(listnum[-1])
print(listnum[1:6])
print(listnum[::-1])
print(listnum[::1])
del listnum[4]
print(listnum[::1])
del listnum[1:3]
print(listnum[::1])