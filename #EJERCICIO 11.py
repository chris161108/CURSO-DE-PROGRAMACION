#ejercicio 11
n1 = float(input("escribe un numero: "))
n2 = float(input("escribe otro numero: "))
operador = input("elije un operador: (+, -, *, /): ")

if operador == "+":
    total = n1 + n2
    print("el resultado es:", total)
elif operador == "-":
    total = n1 - n2
    print("el resultado es:", total)
elif operador == "*":
    total = n1 * n2
    print("el resultado es:", total)
elif operador == "/":
    if n2 == 0:
        print("no puedes dividir entre cero")
    else:
        total = n1 / n2
        print("el resultado es:", total)
else:
    print("operador incorrecto")
