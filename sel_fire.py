from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager

browser = webdriver.Firefox(executable_path=GeckoDriverManager().install())
browser.get('http://inventwithpython.com')

try:
    elem = browser.find_element_by_class_name('bookcover')
    print('Найден элемент <%s> с данным именем класса!' % (elem.tag_name))
except:
    print('Не удалось найти элемент с данным именем класса.')

