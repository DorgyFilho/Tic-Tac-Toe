import random

#1 - Second Option Mode
s=[0,1,2,
    3,4,5,
    6,7,8]

def Board():

    #Show The Board

    print(s[0], '|' , s[1], '|', s[2])
    print('--------')
    print(s[3], '|' , s[4], '|', s[5])
    print('--------')
    print(s[6], '|' , s[7], '|', s[8])

#Check Lines!
def Lines(char, s1, s2, s3):
    if s[s1] == char and s[s2] == char and s[s3] == char:
        return True

#The Winner!!!
def Winner(char):
    if Lines(char, 0, 1, 2):
        return True
    if Lines(char, 3, 4, 5):  #Lines
        return True
    if Lines(char, 6, 7, 8):
        return True
    
    if Lines(char, 0, 3, 6):
        return True
    if Lines(char, 1, 4, 7):  #Columns
        return True
    if Lines(char, 2, 5, 8):
        return True
    
    if Lines(char, 0, 4, 8):
        return True           #Diagonal
    if Lines(char, 2, 4, 6):
        return True

def Game(): 
    Win = None
    while Win != 'o': #CPU Can't Win!!!
        Board()
        Player = input('Choose an Option From 0 to 8: ')
        move = int(Player)
        if s[move] != 'X' and s[move] != 'o':
            s[move] = 'X'

            #Did You Win?
            if Winner('X') == True:
                Win = 'X'
                print()
                print('Yes! Yes! You Win!!!')
                break
        
            #Cpu's Turn
            while True:
                random.seed() #Randomic Generator!
                CPU = random.randint(0,8)
                if s[CPU] != 'o' and s[CPU] != 'X':
                    s[CPU] = 'o'
            
                    #Is CPU Winner?
                    if Winner('o') == True:
                        Win = 'o'
                        print()
                        print('CPU Wins!!!')
                        break
                    break
        else:
            print('Slot not available.')

#2 - Second Game Option.
def PvP():
    #Position Generator
    board = '''       Positions
   |   |           7 | 8 | 9  
---+---+---       ---+---+---
   |   |           4 | 5 | 6
---+---+---       ---+---+--- 
   |   |           1 | 2 | 3      
'''
    pos = [None, (5,1), (5,5), (5,9), (3,1), (3,5), (3,9), (1,1), (1,5), (1,9)]
    #              1      2      3      4      5      6      7      8      9

    Win = [[ 1,2,3], [ 4,5,6], [ 7,8,9], [ 7,4,1], [ 8,5,2], [ 9,6,3], [ 7,5,3], [ 1,5,9]]
    #                  #Lines                    #Columns                    #Diagonal

    table = []
    for i in board.splitlines():
        table.append(list(i))
    
    #2 Players
    You = 'X'
    Play = True
    rounds = 0 #9 rounds
    while True:
        for k in table:
            print(''.join(k))

        if not Play:
            break
        
        if rounds == 9:
            print()
            print('TIE!')
            break

        #The Game is On.            
        Turn = int(input('Choose an Option From 1 to 9 (You = {}): '.format(You)))
        if not (1 <= Turn <= 9):
            print('Invalid Move')
            continue
        if table[pos[Turn][0]][pos[Turn][1]] != " ":
            print('You Cannot Move!')
            continue
        table[pos[Turn][0]][pos[Turn][1]] = You

        #Check The Winner!
        for x in Win:
            for y in x:
                if table[pos[y][0]][pos[y][1]] != You:
                    break
            else:
                print()
                print('{} Wins {}'.format(You, y))
                Play = False
                break
        You = 'X' if You == 'O' else 'O'
        rounds += 1

#Main Program!
def main():
    print('Welcome To The Tic Tac Toe! Choose Your Mode\n1-Player Vs Cpu\n2-Player vs Player\n3-Quit')
    print()
    opt = input('Option: ')
    if opt == '1':
        Game()
    elif opt == '2':
        PvP()
    elif opt == '3':
        print('Turn Off!')
        exit()
    else:
        print('Invalid Answer!')

main()




