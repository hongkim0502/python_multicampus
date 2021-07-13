a = [[10,12,14,16],[18,20,22,24],[26,28,30,32],[34,36,38,40]]
print("1행 1열의 데이터 : ",a[0][0])
print("3행 4열의 데이터 : ",a[2][3])
print('행의 갯수 : ',len(a))
print('열의 갯수 : ',len(a[0]))
print('3행의 데이터들 : ',a[2])
sum = []
for i in range(len(a)) :
    sum.append(a[i][1])
print('2열의 데이터들 : ',sum)
sum.clear()
for i in range(len(a)):
    for j in range(len(a)):
        if(i==j):
            sum.append(a[i][j])
print('왼쪽 대각선 데이터들 : ',sum)
sum = []
for i in range(len(a)):
    for j in range(len(a)):
        if(len(a)-1-i)==j:
            sum.append(a[i][j])
print('오른쪽 대각선 데이터들 : ',sum)