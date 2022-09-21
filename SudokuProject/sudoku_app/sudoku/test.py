arr = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
count_row = 0
count_col = 0
tmp = []
#
# def testNul():
#     #проверка на пустые элементы массива
#
#     for k in arr:
#         if 0 in k:
#            return False
#         else:
#             return True
#
# def testRow():
#     # проверка по строкам
#     for i in range(len(arr)):
#         for j in range(len(arr)-1):
#             arr[j].sort()
#             arr[j + 1].sort()
#             if arr[i][j] == arr[i][j + 1]:
#                 return False
#             else:
#                 return True
# def testCol():
#
#     # Проверка по столбцам
#     for i in range(len(arr)):
#         for j in range(len(arr)):
#             arr.sort()
#             if arr[j - 1][i] == arr[j][i]:
#                 return False
#             else:
#                 return True
#             # print(arr[j][i])
#
#     # print(count_col, count_row)
# def prn():
#     w = 'test'
#     return True
#
# def sudoku(a):
#     if testNul():
#         if testRow():
#             if testCol():
#                 o = 'Судоку верна'
#             else:
#                 o = 'В колонках повторы'
#         else:
#             o = 'В строках повторы'
#     else:
#         o = 'Не корректные или не полные данные'
#     return o
#
#
# print(sudoku(testNul()))

def testRow():
    w = [1, 2, 3]
    w1 = set()
    e = []
    x = []
    e1 = set()
    for i in arr:
        i.sort()
        e1 = set(i)
        print(e1)
        if len(arr) == len(e1):
            return False
        else:
            return True

def testCol():
    x = []
    for row in range(len(arr)):
        for col in range(len(arr[row])):
            x.append(arr[col][row])
        x.sort()
        w1 = set(x)
        print('новый массив е:', x)
        print('новое множество е1:', w1)
        print('длинна е:', len(x))
        print('длинна е1:', len(w1))
        if len(x) == len(w1):
            return False
        else:
            return True
        x = []
        w1 = set()

def testGrid():
    for i in range(0, 9, 3):
        for j in range(0, 9, 3):
            number = set()
            for dx in range(3):
                for dy in range(3):
                    number.add(arr[i + dx][j + dy])
            if len(number)!=9:
                return False

def testNul():
    for i in arr:
        if i == 0:
            return False
        else:
            return True