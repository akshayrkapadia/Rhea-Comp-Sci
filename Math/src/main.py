class Point(object):
    """docstring for Point."""

    def __init__(self, x, y, z):
        super(Point, self).__init__()
        self.x = x
        self.y = y
        self.z = z

    def distance(self, point):
        diff_x = point.x - self.x
        diff_y = point.y - self.y
        diff_z = point.z - self.z
        xSq = diff_x**2
        ySq = diff_y**2
        zSq = diff_z**2
        sum = xSq + ySq + zSq
        distance = sum**0.5
        return distance


print("Point 1")
p1_x = int(input("x: "))
p1_y = int(input("y: "))
p1_z = int(input("z: "))
p1 = Point(p1_x, p1_y, p1_z)

print("Point 2")
p2_x = int(input("x: "))
p2_y = int(input("y: "))
p2_z = int(input("z: "))
p2 = Point(p2_x, p2_y, p2_z)

distance = p1.distance(p2)
print(distance)
