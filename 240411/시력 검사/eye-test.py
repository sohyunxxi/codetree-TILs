left=float(input())
right=float(input())


if left>=1.0 and right>=1.0:
    print("High")
elif 1.0>left>=0.5 and 1.0>right>=0.5:
    print("Middle")
else:
    print("Low")