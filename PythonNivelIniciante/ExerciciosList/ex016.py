"""Utilize uma lista para resolver o problema a seguir. Uma empresa paga seus vendedores 
com base em comissões. O vendedor recebe $200 por semana mais 9 por cento de suas vendas
brutas daquela semana. Por exemplo, um vendedor que teve vendas brutas de $3000 em uma 
semana recebe $200 mais 9 por cento de $3000, ou seja, um total de $470. 
Escreva um programa (usando um array de contadores) que determine quantos vendedores
receberam salários nos seguintes intervalos de valores:
a. $200 - $299
b. $300 - $399
c. $400 - $499
d. $500 - $599
e. $600 - $699
f. $700 - $799
g. $800 - $899
h. $900 - $999
i. $1000 em diante"""
VALOR_SEMANAL = 200
TAXA_ADICIONAL = 0.09
#Lista com vendedores e o valor bruto de vendas na semana
vendedores = [['Vendedor 1', 3000], ["Vendedor 2", 2000], ["Vendedor 3", 1000], ["Vendedor 4", 1000], \
              ["Vendedor 5", 2000], ["Vendedor 6", 5500], ["Vendedor 7", 4500], ["Vendedor 8", 2300], \
              ["Vendedor 9", 3700]]
listaIntervalos = [["a"], ["b"], ["c"], ["d"], ["e"], ["f"], ["g"], ["h"], ["i"]]
for vendedor in vendedores:
    salario = VALOR_SEMANAL + (TAXA_ADICIONAL * vendedor[1])
    if salario <= 299:
        listaIntervalos[0].append(f"{salario:.2f}")
    elif salario >= 300 and salario <= 399:
        listaIntervalos[1].append(f"{salario:.2f}")
    elif salario>= 400 and salario <= 499:
        listaIntervalos[2].append(f"{salario:.2f}")
    elif salario >= 500 and salario <= 599:
        listaIntervalos[3].append(f"{salario:.2f}")
    elif salario >= 600 and salario <= 699:
        listaIntervalos[4].append(f"{salario:.2f}")
    elif salario >= 700 and salario <= 799:
        listaIntervalos[5].append(f"{salario:.2f}")
    elif salario >= 800 and salario <= 899:
        listaIntervalos[6].append(f"{salario:.2f}")
    elif salario >= 900 and salario <= 999:
        listaIntervalos[7].append(f"{salario:.2f}")
    else:
        listaIntervalos[8].append(f"{salario:.2f}")
print(*listaIntervalos)