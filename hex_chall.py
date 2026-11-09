with (open("chall.txt", "r")) as r:
    binary = bytes.fromhex(r.read()).decode().split()

binary = binary[3 - len(binary):] # Getting rid of "this is binary"
octal = ''.join(chr(int(byte, 2)) for byte in binary)
octal = octal[15 - len(octal):] # Getting rid of "this is octal"
print(octal)
