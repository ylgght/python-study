def inicio():
    km=float(input('Digite o valor de km/h: \n'))
    ms=metro(km)
    return ms
def metro(km):
    ms=km/3.6
    return ms
ms=inicio()
print(f'O valor deu {ms}')
