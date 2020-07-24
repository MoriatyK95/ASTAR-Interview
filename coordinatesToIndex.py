import csv
#Author: Huakai
#Date: 25/07/2020
#Description: Q7 ASTAR interview map 2D to 1D

#maps (x1,x2) from 2D to 1D
def coordinateToIndex( x1 , x2):
    m = 57
    return x1 + m * x2

outputfile = open("output_index_7_1.txt", "w")

with open("input_coordinates_7_1.txt") as tsv:
    next(tsv)
    for line in csv.reader(tsv, dialect="excel-tab"):
        x1 = line[0]
        x2 = line[1]

        index = int(x1)+ 50*int(x2)
        #print(int(x1)+ 50*int(x2))
        #write into output file
        outputfile.write(str(index) +"\n")

outputfile.close()