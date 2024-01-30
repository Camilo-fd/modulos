import json
from os import system
from .data import trainer, generos
from .validate import menuNoValid

def save():
    info = {
        "Nombre": input("Ingrese el nombre del trainer: "),
        "Apellido": input("Ingrese el apellido: "),
        "Edad": int(input("Ingrese la edad: ")),
        "Genero": input("Elija su genero:\n\t"+"\t".join([f"{generos.index(i)+1}. {i}\n" for i in sorted(generos)]))
    }
    trainer.append(info)
    with open("module/storage/trainer.json", "w") as f:
        data = json.dumps(trainer, indent=4)
        f.write(data)
        f.close()
    return "Succesfully Trainer"

def edit():
    return "Edit to trainer"

def search():
    print(trainer)
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
            case 2:
                system("clear")
                search()
            case 0:
                system("clear")
                bandera = False
            case _:
                system("clear")
                menuNoValid(opc)