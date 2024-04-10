a=input()
a=int(a)

if a%2==0:
    a= int(a/2)
    print(a)
if a%2!=0:
    a=a+1
    a= int(a/2)
    print(a)