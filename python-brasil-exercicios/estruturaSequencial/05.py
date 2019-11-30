# coding: utf-8

# Exercicio:
# Faça um Programa que converta metros para centímetros

#
# funcao que retorna metros convertidos em centimetros
#

def converter_metros(metragem):
    return metragem * 100

#
# entrada de dados
#

quant = float(input('Metragem que deseja converter? '))

#
# chamada da funcao e saída do resultado
#

print('Medida em centimetros: ', converter_metros(quant))

#
# testes
#

assert 100 == converter_metros(1)
assert 200 == converter_metros(2)
