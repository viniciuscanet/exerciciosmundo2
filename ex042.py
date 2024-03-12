n1 = float(input('digite o primeiro tamanho: '))
n2 = float(input('digite o segundo tamanho: '))
n3 = float(input('digite o terceiro tamanho: '))

n1 = (n1**2)**(1/2)
n2 = (n2**2)**(1/2)
n3 = (n3**2)**(1/2)

print(n1)
print(n2)
print(n3)

if ((n2 - n1)**2)**(1/2) < n3 < (n2+n1):
    print('O seu triangulo é possivel e é: ')
    if n1 == n2 == n3:
        print('Equilátero!')
    elif n1 != n2 != n3 != n1:
        print('Escaleno')
    else:
        print('Isóceles')

else:
    print('O seu triangulo não é possivel!')