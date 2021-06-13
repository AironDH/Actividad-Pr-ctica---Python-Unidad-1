"""
Haz un programa que escriba una pirámide inversa de 
los números del 1 al número que indique el usuario
"""

num = int(input("Ingresa un número\n"))

for pir in range(num,0,-1):
    print(str(pir)*pir)
input()