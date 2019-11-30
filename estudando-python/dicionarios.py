# coding: UTF-8

#
# Criando dicionários
#

people = people = {
    'name': 'joao',
    'age': 39,
    'skylls': ['python', 'ruby', 'php']
}


#
# Acessando os dados
#

print(people['name'])
print(people['age'])
print(people['skylls'])

#
# Funções para dicionários
#

my_dict = {'1': 'a', '2': 'b', '3': 'c',}

my_dict.items()   # dict_items([('1', 'a'), ('3', 'c'), ('2', 'b')])
my_dict.keys()    # dict_keys(['1', '3', '2'])
my_dict.values()  # dict_values(['a', 'c', 'b'])
