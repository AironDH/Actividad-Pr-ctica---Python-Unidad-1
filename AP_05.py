# Escribe un programa que pida dos números y escriba en la pantalla cual es el
# mayor.

num1 = int(input("Inserta un número\n"))
num2 = int(input("Inserta otro número\n"))

if num1 < num2:
    print(str(num2)+ " es el mayor de los dos valores")
elif num1 == num2:
    print("Los dos vaores son iguales")
else:
    print(str(num1) + " es el mayor valor")
input()