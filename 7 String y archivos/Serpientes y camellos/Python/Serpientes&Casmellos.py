def convertirSerpienteaCamello(cadena):
    # se convierte las frases a arreglos "one_two" a ["one", "two"]
    cadenaDividida = cadena.split("_")
    valorConvertido = ""  # se inicializa la frase convertida
    for value in cadenaDividida:
        # se recorre el arreglo de palabras cadenaDividida
        if len(value):  # si la frase no esta vacía
            # se va guardando la frase convertida con el (primer caracter en mayuscula [0:1]) y el resto ([1:tamaño frase] minúscula)
            valorConvertido += f"{value[0:1].upper()}{value[1:len(value)].lower()}"

    print(valorConvertido)  # se muestra la conversión


def listaFrases(size):
    lista = []  # se inicializa el listado vacío
    for i in range(size):
        # se registra y se ingresa cada una de las cadenas
        cadena = input()
        lista.append(cadena)
    return lista  # se devuelve la lista


def main():
    # se registra el listado de palabras en formato serpiente
    # después de ingresar el numero de frases
    lista = listaFrases(int(input()))
    for cadena in lista:
        # se recorre el listado de frases
        convertirSerpienteaCamello(cadena)  # se convierte cada frase a camello


main()
