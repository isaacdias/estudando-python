# coding: utf-8

# Exercicio:
# Tendo como dado de entrada a altura (h) de uma pessoa,
# construa um algoritmo que calcule seu peso ideal, utilizando
# as seguintes fórmulas:
# Para homens: (72.7*h) - 58
# Para mulheres: (62.1*h) - 44.7


def peso_ideal(genero):
    """retrna o peso ideal de acordo com a altura
    e o gênero"""
    if genero == 'm':
        altura = float(input('Informe a altura:'))
        peso = round((72.7*altura) - 58, 2)
        return print('Seu peso ideal é:', peso)
    if genero == 'f':
        altura = float(input('Informe a altura:'))
        peso = round((62.1*altura) - 44.7, 2)
        return print('Seu peso ideal é:', peso)
    else:
        print('Gênero inválido!')
        
    

genero = str(input('Informe o gênero (m/f): '))
peso_ideal(genero)


#assert 69.23 == peso_ideal_masculino(1.75)
#assert 54.66 == peso_ideal_feminino(1.60) 
