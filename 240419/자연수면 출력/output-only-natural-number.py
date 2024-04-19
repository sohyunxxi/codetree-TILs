arr=input()
num=arr.split()

a=int(num[0])
b=int(num[1])

if a>0 :
    for i in range(1,b+1,1):
        print(a,end="")
elif a<=0:
    print(0)