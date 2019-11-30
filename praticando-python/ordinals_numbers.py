# coding: UTF-8

numbers = list(range(1,10))

#
# Função queexibe em cada linha o respectivo numero de forma ordinal inglês
#

def ordinals():
    for number in numbers:
        if number == 1:
            print(str(number) + 'st')
        elif number == 2:
            print(str(number) + 'nd')
        elif number == 3:
            print(str(number) + 'rd')
        else:
            print(str(number) + 'th')

ordinals()
