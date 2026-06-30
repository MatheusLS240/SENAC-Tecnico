def desconto(preco = 0.0, taxa = 0.0):
    """Calcula o preço final após aplicar um desconto"""
    valor_desconto = preco * (taxa / 100)
    preco_final = preco - valor_desconto
    return preco_final

rs = desconto(100.0, 20.0)
print(f"Preço final após desconto: {rs}")