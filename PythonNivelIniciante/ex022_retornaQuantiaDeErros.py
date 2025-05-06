#In a factory a printer prints labels for boxes. For one kind of boxes the printer has to use colors which, for the sake of simplicity, are named with letters from a to m.

def printer_error(s):
    erros = 0
    permitidos = list('abcdefghijklm')
    for i in s:
        if i not in permitidos:
            erros += 1
    return f'{erros}/{len(s)}'
print(printer_error('adasjdwqkseazz'))