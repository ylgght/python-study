#Faça um programa que leia um número Inteiro qualquer e mostre na tela a sua tabuada.
int=int(input('Digite o número que você quer saber a tabuada: '))
a=0
while a<10:
    a+=1
    print(f'{int} * {a} = {int*a}')