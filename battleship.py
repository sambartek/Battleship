from random import randint
#import time
board = []

for x in range(5):
    board.append(["O"] * 5)

def print_board(board):
    for row in board:
        print " ".join(row)

print "Let's play Battleship!"
print "You get five tries!"
print_board(board)

def random_row(board):
    return randint(0, len(board)-1)

def random_col(board):
    return randint(0, len(board[0])-1)

ship_row = random_row(board)
ship_col = random_col(board)
#print ship_row
#print ship_col

# Everything from here on should go in your for loop!
# Be sure to indent four spaces!
for turn in range(5):
    guess_row = int(raw_input("Guess Row:")) - 1 
    guess_col = int(raw_input("Guess Col:")) - 1

    if guess_row == ship_row and guess_col == ship_col:
       print "Congratulations! You sunk my battleship!"
       #board[guess_row][guess_col] = "!"
       break
    else:
        if (guess_row < 0 or guess_row > 5) or (guess_col < 0 or guess_col > 5):
            print "What are you aiming for?"
            print "That's not even in the ocean!"
        elif(board[guess_row][guess_col] == "X"):
            print "You guessed that one already."
        else:
            print "Haha! You missed my battleship!"
            board[guess_row][guess_col] = "X"
    if turn == 4:
        print "Game Over"
    	#time.sleep(3)
    	#print "Loser"
    print "Turn", turn + 1
    print_board(board)
    