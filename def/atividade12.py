def inicio():
    a=int(input('Digite o primeiro Número: \n'))
    b=int(input('Digite o segundo Número: \n'))
    c=mdc(a,b)
    return c
def mdc(a,b):
    while b!=0:
        resto=a%b
        a=b
        b=resto
    return a
c=inicio()
print(f'o mdc desses 2 números é de {c}')
