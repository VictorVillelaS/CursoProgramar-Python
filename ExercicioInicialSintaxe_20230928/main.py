#perguntar nome, como está
#perguntar idade, multiplicar por inteiro e elevar ao quadrado
#casos dando oi pras pessoas
#laço for e laço while

import math

nome = input('Qual o seu nome? ')
if nome == 'Victor':
    humor = input(f'Bem vindo {nome},Como você está hoje?')
    if humor == 'Bem':
        print('Fico feliz em saber disso!')
    else:
        print('Não se preocupe, vai melhorar!')
else:
    print('Desculpe, não te conheço!')


idade = int(input('Qual é a sua idade?'))

a_str = str(idade)

for a in a_str:
    print(a)

print(type(idade))

a = idade + 10
print(a)

b = idade ** 2
print(b)

c = math.sqrt(b)
print(c)


nome = input('Qual é o seu nome? ')
match nome:
    case 'Victor':
        print('Bom dia Victor')
    case 'Roberto':
        print('Bom dia Roberto')
    case 'Sofia':
        print('Bom dia Sofia')
    case _:
        print('Não te conheço!')


opcao = 1
while opcao != 9:
    print('Opção 1: Menu')
    print('Opção 2: Criar documento')
    print('Opção 3: Alterar registro')
    print('Opção 9: Sair')
    opcao = int(input('Digite uma opção: '))