from point import Point
import constant


def findPath(chart, origin, destiny):

    # validating origin and destiny
    if chart[origin["x"]][origin["y"]] == constant.WALL:
        print("You can't start at a wall")
        return None
    if chart[destiny["x"]][destiny["y"]] == constant.WALL:
        print("Your destiny can't be a wall")
        return None

    openedList = []
    closedList = []

    bestPath = None
    bestPathCoordinates = []

    originPoint = Point(origin["x"], origin["y"], origin, destiny, None)
    openedList.append(originPoint)

    while len(openedList) > 0:

        # ordering a list by cost
        openedList.sort(key=lambda point: point.getCost())
        # Getting a point with cheapest cost
        cheapest = openedList[0]

        # verifing if I stay at destiny
        if cheapest.getPoint() == destiny:
            bestPath = cheapest
            break

        # Getting children of cheapest point
        childrenPoints = get_children_points(cheapest.getPoint(), chart)
        # Adding cheapest point to closedList
        closedList.append(cheapest.getPoint())
        # Removing cheapest point from openedList
        openedList.remove(cheapest)

        # Adding children to openedList
        for childPoint in childrenPoints:
            x = childPoint["x"]
            y = childPoint["y"]
            if chart[x][y] is not constant.WALL and childPoint not in closedList:
                point = Point(x, y, origin, destiny, cheapest)
                openedList.append(point)

    else:
        # No path available
        return None

    # Getting coordinates for best path found
    while True:
        bestPathCoordinates.append(bestPath.getPoint())
        bestPath = bestPath.getFather()
        if not bestPath.getFather():
            bestPathCoordinates.append(bestPath.getPoint())
            break

    bestPathCoordinates.reverse()
    return bestPathCoordinates


def get_children_points(point, chart):
    rowLimit = len(chart)
    columnLimt = len(chart[0])

    def get_left_point():
        y = point["y"] - 1
        if y >= 0:
            return {"x": point["x"], "y": y}
        else:
            return None

    def get_right_point():
        y = point["y"] + 1
        if y < columnLimt:
            return {"x": point["x"], "y": y}
        else:
            return None

    def get_up_point():
        x = point["x"] - 1
        if x >= 0:
            return {"x": x, "y": point["y"]}
        else:
            return None

    def get_down_point():
        x = point["x"] + 1
        if x < rowLimit:
            return {"x": x, "y": point["y"]}
        else:
            return None

    childrenPoints = [
        get_left_point(),
        get_right_point(),
        get_up_point(),
        get_down_point()
    ]

    for point in childrenPoints:
        if not point:
            childrenPoints.remove(point)

    return childrenPoints
