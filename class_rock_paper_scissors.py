import random

OPTIONS = ['камень', 'бумага', 'ножницы']

class RockPaperScissorsSimulator:
    def __init__(self):
        self.computer_choice = None
        self.human_choice = None
        
    def get_computer_choice(self):
        return random.choice(OPTIONS)
    
    def get_human_choice(self):
        choice_number = int(input('Введите число по вашему выбору: '))
        return OPTIONS[choice_number - 1]

    def print_options(self):
        print('\n'.join(f'({i}) {option.title()}' for i, option in enumerate(OPTIONS)))

    def print_choices(self, human_choice, computer_choice):
        print(f'Вы выбрали {human_choice}')
        print(f'Компьютер выбрал {computer_choice}')

    def print_win_lose(self, human_choice, computer_choice, human_beats, human_loses_to):
        if computer_choice == human_loses_to:
            print(f'К сожалению, {computer_choice} побеждает {human_choice}')
        elif computer_choice == human_beats:
            print(f'Да, {human_choice} побеждает {computer_choice}!')

    def print_result(self, human_choice, computer_choice):
        if human_choice == computer_choice:
            print('Ничья!')

        if human_choice == 'камень':
            self.print_win_lose('камень', computer_choice, 'ножницы', 'бумага')
        elif human_choice == 'бумага':
            self.print_win_lose('бумага', computer_choice, 'камень', 'ножницы')
        elif human_choice == 'ножницы':
            self.print_win_lose('ножницы', computer_choice, 'бумага', 'камень')
        
     def simulate(self):
         self.print_options()
         human_choice = self.get_human_choice()
         computer_choice = self.get_computer_choice()
         self.print_choices(human_choice, computer_choice)
         self.print_result(human_choice, computer_choice)   