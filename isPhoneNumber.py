def isPhoneNumber(text):
    if len(text) != 12:
        return False
    for i in range(0, 3):
        if not text[i].isdecimal():
            return False
    if text[3] != '-':
        return False
    for i in range(4, 7):
        if not text[i].isdecimal():
            return False
    if text[7] != '-':
        return False
    for i in range(8, 12):
        if not text[i].isdecimal():
            return False
    return True

# print('415-555-4242 - это телефонный номер:')
# print(isPhoneNumber('415-555-4242'))
# print('Moshi moshi - это телефонный номер:')
# print(isPhoneNumber('Moshi moshi'))

message = 'Позвони мне завтра по номеру 415-555-1011. 415-555-9999 - это телефонный номер моего офиса.'
for i in range(len(message)):
    chunk = message[i:i+12]
    if isPhoneNumber(chunk):
        print('Найденный телефонный номер: ' + chunk)
print('Готово')


# Регулярные выражения
import re

phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
mo = phoneNumRegex.search('Мой номер: 415-555-4242.')
print('Найденный телефонный номер: ' + mo.group())
