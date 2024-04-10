i=input()

arr=i.split()

aAge=int(arr[0])
aSex=arr[1]

b=input()

brr=b.split()

bAge=int(brr[0])
bSex=brr[1]

if aAge>=19 and aSex=='M':
    print(1)
elif bAge>=19 and bSex=='M':
    print(1)
else:
    print(0)