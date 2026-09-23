def exercicio26():
    global n1, n2, maior, menor

    n1 = int(input("Digite o primeiro número: "))
    n2 = int(input("Digite o segundo número: "))

    if n1 > n2:
        maior = n1
        menor = n2
    else:
        maior = n2
        menor = n1

    if maior % menor == 0:
        print("O maior número é múltiplo do menor.")
    else:
        print("O maior número não é múltiplo do menor.")


# Programa principal
exercicio26()
