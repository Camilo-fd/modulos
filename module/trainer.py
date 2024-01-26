from os import system
from .data import trainer
from .validate import menuNoValid

def save(nombre):
    trainer.append(nombre)
    return f"Succesfully Trainer {nombre}"
def edit():
    return "Edit to trainer"
def search():
    return "The trainer is avaliable"
def delete():
    return "Trainer deleted"

def menu():
    bandera = True
    while (bandera):
        print("CRUD del trainer")
        print("\t1. Guardar Trainer")
        print("\t2. Buscar Trainer")
        print("\t3. Actualizar Trainer")
        print("\t4. Eliminar Trainer")
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