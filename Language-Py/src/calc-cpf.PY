# 1. Pede o CPF ao usuário e limpa possíveis espaços em branco
cpf_original = input("Digite o seu CPF (apenas números): ").strip()

# Validação básica: verifica se o usuário digitou exatamente 11 dígitos numéricos
if len(cpf_original) != 11 or not cpf_original.isdigit():
    print("Erro: O CPF deve conter exatamente 11 números.")
else:
    # 2. Pega os 9 primeiros dígitos usando fatiamento (slice)
    cpf_gerado = cpf_original[:9]

    # --- CÁLCULO DO 1º DÍGITO VERIFICADOR ---
    peso = 10
    resultado = 0

    # O 'for' percorre cada caractere do CPF gerado automaticamente
    for digito in cpf_gerado:
        resultado += int(digito) * peso
        peso -= 1

    resto = resultado % 11
    if resto < 2:
        cpf_gerado += "0"
    else:
        cpf_gerado += str(11 - resto)

    # --- CÁLCULO DO 2º DÍGITO VERIFICADOR ---
    # Para o segundo dígito, o peso começa em 11
    peso = 11
    resultado = 0

    for digito in cpf_gerado:
        resultado += int(digito) * peso
        peso -= 1

    resto = resultado % 11
    if resto < 2:
        cpf_gerado += "0"
    else:
        cpf_gerado += str(11 - resto)

    # --- VALIDAÇÃO FINAL ---
    # Compara se o CPF que geramos é igual ao que o usuário digitou
    if cpf_gerado == cpf_original:
        print("CPF VÁLIDO!")
    else:
        print("CPF INVÁLIDO!")