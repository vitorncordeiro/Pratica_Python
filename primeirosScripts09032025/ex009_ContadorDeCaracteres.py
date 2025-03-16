frase = 'O python é uma linguagem programação multiparadigma. Python foi criado por Guido van Rossum'
x = 0
qual_letraApareceuMaisAteAgora = ""
i = 0
while i < len(frase):
    letraAtual = frase[i]

    if letraAtual == ' ': #checa se o caracter em questão é um espaço, se for, ele para o loop e não conta ele
        i += 1
        continue

    contagemLetraAtual = frase.count(letraAtual)
    if contagemLetraAtual > x: #checa se a contagem atual é maior do que a máxima registrada, se for, ele salva essa como a nova recordista, salvando a quantidade de vezes, e qual letra foi
        x = contagemLetraAtual
        qual_letraApareceuMaisAteAgora = letraAtual
    elif contagemLetraAtual == x and letraAtual not in qual_letraApareceuMaisAteAgora:  #confere se a quantidade de vezes que a letra atual apareceu é igual ao máximo que já apareceu, ou seja, se a letra em questão está empatando com outra, e ao mesmo checa se a letra não é repetida.
        qual_letraApareceuMaisAteAgora = qual_letraApareceuMaisAteAgora + ', ' + letraAtual #aqui ele só junta a letra anterior que já tinha o record de aparecimentos, com a nova letra que está empatando com ela.
    
    print(f'{letraAtual} -> {contagemLetraAtual}')
    print(f'{x}, {qual_letraApareceuMaisAteAgora}')
    i += 1
if len(qual_letraApareceuMaisAteAgora) == 1: #aqui é para caso só tenha 1 letra que apareceu mais vezes
    print(f'A letra que mais apareceu foi {qual_letraApareceuMaisAteAgora}, aparecendo {x} vezes')
else:#aqui é para caso de várias letras terem aparecido o mesmo tanto de vezes, o que muda é que a frase está no plural
    print(f' As letras que mais apareceram foram {qual_letraApareceuMaisAteAgora}, aparecendo {x} vezes')

