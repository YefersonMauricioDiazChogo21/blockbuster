def crearFormato():
    print()

def gestorFormatos():
    bandera=True
    while bandera:
        print("GESTOR DE FORMATOS")
        opc=int(input("\t1. Crear formato\n"
        "\t2. Listar formatos\n"
        "\t3. Ir al menu principal"))
        if opc==1:
            crearFormato()
        elif opc==2:
            listarFormato()
        elif opc==3:
            bandera=False
        else:
            print("Opcion no valida")