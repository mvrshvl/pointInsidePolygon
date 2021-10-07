import math
from point import *
import matplotlib.pyplot as plt

def pip_cross(point, pgon):
    """
  Определяет, находится ли точка внутри многоугольника. В основе кода
  лежит программа на C из книги Haines "Graphics Gems IV" (1994).
  Вход
  pgon: список вершин многоугольника
  point: точка
  Выход
  Возвращает булево значение True или False и сколько раз луч
  пересекает границу многоугольника
  """
    numvert = len(pgon)
    tx = point.x
    ty = point.y
    p1 = pgon[numvert - 1]
    p2 = pgon[0]
    yflag1 = (p1.y >= ty)  # p1 на одном уровне с point или выше нее
    crossing = 0
    inside_flag = 0
    for j in range(numvert - 1):
        yflag2 = (p2.y >= ty)  # p2 на одном уровне с point или выше нее
        if yflag1 != yflag2:  # по разные стороны от луча
            xflag1 = (p1.x >= tx)  # слева от p1
            xflag2 = (p2.x >= tx)  # слева от p2
            if xflag1 == xflag2:  # обе точки справа
                if xflag1:
                    crossing += 1
                    inside_flag = not inside_flag
            else:
                m = p2.x - float((p2.y - ty)) * (p1.x - p2.x) / (p1.y - p2.y)
                if m >= tx:
                    crossing += 1
                    inside_flag = not inside_flag
        yflag1 = yflag2
        p1 = p2
        p2 = pgon[j + 1]
    return inside_flag, crossing

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

if __name__ == "__main__":
    points = [[0, 10], [5, 0], [10, 10], [15, 0], [20, 10],
              [25, 0], [30, 20], [40, 20], [45, 0], [50, 50],
              [40, 40], [30, 50], [25, 20], [20, 50], [15, 10],
              [10, 50], [8, 8], [4, 50], [0, 10]]
    ppgon = [Point(p[0], p[1]) for p in points]
    inout = lambda pip: "ВНУТРИ" if pip is True else "СНАРУЖИ"

    point = Point(10, 20)
    print("Точка {} находится {}" .format(point, inout(pip_cross(point, ppgon)[0])))
    showPlot(point, points, "")
