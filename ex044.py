valor = float(input('Digite o Valor de sua compra: R$ '))
print('''Escolha uma forma de pagamento:
[ 1 ] à vista dinhieiro/cheque
[ 2 ] à vista cartão
[ 3 ] 2x no cartão
[ 4 ] 3x ou mais no cartão''')

num = int(input('Qual a forma de pagamento? '))

if num == 1:
    print('Sua compra terá desconto de 10% e custará R$ {:.2f}'.format(valor*0.9))
elif num == 2:
    print('Sua compra terá desconto de 5% e custará R$ {:.2f}'.format(valor*0.95))
elif num == 3:
    print('Sua compra custará o preço normal de R$ {:.2f}'.format(valor))
elif num == 4:
    print('Sua compra terá juros de 20% e custará R$ {:.2f}'.format(valor*1.2))

else:
    print('Alternativa incorreta')

