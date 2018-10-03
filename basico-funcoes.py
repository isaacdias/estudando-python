# coding UTF-8

#
# pass retorna uma função que não faz nada
#

def foo():
    pass


#
# return interrompe a execução da função e define o retorno
#

def juntar(frase1, frase2):
   return'frase' + ' ' + frase2

# Os argumentos na função são obrigatórios

juntar('hello', 'world')


#
#podemos passar nomes de variáveis com os valores 
#

juntar(parte2='world', parte1='hello')


#
#podemos utilizar valores default também
#


def juntar(frase1='hello', frase2='world'):
    return frase1 + ' ' + frase2

juntar()


#
# Argumentos da função
#

def biggest_naumber(*args):
    print(max(args))
    return max(args)

def smallest_number(*args):
    print(min(args))
    return min(args)


biggest_number(-10, -5, 5, 10)
smallest-number(-10, -5, 5, 10)



