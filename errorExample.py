import traceback

def spam():
    bacon()

def bacon():
    # raise Exception('Это сообщение об ошибке.')
    try:
        raise Exception('Это сообщение об ошибке.')
    except:
        errorFile = open('errorInfo.txt', 'w')
        errorFile.write(traceback.format_exc())
        errorFile.close()
        print('Информация о стеке вызовов былла записана в файл errorInfo.txt')

spam()

