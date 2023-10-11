def inicio():
    c=float(input('Digite a temperatura em Celsius: \n'))
    f=fahren(c)
    return f
def fahren(c):
    f=(c*9/5)+32
    return f
f=inicio()
print(f'A temperatura em Fahrenheit é de{f}')