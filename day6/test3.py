vac = [[1,2,3,], [4,5,6,], [7,8,9]]

flatten = lambda  list : [item for sublist in list for item in sublist]

print(flatten(vac))