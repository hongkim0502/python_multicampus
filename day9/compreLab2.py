def mycompredict(**b):
    if len(b) == 0:
        return 0
    a = dict
    a = {'my' + k : v for k, v in b.items()}
    return  a

x = {'name':'김도','age':'40','address':'거여동'}
print(mycompredict(**x))