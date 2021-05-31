# ! /usr/bin/python3
# lucky.py - Открывает несколько результатов поиска с помощью Google.

import requests, sys, webbrowser, bs4

print('Гуглим...') # отображается при загрузке страницы Google
res = requests.get('http://google.com/search?q=' + ' '.join(sys.argv[1:]))
res.raise_for_status()

# TODO: Извлечь первые несколько найденных ссылок.

# TODO: Открыть отдельную вкладку для каждого результата.

