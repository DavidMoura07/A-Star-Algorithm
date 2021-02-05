import constant


def readChart(fileName):
    chart = []
    chartFile = open(fileName, 'r')
    for x in chartFile:
        line = str(x)
        line = line.replace('\n', '')
        line = line.split()
        line = list(map(lambda x: int(x), line))
        chart.append(line)

    chartFile.close()
    return chart


def outputChart(chart, pathCoordinates):
    output = open("output.txt", "w")

    def printChart():
        linesQuantity = len(chart[0])
        columnsQuantity = len(chart)
        line = ''
        lines = []
        for i in range(linesQuantity):
            for j in range(columnsQuantity):
                point = {"x": i, "y": j}
                if point in pathCoordinates:
                    line += str(constant.BEST_PATH) + " "
                else:
                    line += str(chart[i][j]) + " "
            print(line)
            line += '\n'
            lines.append(line)
            line = ''
        output.writelines(lines)

    def printPathCoordinates():
        strPathCoordinates = ''
        for coordinate in pathCoordinates:
            x = str(coordinate["x"])
            y = str(coordinate["y"])
            strPathCoordinates += "[" + x + "," + y + "] => "

        strPathCoordinates = strPathCoordinates[:len(
            strPathCoordinates)-3] + "\n"
        print(strPathCoordinates)
        output.write(strPathCoordinates)

    print("CHART PATH")
    output.write("CHART PATH\n")
    printChart()
    print("\n\nPATH COORDINATES")
    output.write("\n\nPATH COORDINATES\n")
    printPathCoordinates()
