def mat():
    print("Matrix order is 2x3 \n !!which means a row must contain 3 elements only!!  ")

    a=input("Enter the elements of 1st row:")
    a2=[]
    a1=""
    b=input("Enter the elements of 2st row:")
    b2=[]
    b1=""

    for k in a:
        for i in a:
            if k==" " or k==",":
                break
        else:
            a1+=k
    for k in b:
        for i in b:
            if k==" " or k==",":
                break
        else:
            b1+=k
            
    for i in a1:
        a2.append(int(i))
    for i in b1:
        b2.append(int(i))
    m=[a2,b2]

    t=[[0,0],[0,0],[0,0]]
    if (len(a2),len(b2))==(3,3):
        for i in range(len(m)):
            for j in range(len(m[0])):
                t[j][i]=m[i][j]
        print('\nActual matrix' )
        for i in m:
            print(i)
        print("\nTranspose")
        for i in t:
            print(i)
    else:
        print("invalid entries")
        mat()
mat()
