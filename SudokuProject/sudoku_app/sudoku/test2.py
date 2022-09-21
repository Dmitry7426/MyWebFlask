# arr = [[1, 2, 3, 4, 5, 6, 7, 8, 9],
#        [1, 2, 3, 4, 5, 6, 7, 8, 9],
#        [1, 2, 3, 4, 5, 6, 7, 8, 9],
#        [1, 2, 3, 4, 5, 6, 7, 8, 9],
#        [1, 2, 3, 4, 5, 6, 7, 8, 9],
#        [1, 2, 3, 4, 5, 6, 7, 8, 9],
#        [1, 2, 3, 4, 5, 6, 7, 8, 9],
#        [1, 2, 3, 4, 5, 6, 7, 8, 9],
#        [1, 2, 3, 4, 5, 6, 7, 8, 9]]

arr = [[1, 2, 3], [4, 0, 6], [7, 8, 0]]

for i in arr:
    if 0 in i:
        print('найдены ноли')
    else:
        print('ноли не найдены')


# w = [1, 2, 3]
# w1 = set()
# e = []
# e1 = set()
# # for i in arr:
#     i.sort()
#     e1 = set(i)
#     print(e1)
#     if len(arr) == len(e1):
#         print('уникальные')
#     else:
#         print('Повторы')


# for row in range(len(arr)):
#     for col in range(len(arr[row])):
#         e.append(arr[col][row])
#     e.sort()
#     e1 = set(e)
#     print('новый массив е:', e)
#     print('новое множество е1:', e1)
#     print('длинна е:', len(e))
#     print('длинна е1:', len(e1))
#     if len(e) == len(e1):
#         print('Все ОК')
#     else:
#         print('Повторы числел')
#     e = []
#     e1 = set()


