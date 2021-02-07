#!/usr/bin/python

import sys
import aStarModule as aStar
import fileManager


def main():

    # Getting args from command line
    fileName = sys.argv[1]
    strOrigin = sys.argv[2]
    strDestiny = sys.argv[3]
    strOrigin = strOrigin.split(",")
    strDestiny = strDestiny.split(",")

    origin = {"x": int(strOrigin[0]), "y": int(strOrigin[1])}
    destiny = {"x": int(strDestiny[0]), "y": int(strDestiny[1])}

    chart = fileManager.readChart(fileName)

    print("File name: ", fileName)
    print("Origin: ", str(origin))
    print("Destiny: ", str(destiny))
    print('\n')

    coordinates = aStar.find_path(chart, origin, destiny)

    if not coordinates:
        print("No path available")
        return 0

    fileManager.outputChart(chart, coordinates)


main()
