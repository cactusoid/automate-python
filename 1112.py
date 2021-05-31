import requests

res = requests.get('http://www.gutenberg.org/cache/epub/1112/pg1112.txt')
print(type(res))
res.status_code == requests.codes.OK
print(res.status_code)
print(len(res.text))
print(res.text[:250])

playFile = open('RomeoAndJuliet.txt', 'wb')
for chunk in res.iter_content(100000):
    playFile.write(chunk)

playFile.close()

res1 = requests.get('http://inventwithpython.com/несуществующая_страница')
try:
    res1.raise_for_status()
except Exception as exc:
    print('Возникла проблема: %s' % (exc))