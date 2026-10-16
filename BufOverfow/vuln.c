/*
 * Reconstructed source for the bof training binary.
 * Rebuild with GCC 11.4.0 on Ubuntu 22.04:
 *   gcc -no-pie -fno-stack-protector vuln.c -o bof
 *
 * The oversized read is intentional for buffer-overflow practice.
 */

#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

__attribute__((force_align_arg_pointer))
void win(void) {
    puts("\n[+] win() reached - spawning /bin/sh");
    system("/bin/sh");
}

int main(void) {
    char buf[8];

    setvbuf(stdout, NULL, _IONBF, 0);
    setvbuf(stdin, NULL, _IONBF, 0);

    puts("64-bit ret2win practice");
    printf("input> ");
    read(0, buf, 256);
    puts("bye");
    return 0;
}
