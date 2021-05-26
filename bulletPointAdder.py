# ! python3
# bulletPointAdder.py - Добавляет маркеры Википедии в начало
# каждой строки текста, сохраненного в буфере обмена.

import pyperclip
text = pyperclip.paste()

# TODO: разделить строки и добавить звёздочки.

# Разделяет строки и добавляет звёздочки.
lines = text.split('\n')
for i in range(len(lines)):      # цикл по списку "lines"
    lines[i] = '* ' + lines[i]   # добавляет звёздочку в каждую
                                 # строку в списке "lines"

text = '\n'.join(lines)
pyperclip.copy(text)
