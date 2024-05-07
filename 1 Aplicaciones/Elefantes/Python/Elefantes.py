def Elefantes(resistencia):
    elefantes = pesoAcumuladoElefante = 0
    # tanto el peso que se acumula como el numero de elefantes debe ser 0
    cantidadElefantes = int(input())  # se ingresa la cantidad maxima de elefantes
    for e in range(cantidadElefantes):
        # se recorre desde 0 a la cantidad maxima de elefantes
        pesoAcumuladoElefante += int(input())
        # se auto incrementa el peso de elefante ....n con un valor n
        if pesoAcumuladoElefante <= resistencia:
            # el peso acumulado es menor la resistencia
            print(
                f"{e+1} Un elefante se balanceaba sobre la tela de una araña, como veía que resistía fue a llamar a otro elefante."
            )  ## Cantemos :3
            elefantes += 1
            # incrementamos los elefantes que están en la tela de una araña
    # mostramos la cantidad final de elefantes que estaban en la tela antes de romperse
    print(f"e: {elefantes}")


def main():
    # Se define la resistencia de la tela de araña
    resistencia = int(input("Ingrese la resistencia"))
    Elefantes(resistencia)  # comprobamos la resistencia


main()
