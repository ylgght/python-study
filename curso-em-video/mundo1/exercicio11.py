#Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta pinta uma área de 2 metros quadrados.
largura=float(input('Qual a largura dessa parede ? \n '))
altura=float(input('Qual a altura dessa parede ? \n '))
print(f'A aréa é de {largura*altura}, o tanto de tinta necessário é de {(largura*altura)/2}')