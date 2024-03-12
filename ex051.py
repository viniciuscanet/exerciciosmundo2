#soma dos 10 termos de uma PA
n1 = int(input('Digire o primeiro termo da PA: '))
r = int(input('Digite a razão: '))
for c in range (0, 10):
    print('{}'.format(n1 + r*c))