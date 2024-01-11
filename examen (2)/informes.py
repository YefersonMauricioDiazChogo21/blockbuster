def listaPeliGenero():
    print("hola")
def gestorInformes():
    bandera=True
    while bandera:
        print("GESTOR DE INFORMES")
        opc=int(input("\t1. Listar peliculas de un genero especifico\n"
        "\t2. Listar peliculas por protagonista\n"
        "\t3. Buscar pelicula y mostrar la sinopsis y los actores"
        "\t4. Ir al menu principal"))
        if opc==1:
            listaPeliGenero()
        elif opc==2:
            listarGeneros()
        elif opc==3:
            bandera=False
        else:
            print("Opcion no valida")