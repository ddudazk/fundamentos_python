print(f"Olá, para começar precisamos de algumas informações basícas ヾ(•ω•`)o ")
idade = int(input('Informe sua idade: '))
credencial = input('Digite S ou N: ')


if idade >= 18 and credencial =='S':
    print(f'Otimo acesso liberado! O(∩_∩)O')
else: 
    print(f'Sinto muito acesso negado! (˘･_･˘)')