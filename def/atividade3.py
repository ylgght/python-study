def inicio():
    x=int(input('Digite um número para saber se é impar ou par: \n'))
    calculo(x)
def calculo(x):
    x=x%2
    if x==0:
        print('Número Par')
    else:
        print('Número Ímpar')
inicio()