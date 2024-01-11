import json
import os
archivo="peliculas.json"
with open(archivo,"r") as json_file:
    blockbuster= json.loads(json_file.read())

def listaPeliGenero():
    print("Aqui podras listar las peliculas por genero")
    opc=int(input("\tDeseas listar las peliculas por:\n"
                  "\t1. Codigo de genero\n"
                  "\t2. Nombre del genero\n"))
    if opc==1:
        selec=str(input("Ingresa el codigo\n"))
        for i in blockbuster["blockbuster"]["peliculas"]:
            for e in blockbuster["blockbuster"]["peliculas"][i]["generos"]: 
                if selec==e:
                    print("Id pelicula:",selec,"-",blockbuster["blockbuster"]["peliculas"][i]["nombre"])
        os.system("pause")
    elif opc==2:
        selec=str(input("Ingresa el nombre(Primera letra mayuscula)\n"))
        for i in blockbuster["blockbuster"]["peliculas"]:
            for e in blockbuster["blockbuster"]["peliculas"][i]["genero"]["nombre"]: 
                if selec==e:
                    print("Id pelicula:",blockbuster["blockbuster"]["peliculas"][i],"-",blockbuster["blockbuster"]["peliculas"][i]["nombre"])
        os.systen("pause")
    else:
        print("Opcion incorrecta")
def listarPorProtagonista():
    print("Aqui podras listar las peliculaS por actor protagonista")
    opc=int(input("\tDeseas listar las peliculas por:\n"
                  "\t1. Codigo de actor\n"
                  "\t2. Nombre del actor\n"))
    if opc==1:
        selec=str(input("Ingresa el codigo\n"))
        for i in blockbuster["blockbuster"]["peliculas"]:
            for e in blockbuster["blockbuster"]["peliculas"][i]["actores"]: 
                if selec==e and blockbuster["blockbuster"]["peliculas"][i]["actores"]["rol"]=="protagonista":
                    print("Id pelicula:",blockbuster["blockbuster"]["peliculas"][i],"-",blockbuster["blockbuster"]["peliculas"][i]["nombre"])
        os.system("pause")
    elif opc==2:
        selec=str(input("Ingresa el nombre(Primera letra mayuscula)\n"))
        for i in blockbuster["blockbuster"]["peliculas"]:
            for e in blockbuster["blockbuster"]["peliculas"][i]["actores"]: 
                if selec==e and blockbuster["blockbuster"]["peliculas"][i]["actores"]["rol"]=="protagonista":
                    print("Id pelicula:",blockbuster["blockbuster"]["peliculas"][i],"-",blockbuster["blockbuster"]["peliculas"][i]["nombre"])
        os.system("pause")
    else:
        print("Opcion incorrecta")
def buscarPeliculaSinop():
    print("Aqui podras buscar una pelicula")
    opc=int(input("\tDeseas buscar las peliculas por:\n"
                  "\t1. Codigo de pelicula\n"
                  "\t2. Nombre del pelicula\n"))
    if opc==1:
        selec=str(input("\tIngresa el codigo\n"))
        print("Id pelicula:",blockbuster["blockbuster"]["peliculas"][selec],"-",blockbuster["blockbuster"]["peliculas"][selec]["nombre"])
        print(blockbuster["blackbuster"]["peliculas"][selec]["sinopsis"])
        os.system("pause")
    elif opc==2:
        selec=str(input("\tIngresa el nombre(Primera letra mayuscula)\n"))
        for i in blockbuster["blockbuster"]["peliculas"]:
            for e in blockbuster["blockbuster"]["peliculas"][i]["nombre"]: 
                if selec==e:
                    print("Id pelicula:",blockbuster["blockbuster"]["peliculas"][i],"-",blockbuster["blockbuster"]["peliculas"][i]["nombre"])
                    print(blockbuster["blackbuster"]["peliculas"][i]["sinopsis"])
        os.system("pause")
    else:
        print("Opcion incorrecta")
def gestorInformes():
    bandera=True
    while bandera:
        print("GESTOR DE INFORMES")
        opc=int(input("\t1. Listar peliculas de un genero especifico\n"
        "\t2. Listar peliculas por protagonista\n"
        "\t3. Buscar pelicula y mostrar la sinopsis y los actores\n"
        "\t4. Ir al menu principal\n\t"))
        if opc==1:
            listaPeliGenero()
        elif opc==2:
            listarPorProtagonista()
        elif opc==3:
            buscarPeliculaSinop()
        elif opc==4:
            bandera=False
        else:
            print("Opcion no valida")