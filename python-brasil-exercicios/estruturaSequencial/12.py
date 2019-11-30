# coding: utf-8

# Exercicio:
# Tendo como dados de entrada a altura de uma pessoa,
# construa um algoritmo que calcule seu peso ideal,
# usando a seguinte fórmula: (72.7*altura) - 58

def peso_ideal(altura):
    """retorna o peso ideal de acordo com a altura informada"""
    return round((72.7 * altura) - 58, 2)

#
# entrada de dados
#

altura = float(input('Informe a altura(x.xx): '))

#
# saída
#

print('o peso ideal para altura informada é:', peso_ideal(altura),'kg')

#
# teste
#

assert 69.23 == peso_ideal(1.75)
