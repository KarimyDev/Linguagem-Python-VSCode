frase = 'O Python é uma linguagem de programação '\
    'multiparadigma.' \
    'Python foi criado por Guido Van Rossum.'

# print(frase.count('Python'))

i = 0
qtd_apareceu_mais_vezes = 0
letra_apareceu_mais_vezes = ''

while i < len(frase):
    letra_atual = frase[i]

    if letra_atual == ' ':
        i += 1
        continue

    qt_vezes_apareceu = frase.count(letra_atual)

    if qtd_apareceu_mais_vezes < qt_vezes_apareceu:
        qtd_apareceu_mais_vezes = qt_vezes_apareceu
        letra_apareceu_mais_vezes = letra_atual
    
    i += 1

print('A letra que apareceu mais vezes foi '
      f'"{letra_apareceu_mais_vezes}" que apareceu '
      f'{qtd_apareceu_mais_vezes}x')
