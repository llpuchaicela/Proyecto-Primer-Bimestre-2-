print ("Ejercicio 19 ")
print("Programa para generar   serie de numeros Fibonacci")
print("Lilibeth Puchaicela ")

num1=0
num2=1
suma=0

#   
n=int(input("Ingrese el limite de la serie Fibonacci " ))

   
#Proceso ciclo for
for i in range(1,n) :
           
    if i < 2:
	    print(i, "," ,num1)
	    print(i+1 , "," ,num2)
	    suma = num1 + num2
		
    else:
    	fibo = num1 + num2
    	suma = suma + fibo
    	num1 = num2
    	num2 = fibo
    	i= i+1
    	print(i , "," ,fibo)
            
    
         
print(" PRIMERA SUMA: " ,suma)

print("............................. ")

print(" Segunda soluciòn : ")
        
num1 =0
num2 = 1
fibo = 0
suma1=0

for  i in range (1, n+1):
	print(i, "," ,num1)
	suma1 = suma1 + num1
	fibo = num1 + num2
	num1 = num2
	num2= fibo
            

        
print(" SEGUNDA SUMA: " ,suma1 );
