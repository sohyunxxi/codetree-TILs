n=int(input())

if n==2:
    print(28)
elif (n%2==1 and n%9>0) or n==8:
    print(31)
else:
    print(30)