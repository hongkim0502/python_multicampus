price = [30, 13500, 2000]
for p in price :
    print("가격:%-7d원" % p)

pie = 3.14159265
print("%10f"%pie)
print("%10.8f"%pie)
print("%10.5f"%pie)
print("%10.2f"%pie)

print(round(3.1415, 2))
print(round(31.415, -1))

print(round(4.5))
print(round(3.5))

name = '김도'
age = 40
height = 175.3
print("이름:{}, 나이:{}, 키:{}".format(name,age,height))

name = '김도'
age = 41
height = 173.5
print("이름:{0:s}, 나이:{1:d}, 키:{2:f}".format(name,age,height))

name = '김도'
age = 42
height = 170.5
print("이름:{0:^10s}, 나이:{1:>5d}, 키:{2:<8.2f}".format(name,age,height))
