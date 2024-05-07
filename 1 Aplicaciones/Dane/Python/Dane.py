def calcularPromedios(lista):
    promedioControl = 0  # iniciamos el promedio de control con 0
    for i in range(len(lista)):  # recorremos los items de la lista de promedios(lista)
        # definimos que el valor de cada promedio es el valor X el dia -  el promedio de control
        valor = lista[i] * (i + 1) - promedioControl
        print(f"{int(valor)}")  # se muestra el valor
        promedioControl += valor  # se incrementa el promedio de control sumando el valor calculado x iteración


def llenarRegistros(size):
    lista = []  # iniciamos las listas
    # ciclo que va desde 0 hasta el numero de días definido (size)
    for i in range(size):
        # almacenamos el promedio de ese dia con un numero tipo float
        lista.append(float(input()))
    return lista  # retornamos la lista


def main():
    nDias = 366  # se inicializa el numero de días con un numero que permita el inicio del ciclo
    while nDias > 365:
        # mientras el numero de días excede los 365 días seguirá pidiendo un valor valido
        nDias = int(input("Ingrese numero de días"))  # se define el numero de días
        if nDias > 365:  # valor no valido?
            # informo que hay un error
            print("La cantidad de días no pueden superar los 365")
    # mediante la función llenarRegistros guardo los datos
    lista = llenarRegistros(nDias)
    calcularPromedios(lista)  # calculamos los promedios


main()
