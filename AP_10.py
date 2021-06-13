# Escribir un programa que escriba en pantalla los divisores de un número dado

num = int(input("Escribe un número\n"))

for div in range(1, num):
    if num%div == 0:
        print("Su número es divisible entre " + str(div))
input()