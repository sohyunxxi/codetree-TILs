i=input()
arr=i.split()

a=int(arr[0])
b=int(arr[1])
c=int(arr[2])

if a>b and b>c:
    print(c)
elif a>c and c>b:
    print(b)
elif b>a and a>c:
    print(c)
elif b>c and c>a:
    print(a)
elif c>a and a>b:
    print(b)
else:
    print(a)