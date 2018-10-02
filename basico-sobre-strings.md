# Podemos acessar uma string pelo seu index

'python'[0] # 'p'
'python'[5] # 'n'



# Fatiando uma string

palavra = 'isaac'

palavra[1:4] # 'saac'



# len() mostra o tamanho da string

palavra = 'foo'

len(palavra) # 3


# Metodo isalpha()
# Retorne False se a string contiver algum caracterer que não seja letras

'abc'.isalpha() # True
'1fg'.isalpha() # False


# Metodo strip()
# Retira espaços em branco no começo e nom fim

' sobrando espaços '.strip() # 'sobrando espaços'


# Metodo join()
# Junta cada item de uma string com um delimtador especificado

', '.joint('abc') # 'a, b, c'

# Metodo .slpit()
# Separa uma string conforme um limitador

palavra = 'n o m e'
palavra.split() # ['n', 'o', 'm', 'e']

