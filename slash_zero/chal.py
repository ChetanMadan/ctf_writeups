import os

import sys
import random
a=input("")
pr=""
ch=a[0]
ch=int(ch)
n=a[2:]


if int(ch)==1:
    with open("newfile","w") as fi:
        n=int(n)
        for i in range(97,97+n):
            j=i
            if j>122:
                j=j-26
            pr=pr+chr(j)
        fi.write(pr)
        print(pr)
elif int(ch)==2:
    with open("newfile","r") as fi:
        string=fi.read()
    i=0
    if n in string:
        for i in range(len(string)):
            if string[i]==n[0]:
                print(i+1)
