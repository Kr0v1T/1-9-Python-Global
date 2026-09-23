def exercicio25():
    global hora_inicio, minuto_inicio
    global hora_final, minuto_final
    global inicio, final, duracao
    global horas, minutos

    hora_inicio = int(input("Digite a hora de início: "))
    minuto_inicio = int(input("Digite os minutos de início: "))

    hora_final = int(input("Digite a hora de término: "))
    minuto_final = int(input("Digite os minutos de término: "))

    inicio = (hora_inicio * 60) + minuto_inicio
    final = (hora_final * 60) + minuto_final

    if final <= inicio:
        final = final + (24 * 60)

    duracao = final - inicio

    horas = duracao // 60
    minutos = duracao % 60

    print("Duração do jogo:", horas, "hora(s) e", minutos, "minuto(s).")


# Programa principal
exercicio25()
