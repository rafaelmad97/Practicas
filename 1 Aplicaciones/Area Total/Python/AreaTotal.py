## Se implementa un método para el calculo del area total
def calcularArea(nLotes, valorMin, incremento):
    areaTotal = iteraciones = controlIncremento = 0  ## se inicializan las variables
    ##corremos un ciclo que va mientras el numero de iteraciones de cada
    ##calculo de los lotes sea menor al numero de lotes que se ingresaron
    while iteraciones < nLotes:
        ## se va acumulando en la variable area total el calculo:
        ## longitud mínima del lote + el valor incrementado(longitud) por iteración
        ## multiplicado
        ## longitud mínima + el valor incrementado(longitud) por iteración
        areaTotal += (valorMin + controlIncremento) * (valorMin + controlIncremento)
        ## Se hacen los incrementos
        controlIncremento += incremento
        iteraciones += 1
    return areaTotal


def main():
    nLotes = int(input())  # Se ingresan los valores
    valorMin = float(input())  # Se ingresan los valores
    incremento = float(input())  # Se ingresan los valores
    print(
        f"El area total es de {calcularArea(nLotes,valorMin,incremento)} metros cuadrados."
    )  # Se visualizan los datos


main()
