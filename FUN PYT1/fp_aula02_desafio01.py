#Autor: Eduarda Martins
#

"""
A empresa |ABC dejesa melhorar seu consumo com os carros.
A empresa deseja inicialmente analisar o desempenho dos carros.

A empresa precisa saber se compensa abastecer com etanol ou gasolina 
dados devem ser apresentados da seguinte forma: 
nome da empresa_carro_combustível_consumo
formatados com 2 casas decimais
gasolina: R$ 6,69 o litro
Etanol: R$ 4,61 o litro
"""
nome_da_empresa = input('Digite o nome da empresa')
veiculo = input ('digite o nome do seu veículo')
gasolina = 6.69
etanol = 4.61 
valor = float (etanol / gasolina) 
print(f"Compensa mais: {round(valor):.2f}")



distancia = float(input('Digite sua distancia'))
litros = float(input('Digite os litros que foi gastado'))
consumo = float(distancia / litros)
print(round(consumo, 2))