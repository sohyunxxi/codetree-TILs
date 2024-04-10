n=int(input())
if n%2==0:
    if n==2:
        print(28)
    elif 2<n<8:
        print(30)
    elif 8<=n<=12:
        print(31)
else:
    if n<9:
        print(31)
    elif n==9 or n==11:
        print(30)