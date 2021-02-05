import aStarModule as aStar
import constant

chart = [
    [0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
    [1, 1, 1, 0, 0, 1, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 1, 1],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
]

origin = {"x": 0, "y": 0}
destiny = {"x": 9, "y": 8}


def main():

    coordinates = aStar.findPath(chart, origin, destiny)

    if not coordinates:
        print("No path available")
        return 0

    def printChart():
        linesQuantity = len(chart[0])
        columnsQuantity = len(chart)
        for i in range(linesQuantity):
            for j in range(columnsQuantity):
                point = {"x": i, "y": j}
                if point in coordinates:
                    print(str(constant.BEST_PATH) + " ", end='')
                else:
                    print(str(chart[i][j]) + " ", end='')

                if(j == len(chart)-1):
                    print("\n")

    def printCoordinates():
        strCoordinates = ''
        for coordinate in coordinates:
            x = str(coordinate["x"])
            y = str(coordinate["y"])
            strCoordinates += "[" + x + "," + y + "] => "
        print(strCoordinates[:len(strCoordinates)-3])

    print("CHART PATH")
    printChart()
    print("\n\nPATH COORDINATES")
    printCoordinates()


main()
