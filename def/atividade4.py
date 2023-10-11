def inicio():
    x=float(input('Digite um Valor: \n'))
    calculo(x)
def calculo(x):
    if x>0:
        print('Número Positivo')
    elif x<0:
        print('Número Negativo')
    else:
        print('Zero')
inicio()