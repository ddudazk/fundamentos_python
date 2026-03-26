# Autor: Eduarda Martins 
# Projeto Estrutura Condicional

nota1 = float(input('Digite a nota primeira do aluno: '))
nota2 = float(input('Digite a nota segunda do aluno: '))
nota3 = float(input('Digite a nota terceira do aluno: '))
nota4 = float(input('Digite a nota quarta do aluno: '))
media = (nota1 + nota2 + nota3 + nota4) / 4

if media >=5: 
    print(f'Aluno aprovado! {media:.2f} MUITO BEM O(∩_∩)O')
else: 
    print(f'Aluno reprovado! {media:.2f} tudo pode melhorar, não desista (っ °Д °;)っ')
