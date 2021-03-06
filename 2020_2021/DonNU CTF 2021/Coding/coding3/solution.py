from pwn import *


def hamming_distance(a, b):
	count = 0
	for i in bin(a ^ b):
		if i == '1': count += 1
	return count


port = int(input("Port >> "))
address = ("localhost", port)

conn = remote(address[0], address[1])

for _ in range(100):

	a, b = tuple(map(int, conn.recvuntil(b">> ").decode().split("\n")[-2].split(":")[1].strip().split(" ")))
	conn.send(f"{hamming_distance(a, b)}\n".encode())

print(conn.recvall())