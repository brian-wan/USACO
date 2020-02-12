fin = open("cownomics.in", "r+")
numGenePairs, numGenes = fin.readline().rstrip("\n").split(" ")

numGenePairs = int(numGenePairs)
numGenes = int(numGenes)
spottySequence = []
plainSequence = []
count = 0

for i in range(numGenePairs):
    spottySequence.append(fin.readline().rstrip("\n"))
for j in range(numGenePairs):
    plainSequence.append(fin.readline().rstrip("\n"))
fin.close()
for k in range(numGenes):
    # run through each index
    posSpot = True
    spotGenes = []
    plainGenes = []
    for sequence in spottySequence:
        if sequence[k] not in spotGenes:
            spotGenes.append(sequence[k])
    for sequence in plainSequence:
        if sequence[k] not in plainGenes:
            plainGenes.append(sequence[k])
    # now have bases at that index in each gene list
    # implement logic at each index

    for base in spotGenes:
        if base in plainGenes:
            posSpot = False

    if posSpot:
        print(k)
        count += 1
"""
print(spottySequence)
print(plainSequence)
print(count)
"""

fout = open("cownomics.out", "w")
fout.writelines(str(count))
fout.close()

