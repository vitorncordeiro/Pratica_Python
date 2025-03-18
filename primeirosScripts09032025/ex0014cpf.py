cpfDoUsuario = '314316080'
listaCPF = list(cpfDoUsuario) #Transforma o string do cpf em uma lista, para ser manipulada
listaDigitosUmMultiplicados = []
listaDigitosDoisMultiplicados = []
somaDigitosUm = 0
somaDigitoDois = 0


multiplicadorRegressivoUm = 10
for item in listaCPF:
    itemUmFormatado = int(item) #transforma o item da lista, que é uma string, para um numero inteiro
    itemUmMultiplicado = itemUmFormatado * multiplicadorRegressivoUm #pega o digito que está na vez, multiplica pelo multiplicador regressivo
    multiplicadorRegressivoUm = multiplicadorRegressivoUm - 1 #subtrai 1 do multiplicador regressivo, para que ele de fato regrida para a próxima repetição
    listaDigitosUmMultiplicados.append(itemUmMultiplicado)#pega o resultado da multiplicação e joga numa nova lista
for digito in listaDigitosUmMultiplicados:
    somaDigitosUm = somaDigitosUm + digito #pega a nova lista com os itens já multiplicados e soma todos eles
DigitoUmFinal = (somaDigitosUm * 10) % 11 #pega a o resto da divisão por 11 da soma de todos os digitos multiplicados 
if DigitoUmFinal > 10: #se o quociente for maior que 10, ele vale 0 
    DigitoUmFinal = 0
listaCPF.append(DigitoUmFinal)
print(f'O primeiro digito do cpf é {DigitoUmFinal}')

#Segunda parte, vai literalmente repetir tudo que aconteceu acima, mas agora o cpf possui 10 digitos invés de 9, e o multiplicador regressivo começa em 11

multiplicadorRegressivoDois = 11
for j in listaCPF:
    itemDoisFormatado = int(j)
    itemDoisMultiplicado = itemDoisFormatado * multiplicadorRegressivoDois
    multiplicadorRegressivoDois = multiplicadorRegressivoDois - 1
    listaDigitosDoisMultiplicados.append(itemDoisMultiplicado)
for digitoDois in listaDigitosDoisMultiplicados:
    somaDigitoDois = somaDigitoDois + digitoDois
DigitoDoisFinal = (somaDigitoDois * 10) % 11
if DigitoDoisFinal > 10:
    DigitoDoisFinal = 0
print(f'O segundo digito do cpf é {DigitoDoisFinal}')



