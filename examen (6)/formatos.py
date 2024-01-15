from validación import *
import json
archivo = "formatos.json"
with open(archivo, "r") as json_file:
    formatos = json.loads(json_file.read())
def crearFormato():
    cont=1
    print("Crear formato")
    for i in formatos:
        i
        cont+=1
    idFormato= f"F0{cont}"
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
        print("\t1. Crear formato\n"
        "\t2. Listar formatos\n"
        "\t3. Ir al menu principal\n\t")
        opc =validacionint()
        if opc==1:
            crearFormato()
        elif opc==2:
            listarFormato()
        elif opc==3:
            bandera=False
        else:
            print("Opcion no valida")
            