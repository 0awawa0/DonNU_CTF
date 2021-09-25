import os


def doBitwiseEncryption(x, y):
	res = 0
	for i in range(8):
		mask = 1 << i
		c = (((x & mask) >> i) + ((y & mask) >> i)) % 2
		res = ((c << i) | res)
	return res


def encrypt(flag, key):
	res = b""
	for i in range(len(flag)):
		res += bytes([doBitwiseEncryption(flag[i], key[i % len(key)])])
	return res


flag = open("flag", "rb").read()
key = os.urandom(8)
ciphertext = encrypt(flag, key)
print(ciphertext.hex())

# 67b4cf7390ff94c178eec57e83dea3bf36e39579d2d8a4e367e8922f818df1e133ba987e8785f7e63ba6
