"""Em uma competição de salto em distância cada atleta tem direito a cinco saltos. 
O resultado do atleta será determinado pela média dos cinco valores restantes.
Você deve fazer um programa que receba o nome e as cinco distâncias alcançadas pelo
atleta em seus saltos e depois informe o nome, os saltos e a média dos saltos.
O programa deve ser encerrado quando não for informado o nome do atleta.
A saída do programa deve ser conforme o exemplo abaixo:
Atleta: Rodrigo Curvêllo
Primeiro Salto: 6.5 m
Segundo Salto: 6.1 m
Terceiro Salto: 6.2 m
Quarto Salto: 5.4 m
Quinto Salto: 5.3 m
Resultado final:
Atleta: Rodrigo Curvêllo
Saltos: 6.5 - 6.1 - 6.2 - 5.4 - 5.3
Média dos saltos: 5.9 m"""
while True:
    nome_atleta = input('Digite o nome do atleta: ')
    if nome_atleta == "":
        print('Finalizando programa...')
        break
    saltos = []
    for i in range(5):
        salto = float(input(f'Informe a distância do salto nº{i+1}: '))
        saltos.append(salto)
    mediaSaltos = sum(saltos) / 5
    mensagemFormatada = f"Atleta: {nome_atleta}\nPrimero Salto: {saltos[0]}"\
                        f"\nSegundo Salto: {saltos[1]} m"\
                        f"\nTerceiro Salto: {saltos[2]} m"\
                        f"\nQuarto Salto: {saltos[3]} m"\
                        f"\nQuinto Salto: {saltos[4]} m"\
                        f"\nResultado final:"\
                        f"\nAtleta: {nome_atleta}"\
                        f"\nSaltos: {saltos[0]} m - {saltos[1]} m - {saltos[2]} m - {saltos[3]} m - {saltos[4]} m"\
                        f"\nMédia dos saltos: {mediaSaltos:.2f} m\n"
    print(mensagemFormatada)


    