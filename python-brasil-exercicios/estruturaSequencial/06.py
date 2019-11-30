# coding: utf-8

# Exercicio:
# Faça um Programa que peça o raio de um círculo, calcule e mostre sua área

def area_circulo(raio):
    pi = 3.1416
    return pi * raio**2

#
# entrada de dados
#
raio = float(input('Informe o tamanho de raio: '))

#
# saída + chamada da funcao
#

print('A área do circulo é equivamelente à:', area_circulo(raio))

#
# teste
#

assert 28.2744 == area_circulo(3)
