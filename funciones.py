import random, time, os, csv


trabajadores = ["Juan Pérez", "María García", "Carlos López", "Ana Martínez", "Pedro Rodríguez", "Laura Hernández", "Miguel Sánchez","Isabel Gómez","Francisco Díaz","Elena Fernández"]

trabajadores_sueldos=[]

def limpiar():
    os.system("cls")

    
def menu_principal():
    print("1. Asignar sueldos aleatorio\n 2. Clasificar sueldos\n 3. Ver estadisticas\n 4. Reporte de sueldos\n 5. Salir del programa")
 
    
def asignar_sueldos():
    for x in trabajadores:
        trabajador=[]
        trabajador.append(x)
        sueldo=random.randint(300000, 2500000)
        trabajador.append(sueldo)
        trabajadores_sueldos.append(trabajador)
        print(f"{x}: ${sueldo}")
    print("sueldos asignados correctamente")
    print("")
    

def clasificar_sueldos():
    sueldo_menor=[]
    sueldo_medio=[]
    sueldo_mayor=[]
    sueldo_menornombre=[]
    sueldo_medionombre=[]
    sueldo_mayornombre=[]
    cont_1=0
    cont_2=0
    cont_3=0
    sum1=0
    sum2=0
    sum3=0
    for x in trabajadores_sueldos:
        if x[1]<800000:
            cont_1+=1
            nombre_bajo=x[0]
            sueldo_menornombre.append(nombre_bajo)
            sueldo_bajo=x[1]
            sueldo_menor.append(sueldo_bajo)
            sum1+=x[1]
        elif x[1]>=800000 and x[1]<2000000:
            cont_2+=1
            nombre_medio=x[0]
            sueldo_medionombre.append(nombre_medio)
            sueldo_mediano=x[1]
            sueldo_medio.append(sueldo_mediano)
            sum2+=x[1]
        else:
            cont_3+=1
            nombre_alto=x[0]
            sueldo_mayornombre.append(nombre_alto)
            sueldo_alto=x[1]
            sueldo_mayor.append(sueldo_alto)
            sum3+=x[1]
            
    print(f"sueldos menores a $800.000 Total: {cont_1}")
    print("nombre empleado      sueldo")
    print("")
    for x in range(len(sueldo_menor)):
        print(f"{sueldo_menornombre[x]}:        {sueldo_menor[x]}")
        print("")
        
    print(f"sueldos entre $800.000 y $2000000 Total: {cont_2}")
    print("nombre empleado      sueldo")
    print("")
    for x in range(len(sueldo_medio)):
        print(f"{sueldo_medionombre[x]}:       {sueldo_medio[x]}")
        print("")
        
    
    print(f"sueldos sobre $2000000 Total: {cont_3}")
    print("nombre empleado      sueldo")
    print("")
    for x in range(len(sueldo_mayor)):
        print(f"{sueldo_mayornombre[x]}:        {sueldo_mayor[x]}")
        print("")
    suma=sum1+sum2+sum3
    print(f"Total: ${suma}")
        
    
def mostrar_estadisticas():
    sueldos=[x[1] for x in trabajadores_sueldos]
    
    menor=sueldos[0]
    mayor=sueldos[0]
    
    for x in sueldos:
        if x > mayor:
            mayor=x
        
    print(f"Sueldo más alto es: ${mayor}")
    
    for x in sueldos:
        if x < menor:
            menor=x
    print(f"Sueldo menor es: ${menor}")
    
    cont=0
    
    for x in sueldos:
        cont+=x
        suma=cont
    promedio=round(suma/len(sueldos))
    print(f"el promedio de los precios es: ${promedio}")
    
    mult=1
    
    for x in sueldos:
        mult=mult*x
    media_geometrica= round(mult**(1/len(sueldos)))
    print(f"La media geometrica es: ${media_geometrica}")


def reportes():
    with open('reporte_sueldos.csv', 'w', newline='') as archivo_csv:
        escritor_csv=csv.writer(archivo_csv, delimiter=',')
        escritor_csv.writerow(["Nombre empleado", "Sueldo Base", "Descuento salud","Descuento afp", "sueldo Liquido"])
        sueldo=[x[1]for x in trabajadores_sueldos]
        print ("trabajadores    sueldo base     descuento salud     descuento afp       sueldo liquido         ")
        for x in range(len(sueldo)):
            sueldo[x]
            sueldo_base=sueldo[x]
            descuento_salud=sueldo_base*0.07
            descuento_afp=sueldo_base*0.12
            sueldo_liquido=sueldo_base-descuento_salud-descuento_afp
            print(f"{trabajadores[x]}:  {sueldo_base}   {descuento_salud}   {descuento_afp} {sueldo_liquido}")
            print("")
            escritor_csv.writerow([trabajadores[x],  sueldo_base,   descuento_salud,   descuento_afp, sueldo_liquido])

