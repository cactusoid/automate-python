spam = ['apples', 'bananas', 'tofu', 'cats']


def introduce_stooges(names):
    message = ''
    for index, name in enumerate(names):
        if index > 0:
            message += ', '
        if index == len(names) - 1:
            message += 'and '
        message += name
    print(message)

introduce_stooges(spam)