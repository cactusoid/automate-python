def spam():
    global eggs
    eggs = 'spam' # это глобальная переменная

def bacon():
    eggs = 'bacon' # это локальная переменная

def ham():
    print(eggs) # это глобальная переменная

eggs = 42 # это глобальная переменная
spam()
print(eggs)
