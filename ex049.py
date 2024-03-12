#construindo uma tabuada

x = int(input('Digite no número que deseja saber a tabuada: '))
for n in range (1,166):
    print('{} X {} = {}'.format(n, x, (n*x)))
