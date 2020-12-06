print("Ejercicio20")
print("Programa para saber la potencia de un número ")
print("Lilibeth Puchaicela")

#Proceso
base= int(input("Ingrese la base de la potencia " ))
pot= int(input("Ingrese la potencia " ))

#Ciclo repetitivo que obtiene la potencia de un número
i=1
res=1


while i<= pot:
		res=res*base
		print(res)
		i= i +1
print("La potencia de ", base, "elevado a", pot, "es" ,res)
