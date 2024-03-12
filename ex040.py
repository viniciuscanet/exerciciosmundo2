n1 = float(input('Digie a primeira nota: '))
n2 = float(input('Digie a segunda nota: '))
n3 = float(input('Digie a terceira nota: '))

media = (n1 + n2 + n3)/3
print('A média do estudante é {:.2f}'.format(media))
if media >= 7:
    print('O estudante está aprovado!')
elif media < 5:
    print('O estudante está reprovado!')
else:
    print('O estudante está de recuperação!')

