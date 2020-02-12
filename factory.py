def main():
    fin = open("1.in", "r+")
    numTowns = int(fin.readline())
    print(numTowns)
    pairs = []
    outgoing = {}
    incoming = {}
    for i in range(numTowns - 1):
        pair = fin.readline().rstrip("\n").split(" ")
        for i in range(0, 2):
            pair[i] = int(pair[i])
        pairs.append(pair)

        if(pair[0] in outgoing):
            outgoing[pair[0]] += 1
        else:
            outgoing[pair[0]] == 0
        if(pair[1] in incoming):
            incoming[pair[1]] += 1
        else:
            incoming[pair[1]] == 0

        print(pair)
    print(outgoing)
    print(incoming)

    sink = -1

    fin.close()


main()
