def Panini(laminas):
    laminasRepetidas = i = aux = 0  # se definen los valores en 0
    while i < len(laminas):
        # se recorren las laminas
        if i != aux:  # es i(posición) distinto a aux(posición auxiliar)
            # para que no se comparen elementos con la misma posición
            # el valor que esta en i y aux son iguales?
            if laminas[i] == laminas[aux]:
                # solo se suma 0.5 ya que pueden encontrar  a([i]==[aux])=0.5 y b([aux]==[i])=0.5
                # si hay 1 repetidos serian dos posiciones validas (0.5+0.5) = 1
                laminasRepetidas += 0.5
        i += 1  # se incrementa i (posición)
        # si i == cantidad de paninis y el aux es menor a la (cantidad de paininis - 1)
        if i == len(laminas) and aux < len(laminas) - 1:
            # incrementa el auxiliar
            aux += 1
            # se resetea i (posición) para volver a recorrer el listado
            i = 0
    # se retorna el numero de paninis - laminas repetidas para saber los paninis únicos
    return int(len(laminas) - laminasRepetidas)


def agregarLaminas():
    laminas = []  # se inicializa el listado vacío
    # se inicializa un valor valido para un panini
    lamina = 1
    while lamina > 0:
        # se van agregar paninis mientras que no sea el numero 0
        lamina = int(input())
        # se ingresa y se guarda el panini
        laminas.append(lamina)
    return laminas  # se retorna el listado


def main():
    laminas = agregarLaminas()  # Se registra el listado de paninis
    print(laminas)  # se muestra el listado de paninis
    print(Panini(laminas))  # se muestra el resultado de paninis no repetidos


main()
