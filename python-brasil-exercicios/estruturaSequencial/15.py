# coding: utf-8

# Exercicio:
# Faça um Programa que pergunte quanto você ganha por hora e o número de horas
# trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês,
# sabendo-se que são descontados 11% para o Imposto de Renda, 8% para o INSS
# e 5% para o sindicato, faça um programa que nos dê:
# salário bruto.
# quanto pagou ao INSS.
# quanto pagou ao sindicato.
# o salário líquido.
# calcule os descontos e o salário líquido, conforme a tabela abaixo:

# + Salário Bruto : R$
# - IR (11%) : R$
# - INSS (8%) : R$
# - Sindicato ( 5%) : R$
# = Salário Liquido : R$

def calculo_salario_bruto(horas_trabalhadas, valor_hora):
    """retorna o salario bruto"""
    return horas_trabalhadas * valor_hora

def desconto_ir(salario):
    """retorna o valor do desconto de IR"""
    return (11*salario) / 100

def desconto_inss(salario):
    """retorna o valor do desconto de INSS"""
    return (8*salario) / 100

def desconto_sindicato(salario):
    """retorna o valor do desconto do sindicato"""
    return (5*salario) / 100

def calculo_salario_liquido(salario, ir, inss, sindicato):
    """retorna o valor do salario liquido"""
    return salario - ir - inss - sindicato

#
# entrada de dados
#

horas_trabalhadas = float(input('Informe a quantidade de horas trabalhadas:'))
valor_hora = float(input('Informe o valor da sua hora de trabalho:'))

#
# processamento
#

salario = calculo_salario_bruto(horas_trabalhadas, valor_hora)
ir = desconto_ir(salario)
inss = desconto_inss(salario)
sindicato = desconto_sindicato(salario)
salario_liquido = calculo_salario_liquido(salario, ir, inss, sindicato)

#
# saida
#

print('\n+ Salário Bruto : R$ %.2f' % salario)
print('- IR (11%%) : R$ %.2f' % ir)
print('- INSS (8%%) : R$ %.2f' % inss)
print('- Sindicato (5%%) : R$ %.2f' % sindicato)
print('= Salário Líquido : R$ %.2f' % salario_liquido)

#
# testes
#

assert 1200 == calculo_salario_bruto(40, 30)
assert 132 == desconto_ir(1200)
assert 96 == desconto_inss(1200)
assert 60 == desconto_sindicato(1200)
assert 912 == calculo_salario_liquido(1200, 132, 96, 60)
