i=input()
arr=i.split()

a=int(arr[0])
b=int(arr[1])
c=int(arr[2])

min=a

if min>b:
    min=b
elif min>c:
    min=c
else:
    min=a

if a==min:
    print(1 end=" ")
else:
    print(0 end=" ")

if a==b==c:
    print(1 end=" ")
else:
    print(0 end=" ")