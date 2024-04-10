sex=input()
sex=int(sex)

age=input()
age=int(age)

if sex==1:
    if age>=19:
        print("MAN")
    else:
        print("BOY")
else:
    if age>=19:
        print("WOMAN")
    else:
        print("GIRL")