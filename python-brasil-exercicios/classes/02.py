# coding utf-8

# Crie uma classe que modele um quadrado:
# Atributos: Tamanho do lado
# Métodos: Mudar valor do Lado, Retornar valor do Lado e 
# calcular Área;

class Quadrado(object):
    def __init__(self, tamanho_lado):
        self.tamanho_lado = tamanho_lado        
    
    def mudarTamanhoLado(self, novo_tamanho):
        """metodo que altera o valor do lado"""
        self.tamanho_lado = novo_tamanho
        return self.tamanho_lado
    
    def retornarValorLado(self):
        """metodo que retorna o valor do lado"""
        return self.tamanho_lado
    
    def calcularArea(self):
        """metodo que calcula a area quadrada do quadrado"""
        return self.tamanho_lado ** 2

#
# instancia da classe Quadrado
#

quadrado1 = Quadrado(10)

#
# testes
#

assert 10 == quadrado1.retornarValorLado()
assert 15 == quadrado1.mudarTamanhoLado(15)
assert 15 == quadrado1.retornarValorLado()
assert 225 == quadrado1.calcularArea()
