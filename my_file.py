import os

# myFile = ['accounts.txt', 'details.csv','invite.docx']
# for filename in myFile:
#     print(os.path.join('/home/dio/test', filename))

# # os.makedirs('/home/dio/test')

# totalSize = 0
# for filename in os.listdir('/home/dio/'):
#     totalSize = totalSize + os.path.getsize(os.path.join('/home/dio/', filename))

# print(totalSize)

# print(os.path.exists('/home/dio/test'))


# helloFile = open('/home/dio/test/hello.txt')
# helloContent = helloFile.read()
# print(helloContent)

# sonnetFile = open('/home/dio/test/sonnet29.txt')
# print(sonnetFile.readlines())
# helloFile.close()
# sonnetFile.close()

# import shelve

# shelFile = shelve.open('mydata')
# cats = ['Zophie', 'Pooka', 'Simon']
# shelFile['cats'] = cats
# print(list(shelFile.keys()))
# print(list(shelFile.values()))
# print(shelFile['cats'])
# shelFile.close()

import pprint

cats = [{'name': 'Zophie', 'desc': 'chubby'}, {'name': 'Pooka', 'desc': 'fluffy'}]
pprint.pformat(cats)

fileObj = open('myCats.py', 'w')
fileObj.write('cats = ' + pprint.pformat(cats) + '\n')
fileObj.close()


