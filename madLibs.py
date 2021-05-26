# !python3
# madLibs.py - Создайте программу Mad Libs, которая читает текстовые файлы и
# предоставляет пользователю возможность добавлять собственный текст
# в любом месте файла, где встречаются слова ADJECTIVE (прилагательное),
# NOUN (существительное), ADVERB (наречие) и VERB (глагол).

l = []
with open('madLibs.txt','r') as f:
    for line in f:
        l = line.split()
        # print(l)
        for i in range(len(l)):
            if l[i] == 'ADJECTIVE':
                l[i] = input('Введите имя прилагательное: ')
            elif l[i] == 'NOUN':
                l[i] = input('Введите имя существительное: ')
            elif l[i] == 'ADVERB':
                l[i] = input('Введите имя наречие: ')
            elif l[i] == 'VERB.':
                l[i] = input('Введите имя глагол: ') + str('.')
        # print(l)
        full_text = ' '.join(l)
        print(full_text)
        with open('madLibs1.txt', 'w') as file:
            for line in full_text:
                file.write(line)







