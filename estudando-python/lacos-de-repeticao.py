# coding UTF-8

#
# for
#

#
# Para percorrer sequências previamente conhecidas
#

lista = ['p','y','t','h','o','n',]

for item in lista:
    print(item)

"""
p
y
t
h
o
n

"""

#
# Se for necessário um indice numérico, posso utilizar o enumerate
#

for key, value in enumerate(["p", "y", "t", "h", "o", "n"]):
    print(key, value)

"""
0 p
1 y
2 t
3 h
4 o
5 n

"""

#
# Utilizando laço for com a função range()
#

for i in range(5):
    print(i)

"""
0
1
2
3
4

"""

#
# while
#

count = 0
while count <= 5:
    print(count)
    count += 1


# 0 1 2 3 4 5


#
# Utilizando o break
#

count = 0
while count <= 5:
    print(count)
    count += 1
    if count > 3: break


#
# Utilizando for-else 
#

for i in range(5):
    print(i)
else:
    print('após iteração')


#
# Utilizando o while-else
#

count = 0
while count <= 5:
    print(count)
    count += 1
else:
    print('após iteração')
