def inicio():
    i=int(input('Quantos anos Você tem ? \n'))
    bebida(i)
def bebida(i):
    if i>=18:
       print('Você Pode Comprar Bebida')
    elif i<18 and i>=16:
        auto=int(input('[1]SIM\n[2]NÃO\nVocê tem autorização dos seus Pais Para comprar Bebida ?\n'))
        if auto!=1:
            print('Você Não Pode Comprar Bebida')
        else:
            print('Você Pode Comprar Bebida')
    else:
        print('Você Não Pode Comprar Bebida')
inicio()
