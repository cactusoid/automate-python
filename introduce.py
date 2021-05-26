'''def introduce(title, names):
    message = f'{title}: '
    for index, name in enumerate(names):
        if index > 0:
            message += ', '
        if index == len(names) - 1:
            message += 'и '
        message += name
    print(message)


introduce('Три балбеса', ['Мо', 'Ларри', 'Шемп'])
introduce('Три балбеса', ['Ларри', 'Керли', 'Мо'])
introduce('Черепашки-Ниндзя', ['Донателло', 'Рафаэль', 'Микеланджело', 'Леонардо'])
introduce('Бурундуки', ['Элвин', 'Саймон', 'Теодор'])'''



def join_names(names):
    name_string = ''
    for index, name in enumerate(names):
        if index > 0:
            name_string += ', '
        if index == len(names) - 1:
            name_string += 'и '
        name_string += name
    return name_string

def introduce(title, names):
    print(f'{title}: {join_names(names)}')

introduce('Три балбеса', ['Мо', 'Ларри', 'Шемп'])
introduce('Три балбеса', ['Ларри', 'Керли', 'Мо'])
introduce('Черепашки-Ниндзя', ['Донателло', 'Рафаэль', 'Микеланджело', 'Леонардо'])
introduce('Бурундуки', ['Элвин', 'Саймон', 'Теодор'])
