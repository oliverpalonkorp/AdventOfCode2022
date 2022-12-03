

test_data = [
    ["A", "Y"],
    ["B", "X"],
    ["C", "Z"]
    ]

shapePoints = {
    "A": 1,
    "B": 2,
    "C": 3,
    }

def formatData(fname):
    data = []
    with open(fname) as file:
        data = [line.rstrip().split(" ") for line in file]
    
    return data

def calculateResultPoints(ownShape, opponentShape):
    match ownShape:
        case "A":
            if opponentShape == "C": #rock > scissors
                return 6 #win
            if opponentShape == "B": #rock < paper
                return 0 #lose
        case "B":
            if opponentShape == "A": #paper > rock
                return 6 #win
            if opponentShape == "C": #paper < scissors
                return 0 #lose
        case "C":
            if opponentShape == "B": #scissors > paper
                return 6 #win
            if opponentShape == "A": #scissors < rock
                return 0 #lose
    return 3 #tie

def calculateShapePoints(shape):
    return shapePoints[shape]

def getShapeToPlay(row):
    for shape in ["A", "B", "C"]:
        match row[1]:
            case "X":
                if (calculateResultPoints(shape, row[0]) == 0): #lose
                    return shape
            case "Y":
                if (calculateResultPoints(shape, row[0]) == 3): #tie
                    return shape
            case "Z":
                if (calculateResultPoints(shape, row[0]) == 6): #win
                    return shape


def run():
    data = formatData("data2.txt")

    totalPoints = 0
    
    for row in data:
        ownShape = getShapeToPlay(row)
        totalPoints += calculateShapePoints(ownShape)
        totalPoints += calculateResultPoints(ownShape, row[0])
                
    #totalPoints = sum([(calculateShapePoints(row) + calculateResultPoints(row[1], row[0])) for row in data])
    
    print("Total score: " + str(totalPoints))

run()

'''
rock (1) > scissors (3)
scissors (3) > paper (2)
paper (2) > rock (1)
'''
'''
rock = 1p (A)
paper = 2p (B)
scissors = 3p (C)

lose = 0p
draw = 3p
win = 6p
'''
