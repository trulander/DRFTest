class Point():
    MAX_COORD = 100
    def __init__(self, x, y ):
        self.x = x
        self.y = y


class Point2D():
    __slots__ = ('x', 'y')
    MAX_COORD = 100

    def __init__(self, x, y):
        self.x = x
        self.y = y
        #self.z = y

class Point3D(Point2D):
    __slots__ = ('z')

    def __init__(self, x, y, z):
        super().__init__(x,y)
        self.z = z

class PointFree(Point2D):
    def __init__(self, x, y, z):
        super().__init__(x,y)
        self.z = z

point1 = Point2D(10, 20)
point2 = Point2D(100, 200)
point3 = Point3D(100, 200, 300)
point4 = PointFree(100, 200, 300)

#print(point3.__dict__)
print(point3.__slots__)

print(point4.__dict__)
print(point4.__slots__)