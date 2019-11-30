# coding: utf-8

#
# Lista com  usernames
#

users = ['isaac', 'carlos', 'admin', 'alberto', 'amanda']
banned_users = ['carlos',]

#
# Função que verifica permissão de acesso e mostra mensagem de acordo com o tipo de usuário
#

def user_admin():
	
    for user in users:
    	if user not in banned_users:
            if user.lower() == 'admin':
                print('Olá ' + user.title() + ', gostaria de ver um relatório de status?')
            else:
                print('Olá ' + user.title() + ', seja bem vindo.')
        else:
        	print('Você não tem permissão de acesso.')
#
# Chamada da função
#

user_admin()
