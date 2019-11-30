# coding: utf-8

#Exercicio
# João Papo-de-Pescador, homem de bem, comprou um microcomputador
# para controlar o rendimento diário de seu trabalho. Toda vez que
# ele traz um peso de peixes maior que o estabelecido pelo regulamento
# de pesca do estado de São Paulo (50 quilos) deve pagar uma multa
# de R$ 4,00 por quilo excedente. João precisa que você faça um
# programa que leia a variável peso (peso de peixes) e calcule o excesso.
# Gravar na variável excesso a quantidade de quilos além do limite e
# na variável multa o valor da multa que João deverá pagar.
#Imprima os dados do programa com as mensagens adequadas.


def pesagem(peso):
    """retorna o peso total da pescaria"""
    return peso

def controle_de_peso(peso):
    """retorna o excesso de peso permitido"""
    if peso > 50:
        excesso = peso - 50
        return excesso
    else:
        return 0

def multa(peso):
    """retorna o valor da multa pelo peso excedido"""
    if peso > 50:
        return (peso - 50) * 4
    else:
        return 0
#
# entrada de dados
#

peso = float(input('Informe o peso total:' ))    
print('Sua pescaria tem o peso total de: %.2f' % pesagem(peso),'Kg.')    
print('peso acima do permitido: %.2f' % controle_de_peso(peso),'Kg.')
print('Total da multa à pagar: R$ %.2f' % multa(peso), 'reais,')    

#
# testes
#

assert 40 == pesagem(40)
assert 10 == controle_de_peso(60)
assert 40 == multa(60)
