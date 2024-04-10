a=input()

arr=a.split()

am=int(arr[0])
ae=int(arr[1])

b=input()

brr=b.split()

bm=int(brr[0])
be=int(brr[1])


if am>=bm:
    if(am==bm):
        if(ae>be):
            print("A")
        else:
            print("B")
    else:
        print("A")
else:
    print("B")