vo=['a','e','i','o','u','A','E','I','O','U']
stri=""
for i in input():
    if i not in vo:
        stri+=i
print(stri)