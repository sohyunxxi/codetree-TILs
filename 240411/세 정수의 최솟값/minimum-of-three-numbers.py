i=input()
arr=i.split()

a=int(arr[0])
b=int(arr[1])
c=int(arr[2])

if a>b>c:
    print(c)
elif a>c>b:
    print(b)
elif b>a>c:
    print(c)
elif b>c>a:
    print(a)
elif c>a>b:
    print(b)
else:
    print(a)