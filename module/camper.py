import json
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
    with open("module/storage/camper.json", "w") as f:
        data = json.dumps(camper, indent=4)
        f.write(data)
        f.close()
    return "Succesfully Camper"

def edit():
    bandera=True
    while (bandera):
        system("clear")
        print("""
        ***********************
        * Acualizacion Camper *
        ***********************
        """)
        codigo = int(input("Ingrese el codigo del camper que deseas actualizar: "))
        print(f"""
    ________________________
    Codigo: {codigo}
    Nombre: {camper[codigo].get('Nombre')}
    Apellido: {camper[codigo].get('Apellido')}
    Edad: {camper[codigo].get('Edad')}
    Genero: {camper[codigo].get('Genero')}
    ________________________
        """)
        print("¿Este es el camper que deseas actualizar?")
        print("1. Si")
        print("2. No")
        print("3. Salir")
        opc = int(input())
        if(opc == 1):
            info = {
                "Nombre": input("Ingrese el nombre del camper\n"),
                "Apellido": input("Ingrese el apellido del camper\n"),
                "Edad": int(input("Ingrese la edad del camper\n")),
                "Genero": input("Elija su genero:\n\t"+"\t".join([f"{generos.index(i)+1}. {i}\n" for i in sorted(generos)]))
            }
            camper[codigo] = info
            with open("module/storage/camper.json", "w") as f:
                data = json.dumps(camper, indent=4)
                f.write(data)
                f.close()
            bandera = False
        elif(opc == 3):
            bandera = False
            system("clear")
    return "Edit to camper"

def search():
    system("clear")
    print(f"""
    *******************
    *  Lista Campers  *
    *******************
    """)
    for i,val in enumerate(camper):
        print(f"""
    ____________________________
    Codigo: {i}
    Nombre: {val.get('Nombre')}
    Apellido: {val.get('Apellido')}
    Edad: {val.get('Edad')}
    Genero: {val.get('Genero')}
    ____________________________
        """)
    return "The camper is avaliable"

def delete():
    bandera = True
    while(bandera):
        system("clear")
        print("""
        ***************************
        * Eliminacion Camper  *
        ***************************
        """)
        codigo = int(input("Ingrese el codigo del camper que deseas eliminar: "))
        print(f"""
    ________________________
    Codigo: {codigo}
    Nombre: {camper[codigo].get('Nombre')}
    Apellido: {camper[codigo].get('Apellido')}
    Edad: {camper[codigo].get('Edad')}
    Genero: {camper[codigo].get('Genero')}
    ________________________
        """)
        print("¿Este es el camper que deseas eliminar?")
        print("1. Si")
        print("2. No")
        print("3. Salir")
        opc = int(input())
        if(opc == 1):
            camper.pop(codigo)
            with open("module/storage/camper.json", "w") as f:
                data = json.dumps(camper, indent=4)
                f.write(data)
                f.close()
            bandera = False
        elif(opc == 2):
            print("________________________")
            print("Que desea hacer entonces?")
            print("1. Volver al menu")
            print("2. Eliminar camper")
            opc2 = int(input())
            if (opc2 == 1):
                system("clear")
                menu()
            elif (opc2 == 2):
                system("clear")
                camper.pop(codigo)
                with open("module/storage/camper.json", "w") as f:
                    data = json.dumps(camper, indent=4)
                    f.write(data)
                    f.close()
                bandera = False
        elif(opc == 3):
            bandera = False
    return "Camper deleted"

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