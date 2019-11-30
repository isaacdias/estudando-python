# coding: utf-8

# Exercicio:
# Crie uma classe que modele uma bola:
# Atributos: Cor, circunferência, material
# Métodos: trocaCor e mostraCor

class Bola(object):
    def __init__(self, cor, circuf, material):
        self.cor = cor.capitalize()
        self.circuf = circuf
        self.material = material.capitalize()

    def corAtual(self):
        """metodo que retorna a cor atual da bola"""
        return self.cor

    def circuferenciaBola(self):
        """metodo que retonar a circunferencia da bola"""
        return self.circuf

    def materialBola(self):
        """metodo que retorna o material da bola"""
        return self.material

    def trocarCor(self, nova_cor):
        """metodo para trocara a cor da bola"""
        self.cor = nova_cor.capitalize()
        return self.cor

    def mostrarCor(self):
        """metodo para imprimir a cor atual da bola"""
        print('A cor atual da bola é: ', self.cor)

#
# instancia da classe
#

bola = Bola('branca', 68, 'couro')

#
# testes
#

assert 'Branca' == bola.corAtual()
assert 68 == bola.circuferenciaBola()
assert 'Couro' == bola.materialBola()
bola.mostrarCor()
assert 'Amarelo' == bola.trocarCor('amarelo')
assert 'Amarelo' == bola.corAtual()
bola.mostrarCor()
