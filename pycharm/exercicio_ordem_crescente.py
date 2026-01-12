#ESTRUTURA DE REPETIÇÃO ENQUANTO.

print("Digite dois numeros")
x = int(input())
y = int(input())

while x != y:
    if x < y:
        print("Crescente")
    else:
        print("Decrescente")
    print("Digite outros dois numeros")
    x = int(input())
    y = int(input())
