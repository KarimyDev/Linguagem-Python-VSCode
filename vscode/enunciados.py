"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""

# Solicita que o usuário insira um número
try:
    numero = float(input("Digite um número: "))

    # Verifica se o número é inteiro
    if numero.is_integer():
        numero = int(numero)  # Converte para inteiro, já que sabemos que é
        # Verifica se o número é par ou ímpar
        if numero % 2 == 0:
            print(f"O número {numero} é inteiro e par.")
        else:
            print(f"O número {numero} é inteiro e ímpar.")
    else:
        print(f"O número {numero} não é um número inteiro.")
        
except ValueError:
    print("Você não digitou um número inteiro, tente novamente")

"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. Ex. 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""
# Solicita que o usuário insira a hora
try:
    hora = int(input("Por favor, informe a hora atual (0-23): "))

    # Verifica se a hora está dentro do intervalo válido
    if 0 <= hora <= 23:
        # Exibe a saudação apropriada com base na hora
        if 0 <= hora <= 11:
            print("Bom dia!")
        elif 12 <= hora <= 17:
            print("Boa tarde!")
        else:
            print("Boa noite!")
    else:
        print("Por favor, insira um valor entre 0 e 23.")

except ValueError:
    print("Entrada inválida. Por favor, insira um número inteiro para a hora.")

"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou 
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva 
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande". 
"""
# Solicita o primeiro nome do usuário
nome = input("Digite o seu primeiro nome: ")

# Verifica o tamanho do nome e exibe a mensagem apropriada
tamanho_nome = len(nome)

if tamanho_nome <= 4:
    print("Seu nome é curto.")
elif 5 <= tamanho_nome <= 6:
    print("Seu nome é normal.")
else:
    print("Seu nome é muito grande.")
