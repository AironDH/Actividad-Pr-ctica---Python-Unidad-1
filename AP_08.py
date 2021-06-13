# Escribe un programa que pida un número y nos diga si es divisible por 2, 3, 5 o 7
# (sólo hay que comprobar si lo es por uno de los cuatro)

num = int(input("Ingresa un número\n"))
if num%2==0 or num%3==0 or num%5==0 or num%7==0:
    print("Es divisible por 2, 3, 5 o 7")
else:
    print("No es divisible por ninguno")
input()