person = [('김',30),('도',35),('좋,25')]
mydict = dict(person)
print(mydict)

age = mydict['이택기']
print(age)

a = [1.2,2.5,3.7,4.6]
for i in range(len(a)):
    a[i] = int(a[i])

a[1,2,3,4]

a = [1.2,2.5,3.7,4.6]
a = list(map(int,a))

for number, upper, lower in zip("12345", "ABCDE", "abcde"):
    print(number, upper, lower)

type(number)