"""
Crear un programa que escriba los números del 1 al 500, y que indique cuales
son múltiplos de 4 y de 9 y que cada 5 líneas muestre una línea horizontal.
"""

for n in range(1,501):
    print(str(n), end=" ")
    if n%4==0:
        print("(es múltiplo de 4)", end=" ")
    if n%9==0:
        print("(es múltiplo de 9)", end=" ")
    print(" ")
    if n%5==0:
        print("______________________________________")
input()