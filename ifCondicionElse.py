print("Hola, buen día") 
costo = float(input("¿Qué costo tienen hoy las manzanas? "))
cantidad = float(input("¿Cuantas manzanas requiere el cliente? "))

if(cantidad>10): #Si el cliente pide más de 10 manzanas le daremos un 10% de descuento
    descuento=costo*cantidad*.1
    print(f"Gracias por su compra")
    print(f"El descuento es: {round(descuento,2)}")
    print(f"El cliente pagara en total {(costo*cantidad)-descuento}")
else:
    print("NO HAY DESCUENTO")
    print(f"El precio total es de: {costo*cantidad}")