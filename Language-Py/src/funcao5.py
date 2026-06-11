def area_quadrado(lado = 0):
    return lado ** 2

lado = float(input("Digite o lado do quadrado: "))
area = area_quadrado(lado)
print("A área do quadrado é:", area)