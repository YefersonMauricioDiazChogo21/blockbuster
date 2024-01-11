import json
archivo = "actores.json"
with open(archivo, "r") as json_file:
    actores = json.loads(json_file.read())
def crearActores():
    print("Crear actor")
    idActor=str(input("\tIngrese el Codigo del actor\n"))

    actores[idActor]= {"id":idActor,
                        "nombre": str(input("\tIngrese el nombre del actor\n"))
                        }
    with open(archivo, "w") as json_file:
        json_file.write(json.dumps(actores, indent=4))
def listarFormato():
    for i in actores:
        print("Id:",i,"-",actores[i]["nombre"])
def gestorActores():
    bandera=True
    while bandera:
        print("GESTOR DE ACTORES")
        opc=int(input("\t1. Crear actor\n"
        "\t2. Listar actores\n"
        "\t3. Ir al menu principal\n\t"))
        if opc==1:
            crearActores()
        elif opc==2:
            listarFormato()
        elif opc==3:
            bandera=False
        else:
            print("Opcion no valida")