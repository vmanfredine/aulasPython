# Operadores in e not in
# Strings são iteráveis
#  0 1 2 3 4
#  V i t o r
# -5-4-3-2-1

nome = 'Vitor'
print(nome[2])
print(nome[-3])
print ('t' in nome) # Verifica se 't' está entre as strings de nome
print ('z' in nome)
print ('z' not in nome) # Verifica se 'z' não está entre as strings de nome

nome_2 = input ('Digite seu nome: ')
encontrar = input('Digite o que deseja encontrar: ')

if encontrar in nome_2:
    print(f'{encontrar} está em {nome_2}')
else:
    print(f'{encontrar} não está em {nome_2}')