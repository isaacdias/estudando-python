# coding: utf-8

#
# Lista de usuarios cadastrados
#

registered_id = ['idias', 'iaraujo', 'msouza',]

#
# Função que verifica e cadastra id disponivel 
#

def id():
	register = 'n'
	while register == 'n':
	    new_id = input('Informe um nome de identificação: ')
	    if new_id.lower() not in registered_id:
		    register = input('Nome de identificação disponivel. Confirmar cadastro (Y/N)? ')
		    if register.lower() == 'y':
		    	registered_id.append(new_id.lower())
		    	print('Cadastro realizado com sucesso!')
	    else:
		    print('Nome de identificação já está em uso.')
		    register = 'n'

#
# Chamada da função
#

id()

