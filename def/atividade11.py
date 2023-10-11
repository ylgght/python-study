def inicio():
    x=float(input('Digite o primeiro Número: \n'))
    y=float(input('Digite o segundo Número: \n'))
    z=maior(x,y)
    return z
def maior(x,y):
    if x>y:
        return x
    elif x==y:
        print('Os Números são iguais')
        return False
    else:
        return y        
z=inicio()
if z!=False:
    print(f'O maior Número é {z}')
