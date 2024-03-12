salario = float(input('Digite o seu salário: '))
casa = float(input('Digite o valor da casa que queres comprar: '))
vezes = int(input('Em quantos anos você deseja parcelar esse valor?'))

prestacao = casa/(vezes*12)

if prestacao <= 0.30 * salario:
    print('A prestação da sua casa é: R$ {:.2f} mensais e você poderá financiar essa casa'.format(prestacao))
else:
    print('A prestação da sua casa é: R$ {:.2f} mensais e você não poderá financiar essa casa'.format(prestacao))
    print('Tente financiá-la em mais anos!')