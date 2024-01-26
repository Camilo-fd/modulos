from os import system
from .data import camper
from .validate import menuNoValid

def save(nombre):
    camper.append(nombre)
    return f"Succesfully Camper {nombre}"
def edit():
    return "Edit to trainer"
def search():
    return "The trainer is avaliable"
def delete():
    return "Trainer deleted"

def menu():
    bandera = True
    while (bandera):
        print("CRUD del camper")
        print("\t1. Guardar Camper")
        print("\t2. Buscar Camper")
        print("\t3. Actualizar Camper")
        print("\t4. Eliminar Camper")
        print("\t0. Atras")
        opc = int(input())
        match(opc):
            case 1:
                save()
            case 0:
                system("clear")
                bandera = False
            case _:
                system("clear")
                menuNoValid(opc)