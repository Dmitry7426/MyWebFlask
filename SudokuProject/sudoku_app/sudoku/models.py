arr = [[2, 2, 3, 4, 2, 3, 2, 7, 0],[0, 9, 2, 2, 3, 4, 5, 2, 1],
       [0, 2, 3, 0, 1, 6, 1, 8, 0],[1, 1, 2, 2, 5, 0, 3, 1, 2],
       [3, 0, 2, 1, 6, 7, 2, 1, 8],[1, 0, 8, 7, 8, 2, 8, 6, 3],
       [1, 1, 3, 0, 3, 1, 2, 6, 0],[2, 5, 4, 2, 8, 1, 6, 2, 0],
       [0, 5, 3, 3, 4, 9, 1, 1, 8]]


# class Sudoku:
#     def __init__(self, arr):
#         self.arr = arr
#
#     def view(self):
#         return arr


# st = Sudoku(arr)

def sudokuapp():
    if testNul():
        return True
    else:
        return testNul()

def testRow():
    w = [1, 2, 3]
    w1 = set()
    e = []
    x = []
    e1 = set()
    for i in arr:
        i.sort()
        e1 = set(i)
        # print(e1)
        if len(arr) == len(e1):
            return testCol()
        else:
            return True

def testCol():
    x = []
    for row in range(len(arr)):
        for col in range(len(arr[row])):
            x.append(arr[col][row])
        x.sort()
        w1 = set(x)
        # print('новый массив е:', x)
        # print('новое множество е1:', w1)
        # print('длинна е:', len(x))
        # print('длинна е1:', len(w1))
        if len(x) == len(w1):
            return testGrid()
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
            if len(number) != 9:
                return False

def testNul():
    for i in arr:
        if 0 in i:
            result = 'Игра 1'
            return result
        else:
            result = 'Игра 2'
            return result