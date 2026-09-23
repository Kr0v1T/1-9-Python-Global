def exercicio18():
    global n1, n2, diferenca

    n1 = int(input("Digite o primeiro valor: "))
    n2 = int(input("Digite o segundo valor: "))

    if n1 > n2:
        diferenca = n1 - n2
    else:
        diferenca = n2 - n1

    print("A diferença do maior pelo menor é:", diferenca)


# Programa principal
exercicio18()
