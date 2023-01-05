FIBONACCI = [1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181, 6765, 10946, 17711, 28657,
             46368, 75025, 121393, 196418, 317811, 514229, 832040, 1346269]

def Zeckendorf(inputN):
    tempN = inputN
    upperLimit = len(FIBONACCI)
    correctNumbers = []
    while tempN > 0:
        for i in range(upperLimit - 1, -1, -1):
            if tempN in FIBONACCI:
                correctNumbers.append(tempN)
                return correctNumbers
            if FIBONACCI[i] < tempN:
                correctNumbers.append(FIBONACCI[i])
                tempN -= FIBONACCI[i]

        if tempN != 0:
            upperLimit = FIBONACCI.index(correctNumbers[0])
            correctNumbers.clear()
            tempN = inputN

    return correctNumbers


if __name__ == "__main__":

    print("Lorenzo Frescobaldi - Brighton College \n\n")
    print(Zeckendorf(int(input("> "))))