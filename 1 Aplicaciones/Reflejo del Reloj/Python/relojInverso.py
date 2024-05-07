def convertirHoraReflejada(horas, minutos):
    hora_real = minuto_real = 0  # empezamos con una la hora 0 y el minuto 0
    if minutos == 00:
        # si los minutos ingresados son cero la hora real indica las 12
        hora_real = 12
    else:
        # de no serlo dividimos los minutos los dividimos sobre 5 para obtener las 12 horas del reloj
        hora_real = minutos // 5
    if horas == 12:
        # si las horas indican las 12 entonces los minutos empiezan a contar desde 00
        minuto_real = 00
    else:
        # si no realizamos una multiplicación para saber si el indicador de las horas indican en el 2 entonces han pasado 10 minutos
        minuto_real = horas * 5
        if minutos % 5 != 0:
            # si en los minutos ingresados no son múltiplos de 5
            minuto_real += minutos % 5 + 1
            # añadimos el residuo de los minutos ingresados y se adicionamos un minuto mas de ñapa
    # dibujamos la hora mas aproximada a la que deberia ser al verse reflejada en el espejo
    print(
        f"hora reflejada ingresada -> hrs: {horas}:{minutos} \n hora real convertida -> hrs: {hora_real} : mins {minuto_real}"
    )


convertirHoraReflejada(
    12, 00
)  # ingresamos horas que se visualizan en el reflejo del espejo
convertirHoraReflejada(
    12, 30
)  # ingresamos horas que se visualizan en el reflejo del espejo
convertirHoraReflejada(
    6, 00
)  # ingresamos horas que se visualizan en el reflejo del espejo
convertirHoraReflejada(
    6, 30
)  # ingresamos horas que se visualizan en el reflejo del espejo
convertirHoraReflejada(
    2, 48
)  # ingresamos horas que se visualizan en el reflejo del espejo
convertirHoraReflejada(
    6, 42
)  # ingresamos horas que se visualizan en el reflejo del espejo
