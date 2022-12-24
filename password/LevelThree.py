def onelevel(a):
    if(ord(a) < 115):
        return twolevel(int(ord(a))+12)
    else:
        return twolevel(int(ord(a))-115)

def twolevel(pchar):
    ahoy = str(pchar)
    if(pchar%7 == 3):
        return threelevel(ahoy+"n")
    elif(pchar%3 == 1):
        return threelevel(ahoy+"f")
    else:
        return threelevel(ahoy+"z")


def threelevel(pchar):
    seenarray = [char for char in pchar]
    if(len(seenarray) == 2):
        clear = seenarray[1] + seenarray[0]
        return clear
    elif(len(seenarray) == 3):
        clear = seenarray[0] + seenarray[2] + seenarray[1]
        return clear
    elif(len(seenarray) == 4):
        clear = seenarray[2]+seenarray[3]+seenarray[0]+seenarray[1]
        return clear


print("Enter the Password")
password = input()
passwordarray = [char for char in password]
sanitized = ""
for a in passwordarray:
    sanitized += onelevel(a)
if(sanitized == "9z113z113z114f125n113z127z112n125n117f05z3"):
    print("Password is correct")
else:
    print("Password is incorrect")
