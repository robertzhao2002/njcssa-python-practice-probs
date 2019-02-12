from turtle import *
import numpy as np

<<<<<<< HEAD
=======
t = turtle.Turtle()
screen = turtle.Screen()

# slow mode:
# t.speed(10)


#optmizations:
t.speed(0)
screen.tracer(100, 1)
t.hideturtle()

screenx = screen.screensize()[0]
screeny = screen.screensize()[1]

# this function draws a rectangle around the screen to show board
def draw_bounding():
    t.penup()
    t.goto(-screenx, screeny)
    t.pendown()
    for i in range(2):
        t.forward(screenx*2)
        t.right(90)
        t.forward(screeny*2)
        t.right(90)
    t.penup()


>>>>>>> d915d1e328c4072d1b5ca97a74f667118d93ad14
def createBoard(sideLength):
    b = np.zeros((sideLength,sideLength))
    color('red', 'yellow')
    begin_fill()
    counter = 0;
    startX = 0
    startY = 0
    for x in range(sideLength*sideLength):
        i = 0
        while i< 4:
            forward(50)
            left(90)
            i +=1
        penup()
        if counter < sideLength - 1:
            goto(startX-50, startY)
            startX-=50
            counter+=1
        elif x!= sideLength*sideLength -1:
            goto(startX+50*(sideLength-1), startY-50)
            startX=startX+50*(sideLength-1)
            startY-=50
            counter = 0
        pendown()       
    penup()
    goto(startX+50*(sideLength-1), startY)
    pendown()
    end_fill()
    done()
    return b

boardSet = False
while(not boardSet):
    size = input()
    try:
        board = createBoard(int(size))
        boardSet  = True
    except ValueError:
        print("Invalid board size")

def leftDiag():
    global board
    count = 0
    for i in range(len(board)-1):
        count = 0
        for j in range(len(board)-1):
            if((board[i][j] == board[i+1][j+1]) and (board[i][j] != 0 and board [i+1][j+1] != 0)):
                count +=1
                if(count == len(board) -1):
                    return True
    return False

def rightDiag():
    global board
    count = 0
    for i in range(len(board)-1):
        count = 0
        for j in range(len(board)-1,1,-1):
            if((board[i][j] == board[i+1][j-1]) and (board[i][j] != 0 and board [i+1][j-1] != 0)):
                count +=1
                if(count == len(board) -1):
                    return True
    return False

def colEqual():
    global board
    count = 0
    for i in range(len(board[0])):
        count = 0
        for j in range(len(board)-1):
            if((board[j][i] == board[j+1][i]) and (board[j][i] != 0 and board [j+1][i] != 0)):
                count +=1
                if(count == len(board) -1):
                    return True
    return False

def rowEqual():
    global board
    count = 0
    for i in range(len(board)):
        count = 0
        for j in range(len(board[i])-1):
            if ((board[i][j] == board[i][j+1]) and (board[i][j] != 0 and board[i][j+1] != 0)):
                count += 1
                if(count == len(board) - 1):
                    return True
    return False

def printPos():
    global board
    x=[]
    for i in range(len(board)):
        x.append([])
        for j in range(len(board[i])):
            x[i].append(' ')
    for i in range(len(x)):
        for j in range(len(x[i])):
            x[i][j]=str(i)+str(j)
    for i in x:
        print(i)

def printBoard():
    global board
    for i in board:
        print(i)

def boardFilled():
    global board
    for i in board:
        for j in i:
            if j == 0:
                return False
    return True

def game():
    global board
    print('Position Names to Type')
    printPos()
    turn = 1
    while((not colEqual()) and (not rowEqual()) and (not leftDiag()) and (not rightDiag()) and (not boardFilled())):
        move = input()
        try:
            if(board[int(move[0])][int(move[1])]==0):
                board[int(move[0])][int(move[1])]=turn
                printPos()
                printBoard()
                if turn == 1:
                    turn = 2
                else:
                    turn = 1
            else:
                print("Spot taken. Try again")  
        except ValueError:
            if(move == "exit"):
                break
            else:
                print("Invalid input")  
    if (colEqual() or rowEqual() or leftDiag() or rightDiag()):
        print("Congratulations Player " + str(3-turn) + " Wins!!")
    elif (boardFilled()):
        print("TIE GAME!!!")

game()
