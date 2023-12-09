a = {'jai': 'krish'}
b, c = input("Enter username:"), input("Enter password:")
if (b in a.keys()) and (c == a[b]):
    print("password verified")
else:
    print("username not found or password not verified")
