# coding: UTF-8

#
# Converter listas em strings
#

list = ['primeiro', 'segundo', 'terceiro',]
', '.join(list)

'primeiro, segundo, terceito'


#
# Converter lista de inteiros separada por virgula
#

list = [10, 20, 30]
str(list)
'[10 , 20 , 30]'

#
# Retirar os colchetes
#

str(list).strip('[]')
'10, 20, 30'

# Ou assim

str(list)[1:-1]
'10, 20, 30'

#
# Transformar lista em strings separadas por traços (-)
#

'-'.join(map(str, list))
'10-20-30'
