i=input()
arr=i.split()

a=int(arr[0])
b=int(arr[1])
c=int(arr[2])

# a가 가장 작은 경우
if a <= b and a <= c:
    print(a)
    
# b가 가장 작은 경우
elif b <= a and b <= c:
    print(b)

# c가 가장 작은 경우
else:
    print(c)