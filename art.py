fin = open("5.in", "r+")
gridSize = int(fin.readline().rstrip("\n"))
grid = []
for i in range(gridSize):
    grid.append(fin.readline().rstrip("\n"))

for line in grid:
    print(line)
