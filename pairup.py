# input is num lines
# then how many of each output
output_times = []


fin = open("2.in", "r+")
numLines = int(fin.readline().rstrip("\n"))


for t in range(numLines):
    data = fin.readline().rstrip("\n").split(" ")
    temp = int(data[0])
    data[0] = int(data[1])
    data[1] = temp
    output_times.append(data)
fin.close()
new_output_times = sorted(output_times)
#print(new_output_times)
m = 0
i = 0
j = numLines - 1
while i <= j:
    data1 = (new_output_times[i])
    data2 = (new_output_times[j])
    x = min(int(data1[1]), int(data2[1]))
    if i == j:
        x /= 2
    m = max(m, int(data1[0]) + int(data2[0]))
    # print(m)
    data1[1] -= 1
    data2[1] -= 1
    if data1[1] == 0:
        i += 1
    if data2[1] == 0:
        j -= 1
#print(m)
fout = open("pairup.out", "w")
fout.writelines(str(m))
fout.close()
