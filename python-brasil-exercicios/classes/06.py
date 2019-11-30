# coding: utf-8

# Exercicio
# Faça um programa que simule um televisor criando-o como um objeto.
# O usuário deve ser capaz de informar o número do canal e aumentar
# ou diminuir o volume. Certifique-se de que o número do canal e o
# nível do volume permanecem dentro de faixas válidas.


class Televisor(object):
    """classe que simula um televisor"""
    def __init__(self, canal=2, volume=0):
        self.canal = canal
        self.volume = volume

    def mudarCanal(self, canal):
        """metodo para alterar o canal"""
        canais_programados = [2, 4, 6, 9, 11, 13]
        if canal in canais_programados:
            self.canal = canal
            return self.canal
        else:
            print('Canal desconheçido')

    def aumentarVolume(self, nivel_volume):
        """metodo para aumentar o volume do televisor"""
        faixa_volume = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        if nivel_volume <= self.volume or nivel_volume not in faixa_volume:
            return self.volume
        else:
            self.volume = nivel_volume
            return self.volume

    def diminuirVolume(self, nivel_volume):
        """metodo para diminuir o volume do televisor"""
        faixa_volume = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        if nivel_volume >= self.volume or nivel_volume not in faixa_volume:
            return self.volume
        else:
            self.volume = nivel_volume
            return self.volume

#
# instancia da classe
#

televisor1 = Televisor()

#
# testes
#

assert 4 == televisor1.mudarCanal(4)
assert 6 == televisor1.aumentarVolume(6)
assert 0 == televisor1.diminuirVolume(0)