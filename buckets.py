def main():
    fin = open("buckets.in", "r+")
    grid = []
    for i in range(10):
        data = fin.readline()
        data = data.rstrip('\n')
        #print(data)
        # get coordinates
        for char in data:
            if(char == "B"):
                bRow = i
                bCol = data.index("B")
            if(char == "L"):
                lRow = i
                lCol = data.index("L")
            if(char == "R"):
                rRow = i
                rCol = data.index("R")
        grid.append(data)
    fin.close()

    a = abs(bRow - lRow)
    b = abs(bCol - lCol)

    cows = a + b - 1
    if(bRow == lRow and bRow == rRow and ((bCol < rCol < lCol) or (bCol > rCol > lCol))):
        cows += 2
    if(bCol == lCol and bCol == rCol and ((bRow < rRow < lRow) or (bRow > rRow > lRow))):
        cows += 2
    #print(cows)
    fout = open("buckets.out", "w")
    fout.writelines(str(cows))
    fout.close()


main()
