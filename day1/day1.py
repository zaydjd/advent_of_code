f = open("input.txt", "r")
array = []

for x in f:
    if x != "\n":
        word = x.split("\n")
        array.append(word[0])
    else:
        array.append(x)
    
f.close()

calories = [0]
currPos = 0;
for n in array:
    if n != "\n":
        calories[currPos] += int(n)
    else:
        currPos += 1
        calories.append(0)

def findLargest():
    largest = calories[0]
    for cal in calories:
        if cal > largest:
            largest = cal

    calories.remove(largest)
    return largest
    
totalOfThree = findLargest()
totalOfThree += findLargest()
totalOfThree += findLargest()

print(totalOfThree)