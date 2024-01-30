from os import system
from .data import camper, generos
from .validate import menuNoValid

def save():
    info = {
        "Nombre": input("Ingrese el nombre del camper: "),
        "Apellido": input("Ingrese el apellido: "),
        "Edad": int(input("Ingrese la edad: ")),
        "Genero": input("Elija su genero:\n\t"+"\t".join([f"{generos.index(i)+1}. {i}\n" for i in sorted(generos)]))
    }
    camper.append(info)
    return f"Succesfully Camper"


def edit():
    return "Edit to trainer"

def search():
    print(camper)
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
            case 2:
                system("clear")
                search()
            case 0:
                system("clear")
                bandera = False
            case _:
                system("clear")
                menuNoValid(opc)