import random
options = ['камень', 'бумага', 'ножницы']
print('(1) Камень\n(2) Бумага\n(3) Ножницы')
human_choice = options[int(input('Введите число по вашему выбору: ')) - 1]
print(f'Вы выбрали {human_choice}')
computer_choice = random.choice(options)
print(f'Компьютер выбрал {computer_choice}')
if human_choice == 'камень':
    if computer_choice == 'бумага':
        print('К сожалению, бумага побеждает камень')
    elif computer_choice == 'ножницы':
        print('Да, камень побеждает ножницы!')
    else:
        print('Ничья!')
elif human_choice == 'бумага':
    if computer_choice == 'ножницы':
        print('К сожалению, ножницы побеждают бумагу')
    elif computer_choice == 'камень':
        print('Да, бумага побеждает камень!')
    else:
        print('Ничья!')
elif human_choice == 'ножницы':
    if computer_choice == 'камень':
        print('К сожалению, камень побеждает ножницы')
    elif computer_choice == 'бумага':
        print('Да, ножницы побеждают бумагу!')
    else:
        print('Ничья!')
    
