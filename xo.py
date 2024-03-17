def isInt(value):
    try:
        int(value)
        return True
    except ValueError:
        return False
        
a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
igrok = 0
x = "X"
o = 'O'
d = ['X','X','X']
c = ['O','O','O']
while True:
    print (list(map(str, a[0:3])))
    print (list(map(str, a[3:6])))
    print (list(map(str, a[6:9])))
    if a[0:3] == d or a[3:6] == d or a[6:9] == d or a[0:9:3] == d or a[1:9:3] == d or a[2:9:3] == d or a[0:9:4] == d or a[2:8:2] == d:
        print('Победил ИКС!!!')
        break
    elif a[0:3] == c or a[3:6] == c or a[6:9] == c or a[0:9:3] == c or a[1:9:3] == c or a[2:9:3] == c or a[0:9:4] == c or a[2:8:2] == c:
        print('Победил НОЛЬ!!!')
        break
    else:
        aa = (''.join(map(str, a)))
        if any(ch.isdigit() for ch in aa):
            pass
        else:
            print('Ничья')
            break
    if igrok % 2 == 0:
        print('Ход ИКС')
    else:
        print('Ход НОЛЬ')    
    b = input('Введите число:')
    if isInt(b):
        b = int(b)
        if b >= 1 and b <= 9 and b in a:
            igrok += 1
            a.pop(b-1)
            if igrok % 2 == 0:
                a.insert(b-1,o)
            else:
                a.insert(b-1,x)
        else:
            print('Введено неверное значение!')
    else:
        print('Введено неверное значение!')
#
#
#
#