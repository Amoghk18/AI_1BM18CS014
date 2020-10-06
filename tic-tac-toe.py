import random
import time


def printBoard(board):
    print()
    print("----------------------- Board ----------------------------")
    print()
    print()
    for i in range(3):
        print("                     ", end="")
        for j in range(3):
            print(" " + str(board[i][j]) + " ", end="")
            if j != 2:
                print("|", end="")
        print()
        if i != 2:
            print("                      __+___+__ ")
    print()
    print()
    print("----------------------------------------------------------")

def insertToBoard(pos, board, user, unoccupied):
    row = pos // 3
    col = pos % 3
    if board[row][col] == 0:
        board[row][col] = user
        unoccupied.remove(pos)
        return 0
    else: 
        return -1

def getEmptyCells(board):
    return [(i, j) for i in range(3) for j in range(3) if board[i][j] == 0]

def minimax(board, depth, isMaximizing, user, scoreLookup):
    result = checkWinner(user, board)
    if result != None:
        return scoreLookup[result] 

    emptyCells = getEmptyCells(board)
    if len(emptyCells) == 0:
        return 0

    if isMaximizing:
        bestScore = -2000000
        for empty in emptyCells:
            board[empty[0]][empty[1]] = 9
            score = minimax(board, depth+1, not isMaximizing, user, scoreLookup)
            board[empty[0]][empty[1]] = 0
            bestScore = max(score, bestScore)
        return bestScore
    else:
        bestScore = 2000000
        for empty in emptyCells:
            board[empty[0]][empty[1]] = user
            score = minimax(board, depth+1, not isMaximizing, user, scoreLookup)
            board[empty[0]][empty[1]] = 0
            bestScore = min(score, bestScore)
        return bestScore


def makeMove(board, unoccupied, user):
    # randPos = random.choice(unoccupied)
    # board[randPos // 3][randPos % 3] = 9
    # unoccupied.remove(randPos)
    # print()
    # print("Computer chooses to insert at position " + str(randPos + 1))
    # print()
    emptyCells = getEmptyCells(board)
    bestMove = (-1, -1)
    bestScore = -2000000
    scoreLookup = {
        user : -1,
        9 : 10,
    }
    for move in emptyCells:
        board[move[0]][move[1]] = 9
        score = minimax(board, 0, False, user, scoreLookup)
        board[move[0]][move[1]] = 0
        if score > bestScore:
            bestScore = score
            bestMove = move
    board[bestMove[0]][bestMove[1]] = 9
    unoccupied.remove((bestMove[0] * 3) + bestMove[1])


def rowCheck(board, user):
    for i in range(3):
        if len(set(board[i])) == 1:
            if board[i][0] == user:
                return user
    return -1

def colCheck(board, user):
    for i,j,k in zip(board[0], board[1], board[2]):
        if len(set([i,j,k])) == 1:
            if i == user:
                return user
    return -1

def diaCheck(board, user):
    dia1 = board[0][0] == board[1][1] and board[1][1] == board[2][2]
    if dia1 == True:
        if board[0][0] == user:
            return user
    dia2 = board[0][2] == board[1][1] and board[1][1] == board[2][0]
    if dia2 == True:
        if board[0][2] == user:
            return user
    
    return -1

def runCheck(board, user):
    if rowCheck(board, user) == user:
        return user
    if colCheck(board, user) == user:
        return user
    if diaCheck(board, user) == user:
        return user
    
    return -1

def checkWinner(user, board):
    for i in [user, 9]:
        if runCheck(board, i) == i:
            return i

def startGame():
    print()
    print()
    print("                Welcome to Tic-Tac-Toe")
    board = [[0 for _ in range(3)] for _ in range(3)]
    print("                  Here is your Board")
    time.sleep(1)
    printBoard(board)
    print("Enter the your Identifier(Must Be a Number other than 9, computer is 9)")
    user = int(input("Your Identifier : "))
    print("Your identifier is : " + str(user))
    print()
    print("Let the game Begin!!!!!!!")
    print()
    winner = 0
    count = 0
    unoccupied = [i for i in range(9)]
    while winner not in [user, 9] and unoccupied:
        time.sleep(1)
        print()
        print("------------------- Make the move -------------------")
        print("Enter the position in which you want to put your Identifier")
        pos = int(input("Position on the board(1-9) : "))
        print()
        print("You choose to insert at position " + str(pos))
        if insertToBoard(pos-1, board, user, unoccupied) == -1:
            print()
            print("SORRY!!!")
            print("You cannot insert in a position where you/computer have already inserted \n (Hint : Choose a different position which is empty)")
            print("Board remains the same")
            print()
            continue
        count += 1
        print()
        print("Board after insertion by you is : ")
        printBoard(board)
        time.sleep(2)
        print()
        if count >= 3:
            winner = checkWinner(user, board)
        if winner in [user, 9] or unoccupied == []:
            break

        print("Now computer will make the move")
        makeMove(board, unoccupied, user)
        print("Board after insertion by computer is : ")
        printBoard(board)
        time.sleep(2)
        if count >= 3:
            winner = checkWinner(user, board)
    
    if winner == user:
        print("     Congratulations!!!")
        print("         You Won!")
    elif winner == 9:
        print("     Better Luck Next Time :)")
        print("         Computer Won!")
    else:
        print("     Try Harder Next Time!!!")
        print("          It's a Draw!")

startGame()