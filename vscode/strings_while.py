'''
Iterando strings com while
'''
nome = 'Karimy Alves'
tamanho_nome = len(nome)
print(f'Seu nome é {nome}', end=' ')
print(f'e tem {tamanho_nome} letras seu nome.')

#   E

indice = 0
while indice < len(nome):
    print(nome[indice])
    indice += 1

#   OU

indice = 0
novo_nome = ''
while indice < len(nome):
    letra = nome[indice]
    novo_nome += f'*{letra}'
    indice += 1

novo_nome += '*'
print(novo_nome)
