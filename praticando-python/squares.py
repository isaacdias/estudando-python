# coding: UTF-8

squares = []

#
# Função que retorna uma lista de numers elevados ao quadrado
#
def number_list():
    for value in range(1,11):
        squares.append(value**2)
    print(squares)

#
# Função que exibe informações sobre a lista
#
def message():
    print('O menor valor da lista é: ' + str(min(squares)))
    print('O maior valor da lista é: ' + str(max(squares)))
    print('A soma dos valores é: ' + str(sum(squares)))

number_list()
message()
