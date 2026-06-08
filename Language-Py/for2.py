contador = 0
for ano in range(1950, 2027):
    if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
        print(f"{ano} é um ano bissexto.")
        contador += 1

print(f"Total de anos bissextos entre 1950 e 2026: {contador}")