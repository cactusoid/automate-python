# ! python3
# backupToZip.py - Копирует папку вместе со всем её содержимым
# в ZIP-файл с инкрементируемым номером копии в имени файла.

import zipfile, os

def backupToZip(folder):
    # Создание резервной копии всего содержимого папки "folder"
    # в виде ZIP-файла.

    folder = os.path.abspath(folder)  # убедиться в том, что
                                      # задан абсолютный путь
                                      # к файлу
    # Определить, какое имя файла должен использовать этот код,
    # исходя из имен уже существующих файлов.

    number = 1
    while True:
        zipFilename = os.path.basename(folder) + '_' + str(number) + '.zip'
        os.chdir('/home/dio/test')
        if not os.path.exists(zipFilename):
            break
        number = number + 1

    # TODO: Создать ZIP-файл.
    # Создание ZIP-файла.

    print('Создаётся файл %s...' % (zipFilename))
    os.chdir('/home/dio/test')
    backupZip = zipfile.ZipFile(zipFilename, 'w')

    # TODO: Обойти все дерево папки и сжать файлы, содержащиеся
    #       в каждой папке.
    
    # Обход всего дерева папки и сжатие файлов, содержащихся
    # в каждой папке.

    for foldername, subfolders, filenames in os.walk(folder):
        print('Добавление файлов из папки %s...' % (foldername))

        # Добавить в ZIP-файл все файлы из папки.
        for filename in filenames:
            newBase = os.path.basename(folder) + '_'
            if filename.startswith(newBase) and filename.endswith('.zip'):
                continue # не создавать резервные копии
                         # ZIP-файлов

            backupZip.write(os.path.join(foldername, filename))
    backupZip.close()
    print('Готово')

backupToZip('/home/dio/Документы/python')
