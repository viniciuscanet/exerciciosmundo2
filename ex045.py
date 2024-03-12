from random import randint
itens = ('Pedra', 'Papel', 'Tesoura')
computador = (randint(0, 2))
print('''Suas opções:
[ 0 ] Pedra
[ 1 ] Papel
[ 2 ] Tesoura''')
jogador = int(input('Qual é sua jogada? '))
print('-=' * 14)
print('O computador escolheu {}'.format(itens[computador]))
print('Jogador escolheu {}'.format(itens[jogador]))
print('-=' * 14)

if computador == 0

elif computador == 1

elif computador == 2