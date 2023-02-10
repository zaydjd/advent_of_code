f = open("input.txt", "r")

# Rock = 1 point, Paper = 2 points, Scissors = 3 points
# Loss = 0 points, Draw = 3 points, Win = 6 points

array = []

for x in f:
    if x != "\n":
        word = x.split("\n")
        array.append(word[0])
    else:
        array.append(x)
    
f.close()

def getResults(decider):
    score = 0;
    choices = decider.split(" ")

    opponentChoice = getShape(choices[0])
    playerChoice = getShape(choices[1])

    if playerChoice == "Not an option" or opponentChoice == "Not an option":
        return -1

    if opponentChoice == playerChoice:
        score += 3
    elif opponentChoice == 1:
        if playerChoice == 2:
            score += 6
        elif playerChoice == 3:
            score += 0
    elif opponentChoice == 2:
        if playerChoice == 1:
            score += 0
        elif playerChoice == 3:
            score += 6
    elif opponentChoice == 3:
        if playerChoice == 1:
            score += 6
        elif playerChoice == 2:
            score += 0

    return score + playerChoice

def getShape(letter):
    # print(letter)
    if letter == "A" or letter == "X":
        return 1 # Is Rock
    elif letter == "B" or letter == "Y":
        return 2 # Is Paper
    elif letter == "C" or letter == "Z":
        return 3 # Is Scissors
    else:
        return "Not an option" 

def checkResults(arr):
    totalScore = 0;
    for x in arr:
        totalScore += getResults(x)
    return totalScore


print(checkResults(array));