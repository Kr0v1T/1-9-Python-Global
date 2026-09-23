import math

def exercicio20():
    global a, b, c, delta, x1, x2

    a = float(input("Digite o valor de A: "))
    b = float(input("Digite o valor de B: "))
    c = float(input("Digite o valor de C: "))

    delta = (b ** 2) - (4 * a * c)

    if delta < 0:
        print("Não existem raízes reais.")
    elif delta == 0:
        x1 = -b / (2 * a)
        print("Existe uma raiz real:")
        print("X =", x1)
    else:
        x1 = (-b + math.sqrt(delta)) / (2 * a)
        x2 = (-b - math.sqrt(delta)) / (2 * a)

        print("Existem duas raízes reais:")
        print("X1 =", x1)
        print("X2 =", x2)


# Programa principal
exercicio20()
