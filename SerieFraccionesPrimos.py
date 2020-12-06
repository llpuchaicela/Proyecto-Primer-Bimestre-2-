print("Ejercicio22")
num = 0
den = 0
suma = 0
primo = 2
divisor = 0
bandera = False

n = int(input("Programa para generar la serie \nIngrese el limite de la serie\n"))

for i in range(1, n+1):
    num += 1

    bandera = False
    while (not bandera):
        for j in range(1, primo+1):
            if (primo % j) == 0:
                divisor += 1

        if divisor == 2:
            bandera = True
            den = primo
            primo += 1
        else:
            primo += 1
        divisor = 0

    if (i % 2) == 0:
        print(f'{i} -{num}/{den}')
        suma -= num/den
    else:
        print(f'{i} +{num}/{den}')
        suma += num/den
        
print("------------------------------")
print(f'La suma de la serie es: {suma}')