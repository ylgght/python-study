x=int(input('Digite o primeiro número: '))
y=int(input('Digite o segundo número: '))
if x>y:
    for z in range(x,y,-1):
        
        print(z)
else:
    for z in range(y,x,-1):
        
        print(z)