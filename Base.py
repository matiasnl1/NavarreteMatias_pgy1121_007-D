import numpy
import os
import msvcrt
import time

evento=numpy.zeros((10,10), int)

lista_ruts=[]
lista_nombre=[]
lista_entrada=[]
lista_filas=[]
lista_columnas=[]
precio_platinum=[120000]
precio_gold=[80000]
precio_silver=[50000]

acum_entrada_p=0
acum_entrada_g=0
acum_entrada_s=0

def menu_principal():
    print("""MENU
    1. Comprar entradas
    2. Mostrar ubicación disponible
    3. Ver listado de asistentes
    4. Mostrar ganancias totales
    5. Salir """)

def validar_opcion():
    while True:
        try:
            opc=int(input("Ingrese la opción que desea: "))
            if opc in (1,2,3,4,5):
                return opc
            else:
                print("Error! Debe elegir alguna opción indicada (1-5)")
        except:
            print("Error! debe ser un número entero")

def validar_cant_entrada():
    while True:
        try:
            entrada=int(input("Ingrese la cantidad de entras: "))
            if entrada>=1 and entrada <=3:
                return entrada
            else:
                print("Error! supera el límite de entradas disponibles (1-3)")
        except:
            print("Error! debe ser un número entero")

def validar_ruts():
    while True:
        try:
            rut=int(input("Ingrese rut: "))
            if rut>=1000000 and rut<=99999999:
                return rut
            else:
                print("Error! el rut infringe el rango indicado (1000000-99999999")
        except:
            print("Error! deben ser números entero")

        lista_ruts.append(rut)

def ver_asiento():
    for x in range(10):
        print("Ascientos", x+1,":",end=" ")
        for y in range(10):
            print(evento [x][y], end=" ")
            print()
        print("Asientos disponibles ")

def validar_asiento():
    rut=validar_ruts()
    lista_filas=ver_fila()
    lista_columnas=ver_columna()
    while True:
        try:
            rut=int(input("Ingrese rut: "))
            if rut in range(len(lista_ruts)):
                print("Su asiento es: ", lista_filas, lista_columnas)
                return rut
            else:
                print("Rut no ingresado")
        except:
            print("Error! debe ser números entero")

def ver_fila():
    while True:
        try:
            fila=int(input("Filas disponibles: "))
            if fila in range(len(lista_filas))==1:
                print("Fila ocupada")
                return fila
        except:
            print("Error! debe ser número entero")

        lista_filas.append(fila)

def ver_columna():
    while True:
        try:
            columna=int(input("Columnas disponibles: "))
            if columna in range(len(lista_columnas))==1:
                print("Columna ocupada")
                return columna
        except:
            print("Error! debe ser un número entero")
        lista_columnas.append(columna)

def ver_compra():

    print("""Entradas
     Asientos de 1-20 = $120.000
     Asientos de 21-50 = $80.000
     Asientos de 51-100 = $50.000 """)
    
    entrada=validar_cant_entrada()
        
    while True:
            try:
                cant_entrada=input("Elija cantidad de entras (1-3): ")
                if cant_entrada>=1 and cant_entrada<=3:
                    compra=input("Elija tipo de entrada (PLATINUM-GOLD-SILVER): ")
                    if compra.upper()=="PLATINUM":
                        compra=cant_entrada*120000
                        acum_entrada_p=acum_entrada_p + cant_entrada
                        print("Valor de la entrada ","$", compra)
                        return compra
                    if compra.upper()=="GOLD":
                        compra=cant_entrada*80000
                        acum_entrada_g=acum_entrada_g+cant_entrada
                        print("Valor de la entrada ", "$", compra)
                        return compra
                    if compra.upper()=="SILVER":
                        compra=cant_entrada*50000
                        acum_entrada_s=acum_entrada_s+cant_entrada
                        print("Valor de la entrada ", "$", compra)
                    else:
                        print("Error! debe elegir alguna opción indicada")
            except:
                print("Error! debe ser números entero")
            lista_entrada.append(entrada)

def validar_nombre():
    while True:
        nombre=input("Ingrese nombre: ")
        if len(nombre.strip())>=3 and nombre.isalpha():
            return nombre
        else:
            print("Error! Nombre incorrecto")

        lista_nombre.append(nombre)

def listado_asistentes():
    rut=validar_ruts()
    while True:
        try:
            rut=int(input("Ingrese rut: "))
            if rut in range(lista_ruts):
                for x in range(len(lista_ruts)):
                    posicion_encontrada=[x]
                    print("Rut: ", lista_ruts[posicion_encontrada])
                    print("Nombre: ", lista_nombre[posicion_encontrada])
                    print("Entradas: ", lista_entrada[posicion_encontrada])
                    print("Fila: ", lista_filas[posicion_encontrada])
                    print("Columna: ", lista_columnas[posicion_encontrada])
                    return
                else:
                    print("Error! rut no registrado")
        except:
            print("Error! deben ser números entero")

def ver_ganancias():
    compra=ver_compra()
    while True:
        if compra in range(len(lista_entrada)):
            if compra.upper()=="PLATINUM":
                print(f"Total ganancias Platinum: ${acum_entrada_p*120000}")
                return compra
            if compra.upper()=="GOLD":
                print(f"Total ganancias Gold: ${acum_entrada_g+80000}")
                return compra
            if compra.upper()=="SILVER":
                print(f"Total ganancias Silver: ${acum_entrada_s*50000}")
                return compra
            else:
                print("Error! no hay entradas vendidas en el sistemas")

        print("Total Ganancias: $",acum_entrada_p*(120000)+acum_entrada_g*(80000)+acum_entrada_s*(50000))
    

def ubicacion_disponible():
    asiento=ver_asiento()
    fila=ver_fila()
    columna=ver_columna()
    for x in range(evento):
        x==[fila-1] [columna-1]
        if evento[fila-1][columna-1]==1:
            print("Ubicación ocupada")
            time.sleep(2)
        else:
            print("Ubicación disponible")
            print("Presione cualquier tecla para continuar ")
            msvcrt.getch()

def salir():
    print("Gracias por su trabajo")
    time.sleep(2)
    os.system('cls')
    print(""" Matias Navarrete Leyton
            fecha: 06/07/2023 """)


        

