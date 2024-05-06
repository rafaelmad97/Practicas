def generarBandera(sizey, sizex):
    # Se inicializan las variables de control para el ciclo
    x = y = 0
    # Se incializa una variable bandera la cual almacenará el lienzo de la bandera
    bandera = ""
    # se prosigue a obtener los puntos medios para dibujar los caracteres que arman las cruz
    midx = sizex // 2
    midy = sizey // 2
    while x < sizex and y < sizey:
        # mientras que las variables de control sean menores a el largo y ancho sigue iterando
        if x == midx or y == midy:
            # si la variables de control x ó y sean iguales a los puntos medios dibuja la el carácter que conforma la cruz
            bandera += " + "
        else:
            # si no dibuja el cuerpo de la bandera
            bandera += " 0 "
        # realiza un incremento hacia lo largo en una de las variables de control
        x += +1
        if x == sizex:
            # si llegas a el tope maximo del largo
            bandera += "\n"
            # agrega salto de linea
            x = 0
            # regresa el inicio de la bandera
            y += +1
            # bajas una casilla de la bandera realizando un incremento en la otra variable de control
    # devuelveme el valor de la bandera
    return bandera


def main():
    size_x = size_y = 0  # se supone que los valores del largo y el ancho son cero
    x = y = False  # se supone que los valores del largo y el ancho son incorrectos
    while size_x % 2 == 0 or size_y % 2 == 0:
        # itera mientras que los valores del largo y el ancho sean impares
        if x == False:
            # parece que el valor de ancho lo debes reescribir
            print("Ingrese el x tamaño de la bandera")
            size_x = int(input())
        if y == False:
            # parece que el valor de largo lo debes reescribir
            print("Ingrese el y tamaño de la bandera")
            size_y = int(input())

        y = (
            size_y % 2 != 0 and size_y < 200 and size_y > 0
        )  # validamos que el valor del "largo" esté "correcto"

        x = (
            size_x % 2 != 0 and size_x < 200 and size_x > 0
        )  # validamos que el valor del "ancho" esté "correcto"

        if x and y:
            # los valores del largo están buenos
            break  # te libro de la cadena de odio de iterar
        else:
            # vuelve a intentarlo me dijo coca cola en sus latas
            print(
                "el valor debe ser impar, no debe exceder a 200 y debe ser mayor a cero"
            )
    print(
        "\n"
    )  # hago un salto de linea para indicar que todo lo de arriba ya dejo de ejecutarse
    print(f"x={size_x} y={size_y}\n")  # muestro los valores que pasaron el filtro

    print(generarBandera(size_y, size_x))  # dibujame la bandera


main()
