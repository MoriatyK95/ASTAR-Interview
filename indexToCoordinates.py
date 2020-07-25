import csv
#Author: Huakai
#Date: 25/07/2020
#Description: Q7 ASTAR interview map 1D to 2D


outputfile = open("output_coordinates_7_1.txt", "w")


with open("input_index_7_1.txt") as f:
    next(f)
    for line in f:
        c = line
        c = int(c)
        x1 = c % 50
        #floor of c divide by n + 1 to get x2
        x2 = c //  (57 + 1)
       
        outputfile.write(str(x1)  + str(x2) + "\n")
outputfile.close()1
