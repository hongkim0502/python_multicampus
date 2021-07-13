a = [[10,20,30,40,50],[5,10,15],[11,22,33,44],[9,8,7,6,5,4,3,2,13]]
sum = 0
for i in range(0,5):
    sum += a[0][i]
print('1행의 합은',sum)
sum = 0
for i in range(0,3):
    sum += a[1][i]
print('2행의 합은',sum)
sum = 0
for i in range(0,4):
    sum += a[2][i]
print('3행의 합은',sum)
sum = 0
for i in range(0,9):
    sum += a[3][i]
print('4행의 합은',sum)