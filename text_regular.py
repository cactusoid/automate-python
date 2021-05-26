# !python3
# text_regular.py - Напишите программу, которая открывает все файлы с расширением .txt,
# находящиеся в папке, и выполняет поиск строк, соответствующих предоставленному
# пользователем регулярному выражению. Результаты должны выводиться на экран.

import pathlib

directory = r''
file = r'*.txt'
tag = r'Arizona'

for path in pathlib.Path(directory).rglob(file):
    with open(path) as f:
        lines = f.readlines()
        for i in range(len(lines)):
            if tag in lines[i]:
                print(f'Путь: {path}\nСтроки:')
                if i == 0:
                    print(lines[0])
                elif i == 1:
                    print(*lines[:2], sep='')
                else:
                    print(*lines[i:i+1], sep='')