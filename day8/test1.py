rg = 5

for i in range(rg, 0, -1):
    print(i, ' ' * (i), end='')
    print('*' * (rg - (i - 1)))

def sum_all(*args):
    result = 0
    for i in args:
        result += i

    return result

print(sum_all(1, 2, 3, 4, 5))
print(sum_all(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))

my_list = ['A', 'B', 'C', 'D', 'B', 'D', 'E']
# 집합으로 변환
my_set = set(my_list)

# 리스트로 변환
new_list = list(my_set)

# 결과 출력
print(type(new_list))
# >>> <class 'list'>

print(new_list)
# >>> ['D', 'B', 'A', 'E', 'C']

new_list = []

for v in my_list:
    if v not in new_list:
        new_list.append(v)

print(type(new_list))
# >>> <class 'list'>

print(new_list)
# >>> ['A', 'B', 'C', 'D', 'E']