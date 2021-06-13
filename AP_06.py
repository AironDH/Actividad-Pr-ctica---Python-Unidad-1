# Escribe un programa que pida 3 números y escriba en la pantalla el mayor de
# los tres.

num1 = int(input("Escribe el primer número\n"))
num2 = int(input("Escribe el segundo número\n"))
num3 = int(input("Escribe el tercer número\n"))

if num1 > num2:
    if num1 > num3:
        print('El mayor de los números es ' + str(num1))
    elif num1 < num3:
        print('El mayor de los números es ' + str(num3))
    else:
        print('El mayor de los números es ' + str(num1) + ', y lo ingresaste dos veces')
elif num1 < num2:
    if num2 > num3:
        print('El mayor de los números es ' + str(num2))
    elif num2 < num3:
        print('El mayor de los números es ' + str(num3))
    else:
        print('El mayor de los números es ' + str(num2) + ', y lo ingresaste dos veces')
else:
    if num1 > num3:
        print('El mayor de los números es ' + str(num1) + ', y lo ingresaste dos veces')
    elif num1 < num3:
        print('El mayor de los números es ' + str(num3))
    else:
        print('ingresaste tres veces el mismo número: ' + str(num1))
input()
