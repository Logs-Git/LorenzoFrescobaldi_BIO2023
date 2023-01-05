from collections import deque


def moves(state):
    newState = state.copy()
    possibleMoves = []

    for i in range(len(newState)):
        newState = state.copy()

        if newState[i] == "0":
            continue

        toMove = newState[i][len(newState[i]) - 1]
        if len(newState[i]) == 1:
            newState[i] = "0"
        else:
            newState[i] = newState[i][:-1]
        baseState = newState.copy()

        for j in range(4):
            newState = baseState.copy()
            if j != i and len(newState[j]) < 4:
                if newState[j] == "0":
                    newState[j] = ""
                newState[j] += toMove

                possibleMoves.append(newState.copy())

    return possibleMoves


def bfs(initialState, endState):
    seen = set()

    transforms = deque([(initialState, 0)])

    while deque:
        currentGame, numMoves = transforms.popleft()
        currentGame = tuple(currentGame)

        if currentGame in seen:
            continue

        seen.add(currentGame)

        nextGames = moves(list(currentGame))
        for i in nextGames:
            if list(i) == endState:
                return numMoves + 1
            transforms.append((i, numMoves + 1))


if __name__ == "__main__":

    print("Lorenzo Frescobaldi - Brighton College \n")

    initialGameIn = input("> ")
    endGameIn = input("> ")

    initialGameIn = initialGameIn.split(" ")
    endGameIn = endGameIn.split(" ")

    print(bfs(initialGameIn, endGameIn))
