def divisionSalomonica(valor):
    # se inicializa la variable div con el valor ingresado
    div = valor
    beneficiarios = 0  # se inicializan 0 beneficiarios
    while div > 9:  # div debe ser mayor a 9 para seguir con el ciclo
        div = div / 2  # se reescribe div con el valor de el mismo divido entre 2
        beneficiarios += 1  # se incrementa el numero de beneficiarios x iteración
    return beneficiarios  # retornamos el numero de beneficiarios totales


def main():
    valor = float(input())  # se inicializa un valor n
    # se pinta el resultado de la función divisionSalomonica
    print(divisionSalomonica(valor))


main()
