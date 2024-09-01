section .data
    hello db 'Hello, World!', 0    ; The string to print, null-terminated
	

section .text
    global _start

_start:
    ; Call WriteConsoleA
    mov  edx, 13                   ; Length of the string
    mov  ecx, hello                ; Pointer to the string
    mov  ebx, 1                    ; Handle to the standard output (stdout)
    mov  eax, 4                    ; System call number (sys_write)
    int  0x80                      ; Call the kernel

    ; Exit the program
    mov  eax, 1                    ; System call number (sys_exit)
    xor  ebx, ebx                  ; Exit code 0
    int  0x80                      ; Call the kernel

