arr = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
count_row = 0
count_col = 0
tmp = []

def testNul():
    #проверка на пустые элементы массива
    
    for k in arr:
        if 0 in k:
           return False
        else:
            return True

def testRow():
    # проверка по строкам
    for i in range(len(arr)):
        for j in range(len(arr)-1):
            arr[j].sort()
            arr[j + 1].sort()
            if arr[i][j] == arr[i][j + 1]:
                return False
            else:
                return True
def testCol():

    # Проверка по столбцам
    for i in range(len(arr)):
        for j in range(len(arr)):
            arr.sort()
            if arr[j - 1][i] == arr[j][i]:
                return False
            else:
                return True
            # print(arr[j][i])

    # print(count_col, count_row)
def prn():
    w = 'test'
    return True

def sudoku(a):
    if testNul():
        if testRow():
            if testCol():
                o = 'Судоку верна'
            else:
                o = 'В колонках повторы'
        else:
            o = 'В строках повторы'
    else:
        o = 'Не корректные или не полные данные'
    return o


print(sudoku(testNul()))