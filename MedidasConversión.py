print("Ejercicio13")
print("Programa para convertir medidas")
print("Lilibeth Puchaicela")
#Inicialización de variables
m= float(0)
cm= float(0)
km = float(0)
f = float(0)
p=float(0)
# Ingreso de datos
m=float(input("Ingrese el valor en metros " ))
cm=float(input("Ingrese el valor de un centimetro " ))
km = float(input("Ingrese el valor de 1 Kilómetro "))
f= float(input("Ingrese el valor de 1 pies " ))
p= float(input("Ingrese ell valor de 1 Pulgadas "))
# Proceso

cm = m/100
km = m/1000
f= m* 3.28
p= m* 39.37

print("La conversión de metros es" ,m, "cm es igual a %.5f " % cm,
  "km es igual %.5f " % km, "F es igual a ",f , "Y P es igual a ", p)