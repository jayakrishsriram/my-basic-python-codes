n=input("Enter a string: ")
m=""
for i in range(len(n)):
    m+=n[len(n)-(i+1)]
if m==n:
    print("{} is a PALINDROME".format(n))
else:
    print("{} is not a PALINDROME".format(n))
