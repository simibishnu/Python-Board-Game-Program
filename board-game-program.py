#Name: Simi Bishnu
#Student Number: 101264827
#for assignment 6
#special features include numbered tiles and extra turns (the player gets an extra turn if they roll the same number on both die)


import random
import pygame
pygame.init()

#creating a display board
#flags = pygame.SCALED | pygame.RESIZABLE
board = pygame.display.set_mode((900,800))

#colours for player A and player B
colourA = ((102,119,97))
colourB = ((173,106,108))

#max number of columns and rows
maxcol = 8
maxrow = 7

#current column and rows for player A and player B set to 0 initially, z_A and z_B are counters for the rows, which are also set to 0 initially
cur_col_A = 0
cur_row_A = 0
z_A = 0
cur_col_B = 0
cur_row_B = 0
z_B = 0

#setting the dice total equal to 0 initially
dicetotal = 0

#activeplayer will be used to toggle turns between each player
activeplayer = True

#initial positions of player A and player B
positionA = (20,30)
positionB = (50,50)


#function for the checker board surface
def board_surface():

    
    #flags = pygame.SCALED | pygame.RESIZABLE

    #squares are 100x100, the board is 9 squares x 8 squares (aka 900x800)
    squaredim = 100
    width_in_squares = 9
    height_in_squares = 8

    #square colours that the loop will toggle between
    squarecolour1 = ((59,98,145))
    squarecolour2 = ((194,168,62))
    currentcolour = squarecolour1

    #font for the numbers
    game_font = pygame.font.Font(None,30)

    #creating a window to draw the squares on
    board = pygame.display.set_mode((squaredim*width_in_squares,squaredim*height_in_squares))
    
    #counter for the numbers on each tile
    num = 0

    for i in range (0,height_in_squares):
    #j is for columns
        for j in range (0,width_in_squares):
        
            #num is for numbering the tiles, will go up by 1 each for tile
            num = num+1
            
            #drawing square tiles on the board
            pygame.draw.rect(board,currentcolour,(j*squaredim,i*squaredim,squaredim,squaredim))
        
            #toggling between tile colours in the columns
            if currentcolour == squarecolour1:
                currentcolour = squarecolour2
            else:
                currentcolour = squarecolour1

            #adding text to each tile to number them
            text = game_font.render(str(num),True,(0,0,0))
            board.blit(text, (j*squaredim, i*squaredim))

    #toggling between tile colours in the rows
    if currentcolour == squarecolour1:
        currentcolour = squarecolour2        
    else:
        currentcolour = squarecolour1

#giving the user game instructions to understand the game play the computer players are doing
print("GAME INSTRUCTIONS:")
print("1. To move, players roll two 4-sided dice.")
print("2. If the player rolls the same number on die 1 and 2, then they get to roll again.")
print("3. In order to win the game, players must land on the last tile. If they're in the last row, and roll a number higher than the amount of spaces needed to get to the end (meaning they'll go off the board), then they'll have to count up and start back around from the beginning of the row.")
print("For example, if player A is at tile 70 and they roll a 4, they'll go up the 2 spaces to the end, and then they'll go back to the beginning of the row to go up the remaining 2 spaces to tile 65.")

#drawing the initial positions of player A and player B and updating the display
board_surface()
pygame.draw.circle(board,colourA,(positionA),10)
pygame.draw.circle(board,colourB,(positionB),10)
pygame.display.update()


#main game loop
while True:

    #players will use two 4-sided die (2d4)
    dice1 = random.randint(1,4)
    dice2 = random.randint(1,4)
    
    #the total number of spaces the players will go up by will be determined by adding up the numbers dice1 and dice2 land on
    dicetotal = dice1+dice2

    #this is to display whose turn it is 
    print("\n")
    print(activeplayer)

    #when it's player A's turn, this is what will happen
    if activeplayer == True:
        
        #calling board_surface again and redrawing where the other player is. this is to give the illusion that a player is moving from one tile to another without erasing the other player who isn't moving
        board_surface()
        pygame.draw.circle(board,colourB,(positionB),10)
        
        #this is to tell the user what numbers player A rolled
        print("player A has rolled a", dice1,"and a",dice2)

        #adding the dicetotal to player A's current column
        cur_col_A = cur_col_A + dicetotal

        #if the current column is less than 8 (the columns are numbered 0-8), the row doesn't increase and stays the same
        if cur_col_A <= maxcol:
            cur_row_A = z_A
        
        #if the current column is greater than 8, then program subtracts the current column by 9 in order to make player go to the next row (eg. if a player is at column 8 and rolls a 4 then their current column becomes 12 (8+4). to move up the board, the player needs to go to the next row at column at 3 (12-9). it makes more sense when you see what the board looks like)
        else:
            cur_col_A = cur_col_A - 9
            
            #if the current row is less than 7 (the rows are numbered 0-7), then the row will be added by 1. then the row counter will be set to what the current row is.
            if cur_row_A < maxrow:
              cur_row_A = cur_row_A + 1
            z_A = cur_row_A
        
        #this is to show what column and row player A is at
        print("player A is now at",cur_row_A,",",cur_col_A)
        
        #if the player rolls the same two numbers, then they get have another turn. otherwise, it's the other player's turn
        if dice1 == dice2:
            activeplayer = True
        else:
            activeplayer = False
        
        #calculting the position of the player using the column and the row they're at
        positionA = (((cur_col_A*100)+20,(cur_row_A*100)+30))
        #this is to show the position of the player on the board
        print(positionA)
        
        #drawing the player's piece, updating the display, and adding a delay so the gameplay isn't too fast
        pygame.draw.circle(board,colourA,(positionA),10)
        pygame.display.update()
        pygame.time.delay(3000)

    #player B's move, everything described above applies here too
    else:
        
        board_surface()
        pygame.draw.circle(board,colourA,(positionA),10)
        print("player B has rolled a", dice1,"and a",dice2)
        cur_col_B = cur_col_B + dicetotal
        if cur_col_B <= maxcol:
            cur_row_B = z_B
        else:
            cur_col_B = cur_col_B - 9
            if cur_row_B < maxrow:
              cur_row_B = cur_row_B + 1
            z_B = cur_row_B

        print("player B is now at",cur_row_B,",",cur_col_B)

        if dice1 == dice2:
            activeplayer = False
        else:
            activeplayer = True
        
        positionB = (((cur_col_B*100)+50,(cur_row_B*100)+50))
        print(positionB)

        pygame.draw.circle(board,colourB,(positionB),10)
        pygame.display.update()
        pygame.time.delay(3000)

    
    if (cur_col_A*cur_row_A)>=(maxcol*maxrow) or (cur_col_B*cur_row_B)>=(maxcol*maxrow):
        break

#event loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

