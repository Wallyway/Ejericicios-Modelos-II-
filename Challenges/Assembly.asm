global _start ; Declaración global de la etiqueta _start

section .text ; Sección de código ejecutable
_start:
    mov rax, 1                              ; Cargar el número de sistema 1 en el registro rax (para la llamada al sistema write)
    mov rdi, 1                              ; Cargar el descriptor de archivo 1 (stdout) en el registro rdi
    mov rsi, message                        ; Cargar la dirección de la cadena "Hello, World!" en el registro rsi
    mov rdx, 13                             ; Cargar la longitud de la cadena (13 caracteres) en el registro rdx
    syscall                                 ; Llamar al sistema para escribir la cadena en la consola

    mov rax, 60                             ; Cargar el número de sistema 60 en el registro rax (para la llamada al sistema exit)
    xor rdi, rdi                            ; Establecer el código de salida en 0 (en rdi)
    syscall                                 ; Llamar al sistema para salir del programa

section .data                               ; Sección de datos
message: db "Hello, World!", 10             ; Definir la cadena "Hello, World!" seguida de un salto de línea (carácter 10)
