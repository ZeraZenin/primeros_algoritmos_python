#Descuento Practica1
precio = float(input("Ingrese el pecio del producto:")) 
if precio > 500:
    descuento = precio * 0.10
    print (" Se aplico un descuento del 10%")
else: 
    descuento = precio * 0.04
    print (" Se aplico un descuento del 4%")
Nuevo_precio = precio - descuento 
print("Nuevo precio: " + str(Nuevo_precio))       