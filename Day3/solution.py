

test_data = [
    "vJrwpWtwJgWrhcsFMMfFFhFp",
    "jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL",
    "PmmdzqPrVvPwwTWBwg",
    "wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn",
    "ttgJtRGJQctTZtZT",
    "CrZsJsPPZsGzwwsLwLmpwMDw"
    ]

priorities = {"a": 1, "b": 2, "c": 3, "d": 4, "e": 5, "f": 6, "g": 7,
              "h": 8, "i": 9, "j": 10, "k": 11, "l": 12, "m": 13,
              "n": 14, "o": 15, "p": 16, "q": 17, "r": 18, "s": 19,
              "t": 20, "u": 21, "v": 22, "w": 23, "x": 24, "y": 25,
              "z": 26, "A": 27, "B": 28, "C": 29, "D": 30, "E": 31,
              "F": 32, "G": 33, "H": 34, "I": 35, "J": 36, "K": 37,
              "L": 38, "M": 39, "N": 40, "O": 41, "P": 42, "Q": 43,
              "R": 44, "S": 45, "T": 46, "U": 47, "V": 48, "W": 49,
              "X": 50, "Y": 51, "Z": 52}

def formatData(fname):
    data = []
    with open(fname) as file:
        data = [line.rstrip() for line in file]
    
    return data


def solvePartOne():
    rucksacks = formatData("data.txt")

    totalSumOfPriorities = 0
    
    for rucksack in rucksacks:
        firstHalf, secondHalf = rucksack[:len(rucksack)//2], rucksack[len(rucksack)//2:]

        commonLetters = list(set(firstHalf)&set(secondHalf))

        sumOfCommonLetterPriorities = 0

        for letter in commonLetters:
            sumOfCommonLetterPriorities += priorities[letter]

        totalSumOfPriorities += sumOfCommonLetterPriorities

    print("Part 1 | Sum of common items in all rucksacks: " + str(totalSumOfPriorities))


def solvePartTwo():
    rucksacks = formatData("data.txt")
    groupsOfN = 3
    rucksackGroups = [rucksacks[i:i+groupsOfN] for i in range(0, len(rucksacks), groupsOfN)]

    totalSumOfPriorities = 0
    
    for group in rucksackGroups:
        
        commonLetters = list(set(group[0])&set(group[1])&set(group[2]))

        sumOfCommonLetterPriorities = 0

        for letter in commonLetters:
            sumOfCommonLetterPriorities += priorities[letter]

        totalSumOfPriorities += sumOfCommonLetterPriorities

    print("Part 2 | Badge Total Sum: " + str(totalSumOfPriorities))

#solvePartOne()
solvePartTwo()
