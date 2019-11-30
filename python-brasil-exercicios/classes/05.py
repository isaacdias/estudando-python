# coding: utf-8

# Exercicio
#  Crie uma classe para implementar uma conta corrente.
# A classe deve possuir os seguintes atributos: número da conta, nome do correntista e saldo.
# Os métodos são os seguintes: alterarNome, depósito e saque;
# No construtor, saldo é opcional, com valor default zero e os
# demais atributos são obrigatórios.

class contaCorrente(object):
    def __init__(self, conta, nome, saldo=0):
        self.conta = conta
        self.nome = nome.capitalize()
        self.saldo = saldo

    def alterarNome(self, novo_nome):
        """metodo que altera o nome do correntista"""
        self.nome = novo_nome.capitalize()
        return self.nome

    def deposito(self, credito):
        """metodo para creditar saldo na conta corrente"""
        self.saldo += credito
        return self.saldo

    def saque(self, debito):
        """meodo para debitar saldo da conta corrente"""
        self.saldo -= debito
        return self.saldo

#
# instancia da classe contaCorrente
#

conta01 = contaCorrente(123456, 'isaac')

conta01.alterarNome('Rafael')

# testes

assert 'Rafael' == conta01.alterarNome('rafael')
assert 30 == conta01.deposito(30)
assert 20 == conta01.saque(10)
