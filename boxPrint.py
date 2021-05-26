def boxPrint(symbol, width, height):
    if len(symbol) != 1:
        raise Exception('Переменная symbol должна быть односимвольной строкой.')
    if width <= 2:
        raise Exception('Значение width должно превышать 2.')
    if height <= 2:
        raise Exception('Значение height должно превышать 2.')
    print(symbol * width)
    for i in range(height - 2):
        print(symbol + (' ' * (width - 2)) + symbol)
    print(symbol * width)

for sym, w, h in (('*', 4, 4), ('O', 20, 5), ('x', 1, 3), ('ZZ', 3, 3)):
    try:
        boxPrint(sym, w, h)
    except Exception as err:
        print('Возникло исключение: ' + str(err))
