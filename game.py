import algo
positions = {}
for p in range(1, 10):
    positions[p] = str(p)

board = '   |   |   \n {} | {} | {} \n   |   |   \n-----------\n   |   |   \n {} | {} | {} \n   |   |   \n-----------\n   |   |   \n {} | {} | {} \n   |   |   '


def print_board(counter=1):
    print(board.format(positions[1], positions[2], positions[3], positions[4], positions[5], positions[6], positions[7],
                       positions[8], positions[9]))
    if counter > 9:
        print("WINNER!")
        pass
    else:
        if counter % 2 == 0:
            o_place = int(input("O's Turn!\nPick a position: "))
            positions[o_place] = "O"
            counter += 1
        else:
            x_place = int(input("X's Turn!\nPick a position: "))
            positions[x_place] = "X"
            counter += 1
    if algo.checkWinner(positions) == 'X':
        print_board(counter)
        print("X WINS!")
    elif algo.checkWinner(positions) == 'O':
        print_board(counter)
        print("O WINS!")
    else:
        return print_board(counter)


print_board()
