def acrescimo(preco: float = 0.0, taxa: float = 0.0) -> float:
    """
    Calcula o valor final de um produto após aplicar um acréscimo percentual.

    O acréscimo é calculado sobre o preço original e somado ao valor inicial,
    retornando o preço atualizado.

    Args:
        preco (float): Valor original do produto. Deve ser maior ou igual a zero.
        taxa (float): Percentual de acréscimo a ser aplicado.
            Exemplo: 10 representa um acréscimo de 10%.

    Returns:
        float: Valor final após a aplicação do acréscimo.
    """
    valor_acrescimo = preco * (taxa / 100)
    preco_final = preco + valor_acrescimo
    return preco_final

acrescimo_resultado = acrescimo(100, 15)
print(f"Preço final após acréscimo: {acrescimo_resultado}")