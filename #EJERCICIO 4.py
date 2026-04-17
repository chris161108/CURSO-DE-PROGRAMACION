#ejercicio 4

calificacion = float(input("¿cual fue tu calificacion?"))
if   calificacion > 100:
     print("eres un genio")
elif calificacion >= 60:
    print("aprovado")
elif calificacion <= 0: 
     print("no sirves")
elif calificacion < 60:
     print("reprovado")
else:
    print("error")