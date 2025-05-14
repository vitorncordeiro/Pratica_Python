ano_luz = {
"pc": 0.31,
"al": 1,
"ae": 63241.09,
"ml": 525960.23,
"sl": 31557609.92
}
unidades = ["Parsec (pc)", "Ano-Luz (al)", "Unidade Astronômica (ae)", "Minuto-Luz\
(ml)", "Segundo-Luz (sl)"]
while True:
    print('--------------')
    for unidades in ano_luz:
        print(unidades) 
    print('--------------')
    valorPConversao = float(input("Valor a ser convertido: "))
    unidadeOrigem = (input("Converter de: "))
    unidadeDestino = (input("Converter para: "))


    X =( ano_luz[unidadeDestino] * valorPConversao)/ ano_luz[unidadeOrigem]
    print(f"Conversão de {valorPConversao} {unidadeOrigem} = {X} {unidadeDestino}")