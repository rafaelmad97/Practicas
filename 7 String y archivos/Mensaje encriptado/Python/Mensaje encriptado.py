def leerArchivo():
    try:  # intento
        contenido = open("mensaje.txt", "r")  # leer el archivo "mensaje.txt"
        for mensaje in contenido:
            # se recorre el contenido del archivo
            # se quitan los saltos de linea con strip() y con el [::-1] se escriba volteado y se pinta
            print(mensaje.strip("\n")[::-1])
    except:  # fallo algo puede ser que el archivo no exista
        print("el archivo no existe")


leerArchivo()
