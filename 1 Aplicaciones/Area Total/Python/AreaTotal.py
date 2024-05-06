def calcularArea(nLotes, valorMin, incremento):
    areaTotal = iteraciones = controlIncremento = 0
    while iteraciones < nLotes:
        areaTotal += (valorMin + controlIncremento) * (valorMin + controlIncremento)
        controlIncremento += incremento
        iteraciones += 1
    return areaTotal


def main():
    nLotes = int(input())
    valorMin = float(input())
    incremento = float(input())
    print(
        f"El area total es de {calcularArea(nLotes,valorMin,incremento)} metros cuadrados."
    )


main()
