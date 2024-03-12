print('Os numetros pares entre 1 e 50 são:')
for c in range (2, 51, 2):
    print('.', end='')
    if c % 2 == 0:
        print(c, end=' ')
print('Acabou')