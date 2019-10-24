from pwn import *

io = remote('111.198.29.45', 56845)
io.interactive()