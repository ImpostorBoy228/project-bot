.global _start
.data
    res: .long 0

.text
_start:
    
    mov $60, %rax
    xor %rdi, %rdi
    syscall


