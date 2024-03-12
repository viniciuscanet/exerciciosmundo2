peso = int(input('Digite o seu peso em quilogramas: '))
altura = float(input('Digite a sua altura em centímetros: '))

imc = (peso/((altura)**2))*10000

print('Seu IMC é: {:.2f}'.format(imc))

if imc > 40:
    print('Obesidade mórbida')
elif 30 <= imc < 40:
    print('Obesidade')
elif 25 <= imc < 30:
    print('Sobrepeso')
elif 18.5 <= imc < 25:
    print('Peso ideal')
else:
    print('Abaixo do peso')
