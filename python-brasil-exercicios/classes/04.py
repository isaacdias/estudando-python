# coding: utf-8

# Exercicio
# Crie uma classe que modele uma pessoa:
# Atributos: nome, idade, peso e altura
# Métodos: Envelhercer, engordar, emagrecer, crescer.
# Obs: Por padrão, a cada ano que nossa pessoa envelhece,
# sendo a idade dela menor que 21 anos, ela deve crescer 0,5 cm.

class Pessoa(object):
    def __init__(self, nome, idade, peso, altura):
        self.nome = nome
        self.idade = idade
        self.peso = peso
        self.altura = altura

    def infoPessoa(self):
        """metdo que exibe os valores dos atributos da classe pessoa"""
        pessoa = {'nome':self.nome.capitalize(), 'idade':self.idade, 'peso': self.peso, 'altura':self.altura}
        print('\nPessoa')
        for k,v in pessoa.items():
            print(k,v)

    def envelhecer(self, anos):
        """metodo para envelhecer, no atributo anos é acrescentado na idade"""
        self.idade += anos
        if self.idade <= 21:
            self.altura += anos * 0.05
        return self.idade, self.altura

    def engordar(self, kilos):
        """metodo para engorda, o atributo kilos é somado ao pesor"""
        self.peso += kilos
        return self.peso

    def emagrecer(self, kilos):
        """metodo para emagrecer, o atributo kilos é subtraido do peso"""
        return self.peso - kilos

    def crescer(self, crescimento):
        """metodo para crescer, o atributo crescimento é soma a altura"""
        self.altura += crescimento
        return self.altura

#
# instancia da classe pessoa
#

pessoa1 = Pessoa('isaac', 20, 66, 1.75)

# testes

assert (21, 1.8) == pessoa1.envelhecer(1)
assert 69.5 == pessoa1.engordar(3.5)
assert 64.5 == pessoa1.emagrecer(5)
assert 1.95 == pessoa1.crescer(0.15)