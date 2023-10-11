def inicio():
    h=float(input('Digite as Horas: \n'))
    m=min(h)
    return m
def min(h):
    m=h*60
    return m
m=inicio()
print(f'Deu {m} Minutos')