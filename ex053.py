#palíndromo

frase = str(input('Digite uma frase: ')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = ''
for letra in range(len(junto) -1, -1, -1):
    inverso = inverso + junto[letra]
if inverso == junto:
    print('Temos um palindromo')
else:
    print('A frase nao é um palindromo')
