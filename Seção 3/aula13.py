# Formatação de strings: f-strings
# :.2f limita número de casas decimais
# f' texto {variavel} texto'

nome = 'Vitor Manfredine'
altura = 1.72
peso = 67
imc = peso / altura ** 2

linha_1 = f'{nome} tem {altura:.2f} de altura'
linha_2 = f'Pesa {peso} quilos e seu imc é: {imc:.2f}'

print(linha_1)
print(linha_2)