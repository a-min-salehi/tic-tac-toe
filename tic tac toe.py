from random import *

welcome = '''

    hello welcome to the tic tac toe game

           '''

print(welcome)

theBoard = {'1': ' ', '2': ' ', '3': ' ',
            '4': ' ', '5': ' ', '6': ' ',
            '7': ' ', '8': ' ', '9': ' '}

board_keys = []

for key in theBoard:
    board_keys.append(key)


def printboard(board):
    print(' ' + board['1'] + ' | ' + board['2'] + ' | ' + board['3'])
    print(' -- + - + --')
    print(' ' + board['4'] + ' | ' + board['5'] + ' | ' + board['6'])
    print(' -- + - + --')
    print(' ' + board['7'] + ' | ' + board['8'] + ' | ' + board['9'])
    print("\n\n")


def win(b):
    return ((b['7'] == b['8'] == b['9'] != ' ') or
            (b['4'] == b['5'] == b['6'] != ' ') or
            (b['1'] == b['2'] == b['3'] != ' ') or
            (b['1'] == b['4'] == b['7'] != ' ') or
            (b['2'] == b['5'] == b['8'] != ' ') or
            (b['3'] == b['6'] == b['9'] != ' ') or
            (b['7'] == b['5'] == b['3'] != ' ') or
            (b['1'] == b['5'] == b['9'] != ' '))


def find_step(b, c):
    ll = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
    count = 1
    for i in ll:
        if b[i] == c:
            count += 1
    return count


def cpoint(thispoint):
    thelist = ['1', '3', '7', '9']
    for i in range(len(thelist)):
        if thelist[i] == thispoint:
            return thelist[3 - i]
    return 0


def apoint(point, badpoint):
    if (point == '1' and badpoint == '2') or (point == '9' and badpoint == '6'):
        return '7'
    elif (point == '1' and badpoint == '4') or (point == '9' and badpoint == '8'):
        return '3'
    elif (point == '3' and badpoint == '2') and (point == '7' and badpoint == '4'):
        return '9'
    elif (point == '3' and badpoint == '6') or (point == '7' and badpoint == '8'):
        return '1'


def oin(b, list):
    for i in list:
        if b[i] == 'O':
            return i
    return 0


def xcount(b, list):
    count = 0
    for i in list:
        if b[i] == 'X':
            count += 1
    return count


def odanger(b):
    if (b['7'] == b['8'] == 'O' or b['3'] == b['6'] == 'O' or b['1'] == b['5'] == 'O') and b['9'] == ' ':
        return '9'
    elif (b['7'] == b['9'] == 'O' or b['2'] == b['5'] == 'O') and b['8'] == ' ':
        return '8'
    elif (b['8'] == b['9'] == 'O' or b['1'] == b['4'] == 'O' or b['5'] == b['3'] == 'O') and b['7'] == ' ':
        return '7'
    elif (b['4'] == b['5'] == 'O' or b['3'] == b['9'] == 'O') and b['6'] == ' ':
        return '6'
    elif (b['4'] == b['6'] == 'O' or b['2'] == b['8'] == 'O' or b['7'] == b['3'] == 'O' or b['1'] == b['9'] == 'O') and \
            b['5'] == ' ':
        return '5'
    elif (b['5'] == b['6'] == 'O' or b['1'] == b['7'] == 'O') and b['4'] == ' ':
        return '4'
    elif (b['1'] == b['2'] == 'O' or b['6'] == b['9'] == 'O' or b['7'] == b['5'] == 'O') and b['3'] == ' ':
        return '3'
    elif (b['1'] == b['3'] == 'O' or b['5'] == b['8'] == 'O') and b['2'] == ' ':
        return '2'
    elif (b['2'] == b['3'] == 'O' or b['4'] == b['7'] == 'O' or b['5'] == b['9'] == 'O') and b['1'] == ' ':
        return '1'
    return 0


def xdanger(b):
    if (b['7'] == b['8'] == 'X' or b['3'] == b['6'] == 'X' or b['1'] == b['5'] == 'X') and b['9'] == ' ':
        return '9'
    elif (b['7'] == b['9'] == 'X' or b['2'] == b['5'] == 'X') and b['8'] == ' ':
        return '8'
    elif (b['8'] == b['9'] == 'X' or b['1'] == b['4'] == 'X' or b['5'] == b['3'] == 'X') and b['7'] == ' ':
        return '7'
    elif (b['4'] == b['5'] == 'X' or b['3'] == b['9'] == 'X') and b['6'] == ' ':
        return '6'
    elif (b['4'] == b['6'] == 'X' or b['2'] == b['8'] == 'X' or b['7'] == b['3'] == 'X' or b['1'] == b['9'] == 'X') and \
            b['5'] == ' ':
        return '5'
    elif (b['5'] == b['6'] == 'X' or b['1'] == b['7'] == 'X') and b['4'] == ' ':
        return '4'
    elif (b['1'] == b['2'] == 'X' or b['6'] == b['9'] == 'X' or b['7'] == b['5'] == 'X') and b['3'] == ' ':
        return '3'
    elif (b['1'] == b['3'] == 'X' or b['5'] == b['8'] == 'X') and b['2'] == ' ':
        return '2'
    elif (b['2'] == b['3'] == 'X' or b['4'] == b['7'] == 'X' or b['5'] == b['9'] == 'X') and b['1'] == ' ':
        return '1'
    return 0


def emptyhome(b, thelist):
    for i in thelist:
        if b[i] == ' ':
            return i
    return 0


def easy():
    n = randint(1, 9)
    n = str(n)
    return n


def medium(b, c):
    global step1
    step = find_step(b, c)
    corners = ['1', '3', '7', '9']
    sides = ['2', '4', '6', '8']
    if c == 'X':
        if b['1'] == b['3'] == b['7'] == b['9'] == ' ':
            step1 = choice(corners)
            return step1
        elif step == 2:
            if b[cpoint(step1)] == 'O' or oin(b, sides):
                step2 = easy()
            else:
                step2 = cpoint(step1)
            return step2
        elif step == 3:
            if xdanger(b):
                return xdanger(b)
            elif odanger(b):
                step3 = odanger(b)
                return step3
            else:
                return easy()
        elif step == 4:
            if xdanger(b):
                return xdanger(b)
            elif odanger(b):
                return odanger(b)
            else:
                return easy()
        elif step == 5:
            if xdanger(b):
                return xdanger(b)
            else:
                return easy()
    elif c == 'O':
        if step == 1:
            step1 = easy()
            return step1
        elif b['5'] == ' ':
            step1 = '5'
            return step1
        elif step == 2:
            if xdanger(b):
                step2 = xdanger(b)
                return step2
            elif step1 == '5':
                if xcount(b, corners) == 2:
                    step2 = choice(sides)
                    return step2
                step2 = choice(corners)
                return step2
            else:
                step2 = easy()
                return step2
        elif step == 3:
            if odanger(b):
                return odanger(b)
            elif xdanger(b):
                return xdanger(b)
            elif step1 == '5':
                return choice(sides)
            else:
                return choice(corners)
        elif step == 4:
            if odanger(b):
                return odanger(b)
            elif xdanger(b):
                return xdanger(b)
            else:
                return easy()


def hard(b, c):
    global step1
    step = find_step(b, c)
    corners = ['1', '3', '7', '9']
    sides = ['2', '4', '6', '8']
    if c == 'X':
        if b['1'] == b['3'] == b['7'] == b['9'] == ' ':
            step1 = choice(corners)
            return step1
        elif step == 2:
            if b[cpoint(step1)] == 'O' or oin(b, sides):
                step2 = '5'
            else:
                step2 = cpoint(step1)
            return step2
        elif step == 3:
            if xdanger(b):
                return xdanger(b)
            elif odanger(b):
                step3 = odanger(b)
                return step3
            elif oin(b, sides):
                badpoint = oin(b, sides)
                return apoint(step1, badpoint)
        elif step == 4:
            if xdanger(b):
                return xdanger(b)
            elif odanger(b):
                return odanger(b)
            else:
                return emptyhome(b, sides)
        elif step == 5:
            if xdanger(b):
                return xdanger(b)
            else:
                return easy()
    elif c == 'O':
        if b['1'] == b['3'] == b['7'] == b['9'] == ' ':
            step1 = choice(corners)
            return step1
        elif b['5'] == ' ':
            step1 = '5'
            return step1
        elif step == 2:
            if xdanger(b):
                step2 = xdanger(b)
                return step2
            elif step1 == '5':
                if xcount(b, corners) == 2:
                    step2 = choice(sides)
                    return step2
                step2 = choice(corners)
                return step2
            else:
                step2 = choice(corners)
                return step2
        elif step == 3:
            if odanger(b):
                return odanger(b)
            elif xdanger(b):
                return xdanger(b)
            elif step1 == '5':
                return choice(sides)
            else:
                return choice(corners)
        elif step == 4:
            if odanger(b):
                return odanger(b)
            elif xdanger(b):
                return xdanger(b)
            else:
                return easy()


def game():
    global computer
    turn = 'X'
    count = 0
    flag = 0
    player = turn
    menu = '''
           its the start menu choose an option :


           1 - two player game
           2 - play with computer
           3 - Exit

           '''
    c_menu = '''
               choose the level :

               1 - Easy
               2 - Medium
               3 - Impossible

               '''

    mood = input("{}".format(menu))
    c_mood = '1'

    while True:
        if mood == '1' or mood == '3':
            break
        elif mood == '2':
            c_mood = input(f"{c_menu}")
            while True:
                if c_mood == '1' or c_mood == '2' or c_mood == '3':
                    break
                else:
                    c_mood = input("\n\tEnter 1 , 2  or 3  the value that entered is invalid !!\n")
                    continue
            player = input("enter X or O to choose your role : ")
            while True:
                if player == 'X' or player == 'x':
                    computer = 'O'
                    break
                elif player == 'O' or player == 'o':
                    computer = 'X'
                    break
                else:
                    player = input("\n\tEnter X  or  O  the value that entered is invalid !!\n")
                    continue
            break
        else:
            mood = input("\n\tEnter 1 , 2  or 3  the value that entered is invalid !!\n")
            continue

    printboard(theBoard)

    while True:

        if mood == '3':
            flag = 1
            break

        elif mood == '2' and turn != player:
            if c_mood == '1':
                move = easy()

                if theBoard[move] == ' ':

                    theBoard[move] = turn
                    printboard(theBoard)
                    count += 1
                else:
                    continue
            elif c_mood == '2' and turn != player:
                move = medium(theBoard, computer)

                if theBoard[move] == ' ':

                    theBoard[move] = turn
                    printboard(theBoard)
                    count += 1
                else:
                    continue
            elif c_mood == '3' and turn != player:
                move = hard(theBoard, computer)

                if theBoard[move] == ' ':

                    theBoard[move] = turn
                    printboard(theBoard)
                    count += 1
                else:
                    continue
        else:

            print("It's your turn," + turn + ".Move to which place?")

            move = input()

            if theBoard[move] == ' ':

                theBoard[move] = turn
                printboard(theBoard)
                count += 1
            else:
                print("That place is already filled.\nMove to which place?")
                continue

        if count >= 5:
            if win(theBoard):
                printboard(theBoard)
                print("\nGame Over.\n")
                print(" **** " + turn + " won. ****")
                break

        # tie

        if count == 9:
            print("\nGame Over.\n")
            print("It's a Tie!!")
            break

        # change .

        if turn == 'X':
            turn = 'O'
        else:
            turn = 'X'

    if flag:
        restart = ""
    else:
        restart = input("Do you want to play Again?(y/n)")

    if restart == "y" or restart == "Y":
        for key in board_keys:
            theBoard[key] = " "
            mood = ""

        game()


if __name__ == "__main__":
    game()
