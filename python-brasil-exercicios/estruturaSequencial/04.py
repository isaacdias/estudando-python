# coding: utf8

# Exercicio:
# Faça um Programa que peça as 4 notas bimestrais e mostre a média.

#
# funcao que retorna a media de 4 notas bimestrais
#

def media(n1, n2, n3, n4):
    return (n1 + n2 + n3 + n4) / 4

#
# entrada de dados
#

nota1 = int(input('Informe a 1° nota: '))
nota2 = int(input('Informe a 2° nota: '))
nota3 = int(input('Informe a 3° nota: '))
nota4 = int(input('Informe a 4° nota: '))

#
# saída e chamada da funcao
#

print('\nA média das notas é: ', media(nota1, nota2, nota3, nota4))

#
# teste
#

assert 10 == media(10, 10, 10, 10)
assert 7.5 == media(10, 6, 8, 6)
