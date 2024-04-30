from fileinput import input

n = []
for line in input(files = "amostra.txt"):
    for x in line.replace("\n", "").split(" "):
        n.append(float(x))

n.sort()
m = n[0]
M = n[-1]