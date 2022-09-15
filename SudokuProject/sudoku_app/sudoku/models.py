arr = [[0, 0, 3, 4, 0, 0, 2, 7, 0],[0, 9, 2, 0, 3, 0, 0, 0, 0],
       [0, 0, 0, 0, 1, 0, 0, 0, 0],[0, 1, 0, 0, 5, 0, 3, 0, 0],
       [3, 0, 0, 1, 6, 7, 0, 0, 8],[0, 0, 8, 0, 8, 0, 0, 6, 0],
       [0, 0, 0, 0, 3, 0, 0, 0, 0],[0, 0, 0, 0, 8, 0, 6, 2, 0],
       [0, 5, 3, 0, 0, 9, 1, 0, 0]]


# class Sudoku:
#     def __init__(self, arr):
#         self.arr = arr
#
#     def view(self):
#         return arr


# st = Sudoku(arr)


def testGorizonty(a):
       count_row = 0
       count_col = 0
       tmp = []

       # проверка на пустые элементы массива
       for k in arr:
              if 0 in k:
                     print('есть ноль')

       # проверка по строкам
       for i in range(9):
              for j in range(8):
                     arr[j].sort()
                     arr[j + 1].sort()
                     if arr[i][j] == arr[i][j + 1]:
                            count_row = 1

       # Проверка по столбцам
       for i in range(9):
              for j in range(9):
                     arr.sort()
                     if arr[j - 1][i] == arr[j][i]:
                            count_col = 1
                     # print(arr[j][i])

       print(count_col, count_row)
