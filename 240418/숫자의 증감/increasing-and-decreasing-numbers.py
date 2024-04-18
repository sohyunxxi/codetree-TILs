num=input()

arr=num.split()

c=arr[0]
n=int(arr[1])

if c=='A':
    for i in range(1,n+1):
        print(i,end=" ")
        i+=1   

elif c=='D':
    i=n
    for i in range(n,0,-1):
        print(i,end=" ")