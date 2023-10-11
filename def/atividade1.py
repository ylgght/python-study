def inicio():
    x=float(input('Digite um Número para somar'))
    y=float(input('Digite um Número para somar'))
    v = soma(x,y)
    return v
def soma(x,y):
    som=x+y
    return som
v = inicio()
print (v)
