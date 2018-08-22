#$ python3 stats.py
import math

def getNumbers():
    return [10, 10, 20, 20]

def isUnevenNumber(nr):
    return nr % 2 == 1

def getMaximum(numbers):
    maximum = numbers[0]

    for i in range(1, len(numbers)):
        if maximum < numbers[i]:
            maximum = numbers[i]
    
    return maximum

def getMean(numbers):
    totalSum = numbers[0]

    for i in range(1, len(numbers)):
        totalSum += numbers[i]

    return totalSum / len(numbers)

def getMedian(numbers):
    numbersToUse = sorted(numbers)
    arrLength = len(numbers)

    if arrLength == 1:
        return numbersToUse[0]
    
    elif isUnevenNumber(arrLength):
        midIndex = int((arrLength - 1) / 2)
        return numbersToUse[midIndex]

    else:
        lowerHalfMax = numbersToUse[int((arrLength - 2) / 2)]
        upperHalfMax = numbersToUse[int(arrLength / 2)]

        return (lowerHalfMax + upperHalfMax) / 2

def getMinimum(numbers):
    minimum = numbers[0]

    for i in range(1, len(numbers)):
        if minimum > numbers[i]:
            minimum = numbers[i]
    
    return minimum

def getRange(numbers):
    return getMaximum(numbers) - getMinimum(numbers)

def getStandardDeviation(numbers):
    totalSquaredDeviation = 0

    i = 0
    for nr in numbers:
        deviation = numbers[i] - getMean(numbers)
        squaredDeviation = deviation * deviation
        totalSquaredDeviation += squaredDeviation
        i += 1

    return math.sqrt(totalSquaredDeviation / len(numbers))

def printStats():
    numbers = getNumbers()
    
    maximum = getMaximum(numbers)
    mean = getMean(numbers)
    median = getMedian(numbers)
    minimum = getMinimum(numbers)
    range = getRange(numbers)
    standardDeviation = getStandardDeviation(numbers)

    print("Maximum is: " + str(maximum))
    print("Mean is: " + str(mean))
    print("Median is: " + str(median))
    print("Minimum is: " + str(minimum))
    print("Range is: " + str(range))
    print("Standard deviation is: " + str(standardDeviation))
    print(numbers)

printStats()