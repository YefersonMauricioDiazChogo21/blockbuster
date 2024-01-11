import json
import os
archivo="peliculas.json"
with open(archivo,"r") as json_file:
    blockbuster= json.loads(json_file.read())
def agregarPeli():
    idPelicula=str(input("Ingrese el codigo de la pelicula\n"))
    blockbuster["peliculas"][idPelicula]={
                "id":idPelicula,
                "nombre":str(input("Ingrese el nombre de la pelicula\n")),
                "duracion":str(input("Ingrese la duracion\n")),
                "sinopsis":str(input("Ingrese el la sinopsis\n")),
                "generos":{
                    "G01":{
                        "id":"G01",
                        "nombre":""
                    }
                },
                "actores":{
                    "A01":{
                        "id":"A01",
                        "nombre":"",
                        "rol":""
                    }
                },
                "formato":{
                    "F01":{
                        "id":"F01",
                        "nombre":"",
                        "NroCopias":"",
                        "valorPrestamo":""
                },
                "F02":{
                    "id":"F02",
                    "nombre":"",
                    "NroCopias":"",
                    "valorPrestamo":""
                }
            }
       }
    with open(archivo, "w+") as json_file:
        json_file.write(json.dumps(blockbuster, indent=4))
def editarPelicula():
    print("Aqui podras editar la informacion de tus peliculas")
    opc=int(input("\t1. Editar info general\n"
                  "\t2. Editar generos\n"
                  "\t3. Editar actores\n"
                  "\t4. Editar formatos\n"
                  "\t5. salir\n"))
    if opc==1:
        print()
    elif opc==2:
        print()
    elif opc==3:
        print()
    elif opc==4:
        print()
    elif opc==5:
        print()
    else:
        print("Opcion no valida")
def buscarPelicula():
    print("Aqui podras buscar una pelicula")
    opc=int(input("\tDeseas buscar las peliculas por:\n"
                  "\t1. Codigo de pelicula"
                  "\t2. Nombre del pelicula"))
    if opc==1:
        selec=str(input("\tIngresa el codigo\n"))
        print("Id pelicula:",blockbuster["blockbuster"]["peliculas"][selec],"-",blockbuster["blockbuster"]["peliculas"][selec]["nombre"])
        os.system("pause")
    elif opc==2:
        selec=str(input("\tIngresa el nombre(Primera letra mayuscula)\n"))
        for i in blockbuster["blockbuster"]["peliculas"]:
            for e in blockbuster["blockbuster"]["peliculas"][i]["nombre"]: 
                if selec==e:
                    print("Id pelicula:",blockbuster["blockbuster"]["peliculas"][i],"-",blockbuster["blockbuster"]["peliculas"][i]["nombre"])
        os.system("pause")
    else:
        print("Opcion incorrecta")
def listarTodasPelis():
    for i in blockbuster["peliculas"]:
        print("Id pelicula:",blockbuster["blockbuster"]["peliculas"][i],"-",blockbuster["blockbuster"]["peliculas"][i]["nombre"])
def gestorPeliculas():
    bandera=True
    while bandera:
        print("GESTOR DE PELICULAS")
        opc=int(input("\t1. Agregar pelicula\n"
        "\t2. Editar pelicula\n"
        "\t3. Eliminar pelicula"
        "\t4. Eliminar actor"
        "\t5. Buscar pelicula"
        "\t6. Listar todas las peliculas"
        "\t7. Ir al menu principal"))
        if opc==1:
            agregarPeli()
        elif opc==2:
            editarPelicula()
        elif opc==3:
            print("No alcance a terminarlo")
        elif opc==4:
            print("No alcance a terminarlo")
        elif opc==5:
            buscarPelicula()
        elif opc==6:
            listarTodasPelis()
        elif opc==3:
            bandera=False
        else:
            print("Opcion no valida")