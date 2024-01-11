def crearActores():
    print("hola")
def gestorActores():
    bandera=True
    while bandera:
        print("GESTOR DE ACTORES")
        opc=int(input("\t1. Crear actor\n"
        "\t2. Listar actores\n"
        "\t3. Ir al menu principal"))
        if opc==1:
            crearActores()
        elif opc==2:
            listarFormato()
        elif opc==3:
            bandera=False
        else:
            print("Opcion no valida")