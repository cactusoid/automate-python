tableData = [['apples', 'orange', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]

def printTable(data):
    cols = len(data)
    rows = len(data[0])

    col_width = []
    for col in data:
        col_width.append(len(sorted(col, key=len)[-1]))

    for row in range(rows):
        result = []
        for col in range(cols):
            result.append(data[col][row].rjust(col_width[col]))
        print(' '.join(result))


printTable(tableData)

def printTable2(tableData):
    cols = len(tableData)
    rows = len(tableData[0])
    new_list = [ [" " for c in range(cols)] for r in range(rows) ]
    maxLen   = 0
    for i, lists in enumerate(tableData):
        for j, values in enumerate(lists):
            new_list[j][i] = values
            if len(values) > maxLen: maxLen = len(values) 

    for values in new_list:
        print("{:>{maxLen}}{:>{maxLen}}{:>{maxLen}}".format(*values, maxLen=maxLen))

printTable2(tableData)