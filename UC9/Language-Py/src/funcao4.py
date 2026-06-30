def soma(valor1, valor2):
    return valor1 + valor2

def subtracao(valor1, valor2):
    return valor1 - valor2

def multiplicacao(valor1, valor2):
    return valor1 * valor2

def divisao(valor1, valor2):
    if valor2 != 0:
        return valor1 / valor2
    else:
        return "Erro: Divisão por zero não é permitida."
    
def calculadora(operacao, valor1, valor2):
    if operacao == "soma":
        return soma(valor1, valor2)
    elif operacao == "subtracao":
        return subtracao(valor1, valor2)
    elif operacao == "multiplicacao":
        return multiplicacao(valor1, valor2)
    elif operacao == "divisao":
        return divisao(valor1, valor2)
    else:
        return "Operação inválida. Por favor, escolha entre 'soma', 'subtracao', 'multiplicacao' ou 'divisao'."
    
resultado = calculadora("soma", 10, 5)
print("Resultado da soma:", resultado)