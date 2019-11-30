# coding: utf-8

# Exercicio:
# aça um Programa que peça a temperatura em graus Celsius,
# transforme e mostre em graus Farenheit.

def toFarenheit(celsius):
    """Faz a converssão de graus Celsius
    para Farenheit"""
    return (celsius * 9 / 5) + 32

#
# entrada de dados
#

celsius = float(input('Informe a temperatura em graus Celsius: '))

#
# chamada da funcao e saída 
#

print('A temperatura em graus Farenheit é: %.1f' % toFarenheit(celsius))

#
# teste
#

assert 212 == toFarenheit(100)
