def validarCirculodeCables(value):
    listaCables = value.split(
        " "
    )  ## se convierte el la cadena "MF FF" en un arreglo ["MF", "FF"]
    conectoresf = conectoresm = 0  ## de inicializa la cantidad de conectores M Y F en 0
    for cable in listaCables:
        # se recorre el arreglo obtenido en la variable listCables
        conectoresf += cable.count(
            "F"
        )  ## Solo cuenta si en la cadena string hay un conector "F"
        conectoresm += cable.count(
            "M"
        )  ## Solo cuenta si en la cadena string hay un conector "M"
    ## fin del ciclo
    if conectoresm == conectoresf:  ## Son iguales?
        print("Es posible hacer un unico circulo")  # Eureka hay un circulo
    else:
        print("No es posible")  # no se pude formar un ciclo


def leerValores(lista):
    for cables in lista:
        # ciclo que recorre el listado de cables
        validarCirculodeCables(
            cables
        )  # se valida si el conjunto de cables es valido o no es valido


def ingresarValores(size):
    lista = []  ## se define una lista vacía
    for x in range(size):
        ## este ciclo inicia desde cero en rango del 0...(variable size);
        value = (
            input()
        )  ## se ingresa el conjunto de cables en este formato"FM MM FF MF"
        lista.append(
            value.upper()
        )  ## el valor ingresado se le aplica el formato mayúsculas para todos los caracteres
    return lista  # Se devuelve la lista


def main():
    size = int(input())  ## Se define el numero de conjuntos de cables FM
    lista = ingresarValores(
        size
    )  ## Se procede a ejecutar la función ingresarValores que devuelve la lista círculos a evaluar, se le ingresa el numero de conjuntos
    leerValores(
        lista
    )  ## se comprueba cada circulo si es posible o no es posible ingresando la lista almacenada


main()
