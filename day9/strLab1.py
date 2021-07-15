def myemail_info(a):
    if '@' not in a:
        return None
    a = a.split('@')
    s = (a[0])
    d = (a[1])
    return s, d

print(myemail_info('kim@naver.com'))
print(myemail_info('asdasd'))