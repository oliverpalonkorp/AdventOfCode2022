

test_data = [
    ["A", "Y"],
    ["B", "X"],
    ["C", "Z"]
    ]

shapePoints = {
    "X": 1,
    "Y": 2,
    "Z": 3,
    }

def formatData(fname):
    data = []
    with open(fname) as file:
        data = [line.rstrip().split(" ") for line in file]
    
    return data

def calculateResultPoints(ownShape, opponentShape):
    match ownShape:
        case "X":
            if opponentShape == "C": #rock > scissors
                return 6 #win
            if opponentShape == "B": #rock < paper
                return 0 #lose
        case "Y":
            if opponentShape == "A": #paper > rock
                return 6 #win
            if opponentShape == "C": #paper < scissors
                return 0 #lose
        case "Z":
            if opponentShape == "B": #scissors > paper
                return 6 #win
            if opponentShape == "A": #scissors < rock
                return 0 #lose
    return 3 #tie

def calculateShapePoints(roundShapes):
    return shapePoints[roundShapes[1]]


def run():
    data = formatData("data2.txt")

    totalPoints = sum([(calculateShapePoints(row) + calculateResultPoints(row[1], row[0])) for row in data])
    
    print("Total score: " + str(totalPoints))

run()
