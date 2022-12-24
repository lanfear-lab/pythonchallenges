#Password: onlYaCouPleMore!
from datetime import date
import re

def gtnm():
    x = str(date.today())
    z = re.findall("\d+", x)
    y = z[0]+z[1]+z[2]
    b = ""
    for a in y:
        if int(a) >= 2 and int(a) <= 5:
            b = b + a
    return b

def chdtnm(l,g):
    x = [char for char in g]
    xt = []
    bt = []
    y = 0
    b = [char for char in l]
    for a in x:
        xt.append(int(ord(x[y])))
        y = y+1
    y = 0
    for a in b:
        bt.append(int(b[y]))
        y=y+1
    t = mksn(xt,bt)
    w = ""
    for e in t:
        w = w + chr(e)
    if(w=="qpn\\fEqwSqgOquj#"):
        return 1
    else:
        return 0

def mksn(l,g):
    i=0
    x= []
    for a in l:
        if(i < len(l)):
            x.append(a+g[i%5])
        if(x[i] > 127):
            x[i] = x[i]-127
        i = i+1
    return x

x = gtnm()
print("Enter the Password")
y = input()
a = chdtnm(x,y)
if(a):
    print("Password is correct")
else:
    print("Password is incorrect")
