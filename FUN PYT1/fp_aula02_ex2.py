#Autor: Eduarda Martins
# Projeto f-string | round

pi = 3.14159265

# ultilizando o f-strings 
print("Olá, mundo")
print()
print('Meu nome é \nEduarda Martins')

print(f"O valor de pi é: {pi:.2f}")
print(f"O valor de pi é: {pi:.3f}")
print(f"O valor de pi é: {pi:.4f}")
print(40 * '-' )
pi = round(pi, 4)
print(f"O valor de pi é: {round(pi, 2)}")
print(f"O valor de pi é: {round(pi, 3)}")
print(f"O valor de pi é: {round(pi, 4)}")
