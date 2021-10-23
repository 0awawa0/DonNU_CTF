import binascii
p = 0xf661398b
g = 0x02
client_public = 0x42b2769b
server_public = 0x916ddb94
#example secret, find real
secret=hex(123)
print(secret)
s='flag'
print(s)
r=''
i=0
for c in s:
    r += chr(ord(c) ^ ord(secret[i]))
    i+=1
    if i>=len(secret):
        i=0

print(r)
r=binascii.hexlify(bytes(r, "utf-8"))
print(r)
#encryptedflag=5417085b16226d20437b000f394c5314661108405c1c3957063e5a0a5d43550a03471e
