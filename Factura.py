print("Ejercicio12")
print("Programa para calcular el total de una factura de venta")
print("Lilibeth Puchaicela")
#Declaración e inicialización de variables
subtotal=0
total=0
descuento=0
limite1=200
limite2=500
#Ingrese las variables
print ("Factura de Venta")
print("Por compar mayores o iguales a 200$, se le aplicara un descuento del 10%")
print("Por comprar mayores o iguales a 500$, se le aplicara un descuento del 15%")

subtotal=float(input("Ingrese el subtotal de la compra: "))
subtotal= float(subtotal)
# Proceso

if subtotal >= limite1 and subtotal< limite2:
	descuento =0.10
else:
	decuento =0.15
if subtotal<limite1:
	decuento=0.0
print("No tiene decuento")
total=subtotal-(subtotal*descuento)
#Salida de datos
print("El total de la compra es", total, "con un descuento de" , descuento)