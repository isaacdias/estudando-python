# coding: utf-8

# Exercicio:
# Faça um Programa que peça 2 números inteiros e um número real.
# Calcule e mostre:
# o produto do dobro do primeiro com metade do segundo.
# a soma do triplo do primeiro com o terceiro.
# o terceiro elevado ao cubo.

def produto(primeiroNumero, segundoNumero):
    """retorna o produto do dobro do primeiro numero com
    a metade do segundo numero"""
    return (primeiroNumero*2) * (segundoNumero / 2)

def somaTriplo(primeiroNumero, terceiroNumero):
    """retorna a soma do trilo do primeiro numero com
    o terceiro numero"""
    return (primeiroNumero * 3) + terceiroNumero

def cubo(terceiroNumero):
    """retorna o terceiro numero elevado ao cubo"""
    return terceiroNumero**3

#
# entrada de dados
#

primeiroNumero = int(input('Informe um número inteiro: '))
segundoNumero = int(input('Informe outro número inteiro: '))
terceiroNumero = float(input('Informe um número real: '))

#
# saída
#

print('\nProduto do dobro do primeiro com metade do segundo: ',
      produto(primeiroNumero, segundoNumero))
print('Soma do triplo do primero com o terceiro: %.2f' %
      somaTriplo(primeiroNumero, terceiroNumero))
print('O terceiro número elevado ao cubo: %.2f' % cubo(terceiroNumero))

#
# testes
#

assert 100 == produto(10, 10)
assert 35.5 == somaTriplo(10, 5.5)
assert 166.375 == cubo(5.5)
