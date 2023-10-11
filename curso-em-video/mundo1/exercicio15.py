#Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.
km=float(input('Digite Quantos Km você percorreu no carro : '))
print(f'O valor final do aluguel é de R$ {km*0.15+60}')