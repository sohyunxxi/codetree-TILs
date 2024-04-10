i=input()
iarr=i.split()
icold=iarr[0]
item = int(iarr[1])

k=input()
karr=k.split()
kcold=karr[0]
ktem = int(karr[1])

j=input()
jarr=j.split()
jcold=jarr[0]
jtem = int(jarr[1])

A=0
B=0
C=0
D=0

if icold=='Y' and item>=37:
    if (kcold=='Y' and ktem>=37) or (jcold=='Y' and jtem>=37):
        print('E')
    else:
        print('N')