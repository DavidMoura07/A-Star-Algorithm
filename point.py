class Point:

    def __init__(self, initX, initY, originPoint, destinyPoint, fatherPoint):
        self.x = initX  # row
        self.y = initY  # column

        self.point = {"x": self.getX(), "y": self.getY()}

        # cost of start point to this point
        self.originCost = abs(self.x - originPoint["x"]) + \
            abs(self.y - originPoint["y"])

        # cost of this point to destiny
        self.destinyCost = abs(self.x - destinyPoint["x"]) + \
            abs(self.y - destinyPoint["y"])

        self.cost = self.originCost + self.destinyCost

        self.father = fatherPoint

    def getX(self):
        return self.x

    def getY(self):
        return self.y

    def getPoint(self):
        return self.point

    def getCost(self):
        return self.cost

    def getFather(self):
        return self.father

    def __str__(self):
        return "Point: " + str(self.getPoint()) + " | Cost: " + str(self.getCost()) + " | Father: " + str(self.getFather())
