#ejercicio 8
año = int(input("¿cual es el año?:"))

if año % 4 == 0 and año % 100 != 0 or año % 400 == 0:
    print(f"el año {año} si es bisiesto")
else:
    print(f"el año {año} no es bisiesto.")