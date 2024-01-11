import json
archivo = "generos.json"
with open(archivo, "r") as json_file:
    generos = json.loads(json_file.read())
def crearGenero():
    print("hola")
def listarGeneros():
    print("hola")
def gestorGeneros():
    bandera=True
    while bandera:
        print("GESTOR DE GENEROS")
        opc=int(input("\t1. Crear genero\n"
        "\t2. Listar generos\n"
        "\t3. Ir al menu principal"))
        if opc==1:
            crearGenero()
        elif opc==2:
            listarGeneros()
        elif opc==3:
            bandera=False
        else:
            print("Opcion no valida")