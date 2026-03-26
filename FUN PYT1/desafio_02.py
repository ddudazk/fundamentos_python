#Autor: Eduarda Martins

largura = float(input('Digite largura do terreno: '))
comprimento = float(input('Digite comprimento do terreno: '))
area = (comprimento * largura)
print(f'Sua Área é {area}')

valor_02 = float(input('Digite o valor por metros quadrados: '))
valor_total = (area * valor_02)

print(f'O valor total do terreno é de {valor_total}')