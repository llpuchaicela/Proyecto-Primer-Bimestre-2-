print("Ejercicio11")
print("Lilibeth Puchaicela")

#Ingreso de datos
while (True):

	print("Programa de calculadora básica \n ")

	num1=float(input("Ingrese un número : "))
	num2=float(input('Ingrese el otro número: '))

	#Proceso
	print('Selecciona la operación que deseas realizar :')
	print('1. Suma')
	print('2. Resta')
	print('3. Múltiplicación')
	print('4. Dividir')
	opc= int(input('Elija la opción: '))

	if opc==1:
		resp= num1+num2
		print(resp)

	if opc ==2:
		resp= num1-num2
		print(resp)

	if opc == 3:
		resp = num1* num2
		print(resp)

	if opc== 4 :
		resp= num1//num2
		print (resp)
