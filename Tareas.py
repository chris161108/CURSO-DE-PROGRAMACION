"""¡Hola a todos! 🚀👨‍💻 ¡Es hora de poner a prueba nuestra lógica algorítmica con Python! 🐍🔥

Hoy nos enfocaremos en dominar los *Bucles y su Control* (`for`, `while`, `break`, `continue`). Aquí les dejo 5 retos diseñados para que practiquen a fondo:

🟢 *NIVEL FÁCIL* 🟢

*1. Acumulador con interrupción* ➕
_Enunciado:_ Desarrollar un programa que pida números enteros para sumarlos. El programa debe detenerse y mostrar el resultado total SOLAMENTE cuando se ingrese un 0.
_Requerimientos:_ 
- Usar bucle `while`.
- Usar `break` para salir con el 0.

*2. Saltando múltiplos* 🦘
_Enunciado:_ Imprimir los números del 1 al 20, saltándose todos los que sean múltiplos de 3.
_Requerimientos:_ 
- Usar bucle `for` y `range()`.
- Usar `continue` para evitar imprimir los múltiplos.

🟡 *NIVEL INTERMEDIO* 🟡

*3. Verificador de números primos* 🔢
_Enunciado:_ Pedir un número entero y determinar si es primo.
_Requerimientos:_ 
- Iterar con un `for`.
- Usar `break` al encontrar un divisor.
- Aprovechar la estructura `for...else` de Python.

*4. Simulador de acceso* 🔐
_Enunciado:_ Crear un login con contraseña ("python123"). El usuario tiene solo 3 intentos.
_Requerimientos:_ 
- Usar `while` con contador.
- Salir con `break` si la contraseña es correcta, de lo contrario, bloquear al tercer intento fallido."""


# 1. Acumulador con interrupción

total = 0
while True:
    numero = int(input("Ingresa un número (0 para terminar): "))
    if numero == 0:
        break
    total += numero

print(f"La suma total es: {total}")

# 2. Saltando múltiplos
print("Números del 1 al 20, saltando múltiplos de 3:")
for i in range(1, 21):
    if i % 3 == 0:
        continue
    print(i)

# 3. Verificador de números primos
num = int(input("Ingresa un número para verificar si es primo: "))
es_primo = True

for i in range(2, num):
    if num % i == 0:
        es_primo = False
        break

if es_primo:
    print(f"{num} es un número primo.")
else:
    print(f"{num} no es un número primo.")

# 4. Simulador de acceso
contraseña_correcta = "python123"
intentos = 3

while intentos > 0:
    contraseña = input("Ingresa la contraseña: ")
    if contraseña == contraseña_correcta:
        print("Acceso concedido.")
        break
    else:
        intentos -= 1
        print(f"Contraseña incorrecta. Te quedan {intentos} intentos.")

if intentos == 0:
    print("Acceso bloqueado.")

