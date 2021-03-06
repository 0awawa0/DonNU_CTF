
data = open("encrypted.png", "rb").read()

header = data[0]
key = 0

while True:
    if (header - key) % 256 == 0x89:
        break
    key += 1
 
decrypted = b""

for byte in data:
    decrypted += bytes([(byte - key) % 256])

open("decrypted.png", "wb").write(decrypted)