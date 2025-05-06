dia = int (input("Insira o dia de seu nascimento: "))
mês = int (input("Insira o mês de seu nascimento: "))
ano = int (input("Insira o ano de seu nascimento: "))

if type(mês) == int:
    match mês:
        case 1:
            mês = "janeiro"
        case 2:
            mês = "fevereiro"
        case 3:
            mês = "março"
        case 4:
            mês = "abril"
        case 5:
            mês = "maio"
        case 6:
            mês = "junho"
        case 7:
            mês = 'julho'
        case 8:
            mês ="agosto"
        case 9:
            mês = 'setembro'
        case 10:
            mês = "outubro"
        case 11:
            mês = "novembro"
        case 12:
            mês = "dezembro"

            
    

print(f'Você nasceu no dia {dia} de {mês} de {ano}')