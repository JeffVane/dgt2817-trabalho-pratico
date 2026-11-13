saida = ""


def adicao(numero1, numero2):
    return numero1 + numero2


def subracao(numero1, numero2):
    return numero1 - numero2


def multiplicacao(numero1, numero2):
    return numero1 * numero2


def divisao(numero1, numero2):
    if numero1 == 0 or numero2 == 0:
        return "Não foi possível realizar a divisão por 0"
    return numero1 / numero2


def calculadora(numero1, numero2, operacao):
    resultado = ""
    operacao_normalizada = operacao.strip().lower()

    if operacao_normalizada in ["+", "adicao", "adição", "soma"]:
        resultado = adicao(numero1, numero2)
    elif operacao_normalizada in ["-", "subtracao", "subtração", "subtrair"]:
        resultado = subracao(numero1, numero2)
    elif operacao_normalizada in ["*", "multiplicacao", "multiplicação", "multiplicar"]:
        resultado = multiplicacao(numero1, numero2)
    elif operacao_normalizada in ["/", "divisao", "divisão"]:
        resultado = divisao(numero1, numero2)
    else:
        resultado = "Operação inválida."

    return resultado


while saida.upper() != "N":
    numero1 = float(input("Digite o primeiro número: "))
    numero2 = float(input("Digite o segundo número: "))
    operacao = input("Digite a operação (+, -, *, / ou o nome): ")

    resultado = calculadora(numero1, numero2, operacao)
    print("Resultado da operação: " + str(resultado))

    saida = input("Deseja continuar? (S/N): ").strip().upper()
