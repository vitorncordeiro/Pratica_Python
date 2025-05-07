"""Faça um programa que receba a temperatura média de cada mês do ano e 
armazene-as em uma lista. Após isto, calcule a média anual das temperaturas e 
mostre todas as temperaturas acima da média anual, e em que mês elas ocorreram 
(mostrar o mês por extenso: 1 – Janeiro, 2 – Fevereiro, . . . )."""
meses = [['Janeiro', None], ['Fevereiro', None], ['Março', None], ['Abril', None],\
         ['Maio', None], ['Junho', None], ['Julho', None], ['Agosto', None],
         ['Setembro', None], ['Outubro', None], ['Novembro', None], ['Dezembro', None]]
soma = 0
for i in range(len(meses)):
    temperatura = int(input(f'Qual foi a temperatura média de {meses[i][0]}: '))
    meses[i][1] = temperatura
    soma += temperatura
mediaAnual = soma / len(meses)
mesesAcimaDaMedia= []
for mes in meses:
    if mes[1] > mediaAnual:
        mesesAcimaDaMedia.append(mes)
print(*mesesAcimaDaMedia)


