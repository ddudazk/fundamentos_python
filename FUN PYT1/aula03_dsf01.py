#Auotr: Eduarda Martins

peso = float(input('Digite seu peso em IMC: '))
altura = float(input('Digite sua altura em (m): '))
imc = 18,5

if imc <= 18.5: 
    print(f'Classificação: Magreza')

elif imc <= 25: 
    print(f'Classificação: Peso normal')

elif imc<=30:
    print('Classificação: Sobrepeso')
else:
    print('Classificação: obesidade')