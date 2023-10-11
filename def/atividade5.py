from math import factorial
def inicio():
    x=int(input('Digite o Número:\n'))
 
    return factorial(x)
def fator(x):
    
    y=1
    z=1
    while z<=x:
        y*=z
        z+=1
    return y
y=inicio()
print('O valor fatorial deste Número é de : {}'.format(y))