import math

def calculaAreaCirculo() -> float:
    raio = float(input("Digite o raio do seu circulo: "))
    pi = math.pi
    areaTotal = pi * (raio ** 2)

    return f"Valor da Área = {areaTotal:.2f}"

area = calculaAreaCirculo()
print(area)