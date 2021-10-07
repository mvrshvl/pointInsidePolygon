
import math
from point import *
import matplotlib.pyplot as plt

def is_left(p, p1, p2):
    """
    Проверяет, лежит ли точка слева от отрезка, соединяющего
    p1 и p2
    Выход
    0 точка лежит на отрезке
    >0 p лежит слева от отрезка
    <0 p лежит справа от отрезка
    """
    return (p2.x-p1.x) * (p.y - p1.y)-(p.x - p1.x) * (p2.y - p1.y)

def pip_wn(pgon, point):
    """
    Определяет, находится ли точка внутри многоугольника, применяя алгоритм
    на основе числа оборотов с использованием тригонометрических функций.
    В основе коде лежит программа на C из книги Haines "Graphics Gems IV"
    (1994).
    Вход
    pgon: список вершин многоугольника
    point: точка44  Базовые геометрические операции
    Выход
    Возвращает булево значение True или False и сколько раз луч
    пересекает границу многоугольника
    """
    if pgon[0] != pgon[-1]:
        pgon.append(pgon[0])

    n = len(pgon)
    xp = point.x
    yp = point.y
    wn = 0

    for i in range(n - 1):
        xi = pgon[i].x
        yi = pgon[i].y
        xi1 = pgon[i + 1].x
        yi1 = pgon[i + 1].y
        thi = (xp - xi) * (xp - xi1) + (yp - yi) * (yp - yi1)
        norm = (math.sqrt((xp - xi) ** 2 + (yp - yi) ** 2) * math.sqrt((xp-xi1)**2+(yp-yi1)**2))
        if thi != 0:
            thi = thi / norm

        thi = math.acos(thi)
        wn += thi

    wn /= 2 * math.pi
    wn = int(wn)

    return wn != 0, wn

def pip_wn1(pgon, point):
    """
    Определяет, находится ли точка внутри многоугольника, применяя алгоритм
    на основе числа оборотов без использования тригонометрических функций.
    В основе коде лежит программа на C из книги Haines "Graphics Gems IV"
    (1994).
    Вход
    pgon: список вершин многоугольника
    point: точка
    Выход
    Возвращает булево значение True или False и сколько раз луч
    пересекает границу многоугольника
    """
    wn = 0
    n = len(pgon)
    for i in range(n - 1):
        if pgon[i].y <= point.y:
            if pgon[i + 1].y > point.y:
                if is_left(point, pgon[i], pgon[i + 1]) > 0:
                    wn += 1
        else:
            if pgon[i + 1].y <= point.y:
                if is_left(point, pgon[i], pgon[i + 1]) < 0:
                    wn -= 1

    return wn != 0, wn

def showPlot(point, polygonPoints, title):
    plt.scatter(point.x, point.y, color="red")

    for polygonPoint in polygonPoints:
        plt.scatter(polygonPoint[0], polygonPoint[1], color="green")

    plt.fill(
        [polygonPoint[0] for polygonPoint in polygonPoints],
        [polygonPoint[1] for polygonPoint in polygonPoints],
        fill=False
    )

    plt.title(title)
    plt.savefig('demo.png', bbox_inches='tight')
    plt.show()

if __name__ == '__main__':
    pgon = [[2, 3], [7, 4], [6, 6], [4, 2], [11, 5], [5, 11], [2, 3]]
    point = Point(6, 4)

    ppgon = [Point(p[0], p[1]) for p in pgon]

    print(pip_wn(ppgon, point))
    print(pip_wn1(ppgon, point))
    showPlot(point, pgon, "")