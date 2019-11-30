# coding: utf-8

# Exercicio:
# Faça um Programa que calcule a área de um quadrado,
# em seguida mostre o dobro desta área para o usuário.

#
# funcao que retorna a area de um quadrado
#

def area_quadrado(lado1, lado2):
    return lado1 * lado2

#
# funcao que retorna o dobro da area
#

def dobro_area(numero):
    return numero * 2

#
# entrada de dados
#

lado1 = float(input('Informe o valor do primeiro lado:'))
lado2 = float(input('Informe o valor do segundo lado:'))

#
# saída + chamada das funcoes
#

print('Área do quadrado:',area_quadrado(lado1, lado2))
print('O dobro da área:', dobro_area(area_quadrado(lado1, lado2)))

#
# testes
#

assert 9 == area_quadrado(3,3)
assert 18 == dobro_area(9)
