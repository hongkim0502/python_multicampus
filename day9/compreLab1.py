import random
def createList(*type):
    a = {}
    if len(type) == 0 :
        a = random.randint(1,30)
    elif len(type) == 2 :
        a = {i for i in type if i % 2 == 0}
    elif len(type) == 3 :
        a = {i for i in type if i % 2 == 1}
    elif len(type) == 4 :
        a = {i for i in type if i > 10 }
    elif len(type) == 1 :
        a = type
    return a

print(createList(1,2,5))
print(createList(4,7))
print(createList())
print(2,40,1,24)
print(createList("김도"))