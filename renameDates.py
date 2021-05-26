# ! python3
# renameDates.py - Переименовывает файлы, имена которых включают
# даты, указанные в американском формате (ММ-ДД-ГГГГ), приводя
# их в соответствие с европейским форматом дат (ДД-ММ-ГГГГ).

import shutil, os, re

# Создание регулярного выражения, которому соответствуют имена
# файлов, содержащие даты в американском формате.

datePattern = re.compile(r"""^(.*?)  # весь текст перед датой
    ((0|1)?\d)-                      # одна или две цифры месяца
    ((0|1|2|3)?\d)-                  # одна или две цифры числа
    ((19|20)\d\d)                    # четыре цифры года
    (.*?)$                           # весь текст после даты
    """, re.VERBOSE)

# TODO: Организовать цикл по файлам в рабочем каталоге.

# Организация цикла по файлам в рабочем каталоге.

for amerFilename in os.listdir('.'):
    mo = datePattern.search(amerFilename)

# TODO: Пропустить файлы с именами, не содержащими дат.

# Пропуск файлов с именами, не содержащими дат.

    if mo == None:
        continue

# TODO: Получить отдельные части имен файлов.

# Получение отдельных частей имен файлов.

    beforePart = mo.group(1)
    monthPart = mo.group(2)
    dayPart = mo.group(4)
    yearPart = mo.group(6)
    afterPart = mo.group(8)

# TODO: Сформировать имена, соответствующие европейскому стилю
#       указания дат.

# Формирование имен, соответствующих европейскому стилю
# указания дат.

    euroFilename = beforePart + dayPart + '-' + monthPart + '-' + yearPart + afterPart

# TODO: Получить полные абсолютные пути к файлам.

# Получение полных абсолютных путей к файлам.

    absWorkingDir = os.path.abspath('.')
    amerFilename = os.path.join(absWorkingDir, amerFilename)
    euroFilename = os.path.join(absWorkingDir, euroFilename)

# TODO: Переименовать файлы.

# Переименование файлов.

    print('Заменяем имя "%s" именем "%s"...' % (amerFilename,euroFilename))
# shutil.move(amerFilename,euroFilename)   # раскомментировать
                                           # после выполнения
                                           # тестирования

