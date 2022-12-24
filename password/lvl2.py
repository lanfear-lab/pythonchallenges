import base64
import re
print("Enter the Password")
hello = input()
password = base64.b64encode(hello.encode("utf-8"))
passwordd = re.findall(r"'(.*?)'", str(password))
if(passwordd[0] == "eW91ZGlkaXQh"):
    print("Password is correct")
else:
    print("Password is incorrect")
