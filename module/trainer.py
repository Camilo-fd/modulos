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
    bandera=True
    while (bandera):
        system("clear")
        print("""
        ***********************
        * Acualizacion Trainer*
        ***********************
        """)
        codigo = int(input("Ingrese el codigo del trainer que deseas actualizar: "))
        print(f"""
    ________________________
    Codigo: {codigo}
    Nombre: {trainer[codigo].get('Nombre')}
    Apellido: {trainer[codigo].get('Apellido')}
    Edad: {trainer[codigo].get('Edad')}
    Genero: {trainer[codigo].get('Genero')}
    ________________________
        """)
        print("¿Este es el trainer que deseas actualizar?")
        print("1. Si")
        print("2. No")
        print("3. Salir")
        opc = int(input())
        if(opc == 1):
            info = {
                "Nombre": input("Ingrese el nombre del trainer\n"),
                "Apellido": input("Ingrese el apellido del trainer\n"),
                "Edad": int(input("Ingrese la edad del trainer\n")),
                "Genero": input("Elija su genero:\n\t"+"\t".join([f"{generos.index(i)+1}. {i}\n" for i in sorted(generos)]))
            }
            trainer[codigo] = info
            with open("module/storage/trainer.json", "w") as f:
                data = json.dumps(trainer, indent=4)
                f.write(data)
                f.close()
            bandera = False
        elif(opc == 3):
            bandera = False
            system("clear")
    return "Edit to trainer"

def search():
    system("clear")
    print(f"""
    *******************
    *  Lista Trainer  *
    *******************
    """)
    for i,val in enumerate(trainer):
        print(f"""
    ____________________________
    Codigo: {i}
    Nombre: {val.get('Nombre')}
    Apellido: {val.get('Apellido')}
    Edad: {val.get('Edad')}
    Genero: {val.get('Genero')}
    ____________________________
        """)
    return "The trainer is avaliable"

def delete():
    bandera = True
    while(bandera):
        system("clear")
        print("""
        ***************************
        * Eliminacion Trainer  *
        ***************************
        """)
        codigo = int(input("Ingrese el codigo del trainer que deseas eliminar: "))
        print(f"""
    ________________________
    Codigo: {codigo}
    Nombre: {trainer[codigo].get('Nombre')}
    Apellido: {trainer[codigo].get('Apellido')}
    Edad: {trainer[codigo].get('Edad')}
    Genero: {trainer[codigo].get('Genero')}
    ________________________
        """)
        print("¿Este es el trainer que deseas eliminar?")
        print("1. Si")
        print("2. No")
        print("3. Salir")
        opc = int(input())
        if(opc == 1):
            trainer.pop(codigo)
            with open("module/storage/trainer.json", "w") as f:
                data = json.dumps(trainer, indent=4)
                f.write(data)
                f.close()
            bandera = False
        elif(opc == 2):
            print("_________________________")
            print("Que desea hacer entonces?")
            print("1. Volver al menu")
            print("2. Eliminar camper")
            opc2 = int(input())
            if (opc2 == 1):
                system("clear")
                menu()
            elif (opc2 == 2):
                system("clear")
                trainer.pop(codigo)
                with open("module/storage/camper.json", "w") as f:
                    data = json.dumps(trainer, indent=4)
                    f.write(data)
                    f.close()
                bandera = False
        elif(opc == 3):
            bandera = False
    return "trainer deleted"

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
            case 3:
                system("clear")
                edit()
            case 4:
                system("clear")
                delete()
            case 0:
                system("clear")
                bandera = False
            case _:
                system("clear")
                menuNoValid(opc)