names = ['Ларри', 'Керли', 'Мо']
message = 'Три балбеса: '

for index, name in enumerate(names):
    if index > 0:
        message += ', '
    if index == len(names) - 1:
        message += 'и '
    message += name
print(message)



def introduce_stooges(names):
    message = 'Три балбеса: '
    for index, name in enumerate(names):
        if index > 0:
            message += ', '
        if index == len(names) - 1:
            message += 'и '
        message += name
    print(message)

introduce_stooges(['Мо', 'Ларри', 'Шемп'])
introduce_stooges(['Ларри', 'Керли', 'Мо'])