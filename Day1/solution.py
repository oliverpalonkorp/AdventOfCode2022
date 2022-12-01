
def formatDataToArr(fname):
    d = []

    with open(fname) as file:
        lines = [line.rstrip() for line in file]

    current = []
    
    for x in lines:
        if x == "":
            d.append(current)
            current = []
        else:
            current.append(int(x))
    
    return d


def getSumOfTopN(n, d):
    sums = [sum(d[i]) for i in range(0, len(d))]
    sums.sort(reverse=True)

    return sum([sums[l] for l in range(0, n)])

    
def run():
    data = formatDataToArr("data1.txt")
    
    print("Part 1: " + str(getSumOfTopN(1, data)))
    print("Part 2: " + str(getSumOfTopN(3, data)))

run()


