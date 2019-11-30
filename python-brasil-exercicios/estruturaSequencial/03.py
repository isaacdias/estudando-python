# coding: utf-8

# Exercicio:
# Faça um Programa que peça dois números e imprima a soma.

def soma_numeros(n1, n2):
    return n1 + n2

#
# entrada de dados
#

numero1 = int(input('Informe um número: '))
numero2 = int(input('Informe outro número: '))

#
# saída e chamada da funcao
#
print('A soma dos números é: ', soma_numeros(numero1, numero2))

#
# teste
#

assert 10 == soma_numeros(5, 5)
assert 55 == soma_numeros(25, 30)
