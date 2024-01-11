from generos import *
from actores import *
from formatos import *
from informes import *
from peliculas import *
def gestorBlockbuster():
    bandera=True
    while bandera:
        print("MENU PRINCIPAL: SISTEMA GESTOR DE PELICULAS BLOCKBUSTER")
        opc=int(input("\t1. Administrador de generos\n"
        "\t2. Administrador de actores\n"
        "\t3. Administrador de formatos\n"
        "\t4. Gestor de informes\n"
        "\t5. gestor peliculas\n"
        "\t6. Salir\n\t"))
        if opc==1:
            gestorGeneros()
        elif opc==2:
            gestorActores()
        elif opc==3:
            gestorFormatos()
        elif opc==4:
            gestorInformes()
        elif opc==5:
            gestorPeliculas()
        elif opc==6:
            bandera=False
        else:
            print("Opcion no valida")
gestorBlockbuster()
