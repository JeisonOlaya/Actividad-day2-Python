""" Crea una lista con algunos nombres (por ejemplo: "Ana", "Luis", "Sofía").
    Pide al usuario su nombre.
    Usa if para decir si está en la lista de invitados o no.
"""
nombre=["ana","luis","sofia"]

ingNombre = input("Por favor ingresa el nombre: ")

if ingNombre in nombre:
    print(f"el nombre: {ingNombre} esta en la lista")
else:
    print(f"el nombre: {ingNombre} no esta en la lista de invitados")

