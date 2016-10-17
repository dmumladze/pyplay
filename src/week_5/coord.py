
class Coordinate(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distance(self, other):
        x_diff_sq = (self.x-other.x)**2
        y_diff_sq = (self.y-other.y)**2
        return (x_diff_sq + y_diff_sq)**0.5

    def __sub__(self, other):
        return Coordinate(self.x-other.x, self.y-other.y)

    def __str__(self):
        return "[" + self.x + "," + self.y + "]"


c1 = Coordinate(3, 4)
c2 = Coordinate(0, 0)

print(c1.distance(c2))