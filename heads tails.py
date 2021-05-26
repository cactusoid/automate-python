import random

guess = ''
while guess not in ('орел', 'решка'):
    print('Угадайте результат подбрасывания монеты! Введите орел или решка:')
    guess = input()
toss = random.randint(0, 1) # 0 - решка, 1 - орел
if guess == 'орел':
    guess = 1
else:
    guess = 0
if toss == guess:
    print('Есть!')
else:
    print('Увы! Попробуйте снова!')
    guess = input()
    if guess == 'орел':
        guess = 1
    else:
        guess = 0
    if toss == guess:
        print('Есть!')
    else:
        print('Нет. Вам действительно не везёт в этой игре.')
