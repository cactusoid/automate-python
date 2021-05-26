def collatz(number):
    while number != 1 :
        if number % 2 == 0:
            number = number // 2
            print(number)
        elif number % 2 == 1:
            number = 3 * number + 1
            print(number)
    
        
    
    
        


try:
    number = int(input('Введите число: '))
    collatz(number)
except ValueError:
        print('Вы написали строку, а не число.')




