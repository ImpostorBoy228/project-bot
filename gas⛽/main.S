.section .rodata
msg:
    .ascii "Hello, world!\n"
len = . - msg

.section .text
.global _start

_start:
    # write(1, msg, len)
    mov $1, %rax
    mov $1, %rdi
    lea msg(%rip), %rsi
    mov $len, %rdx
    syscall

    # exit(0)
    mov $60, %rax
    xor %rdi, %rdi
    syscall
