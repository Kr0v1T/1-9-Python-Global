def exercicio22():
    global n1, n2

    n1 = int(input("Digite o primeiro valor: "))
    n2 = int(input("Digite o segundo valor: "))

    if n1 < n2:
        print(n1, n2)
    else:
        print(n2, n1)


# Programa principal
exercicio22()
