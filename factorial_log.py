# ! python3


import logging

# logging.disable(logging.DEBUG)

logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(levelname)s - %(message)s')
logging.debug('Начало программы')

def factorial(n):
    logging.debug('Начало factorial (%s%%)' % (n))
    total = 1
    for i in range(1, n + 1):
        total *= i
        logging.debug('i = ' + str(i) + ', total = ' + str(total))
    logging.debug('Конец factorial (%s%%)' % (n))
    return total

print(factorial(5))
logging.debug('Конец программы')
