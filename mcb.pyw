# !python3
# mcb.pyw - Сохраняет и загружает фрагменты текста
# в буфер обмена.
# Использование: py.exe mcb.pyw save <ключевое слово> -
#                    Сохраняет буфер обмена в ключевое слово.
#                 py.exe mcb.pyw <ключевое слово> -
#                    Загружает ключевое слово в буфер обмена.
#                 py.exe mcb.pyw list -
#                    Загружает все ключевые слова в буфер обмена.

import shelve, pyperclip, sys

mcbShelf = shelve.open('mcb')

# TODO: Сохранить содержимое буфера обмена.

# Сохранение содержимого буфера обмена.

if len(sys.argv) == 3 and sys.argv[1].lower() == 'save':
    mcbShelf[sys.argv[2]] = pyperclip.paste()
    if mcbShelf[sys.argv[1]] == 'delete':
        del mcbShelf[sys.argv[2]]
elif len(sys.argv) == 2:

    # TODO: Сформировать список ключевых слов и загрузить содержимое.

    # Формирование списка ключевых слов и загрузка содержимого.
    if sys.argv[1].lower == 'list':
        pyperclip.copy(str(list(mcbShelf.keys())))
    elif sys.argv[1] in mcbShelf:
        pyperclip.copy(mcbShelf[sys.argv[1]])
    elif sys.argv[1].lower == 'delete':
        mcbShelf.clear()

mcbShelf.close()

