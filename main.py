from funciones import*
limpiar()

while True:
    try:
        menu_principal()
        opc=int(input(" escoja una opción\n"))
        while opc<1 or opc>5:
            opc=int(input(" escoja una opción\n"))
        if opc ==1:
            limpiar()
            print("Asignar sueldos\n")
            asignar_sueldos()
            x=input("presione una tecla para continuar")
        elif opc ==2:
            limpiar()
            print("Clasificar sueldos\n")
            clasificar_sueldos()
            x=input("presione una tecla para continuar")
        elif opc ==3:
            limpiar()
            print("Mostrar estadisiticas\n")
            mostrar_estadisticas()
            x=input("presione una tecla para continuar")
        elif opc==4:
            limpiar()
            print("Reporte de sueldos\n")
            reportes()
            x=input("presione una tecla para continuar")
        elif opc==5:
            limpiar()
            print("Salir")
            opc_salir=input("Desea salir 1. SI 2. NO\n")
            while opc_salir!="1" and opc_salir!="2":
                opc_salir=input("Desea salir 1. SI 2. NO\n")
            if opc_salir=="1":
                print("Finalizando programa...")
                print("desarrollado por Benjamin Burgos")
                print("RUT: 19.880.043-0")
                break
            elif opc_salir=="2":
                print("Hola denuevo")
                x=input("presione una tecla para continuar")
    except:
        print("opcion no valida, escoja entre 1 y 5")
                