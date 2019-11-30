# coding: utf-8

# Exercicio:
# Faça um Programa que pergunte quanto você ganha por hora
# e o número de horas trabalhadas no mês. Calcule e mostre o
# total do seu salário no referido mês.

def total_salario(horas_trabalhadas, valor_hora):
    return horas_trabalhadas * valor_hora

#
# entrada de dados
#

horas_trabalhadas = float(input('Informe a quantidade de horas trabalhadas:'))
valor_hora = float(input('Informe o valor da sua hora de trabalho:'))

#
# saída
#

print('O valor do seu salário é:',
      total_salario(horas_trabalhadas, valor_hora),
      'reais.')
#
# teste
#

assert 1200 == total_salario(40, 30)
