# Escribe un programa que pida un número y nos diga si es divisible por 2, 3, 5 o 7
# Añadir al ejercicio anterior que nos diga por cuál de los cuatro es divisible 
# (hay que decir todos por los que es divisible)

num = int(input("Ingrese un número\n"))

for div in [2,3,5,7]:
    if num%div==0:
        print("Su número es divisible entre " + str(div))
input()