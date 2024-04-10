i=input()

arr=i.split()

a=int(arr[0])
b=int(arr[1])


if a>=90:
    if b>=95:
        print("100000")
    elif 90<=b :
        print("50000")
    else:
        print("0")
else:
    print("0")