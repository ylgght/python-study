def inicio():
    numero=int(input('Digite o Número que você quer saber se é Primo ou não: \n'))
    x=primo(numero)
    return x
def primo(numero):
    cont=0
    i=0
    while i<= numero or cont < 2:
        i+=1
        x= numero % i
        if x==0:
            cont=cont+1
    return cont
x=inicio()
if x<=2:
    print('Primo')
else:
    print('Não Primo')
