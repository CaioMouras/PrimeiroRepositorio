# Escreva um programa que leia o número de um funcionário, seu número de horas trabalhadas, o valor que recebe por hora e calcula o salário desse funcionário. A seguir, mostre o número e o salário do funcionário, com duas casas decimais.

# O arquivo de entrada contém 2 números inteiros e 1 número com duas casas decimais, representando o número, quantidade de horas trabalhadas e o valor que o funcionário recebe por hora trabalhada, respectivamente.

# Imprima o número e o salário do funcionário, conforme exemplo fornecido, com um espaço em branco antes e depois da igualdade. No caso do salário, também deve haver um espaço em branco após o $.

# -*- coding: utf-8 -*-

# Leitura da entrada
numero = int(input())
horas_trabalhadas = int(input())
valor_por_hora = float(input())

# Cálculo do salário
salario = horas_trabalhadas * valor_por_hora

# Saída formatada conforme o exemplo
print(f"NUMBER = {numero}")
print(f"SALARY = U$ {salario:.2f}")
