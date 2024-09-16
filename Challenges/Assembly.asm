section .data
    hello db 'Hello, World!', 0    ; The string to print, null-terminated

section .text
    global main

main:
    ; Write the string to stdout
    mov  rdx, 13                   ; Length of the string
    mov  rcx, hello                ; Pointer to the string
    mov  r8, 1                     ; Handle to the standard output (stdout)
    mov  rax, 0                    ; Function code for "WriteConsoleA" (or you can call `syscall` with 0)
    call printf                    ; Call printf function
    
    ; Exit the program
    mov  rax, 60                   ; System call number for exit (sys_exit)
    xor  rdi, rdi                  ; Exit code 0
    syscall                        ; Call the kernel to exit
