from artist.datos import *
from artist.funciones_secundarias import *
from artist.CRUD_funciones import contador_id
from artist.diseños import *
from txt import *
#CREAR

def crear_informacion(datos: dict):
    artistas={}
    clear_screen()
    diseño_logo_discografia()
    artistas["nombre"]=input("Ingrese el nombre del artista: ").lower()
    artistas["descripcion"]=input("Ingrese una breve descripcion del artista: ").lower()
    artistas["contacto"]=input("Ingrese la info de contacto del artista: ").lower()
    
    datos["artistas"].append(artistas)
    print(artistas["nombre"]," registrado con éxito!")
    return datos

def crear_info():
    while True:
        datos = cargar_datos(RUTA_BASE_DE_DATOS_ARTISTAS)
        datos = crear_informacion(datos)
        guardar_datos(datos, RUTA_BASE_DE_DATOS_ARTISTAS)
        continuar = very()
        if continuar == "2": break
        else: clear_screen()
def crear_cont(datos: dict):
    clear_screen()
    diseño_logo_discografia()
    artista = input("Ingrese el nombre del Artista: ").lower()
    for sn in range(len(datos["artistas"])):
        if datos["artistas"][sn]["nombre"] == artista:
            contratos={}
            contratos["nombre_artista"]=datos["artistas"][sn]["nombre"]
            contratos["nombre_discografica"]=input("Ingrese el nombre de la discografica: ").lower()
            contratos["lugar"]=input("Ingrese el lugar del contrato: ").lower()
            contratos["fecha"]= datetime_to_json(fecha)
            contratos["documento_artista"]=input("Ingrese el documento del artista: ").lower()
            contratos["documento_discografica"]=input("Ingrese el documento de la discografica: ").lower()
            contratos["contacto"]=datos["artistas"][sn]["contacto"]
            datos["contratos"].append(contratos)
            print("")
            print_ ("CONTRATO DISCOGRÁFICO")
            print ("")
            print_(f"En ",contratos["lugar"]," a ",contratos["fecha"])
            print ("")
            print_("REUNIDOS")
            print ("")
            print_("De una Parte, como ARTISTA,")
            print (f"El ARTISTA ",contratos["nombre_artista"].capitalize(),", con el documento ",contratos["documento_artista"]," y con domicilio en ",contratos["lugar"].capitalize()," actuando en nombre y representación propia.")
            print ("")
            print ("De otra Parte, como COMPAÑÍA DISCOGRÁFICA,")
            print (f"La COMPAÑÍA DISCOGRÁFICA ",contratos["nombre_discografica"].capitalize()," con el documento ",contratos["documento_discografica"]," y con domicilio en ",contratos["lugar"].capitalize()," actuando en nombre y representación propia.") 
            print("")
            print ("Y, que a continuación, serán referidas, individualmente como Parte, COMPAÑÍA DISCOGRÁFICA, ARTISTA, o, de forma conjunta como Partes...")
            print("")
            print_("...")
            return datos
    print_(f"El artista ",artista," no esta resgistrado...")
    return datos

def crear_contrato():
    while True:
        datos = cargar_datos(RUTA_BASE_DE_DATOS_ARTISTAS)
        datos = crear_cont(datos)
        guardar_datos(datos, RUTA_BASE_DE_DATOS_ARTISTAS)
        continuar = very()
        if continuar == "2": break
        else: clear_screen()
        
# crear_info()

#ELIMINAR
def eliminar_informacion(datos: dict):
    clear_screen()
    diseño_logo_discografia()
    nombre =input("Ingrese el nombre del artista: ").lower()
    for i in range(len(datos["artistas"])):
        if datos["artistas"][i]["nombre"] == nombre:
            informacion = (datos["artistas"][i]["nombre"])
            datos["artistas"].pop(i)
            separador = " "
            informacion = separador.join(map(str, informacion))
            print(informacion," se ha eliminado con exito...")
            return datos
    print (f"El artista ",nombre," no esta resgistrado...")    
    return datos

def eliminar_info():
    while True:
        datos = cargar_datos(RUTA_BASE_DE_DATOS_ARTISTAS)
        datos = eliminar_informacion(datos)
        guardar_datos(datos, RUTA_BASE_DE_DATOS_ARTISTAS)
        continuar = very()
        if continuar == "2": break
        else: clear_screen()
        
# eliminar_info()


#LEER
def leer_informacion(datos: dict):
    clear_screen()
    diseño_logo_discografia()
    nombre =input("Ingrese el nombre del artista: ").lower()    
    for i in range(len(datos["artistas"])):
        if datos["artistas"][i]["nombre"] == nombre:
            linea()
            es()
            line()
            print_("N o m b r e")
            print_(datos["artistas"][i]["nombre"].capitalize())
            line()
            es()
            line()
            print_("D e s c r i p c i o n")
            print_(datos["artistas"][i]["descripcion"].capitalize())
            line()
            es()
            line()
            print_("C o n t a c t o")
            print_(datos["artistas"][i]["contacto"])
            line()
            es()
            line()
            print_("C a n c i o n e s")
            for i in range(len(datos["canciones"])):
                if datos["canciones"][i]["artista"] == nombre:
                    # for sn in range(len(datos["canciones"][i]["nombre"])):
                    print_ (datos["canciones"][i]["nombre"])
            line()
            es()
            linea()
            return datos
    print_(f"El artista ",nombre," no se encuentra registrado...")    
    return datos

def leer_info():
    while True:
        datos = cargar_datos(RUTA_BASE_DE_DATOS_ARTISTAS)
        datos = leer_informacion(datos)
        guardar_datos(datos, RUTA_BASE_DE_DATOS_ARTISTAS)
        continuar = very()
        if continuar == "2": break
        else: clear_screen()
        
def leer_artist(datos: dict):
    clear_screen()
    diseño_logo_discografia()
    for sn in range(len(datos["artistas"])):
        print_(datos["artistas"][sn]["nombre"].capitalize())
    for i in range(len(datos["artistas"])):
        linea()
        es()
        line()
        print_("N o m b r e")
        print_(datos["artistas"][i]["nombre"].capitalize())
        line()
        es()
        line()
        print_("D e s c r i p c i o n")
        print_(datos["artistas"][i]["descripcion"].capitalize())
        line()
        es()
        line()
        print_("C o n t a c t o")
        print_(datos["artistas"][i]["contacto"])
        line()
        es()
        line()
        print_("C a n c i o n e s")
        for p in range(len(datos["canciones"])):
            if datos["artistas"][i]["nombre"] == datos["canciones"][p]["artista"]:
                print_ (datos["canciones"][p]["nombre"])
        line()
        es()
        linea()
    return datos
def leer_artistas():
    while True:
        datos = cargar_datos(RUTA_BASE_DE_DATOS_ARTISTAS)
        datos = leer_artist(datos)
        guardar_datos(datos, RUTA_BASE_DE_DATOS_ARTISTAS)
        continuar = very()
        if continuar == "2": break
        else: clear_screen()
        
def leer_gender(datos: dict):  
    while True:
        clear_screen()
        diseño_logo_discografia()
        mostrar_txt(m_1_2_1)
        op = input("Seleccione una opcion:\n👉   ")
        line()
        if op == "1": 
            print_("C a n c i o n e s")
            for sn in range(len(datos["canciones"])):
                if datos["canciones"][sn]["genero_id"] == "01":
                    print_ (datos["canciones"][sn]["nombre"])
            for i in range(len(datos["canciones"])):
                if datos["canciones"][i]["genero_id"] == "01":
                    line()
                    es()
                    linea()
                    linea()
                    es()
                    line()
                    print_("N o m b r e")
                    print_(datos["canciones"][i]["nombre"].capitalize())
                    line()
                    es()
                    line()
                    print_("A r t i s t a")
                    print_(datos["canciones"][i]["artista"].capitalize())
                    line()
                    es()
                    line()
                    print_("G e n e r o")
                    print_(datos["canciones"][i]["genero"])
                    line()
                    es()
                    line()
                    print_("D u r a c i o n")
                    print_(datos["canciones"][i]["duracion"])
                    line()
                    es()
                    line()
                    print_("L a n z a m i e n t o")
                    print_(datos["canciones"][i]["lanzamiento"])
                    line()
                    es()
                    line()
                    print_("A l b u m")
                    print_(datos["canciones"][i]["album"].capitalize())
                    line()
                    es()
                    linea()
            return datos 
        elif op == "2":
            print_("C a n c i o n e s")
            for sn in range(len(datos["canciones"])):
                if datos["canciones"][sn]["genero_id"] == "02":
                    print_ (datos["canciones"][sn]["nombre"])
            for i in range(len(datos["canciones"])):
                if datos["canciones"][i]["genero_id"] == "02":
                    line()
                    es()
                    linea()
                    linea()
                    es()
                    line()
                    print_("N o m b r e")
                    print_(datos["canciones"][i]["nombre"].capitalize())
                    line()
                    es()
                    line()
                    print_("A r t i s t a")
                    print_(datos["canciones"][i]["artista"].capitalize())
                    line()
                    es()
                    line()
                    print_("G e n e r o")
                    print_(datos["canciones"][i]["genero"])
                    line()
                    es()
                    line()
                    print_("D u r a c i o n")
                    print_(datos["canciones"][i]["duracion"])
                    line()
                    es()
                    line()
                    print_("L a n z a m i e n t o")
                    print_(datos["canciones"][i]["lanzamiento"])
                    line()
                    es()
                    line()
                    print_("A l b u m")
                    print_(datos["canciones"][i]["album"].capitalize())
                    line()
                    es()
                    linea()
            return datos 
        elif op == "3":
            print_("C a n c i o n e s")
            for sn in range(len(datos["canciones"])):
                if datos["canciones"][sn]["genero_id"] == "03":
                    print_ (datos["canciones"][sn]["nombre"])
            for i in range(len(datos["canciones"])):
                if datos["canciones"][i]["genero_id"] == "03":
                    line()
                    es()
                    linea()
                    linea()
                    es()
                    line()
                    print_("N o m b r e")
                    print_(datos["canciones"][i]["nombre"].capitalize())
                    line()
                    es()
                    line()
                    print_("A r t i s t a")
                    print_(datos["canciones"][i]["artista"].capitalize())
                    line()
                    es()
                    line()
                    print_("G e n e r o")
                    print_(datos["canciones"][i]["genero"])
                    line()
                    es()
                    line()
                    print_("D u r a c i o n")
                    print_(datos["canciones"][i]["duracion"])
                    line()
                    es()
                    line()
                    print_("L a n z a m i e n t o")
                    print_(datos["canciones"][i]["lanzamiento"])
                    line()
                    es()
                    line()
                    print_("A l b u m")
                    print_(datos["canciones"][i]["album"].capitalize())
                    line()
                    es()
                    linea()
            return datos 
        elif op == "4":
            print_("C a n c i o n e s")
            for sn in range(len(datos["canciones"])):
                if datos["canciones"][sn]["genero_id"] == "04":
                    print_ (datos["canciones"][sn]["nombre"])
            for i in range(len(datos["canciones"])):
                if datos["canciones"][i]["genero_id"] == "04":
                    line()
                    es()
                    linea()
                    linea()
                    es()
                    line()
                    print_("N o m b r e")
                    print_(datos["canciones"][i]["nombre"].capitalize())
                    line()
                    es()
                    line()
                    print_("A r t i s t a")
                    print_(datos["canciones"][i]["artista"].capitalize())
                    line()
                    es()
                    line()
                    print_("G e n e r o")
                    print_(datos["canciones"][i]["genero"])
                    line()
                    es()
                    line()
                    print_("D u r a c i o n")
                    print_(datos["canciones"][i]["duracion"])
                    line()
                    es()
                    line()
                    print_("L a n z a m i e n t o")
                    print_(datos["canciones"][i]["lanzamiento"])
                    line()
                    es()
                    line()
                    print_("A l b u m")
                    print_(datos["canciones"][i]["album"].capitalize())
                    line()
                    es()
                    linea()
            return datos 
        elif op == "5":
            print_("C a n c i o n e s")
            for sn in range(len(datos["canciones"])):
                if datos["canciones"][sn]["genero_id"] == "05":
                    print_ (datos["canciones"][sn]["nombre"])
            for i in range(len(datos["canciones"])):
                if datos["canciones"][i]["genero_id"] == "05":
                    line()
                    es()
                    linea()
                    linea()
                    es()
                    line()
                    print_("N o m b r e")
                    print_(datos["canciones"][i]["nombre"].capitalize())
                    line()
                    es()
                    line()
                    print_("A r t i s t a")
                    print_(datos["canciones"][i]["artista"].capitalize())
                    line()
                    es()
                    line()
                    print_("G e n e r o")
                    print_(datos["canciones"][i]["genero"])
                    line()
                    es()
                    line()
                    print_("D u r a c i o n")
                    print_(datos["canciones"][i]["duracion"])
                    line()
                    es()
                    line()
                    print_("L a n z a m i e n t o")
                    print_(datos["canciones"][i]["lanzamiento"])
                    line()
                    es()
                    line()
                    print_("A l b u m")
                    print_(datos["canciones"][i]["album"].capitalize())
                    line()
                    es()
                    linea()
            return datos 
        elif op == "6": return datos
        else: print_("El genero no es valido")

def leer_genero():
    while True:
        datos = cargar_datos(RUTA_BASE_DE_DATOS_ARTISTAS)
        datos = leer_gender(datos)
        guardar_datos(datos, RUTA_BASE_DE_DATOS_ARTISTAS)
        continuar = very()
        if continuar == "2": break
        else: clear_screen()
        
# leer_info()
def leer_alb(datos: dict):
    clear_screen()
    diseño_logo_discografia()
    album = input("Ingrese el nombre del Album: ")
    line()
    print_("A l b u m")
    for sn in range(len(datos["canciones"])):
        if datos["canciones"][sn]["album"] == album:
            print_ (datos["canciones"][sn]["nombre"])
    for i in range(len(datos["canciones"])):
        if datos["canciones"][i]["album"] == album:
            line()
            es()
            linea()
            linea()
            es()
            line()
            print_("N o m b r e")
            print_(datos["canciones"][i]["nombre"].capitalize())
            line()
            es()
            line()
            print_("A r t i s t a")
            print_(datos["canciones"][i]["artista"].capitalize())
            line()
            es()
            line()
            print_("G e n e r o")
            print_(datos["canciones"][i]["genero"])
            line()
            es()
            line()
            print_("D u r a c i o n")
            print_(datos["canciones"][i]["duracion"])
            line()
            es()
            line()
            print_("L a n z a m i e n t o")
            print_(datos["canciones"][i]["lanzamiento"])
            line()
            es()
            linea()
    return datos 
        
def leer_album():
    while True:
        datos = cargar_datos(RUTA_BASE_DE_DATOS_ARTISTAS)
        datos = leer_alb(datos)
        guardar_datos(datos, RUTA_BASE_DE_DATOS_ARTISTAS)
        continuar = very()
        if continuar == "2": break
        else: clear_screen()
        
def leer_art(datos: dict):
    clear_screen()
    diseño_logo_discografia()
    artista = input("Ingrese el nombre del Artista: ")
    line()
    print_("C a n c i o n e s")
    for sn in range(len(datos["canciones"])):
        if datos["canciones"][sn]["artista"] == artista:
            print_ (datos["canciones"][sn]["nombre"])
    for i in range(len(datos["canciones"])):
        if datos["canciones"][i]["artista"] == artista:
            line()
            es()
            linea()
            linea()
            es()
            line()
            print_("N o m b r e")
            print_(datos["canciones"][i]["nombre"].capitalize())
            line()
            es()
            line()
            print_("G e n e r o")
            print_(datos["canciones"][i]["genero"])
            line()
            es()
            line()
            print_("D u r a c i o n")
            print_(datos["canciones"][i]["duracion"])
            line()
            es()
            line()
            print_("L a n z a m i e n t o")
            print_(datos["canciones"][i]["lanzamiento"])
            line()
            es()
            linea()
    return datos 
        
def leer_canciones_artista():
    while True:
        datos = cargar_datos(RUTA_BASE_DE_DATOS_ARTISTAS)
        datos = leer_art(datos)
        guardar_datos(datos, RUTA_BASE_DE_DATOS_ARTISTAS)
        continuar = very()
        if continuar == "2": break
        else: clear_screen()

#ACTUALIZAR
def actualizar_informacion(datos: dict):
    clear_screen()
    diseño_logo_discografia()
    nombre =input("Ingrese el nombre del artista: ").lower()    
    for i in range(len(datos["artistas"])):
        if datos["artistas"][i]["nombre"] == nombre:
            while True:
                op = input("Ingrese una opcion:\n    0. Salir \n    1. Nombre\n    2. Descripcion\n    3. Contacto\n\n>>  ")
                if op == "1": 
                    name =  datos["artistas"][i]["nombre"]
                    datos["artistas"][i]["nombre"]=input("Ingrese el nuevo nombre del artista: ").lower()
                    es()
                    print_(f"El nombre ",name," ha sido cambiada a ", datos["artistas"][i]["nombre"]," con éxito!")
                    return datos
                elif op == "2": 
                    descripcion =  datos["artistas"][i]["descripcion"]
                    datos["artistas"][i]["descripcion"]=input("Ingrese la nueva descripcion del artista: ").lower()
                    es()
                    print_(f"La descripcion ",descripcion," ha sido cambiada a ", datos["artistas"][i]["descripcion"]," con éxito!")
                    return datos
                elif op == "3": 
                    contacto =  datos["artistas"][i]["contacto"]
                    datos["artistas"][i]["contacto"]=input("Ingrese el nuevo contacto del artista: ").lower()
                    es()
                    print_(f"El contacto ",contacto," ha sido cambiada a ", datos["artistas"][i]["contacto"]," con éxito!")
                    return datos
                elif op == "0": return datos 
                else: print_("Opcion no valida")
    print(f"El artista ",nombre," no se encuentra registrado...")     
    return datos

def actualizar_info():
    while True:
        datos = cargar_datos(RUTA_BASE_DE_DATOS_ARTISTAS)
        datos = actualizar_informacion(datos)
        guardar_datos(datos, RUTA_BASE_DE_DATOS_ARTISTAS)
        continuar = very()
        if continuar == "2": break
        else: clear_screen()
        
# actualizar_info()

