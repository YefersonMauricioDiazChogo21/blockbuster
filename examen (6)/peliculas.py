from validación import *
import json
import os
archivos="generos.json"
archivo="peliculas.json"
archivo2="actores.json"
archivo3="formatos.json"
with open(archivo,"r") as json_file:
    blockbuster= json.loads(json_file.read())
with open(archivos,"r") as json_file2:
    generos= json.loads(json_file2.read())
with open(archivo2,"r") as json_file3:
    actores= json.loads(json_file3.read()) 
with open(archivo3,"r") as json_file4:
    formatos= json.loads(json_file4.read())  
def agregarPeli():
    cont=1
    for i in blockbuster["blockbuster"]["peliculas"]:
        i
        cont+=1
    idPelicula= f"P0{cont}"
    blockbuster["blockbuster"]["peliculas"][idPelicula]={
                "id":idPelicula,
                "nombre":str(input("Ingrese el nombre de la pelicula\n")),
                "duracion":str(input("Ingrese la duracion\n")),
                "sinopsis":str(input("Ingrese el la sinopsis\n")),
                "generos":{},
                "actores":{},
                "formato":{}
       }
    with open(archivo, "w+") as json_file:
        json_file.write(json.dumps(blockbuster, indent=4))
def editarPelicula():
    print("Aqui podras editar la informacion de tus peliculas")
    selec=int(input("Ingrese el id de la pelicula"))
    idPelicula=selec
    print("\t1. Editar info general\n"
                  "\t2. Editar generos\n"
                  "\t3. Editar actores\n"
                  "\t4. Editar formatos\n"
                  "\t5. salir\n")
    opc = validacionint
    if opc==1:
        blockbuster["blockbuster"]["peliculas"][idPelicula]={
                "id":idPelicula,
                "nombre":str(input("Ingrese el nombre de la pelicula\n")),
                "duracion":str(input("Ingrese la duracion\n")),
                "sinopsis":str(input("Ingrese el la sinopsis\n"))}
        with open(archivo, "w+") as json_file:
            json_file.write(json.dumps(blockbuster, indent=4))
    elif opc==2:
        print("Desea agregar genero por:\n"
              "\t1. Codigo del genero\n"
              "\t2. Nombre del genero")
        opc2=validacionint
        if opc2==1:
            gener=str(input("Ingrese el id del genero que desea agregar"))
            if gener in generos:
                print(generos[gener])
                blockbuster["blockbuster"]["peliculas"][idPelicula]["generos"]=generos[gener]
            else:
                print("Genero aun no esta en el servidor, porfavor ve a el registro de generos y agregalo")
        elif opc2==2:
            gener=str(input("Ingrese el id del nombre que desea agregar"))
            for i in generos:
                if gener==generos[i]["nombre"]:
                        print(generos[i])
                        blockbuster["blockbuster"]["peliculas"][idPelicula]["generos"]=generos[i]
        else:
            print("Opcion invalida")
        with open(archivo, "w+") as json_file:
            json_file.write(json.dumps(blockbuster, indent=4))
                # else:
                #     print("Genero aun no esta en el servidor, porfavor ve a el registro de generos y agregalo")
    elif opc==3:
        print("Desea agregar actor por:\n"
              "\t1. Codigo del actor\n"
              "\t2. Nombre del actor")
        opc2=validacionint
        if opc2==1:
            act=str(input("Ingrese el id del actor que desea agregar"))
            if act in actores:
                print(actores[act])
                blockbuster["blockbuster"]["peliculas"][idPelicula]["actores"]=actores[act]
            else:
                print("Actor aun no esta en el servidor, porfavor ve a el registro de actores y agregalo")
        elif opc2==2:
            act=str(input("Ingrese el nombre del actor que desea agregar"))
            for i in actores:
                if gener==actores[i]["nombre"]:
                        print(actores[i])
                        blockbuster["blockbuster"]["peliculas"][idPelicula]["actores"]=actores[i]
        else:
            print("Opcion invalida")
        with open(archivo, "w+") as json_file:
            json_file.write(json.dumps(blockbuster, indent=4))
    elif opc==4:
        print("Desea agregar formato por:\n"
              "\t1. Codigo del formato\n"
              "\t2. Nombre del formato")
        opc2=validacionint
        if opc2==1:
            form=str(input("Ingrese el id del formato que desea agregar"))
            if form in formatos:
                print(formatos[form])
                blockbuster["blockbuster"]["peliculas"][idPelicula]["formato"]=formatos[form]
            else:
                print("Formato aun no esta en el servidor, porfavor ve a el registro de formatos y agregalo")
        elif opc2==2:
            form=str(input("Ingrese el nombre del formato que desea agregar"))
            for i in formatos:
                if form==formatos[i]["nombre"]:
                        print(formatos[i])
                        blockbuster["blockbuster"]["peliculas"][idPelicula]["formato"]=generos[i]
        else:
            print("Opcion invalida")
        with open(archivo, "w+") as json_file:
            json_file.write(json.dumps(blockbuster, indent=4))
    elif opc==5:
        bandera=False
    else:
        print("Opcion no valida")
def buscarPelicula():
    print("Aqui podras buscar una pelicula")
    print("\tDeseas buscar las peliculas por:\n"
                  "\t1. Codigo de pelicula"
                  "\t2. Nombre del pelicula")
    opc =validacionint
    if opc==1:
        selec=str(input("\tIngresa el codigo\n"))
        if selec in blockbuster["blockbuster"]["peliculas"]:
            print("Id pelicula:",selec,"-",blockbuster["blockbuster"]["peliculas"][selec]["nombre"])
    elif opc==2:
        selec=str(input("\tIngresa el nombre(Primera letra mayuscula)\n"))
        for i in blockbuster["blockbuster"]["peliculas"]:
            for e in blockbuster["blockbuster"]["peliculas"][i]["nombre"]: 
                if selec==e:
                    print("Id pelicula:",blockbuster["blockbuster"]["peliculas"][i]["id"],"-",blockbuster["blockbuster"]["peliculas"][i]["nombre"])
    else:
        print("Opcion incorrecta")
def listarTodasPelis():
    for i in blockbuster["blockbuster"]["peliculas"]:
        print("Id pelicula:",i,"-",blockbuster["blockbuster"]["peliculas"][i]["nombre"])
def gestorPeliculas():
    bandera=True
    while bandera:
        print("GESTOR DE PELICULAS")
        print("\t1. Agregar pelicula\n"
        "\t2. Editar pelicula\n"
        "\t3. Eliminar pelicula\n"
        "\t4. Eliminar actor\n"
        "\t5. Buscar pelicula\n"
        "\t6. Listar todas las peliculas\n"
        "\t7. Ir al menu principal\n")
        opc=validacionint()
        if opc==1:
            agregarPeli()
        elif opc==2:
            editarPelicula()
        elif opc==3:
            print("Digite el ID de la pelicula a eliminar")
            clave=str(input())
            if clave in blockbuster["blockbuster"]["peliculas"]:
                nombre=blockbuster["blockbuster"]["peliculas"][clave]["nombre"]
                del blockbuster["blockbuster"]["peliculas"][clave]
                print("Se elimino la pelicula",nombre)
            else:
                print("Pelicula no esta en el sistema")
            with open(archivo, "w+") as json_file:
                json_file.write(json.dumps(blockbuster, indent=4))
        elif opc==4:
            print("Digite el ID del actor a eliminar")
            clave=str(input())
            # clave_eliminada= actores.pop[clave, None]
            if clave in actores:
                nombre=actores[clave]["nombre"]
                del actores[clave]
                print("Se elimino el actor",nombre)
            else:
                print("Actor no esta en el sistema")
            with open(archivo, "w+") as json_file:
                json_file.write(json.dumps(blockbuster, indent=4))   
        elif opc==5:
            buscarPelicula()
        elif opc==6:
            listarTodasPelis()
        elif opc==7:
            bandera=False
        else:
            print("Opcion no valida")