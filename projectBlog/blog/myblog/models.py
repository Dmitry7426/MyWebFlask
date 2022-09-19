

def start():
    x = 'testWeb'
    return x

def duplicates(a):
    a1 = []
    result = ''
    for i in a:
        if i.author not in a1:
            a1.append(i.author)
    for j in a1:
        print(j)
    if len(a) != len(a1):
        del a[-1]  # если найден дубликат удаляем последнюю запись
        result = 'Пользователь с такими ником уже оставлял пост'
    return result

def nblog(a):
    p = 'Тут будет создан новый блог'
    return p

def allblogs(a):

    return a

def lastblogs(a):
    w = []
    last = ''
    if len(a) == 0:
        w.append('Пока что нет ни кого кто опубликовал бы пост....')
    else:
        for i in a:
            w.append(i.author)
        last = w[-3:]

    return last

def userblog():
    pass