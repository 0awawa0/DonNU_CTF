from pwn import *


def is_mountain(arr):
	if len(arr) < 3: return False
	if arr[0] > arr[1]: return False

	rising = True
	for i in range(len(arr) - 1):
		if arr[i] == arr[i + 1]: return False
		if arr[i] < arr[i + 1] and not rising: return False
		if arr[i] > arr[i + 1] and rising: rising = False

	return True and not rising


port = int(input("Port >> "))
address = ("localhost", port)

conn = remote(address[0], address[1])

for _ in range(100):

	arr = list(map(int, conn.recvuntil(b">> ").decode().split("\n")[-2].split(":")[1].strip().split(" ")))
	if is_mountain(arr):
		conn.send("1\n".encode())
	else:
		conn.send("0\n".encode())

print(conn.recvall())