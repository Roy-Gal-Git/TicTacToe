import algo
positions = {}
for p in range(1, 10):
    positions[p] = str(p)

board = '   |   |   \n {} | {} | {} \n   |   |   \n-----------\n   |   |   \n {} | {} | {} \n   |   |   \n-----------\n   |   |   \n {} | {} | {} \n   |   |   '


class NotInRange(Exception):
    pass


def mapBoard():
    print(board.format(positions[1], positions[2], positions[3], positions[4], positions[5], positions[6], positions[7],
                       positions[8], positions[9]))


def get_input(player):
    while True:
        try:
            user_input = int(input(player + "'s turn!\nPick a position: "))

            if user_input < 1 or user_input > 9:
                raise NotInRange

            return user_input

        except ValueError as e:
            print("Please enter a number between 1-9!\n")

        except NotInRange:
            print("Please enter a number between 1-9!\n")


def print_map(counter=1):
    mapBoard()
    if counter > 9:
        print("WINNER!")
        pass
    else:
        if counter % 2 == 0:
            o_place = get_input("O")
            positions[o_place] = "O"
            counter += 1
        else:
            x_place = get_input("X")
            positions[x_place] = "X"
            counter += 1
    if algo.checkWinner(positions) == 'X':
        mapBoard()
        print("X WINS!")
    elif algo.checkWinner(positions) == 'O':
        mapBoard()
        print("O WINS!")
    else:
        return print_map(counter)


def exit_func():
    print("Press ctrl + c to exit: ")
    while True:
        pass


print_map()
exit_func()
