
 coding: utf-8 


#
# Função que informa a area de um circulo
#
def area_circulo(raio):
    pi = 3.14159
    return pi * raio**2

assert 314.1590 == area_circulo(10)

#
# entrada do valor de raio
#
raio = float(input('Informe o valor de raio :'))

#
# saída da area de um circulo
#
print('A area do circulo é : %.4f' % area_circulo(raio))
