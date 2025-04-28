""""Crea una lista con 5 números.
    Pide un número al usuario y verifica si está en la lista usando in.
"""

lista= [12,55,36,78,25]

buscar_num = int (input("por favor ingresa el numero a buscar: "))

if buscar_num in lista:    
    print(f"el numero {buscar_num} esta en la lista")
else:
    print("el numero no fue encontrado")