#Square Game: make square of 1's while computer tries to stop you
#-------------------------------------------------------------------------------
def create_game():
    empty_list = [] 
    return (empty_list)

#-------------------------------------------------------------------------------

def game_start(empty_list):
    empty_list = [
        [0,0,0,0,0],
        [0,0,0,0,0],
        [0,0,0,0,0],
        [0,0,0,0,0],
        [0,0,0,0,0]
        ]
    start_list=empty_list
    print("GAME START")
    for row in range (len(start_list)):
        for column in range(len(start_list[row])):
            print (start_list[row][column],end=" ")
        print()
    print()
    
    return(start_list)

#-------------------------------------------------------------------------------
def player1(start_list,row_no,col_no):
    
    start_list[(row_no)-1][(col_no)-1]=1 #must minus one due to index easier for user
    for row in range (len(start_list)):
        for column in range(len(start_list[row])):
            print (start_list[row][column],end=" ")
        print()
    print()
    square(start_list,row_no,col_no)
    
    return(start_list)

#-------------------------------------------------------------------------------
def player2(start_list,row_no,col_no):
    print("PLAYER 2")
    import random
    
    start_list[random.randint(0,4)][random.randint(0,4)] = 2
    for row in range (len(start_list)):
        for column in range(len(start_list[row])):
            print (start_list[row][column],end=" ")
        print()
    print()

    start_list[random.randint(0,4)][random.randint(0,4)] = 2
    for row in range (len(start_list)):
        for column in range(len(start_list[row])):
            print (start_list[row][column],end=" ")
        print()
    print()

    check_game(start_list)
    next_round(start_list)

    return(start_list)

#-------------------------------------------------------------------------------
def square(start_list,row_no,col_no):
            if(start_list[0][0]==1 and start_list[0][1]==1 and start_list[1][0]==1 and start_list[1][1]==1):
                print("PLAYER 1 WINS!")
                
            elif(start_list[0][1]==1 and start_list[0][2]==1 and start_list[1][1]==1 and start_list[1][2]==1):
                print("PLAYER 1 WINS!")
                
            elif(start_list[0][2]==1 and start_list[0][3]==1 and start_list[1][2]==1 and start_list[1][3]==1):
                print("PLAYER 1 WINS!")
                
            elif(start_list[0][3]==1 and start_list[0][4]==1 and start_list[1][3]==1 and start_list[1][4]==1):
                print("PLAYER 1 WINS!")
                
            elif(start_list[1][0]==1 and start_list[1][1]==1 and start_list[2][0]==1 and start_list[2][1]==1):
                print("PLAYER 1 WINS!")
                
            elif(start_list[1][1]==1 and start_list[1][2]==1 and start_list[2][1]==1 and start_list[2][2]==1):
                print("PLAYER 1 WINS!")

            elif(start_list[1][2]==1 and start_list[1][3]==1 and start_list[2][2]==1 and start_list[2][3]==1):
                print("PLAYER 1 WINS!")

            elif(start_list[1][3]==1 and start_list[1][4]==1 and start_list[2][3]==1 and start_list[2][4]==1):
                print("PLAYER 1 WINS!")

            elif(start_list[2][0]==1 and start_list[2][1]==1 and start_list[3][0]==1 and start_list[3][1]==1):
                print("PLAYER 1 WINS!")
            
            elif(start_list[2][1]==1 and start_list[2][2]==1 and start_list[3][1]==1 and start_list[3][2]==1):
                print("PLAYER 1 WINS!")
            
            elif(start_list[2][2]==1 and start_list[2][3]==1 and start_list[3][2]==1 and start_list[3][3]==1):
                print("PLAYER 1 WINS!")
            
            elif(start_list[2][3]==1 and start_list[2][4]==1 and start_list[3][3]==1 and start_list[3][4]==1):
                print("PLAYER 1 WINS!")
            
            elif(start_list[3][0]==1 and start_list[3][1]==1 and start_list[4][0]==1 and start_list[4][1]==1):
                print("PLAYER 1 WINS!")
            
            elif(start_list[3][1]==1 and start_list[3][2]==1 and start_list[4][1]==1 and start_list[4][2]==1):
                print("PLAYER 1 WINS!")
            
            elif(start_list[3][2]==1 and start_list[3][3]==1 and start_list[4][2]==1 and start_list[4][3]==1):
                print("PLAYER 1 WINS!")
            
            elif(start_list[3][3]==1 and start_list[3][4]==1 and start_list[4][3]==1 and start_list[4][4]==1):
                print("PLAYER 1 WINS!")
            
            else:
                player2(start_list,row_no,col_no)

#-------------------------------------------------------------------------------
def check_game(start_list):
    counter = 0
    for x in start_list:
        for y in x:
            if y != 0:
                counter += 1
            if counter == 25:
                print("GAME OVER, YOU LOSE")
                exit()
                
#-------------------------------------------------------------------------------
def next_round(start_list):
    print("PLAYER-1")
    row_no=int(input("Enter row number: "))
    col_no=int(input("Enter column number: "))
    for i in start_list:
        while start_list[(row_no)-1][(col_no)-1]==(2):
            print()
            print("Position Occupied")
            row_no=int(input("Enter row number: "))
            col_no=int(input("Enter column number: "))
        while start_list[(row_no)-1][(col_no)-1]==(1):
            print()
            print("Position Occupied")
            row_no=int(input("Enter row number: "))
            col_no=int(input("Enter column number: "))
           
    start_list[(row_no)-1][(col_no)-1]=1
    for row in range (len(start_list)):
        for column in range(len(start_list[row])):
            print (start_list[row][column],end=" ")
        print()
    print()
    square(start_list,row_no,col_no)
    
    return(start_list)
#-------------------------------------------------------------------------------       
def main():
    print("Welcome to the square game!")
    print("Will you beat the computer?")
    print("---------------------------")
    empty_list=create_game()
    start_list=game_start(empty_list)
    print("PLAYER-1")
    row_no=int(input("Enter row number: "))
    col_no=int(input("Enter column number: "))
    
    player1(start_list,row_no,col_no)
    
    
main()

 

