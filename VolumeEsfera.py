import math


def calculaVolumeCirculo() -> float:
    raio = float(input("Digite o valor de seu raio: "))
    pi = math.pi
    volume = (4/3) * pi * raio**3

    return volume

volumeTotal = calculaVolumeCirculo()
print(f"{volumeTotal:.2f}")