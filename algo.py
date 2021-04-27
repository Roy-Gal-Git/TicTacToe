def checkWinner(positionsDict):
    keysList = [[1, 2, 3],
                [4, 5, 6],
                [7, 8, 9]]

    diagX = [0, 0]
    diagO = [0, 0]
    rowX = [0, 0, 0]
    rowO = [0, 0, 0]
    colX = [0, 0, 0]
    colO = [0, 0, 0]

    for i in range(len(keysList)):
        # Check if there are 3 of the same char in the first diagonal
        if positionsDict[keysList[i][i]] == 'X':
            diagX[0] += 1
        elif positionsDict[keysList[i][i]] == 'O':
            diagO[0] += 1

        # Check if there are 3 of the same char in the second diagonal
        if positionsDict[keysList[len(keysList[i]) - 1 - i][i]] == 'X':
            diagX[1] += 1
        elif positionsDict[keysList[len(keysList[i]) - 1 - i][i]] == 'O':
            diagO[1] += 1

        for j in range(len(keysList)):

            # Check if there are 3 of the same char in the same row
            if positionsDict[keysList[i][j]] == 'X':
                rowX[i] += 1
            elif positionsDict[keysList[i][j]] == 'O':
                rowO[i] += 1

            # Check if there are 3 of the same char in the same column
            if positionsDict[keysList[j][i]] == 'X':
                colX[i] += 1
            elif positionsDict[keysList[j][i]] == 'O':
                colO[i] += 1

    for val in diagX:
        if val == 3:
            return 'X'
    for val in diagO:
        if val == 3:
            return 'O'
    for val in rowX:
        if val == 3:
            return 'X'
    for val in rowO:
        if val == 3:
            return 'O'
    for val in colX:
        if val == 3:
            return 'X'
    for val in colO:
        if val == 3:
            return 'O'
