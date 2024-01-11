def agregarPeli():
    print("hola")
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
            listarGeneros()
        elif opc==3:
            bandera=False
        else:
            print("Opcion no valida")