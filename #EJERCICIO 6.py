#ejercicio 6
compra = float(input("¿cual es el valor de su compra?"))
if compra > 100:
    print("felicidades por su compra, se aplico un descuento")
    descuento = compra * 0.15
    total = compra - descuento 
    print(f"el total a pagar es {total}")
else:
    print("felicidades por su compra")
