n=int(input())

i=1
while i<=n:
    if i%10==0 or i%10==3 or i%10==6 or i%10==9 or i//10==3 or i//10==6 or i//10==9:
        print(0,end=" ")
        i+=1
    else:
        print(i,end=" ")
        i+=1