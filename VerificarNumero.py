print("Ejercicio17")
print("Programa para verificar la suma de un numero par, impar, positivo y negativo")
print("Lilibeth Puchaicela")
i=1 
n=1
sumPos=0
sumNeg=0
sumPar=0
sumImpar=0
suma=0

n=int(input("Ingrese el limite"))

while i <= n:

	num= int(input("Ingrese el número a verificar " ))

	if num % 2==0: # Verifica si un número es par
		sumPar=sumPar + num # suma los números pares

	else:  # Verifica si un número es impar
		sumImpar = sumImpar + num  # suma los números impares

	if num > 0: # Verifica si un número es positivo
		sumPos = sumPos+ num # suma los números positivos

	else: # Verifica si un número es negativo
		sumNeg = sumNeg + num # suma los números negativos

	i = i+1

print("La suma de los pares es: " ,sumPar)
print("La suma de los impares es : " , sumImpar)
print("La suma de los positivos es: " , sumPos)
print("La suma de los negativos es : ", sumNeg)