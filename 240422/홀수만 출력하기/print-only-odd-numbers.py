n=int(input())

count=1

while count<=n:
    num=int(input())
    if num%2==1 and num%3==0:
        print(num)
    count+=1