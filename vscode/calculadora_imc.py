nome = 'Karimy Alves'
altura = 1.65
peso = 67
imc = peso / (altura * altura)

print(nome,'tem',altura,'de altura, pesa',peso,'quilos e seu IMC é',imc)

# Ou 'F' de formatação

print(f'{nome} tem {altura:.2f} de altura, pesa {peso} quilos e sei IMC é {imc:.2f}')

nome = "Luiz"
idade = 23
formato = '{1} tem {0} anos'
print(formato.format(nome, idade))

#ou

nome = "Luiz"
idade = 23
formato = '{n} tem {i} anos'
print(formato.format(n=nome, i=idade))

##

numero_1 = 10
numero_2 = 20
resultado = numero_1 * numero_2
print(resultado)
