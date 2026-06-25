import random                    #random module genrally used to randomlly select anything 
                                            #In our it is used to randomlly select number
board = [0,1,2,
            3,4,5,                   #here we had created a list named board containg no from 0-8
            6,7,8]
def show():
        print(board[0],'|',board[1],'|',board[2])
        print('---------')
        print(board[3],'|',board[4],'|',board[5])                    #here we had created a function name show()
        print('---------')                                                           #this is used to create the grid of tic tac toe
        print(board[6],'|',board[7],'|',board[8])
str=("WELCOME TO THE WORLD OF TIC-TAC-TOE!!!")       #here this is the title
str1=str.center(100)                                                              #---.center func is used to place title in center
print(str1)
show()
check=True                                                                          # this is the main loop
while check:
        a = int(input("SELECT A SPOT : "))                         #user input to manually select the space
        if(board[a] != 'x' and board[a] != 'o'):                    #here if user input spot is not eqaul to x or o then it wil assign the spot as X
                board[a] = 'x'
                if    (board[0] == board[1] == board[2] =='x'
                   or board[3] == board[4] == board[5] == 'x'
                   or board[6] == board[7] == board[8] == 'x'
                   or board[0] == board[3] == board[6] == 'x'   #this if statement is used to check whether the player had won or not
                   or board[1] == board[4] == board[7] == 'x'   #here we had typed those patterns which makes user win the game
                   or board[2] == board[5] == board[8] == 'x'
                   or board[0] == board[4] == board[8] =='x'
                   or board[2] == board[4] == board[6] =='x'):
                        print('----YOU WON----')             #if any of the above mentioned patterns are forming the player will won
                        check=False                                     #and the gsme will end.
                find=True
                while find:                                             #this is the opponent side
                        random.seed()                        #both are under random module here (0,8) refer to the no. to be selected
                        b = random.randint(0,8)         #starting from 0 to 8 which is represented by 'b'
                        if(board[b] != 'o' and board[b] != 'x'): #here also created same if stament as above if the given spot is not eqaul to o or x then it will be assign as 'O'
                                board[b] = 'o'                                 #but we had placed this in a while loop bcoz sometimes it misses a spot bocz that spot is already used
                                find = False                                     #if the choosen spot is already taken then it will again search for another spot but if the choosen spoti is empty
                                if(board[0] == board[1] == board[2] =='o'                              #& a ssigned by o then the loop will break
                                   or board[3] == board[4] == board[5] == 'o'
                                   or board[6] == board[7] == board[8] == 'o'
                                   or board[0] == board[3] == board[6] == 'o'
                                   or board[1] == board[4] == board[7] == 'o'                     #here we had created same statement as above to choose for winner
                                   or board[2] == board[5] == board[8] == 'o'
                                   or board[0] == board[4] == board[8] =='o'
                                   or board[2] == board[4] == board[6] =='o'):
                                        print('----PYTHON WON----')
                                        check=False                                                               #here also if python won the game the game will end

        else:
                 print("SPOT IS ALREADY TAKEN!!")               #this else statement is used to display whether the user input spot is taken or not

        show()                                                            #this is used to display the grid after every step.
