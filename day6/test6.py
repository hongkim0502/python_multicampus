name = '이택기'
if name.startswith('이'):
    print('yee')
if name.startswith('택'):
    print('ayy')

file = 'k.jpg'
if file.endswith('.jpg'):
    print('그림파일')

s = "   angel   "
print("+"+ s.lstrip() + "님")
print("+"+ s.rstrip() + "님")
print("+"+ s.strip() + "님")

s = "자장 짬뽕 탕수육"
print(s.split())

s = "서울->대전->대구->부산"
city = s.split("->")
print(city)
for c in city:
    print(c, "찍고", end ='/')

var = 'abc'
print("%s"%var)

var=123
print("%d"%var)

var=123
print("%f"%var)

var = 123.23
print("%f"%var)