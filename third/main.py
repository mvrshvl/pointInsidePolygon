import matplotlib.pyplot as plt

class Rectangle:
    """Класс для прямоугольника"""

    def __init__(self, x1=None, y1=None, x2=None, y2=None):
        self.x1, self.y1 = x1, y1
        self.x2, self.y2 = x2, y2

    def __str__(self):
        return "({0},{1},{2},{3})".format(self.x1, self.y1, self.x2, self.y2)

    def __get_min_x__(self):
        if self.x1 < self.x2:
            return self.x1
        return self.x2

    def __get_max_x__(self):
        if self.x1 > self.x2:
            return self.x1
        return self.x2

    def __get_min_y__(self):
        if self.y1 < self.y2:
            return self.y1
        return self.y2

    def __get_max_y__(self):
        if self.y1 > self.y2:
            return self.y1
        return self.y2


class Rectangles:
    """Класс для прямоугольников"""

    def __init__(self, rs=None):
        self.rs = rs

    def __sort_x__(self, order=None):
        if order:
            return sorted(self.rs, key=lambda rect: rect.__get_min_x__(), reverse=False)
        else:
            return sorted(self.rs, key=lambda rect: rect.__get_max_x__(), reverse=True)

    def __sort_y__(self, order=None):
        if order:
            return sorted(self.rs, key=lambda rect: rect.__get_min_y__(), reverse=False)
        else:
            return sorted(self.rs, key=lambda rect: rect.__get_max_y__(), reverse=True)

    def __get_by_x__(self, x=None):
        arr = []
        for rect in self.rs:
            if rect.x1 == x or rect.x2 == x:
                arr.append(rect)
        return arr

    def __get_by_y__(self, y=None):
        arr = []
        for rect in self.rs:
            if rect.y1 == y or rect.y2 == y:
                arr.append(rect)
        return arr


def showByOrder(rects, title):
    idx = 0
    for rect in rects:
        idx = idx + 1
        plt.text(rect.__get_min_x__(), rect.__get_min_y__(), idx)

    for rect in rects:
        plt.plot(
            [rect.x1, rect.x1, rect.x2, rect.x2, rect.x1],
            [rect.y1, rect.y2, rect.y2, rect.y1, rect.y1],
        )

    plt.title(title)
    plt.savefig("demo.png", bbox_inches='tight')


def showByPoint(all, rects, title):
    idx = 0
    for rect in rects:
        idx = idx + 1
        plt.text(rect.__get_min_x__(), rect.__get_min_y__(), idx)

    for rect in all:
        plt.plot(
            [rect.x1, rect.x1, rect.x2, rect.x2, rect.x1],
            [rect.y1, rect.y2, rect.y2, rect.y1, rect.y1],
            color="black"
        )

    for rect in rects:
        plt.plot(
            [rect.x1, rect.x1, rect.x2, rect.x2, rect.x1],
            [rect.y1, rect.y2, rect.y2, rect.y1, rect.y1],
        )

    plt.title(title)
    plt.savefig("demo.png", bbox_inches='tight')


if __name__ == "__main__":
    points = [[10, 15, 20, 25], [5, 10, 25, 30], [0, 10, 15, 20], [20, 30, 15, 10], [15, 20, 10, 5]]

    rectanglesArr = [Rectangle(p[0], p[1], p[2], p[3]) for p in points]

    rectanglesCollections = Rectangles(rectanglesArr)

    # order = rectanglesCollections.__sort_x__(True)
    # showByOrder(order, "Sort min-max x")

    # order = rectanglesCollections.__sort_x__(False)
    # showByOrder(order, "Sort max-min x")

    # order = rectanglesCollections.__sort_y__(True)
    # showByOrder(order, "Sort min-max y")
    #
    # order = rectanglesCollections.__sort_y__(False)
    # showByOrder(order, "Sort max-min y")
    #
    # get_by_x = rectanglesCollections.__get_by_x__(10)
    # showByPoint(rectanglesArr, get_by_x, "get by x")
    #
    get_by_y = rectanglesCollections.__get_by_y__(10)
    showByPoint(rectanglesArr, get_by_y, "get by y")
