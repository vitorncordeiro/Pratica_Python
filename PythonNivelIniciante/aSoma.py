listaDeNúmerosASomar = []
quantidadeDeNumerosPSomar = int (input ('Quantos números você deseja somar?: '))
for x in range(quantidadeDeNumerosPSomar):
    if x == 0:
        soma = int(input('Digite o primeiro número: '))
    elif x == quantidadeDeNumerosPSomar - 1:
        soma = int(input('Digite o último número: '))
    else:
        soma = int(input("Digite o próximo número: "))        

    listaDeNúmerosASomar.append(soma)
print(f"A soma dos números inseridos é: {sum(listaDeNúmerosASomar)}")

