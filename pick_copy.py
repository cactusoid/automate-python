# ! python3
# pick_copy.py - выборочное копирование

# TODO: Напишите программу, выполняющую обход дерева каталога с целью
#       отбора файлов с заданным расширением (например .pdf).
#       Скопируйте эти файлы из их текущего расположения в новую папку.

import shutil, os


for root, dirs, files in os.walk("/home/dio"):
    for file in files:
        if file.endswith(".pdf"):
            # print(os.path.join(root, file))
            shutil.copy(os.path.join(root, file), '/home/dio/pdf')

            


