s1 = "pythonjavascript"
print(len(s1))
s2 = "010-7777-9999"
s2 = s2.split('-')
s2 ="".join(s2)
print(s2)
s3 = 'PYTHON'
s3 = list(s3)
s3.reverse()
s3 = ''.join(s3)
print(s3)
s4 = 'Python'
s4 = s4.lower()
print(s4)
s5 = 'http:s//www.python.org/'
print(s5[8:22])
s6 = '891022-2473837'
a = s6[7]
if a == '1' or a == '3' :
    print(a, '남성')
elif a == '2' or a == '4' :
    print(a, '여성')
s7 = '100'
print(int(s7),float(s7))
s8 = 'The Zen of Python'
sum = 0
for i in s8:
    if i == 'n':
        sum += 1
print(sum)
index = s8.find('Z')
print(index)
s8 = s8.upper()
s8 = list(s8)
print(s8)



