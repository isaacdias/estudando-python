# coding: utf-8

# Exercicio:
# Crie uma classe que modele um retangulo:
# Atributos: LadoA, LadoB
# Métodos: Mudar valor dos lados, Retornar valor dos lados,
# calcular Área e calcular Perímetro;
# Crie um programa que utilize esta classe.
# Ele deve pedir ao usuário que informe as medidas de um local.
# Depois, deve criar um objeto com as medidas e calcular a 
# quantidade de pisos e de rodapés necessárias para o local.

class Retangulo(object):
    def __init__(self, largura, comprimento):
        self.largura = largura
        self.comprimento = comprimento
    
    def mudarValorLargura(self, novo_valor):
        """metodo que altera o valor da largura"""
        self.largura = novo_valor
        return self.largura
    
    def mudarValorComprimento(self, novo_valor):
        """metodo que altera o comprimento"""
        self.comprimento = novo_valor
        return self.comprimento
    
    def valorLarguraAtual(self):
        """metodo que exibe a largura atual"""
        print ('O valor da largura atual é: ', self.largura)
    
    def valorComprimentoAtual(self):
        """metodo que imprime o comprimento atual"""
        print ('O valor do comprimento atual é: ', self.comprimento)
        
    def calcularArea(self):
        """metodo que calcula a area quadrada"""
        return self.largura * self.comprimento
    
    def calcularPerimetro(self):
        """metodo que calcula o perimetro"""
        return (self.largura + self.comprimento) * 2

# intancia da classe 

retangulo = Retangulo(15, 2)

# testes 

assert 10 == retangulo.mudarValorLargura(10)
assert 9 == retangulo.mudarValorComprimento(9)
assert 90 == retangulo.calcularArea()
assert 38 == retangulo.calcularPerimetro()

import math

#
# processamento
#

def quantidadePisos(area):
    """metodo para calcular quantidade de pisos"""
    pisos = area / 0.90
    if pisos % 2 != 0:
        return math.ceil(pisos)
    else:
        return pisos

def quantidadeRodapes(perimetro):
    """metodo para calcular quantidade de rodapes"""
    rodapes = perimetro / 0.30
    if rodapes % 2 != 0:
        return math.ceil(rodapes)
    else:
        return rodapes

print('PROGRAMA PARA CALCULAR QUANTIDADE DE PISOS E RODAPÉS PARA UMA DETERMINADA AREA')

# entrada de dados

largura = int(input('\nInforme o tamanho da largura:'))
comprimento = int(input('Informe o tamanho do comprimento:'))

# intancia da classe

retangulo1 = Retangulo(largura, comprimento)

#
# processamento e saida
#

area = retangulo1.calcularArea()
print('A area a sem medida é de:', area,'metros quadrados')
print('A quantidade necessária de pisos medindo 30x30cm é: %.0f ' % quantidadePisos(area))
perimetro = retangulo1.calcularPerimetro()
print('A quantidade necessaria de rodapés medindo 30cm é: %.0F ' % quantidadeRodapes(perimetro))
