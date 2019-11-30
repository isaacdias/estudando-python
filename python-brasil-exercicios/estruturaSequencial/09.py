# coding: utf-8

# Exercicio:
# Faça um Programa que peça a temperatura em graus Farenheit,
# transforme e mostre a temperatura em graus Celsius

def toCelsius(farenheit):
    """retorna o valor de graus Farenheit
    convertido para Celsius"""
    return (farenheit - 32)*5 / 9

#
# entrada de dados 
#

farenheit = float(input('Informe a temperatura em Farenheit: '))

#
# saída
#

print('Temperatura covertida para Celsius: %.1f' % toCelsius(farenheit))

#
# teste
#

assert 100 == toCelsius(212)
