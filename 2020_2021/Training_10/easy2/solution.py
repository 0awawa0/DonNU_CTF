from pwn import *


def largestSubArray(arr):
    currSum = arr[0]
    maxSum = arr[0]

    for i in range(1, len(arr)):
        currSum = max(arr[i], currSum + arr[i])
        maxSum = max(currSum, maxSum)

    return maxSum


address = ("127.0.0.1", 43584)

conn = remote(address[0], address[1])

for _ in range(100):
	arr = list(
		map(
			int, 
			conn.recvuntil(b">> ").decode().strip().split("\n")[-2].split(":")[-1].strip().split(" ")
		)
	)

	conn.send(f"{largestSubArray(arr)}\n".encode())

print(conn.recvall())