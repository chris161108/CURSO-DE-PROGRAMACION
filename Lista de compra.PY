  # LISTA DE COMPRA 

carrito = []
precios = []
continuar = True

print(" CARRITO DE COMPRAS")

while continuar:
    print("\nelije un numero del (1-5) ")
    print("1. agregar producto")
    print("2. eliminar producto")
    print("3. ver cesta")
    print("4. calcular total")
    print("5. salir")
    
    opcion = input("\nSelecciona una opción (1-5): ")

    if opcion == "1":
        nombre = input("Nombre del producto: ")
        precio = float(input(f"precio de {nombre}: "))
        carrito.append(nombre)
        precios.append(precio)
        print(f"¡{nombre}  añadido a la cesta!")

    elif opcion == "2":
        if len(carrito) > 0:
            eliminar = input("Nombre del producto a quitar: ")
            if eliminar in carrito:
                indice = carrito.index(eliminar)
                carrito.pop(indice)
                precios.pop(indice)
                print(f" quitaste {eliminar} de la lista.")
            else:
                print("ese producto no esta en tu cesta.")
        else:
            print("el carrito está vacío, no hay nada que eliminar.")

    elif opcion == "3":
        print("\n--- tu cesta---")
        if not carrito:
            print("la cesta esta vacia.")
        else:
            for i in range(len(carrito)):
                print(f"{i+1}. {carrito[i]} - ${precios[i]}")

    elif opcion == "4":
        total = sum(precios)
        print(f"\nel total a pagar es: ${total}")

    elif opcion == "5":
        print("gracias por tu compra.")
        continuar = False

    else:
        print("opcion no valida.")