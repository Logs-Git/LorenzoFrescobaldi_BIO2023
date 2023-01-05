from collections import deque


def moves(state):
    possibleMoves =
    newState = state

    for i in range(len(newState)):
        toMove = newState[i][len(newState[i]) - 1]
        if len(newState[i]) == "1":
            newState[i] = "0"
        else:
            newState[i] = newState[i][:-1]

        for j in range(4):
            if j != i and len(newState[j]) < 4:
                if newState[j] == "0":
                    newState[j] == ""
                newState[j] += toMove
                possibleMoves.append(newState)
                newState[j] = newState[j][:-1]

    return possibleMoves


def bfs(initialState, endState):
    print("no")


if __name__ == "__main__":

    userin = "1 2 3 4"

    userin = userin.split(" ")

    print(userin)

    print(moves(userin))