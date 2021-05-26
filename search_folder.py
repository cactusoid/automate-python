# !python3
# search_folder.py - Пример программы для обхода дерева каталогов с помощью функции os.walk()

import os

for folderName, subfolders, filenames in os.walk('/home/dio/Документы'):
    print('Текущая папка - ' + folderName)

    for subfolder in subfolders:
        print('ПОДПАПКА ПАПКИ ' + folderName + ': ' + subfolder)

    for filename in filenames:
        print('ФАЙЛ В ПАПКЕ ' + folderName + ': ' + filename)
    print('')
