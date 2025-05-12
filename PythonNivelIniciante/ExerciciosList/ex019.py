sistemasEVotos = [["Windows Server", 0], ["Unix", 0], ["Linux", 0], ["Netware", 0],\
                     ["Mac OS", 0], ["Outro", 0]]
contadorDeVotos = 0
while True:
    
    numeroEscolhido = input('"Qual o melhor Sistema Operacional para uso em servidores?"\n\
    As possíveis respostas são:\n\
    1- Windows Server\n\
    2- Unix\n\
    3- Linux\n\
    4- Netware\n\
    5- Mac OS\n\
    6- Outro\n')
    if numeroEscolhido.isnumeric() == False:
        print('Informe um número ')
    else:
        numeroEscolhido = int(numeroEscolhido)
        if numeroEscolhido > 6 or numeroEscolhido < 0:
            print("Informe um valor entre 1 e 6 ou 0 para sair!")
            continue
    if numeroEscolhido == 0:
        print(f'\nResultado da votação:')
        break

    sistemasEVotos[numeroEscolhido - 1][1] += 1 #somando 1 ponto pro sistema votado
    contadorDeVotos += 1

    
sistemasVotados = []
for parValores in sistemasEVotos:
    if parValores[1] > 0:
        sistemasVotados.append(parValores)
sistemasVotados.sort(reverse=True, key=lambda a: a[1])
msgFormatada = f"Foram computados {contadorDeVotos} votos.\n\nSistema Operacional:          Votos:        %"

def calcularPercentual(nvotos, TotalVotos):
    resultado = nvotos/TotalVotos*100
    return resultado
for sistema in sistemasVotados:
    msgFormatada = msgFormatada + f"\n{sistema[0]}          {sistema[1]}        {calcularPercentual(sistema[1], contadorDeVotos):.2f}"
sistemaMaisVotado = max(sistemasVotados, key=lambda a: a[1])    
msgFinal = f"{msgFormatada}\nTotal          {contadorDeVotos}\nO Sistema Operacional mais votado foi o {sistemaMaisVotado[0]}, com "\
        f"{sistemaMaisVotado[1]} votos, correspondendo a {calcularPercentual(sistemaMaisVotado[1], contadorDeVotos):.2f}% do total de votos"
print(msgFinal)


