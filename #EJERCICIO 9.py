#ejercicio 9
lado1 = float(input("cual es la medida del primer lado?:"))
lado2 = float(input("cual es la medida del segundo lado?:"))
lado3 = float(input("cual es la medida del tercer lado?:"))

if lado1 == lado2 == lado3:
    print("el triangulo es equilatero")
elif lado1 != lado2 and lado1 != lado3 and lado2 != lado3:
    print("el triangulo es escaleno")
else:
    print("el triangulo es isosceles")