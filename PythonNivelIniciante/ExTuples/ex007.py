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
    valorPConversao = int(input("Valor a ser convertido: "))
    unidadeOrigem = (input("Converter de: "))
    unidadeDestino = (input("Converter para: "))
    valorConvertido = 0

    conversaoPraAl = ano_luz[unidadeOrigem] * ano_luz["al"] * valorPConversao
    valorConvertido = conversaoPraAl * ano_luz[unidadeDestino] 
    print(f"Conversão de {valorPConversao} {unidadeOrigem} = {valorConvertido} {unidadeDestino}")
