print("Dados da primeira pessoa")
nome1 = input("Primeiro Nome: ")
idade1 = int(input("Primeira Idade: "))

print("Dados da segunda pessoa")
nome2 = input("Segundo Nome: ")
idade2 = int(input("Segunda Idade: "))

media = (idade1 + idade2) / 2

print(f"A idade media entre {nome1} e {nome2} é de {media:.0f} anos.")
