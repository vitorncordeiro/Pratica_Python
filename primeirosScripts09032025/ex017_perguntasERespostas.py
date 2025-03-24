listasPerguntas = [
    {
        'Pergunta': 'Quanto é 2+2? ',
        'Opcoes': ['1', '2', '3', '4'],
        'Resposta': '4'
    },
    {
        'Pergunta': 'Quanto é 5x5? ',
        'Opcoes': ['25', '3', '10', '125'],
        'Resposta': '25',
    },
    {
        'Pergunta': 'Qual o valor aproximado de π? ',
        'Opcoes': ['2,4', '3,14', '1,77', '3,33'],
        'Resposta' : '3,14',
    }
]
def perguntar(pergunta):
    acertos = 0
    print(listasPerguntas[pergunta]['Pergunta'])
    opcoesFormatadas = listasPerguntas[pergunta]['Opcoes']
    print(opcoesFormatadas)
    respostaUser = input('Digite sua resposta: ')
    if respostaUser == listasPerguntas[pergunta]['Resposta']:
        print('Acertou')
        acertos += 1
    else:
        print('Errou')
contador = 0
for i in listasPerguntas:
    perguntar(contador)
    contador = contador + 1
    