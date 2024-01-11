import json
archivo = "generos.json"
with open(archivo, "r") as json_file:
    generos = json.loads(json_file.read())
def crearGenero():
    print("Crear genero")
    idGenero=str(input("\tIngrese el Codigo del genero\n"))

    generos[idGenero]= {"id":idGenero,
                        "nombre": str(input("\tIngrese el nombre del genero\n"))
                        }
    with open(archivo, "w+") as json_file:
        json_file.write(json.dumps(generos, indent=4))
def listarGeneros():
    for i in generos:
        print("Id:",i,"-",generos[i]["nombre"])
def gestorGeneros():
    bandera=True
    while bandera:
        print("GESTOR DE GENEROS")
        opc=int(input("\t1. Crear genero\n"
        "\t2. Listar generos\n"
        "\t3. Ir al menu principal\n\t"))
        if opc==1:
            crearGenero()
        elif opc==2:
            listarGeneros()
        elif opc==3:
            bandera=False
        else:
            print("Opcion no valida")