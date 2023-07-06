import funciones as fn

while True:
    fn.mostrar_menu()
    opc=fn.validar_opcion()
    if opc==1:
        fn.ver_compra()
    elif opc==2:
        fn.ver_asiento()
    elif opc==3:
        fn.listado_asistentes()
    elif opc==4:
        fn.ver_ganancias()
    elif opc==5:
        fn.salir()
        break
    

