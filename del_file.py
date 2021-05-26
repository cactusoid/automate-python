# !python3
# del_file.py - Удаление файлов с расширением .txt


import os
for filename in os.listdir():
    if filename.endswith('.txt'):
        # os.unlink(filename) # прежде чем выполнять эту команду, сначала проверьте с помощью print
        print(filename)