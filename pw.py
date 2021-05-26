# ! python3
# pw.py - Программа для незащищенного хранения паролей.

PASSWORDS = {'email': 'F7minlBDDuvMJuxESSKHFhTxFtjVB6',
             'blog': 'VmALvQyKAxiVH5G8v01MLZF3sdt',
             'luggage': '12345'}

import sys, pyperclip
if len(sys.argv) < 2:
    print('Использование: python pw.py [имя учётной записи] - копирование пароля учётной записи')
    sys.exit()

account = sys.argv[1] # первый аргумент командной строки - это имя учётной записи

if account in PASSWORDS:
    pyperclip.copy(PASSWORDS[account])
    print('Пароль для ' + account + ' скопирован в буфер.')
else:
    print('Учётная запись ' + account + 'отсутствует в списке.')
