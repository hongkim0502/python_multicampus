listnum = 10,5,7,21,4,8,18
mi = listnum[0]
ma = listnum[0]
for i in listnum :
    if(i < mi) :
        mi = i
    elif(i > ma) :
        ma = i
print('최솟값 : ',mi," 최댓값 : ", ma)