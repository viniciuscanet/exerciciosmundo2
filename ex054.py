from datetime import date
atual = date.today().year
totmaior = 0
totmenor = 0
for pessoas in range (1, 8):
    ano = int(input('Em que ano a {}ª Pessoa nasceu? '.format(pessoas)))
    idade = atual - ano
    if idade >= 21:
        totmaior = totmaior + 1
    else:
        totmenor = totmenor + 1
print('Ao todo tivemos {} maiores e {} menores'.format(totmaior, totmenor))



