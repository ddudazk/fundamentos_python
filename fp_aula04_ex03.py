cnh = input('Você tem cnh?')
teste_bafometro = float(input('quanto deu o teste de bafometro?: '))

if cnh == 'sim' and teste_bafometro < 0.34:
    print('acesso liberado')
else:
    print('acesso negado')