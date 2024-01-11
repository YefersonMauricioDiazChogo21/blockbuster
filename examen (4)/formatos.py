import json
archivo = "formatos.json"
with open(archivo, "r") as json_file:
    formatos = json.loads(json_file.read())
def crearFormato():
    print("Crear formato")
    idFormato=str(input("\tIngrese el Codigo del formato\n"))

    formatos[idFormato]= {"id":idFormato,
                        "nombre": str(input("\tIngrese el nombre del formato\n"))
                       }
    with open(archivo, "w") as json_file:
        json_file.write(json.dumps(formatos, indent=4))
def listarFormato():
    for i in formatos:
        print("Id:",i,"-",formatos[i]["nombre"])
def gestorFormatos():
    bandera=True
    while bandera:
        print("GESTOR DE FORMATOS")
        opc=int(input("\t1. Crear formato\n"
        "\t2. Listar formatos\n"
        "\t3. Ir al menu principal\n\t"))
        if opc==1:
            crearFormato()
        elif opc==2:
            listarFormato()
        elif opc==3:
            bandera=False
        else:
            print("Opcion no valida")