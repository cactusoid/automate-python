# ! python3
# pass_num.py - Напишите программу, которая ищет в папке все файлы с именами,
# содержащими заданный префикс, такими как spam001.txt, spam002.txt и т.д.,
# и обнаруживает любые пропуски в нумерации файлов. 
# Программа должна изменять имена файлов с большими номерами таким образом,
# чтобы ликвидировать имеющие пропуски.

import os, shutil

folder = os.chdir('/home/dio/txt')
files = [filename for filename in os.listdir(folder) if filename.startswith('capitalsquiz')]
numbers = [int(filename.lstrip('capitalsquiz').rstrip('.txt')) for filename in files]
newfilenames = ['capitalsquiz{:0>3}.txt'.format(number+1) for number in range(len(files))]
print(newfilenames)
for oldname, newname in zip(files, newfilenames):
    shutil.copy(oldname, newname)
    os.unlink(oldname)

