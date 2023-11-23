import math

variavel1 = input("Qual é seu nome? ")
print(variavel1)
print(len(variavel1))

if variavel1 == 'Victor':
    print(f'Olá {variavel1}, seja bem vindo!')
    humor = input("Como você está hoje? ")
    if humor == 'Bem':
        print('Fico feliz em saber disso!')
    else:
        print('Não se preocupe, vai melhorar!')

    tempo = input('Como está o clima hoje? ')
    if tempo == 'Ensolarado' and humor == 'Bem':
        print('Que ótimo!')
    else:
        print('Vai melhorar!')
else:
    print('Desculpa, não te conheço!')


nome = input('Qual o seu nome? ')
if nome == 'Roberto':
    print(f'Seu nome é {nome}')
elif nome == 'Victor':
    print(f'Bem vindo, {nome}')
elif nome == 'Sofia':
    print(f'Bem vinda, {nome}')
elif nome == 'Henrique':
    print(f'Bem vindo, {nome}')
else:
    print('Ok... até mais!')


nome = input('Qual o seu nome? ')
match nome:
    case 'Roberto':
        print(f'Seu nome é {nome}')
    case 'Victor':
        print(f'Bem vindo, {nome}')
    case 'Sofia':
        print(f'Bem vinda, {nome}')
    case 'Henrique':
        print(f'Bem vindo, {nome}')
    case _:
        print('Ok... até mais!')


idade = input("Quantos anos vc tem? ")
print(idade)
print(type(idade))

idade_futura = int(idade) + 10

for x in idade:
    print(x)

a = int(input("Qual o número? "))
a = a + 10

b = a ** 2
print(a)

b = math.sqrt(a)

p = math.pi

opcao = 0
while opcao != 9:
    print("1 - cadastro")
    print("2 - alterar")
    print("3 - exclucir")
    print("9 - sair")
    opcao = int(input("Informe a opção desejada"))
