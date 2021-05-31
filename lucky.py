# !/usr/bin/python
# lucky.py - Открывает несколько результатов поиска с помощью Google.

import requests, sys, webbrowser, bs4

print('Гуглим...') # отображается при загрузке страницы Google
res = requests.get('https://google.com/search?q=' + ' '.join(sys.argv[1:]))
res.raise_for_status()

# Извлечение первых нескольких найденных ссылок.

soup = bs4.BeautifulSoup(res.text, 'lxml')

# Открытие отдельной вкладки для каждого результата.

# linkElems = soup.select('.r  a') # Это устаревший код, ниже код рабочий.
linkElems = soup.select('div#main > div > div > div > a')
numOpen = min(5, len(linkElems))
for i in range(numOpen):
    webbrowser.open('https://google.com' + linkElems[i].get('href'))


