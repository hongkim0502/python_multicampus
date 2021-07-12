price = 1000
print(id(price))

def sale():
    global price
    price = 500
    print(id(price))

sale()
print(price)
print(id(price))