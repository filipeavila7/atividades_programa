#pedir o capital, taxa e tempo:
capital = float(input('digite um valor inicial:'))
taxa = float(input('digite a taxa:'))
tempo = float(input('digite o tempo:'))
#calcular o juros simples usando a formula J = CIT:
juros = capital * taxa * tempo
print(f'o juros simples é: {juros}')