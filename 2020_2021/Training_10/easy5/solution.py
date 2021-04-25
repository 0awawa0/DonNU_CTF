from pwn import *


def roman_to_int(s):
    number = 0
    prevChar = '_'

    for i in range(len(s) - 1, -1, -1):
        if s[i] == 'I':
            if prevChar in "VX":
                number += -1
            else:
                number += 1
        elif s[i] == 'V':
            number += 5
        elif s[i] == 'X':
            if prevChar in "LC":
                number += -10
            else:
                number += 10
        elif s[i] == 'L':
            number += 50
        elif s[i] == 'C':
            if prevChar in "DM":
                number += -100
            else:
                number += 100
        elif s[i] == 'D':
            number += 500
        elif s[i] == 'M':
            number += 1000
        else:
            number += 0
        prevChar = s[i]

    return number




address = ("127.0.0.1", 43585)

conn = remote(address[0], address[1])

for _ in range(1000):
    s = conn.recvuntil(b">> ").decode().strip().split("\n")[-2].split(":")[-1].strip()

    conn.send(f"{roman_to_int(s)}\n".encode())

print(conn.recvall())