# Escribir un programa que nos diga si un número dado es primo (no es divisible
# por ninguno otro número que no sea él mismo o la unidad)

num = int(input("Escribe un número y te digo si es primo\n"))
raiz = num**0.5
primos = [2,3,5,7,11,13,17,19]

if num in primos:
    print("Tu número es primo")
elif num < 20 and not num in primos:
    print("Tu número no es primo")
else:
    for div in range(2,int(round(raiz) + 1)):
        if num%div == 0:
            print("Su número no es primo")
            break
        elif div == (int(round(raiz))):
            print("Su número es primo")
            break
input()