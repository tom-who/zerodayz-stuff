import base64
import html
from urllib.parse import unquote

with (open("chall.txt", "r")) as r:
    binary = bytes.fromhex(r.read()).decode().split()

binary = binary[3 - len(binary):] # Getting rid of "this is binary"
octal = ''.join(chr(int(byte, 2)) for byte in binary).split()
octal = octal[3 - len(octal):] # Getting rid of "this is octal"
b64 = ''.join(chr(int(num, 8)) for num in octal).split()
b64 = base64.b64decode(b64[-1]).decode()
htmlID = html.unescape(b64).split()
htmlID = unquote(htmlID[9 - len(htmlID)]).split()[-1]
print(htmlID)

# Continue on cyberchef or some other online decode !!!!!!!
