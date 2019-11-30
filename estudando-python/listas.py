# coding: UTF-8

#
# Listas
#

animals = ['pangolin', 'casowarry', 'sloth', 'dog']



#
# Acessando um indice da lista
#

animals[2]



#
# Criando uma lista vazia
#

lis = []



#
# list comprehension
#

lis = [1, 2, 3,4]

[x for x**2 in lis]



#
# Percorrendo uma lista 
#

list = [1, 2, 3, 4,]

for number in list:
    print(number)

# 1
# 2
# 3
# 4


#
# Copiando listas
# (Neste caso as duas listas apontam para o mesmo objeto)
#

list_a = [1, 2, 3, 4,]
list_b = list_a


#
# Clonando listas
# (A alteração de uma lista não afeta a outra)
#

list_a = [1, 2, 3, 4,]
list_b = list_a[:]


#
# Funções nativas para liostas 
#

# index()

#
# Retorna o index de determinado elemento.
#

animals = ['ant', 'bat', 'cat',]
print(animals.index('bat'))
# 1

# insert()

nimals = ["ant", "bat", "cat"]
animals.insert(1, "dog")
print(animals) 
# ["ant", "dog", "bat", "cat"]

#
# remove
#

# Remove artravés do valor

animals = ['ant', 'bat', 'cat']
animals.remove('ant')
print(animals)
# ['bat', 'cat']

#
# pop()
#

# Remove através de índice (retorna o valor removido)

animals = ['ant', 'bat', 'cat']
animals.pop(0) # 'ant'
print(animals) # ['bat", 'cat']

#
# sort()
#

lista = ['c', 'b', 'a']
print(lista) # ['c', 'b', 'a']

lista.sort()
print(lista) # ['a', 'b', 'c']

# Para ordenar uma lista também é possível utilizar a função sorted()

sorted([5, 2, 3, 1, 4,])
# [1, 2, 3, 4, 5,]

#
# Uma observação importante é que a função sort() não retorna a lista
#
