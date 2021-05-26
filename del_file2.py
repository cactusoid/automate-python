# ! python3
# del_file2.py - Напишите программу, которая обходит дерево папок,
# выполняя поиск исключительно больших по своим размерам папок и файлов (например 100 мб).
# Выведите абсолютные пути доступа к этим файлам на экран.

import os.path

for root, dirs, files in os.walk('/home/dio/Загрузки'):
    for file in files:
        if os.path.getsize(os.path.join(root, file)) >= 104857600:
            print(file)
            # os.unlink(file) # прежде чем выполнять эту команду, сначала проверьте с помощью print
