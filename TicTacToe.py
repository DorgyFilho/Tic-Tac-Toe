import random

def TTT():
   game = '''       Positions
   |   |           7 | 8 | 9  
---+---+---       ---+---+---
   |   |           4 | 5 | 6
---+---+---       ---+---+--- 
   |   |           1 | 2 | 3      
'''
   pos = [None,
   (5, 1), #1
   (5, 5), #2
   (5, 9), #3
   (3, 1), #4
   (3, 5), #5
   (3, 9), #6
   (1, 1), #7
   (1, 5), #8
   (1, 9), #9
]

   Win = [
         [ 1, 2, 3],
         [ 4, 5, 6],     #Lines
         [ 7, 8, 9],
         [ 7, 4, 1],     
         [ 8, 5, 2],     #Columns
         [ 9, 6, 3],
         [ 7, 5, 3],     #Diagonal
         [ 1, 5, 9]
      ]
   table = []
   for elem in game.splitlines():
      table.append(list(elem))

   You = 'X'
   play = True
   rounds = 0
   while True:
      for k in table:
         print(''.join(k))
      
      if not play:
         break
      
      if rounds == 9:
         print('Draw!')
         break

      Turn = int(input('Choose a value from 1 to 9(You = {}): '.format(You)))
      if not (1 <= Turn <= 9):
         print('Invalid Move!')
         continue
      if table[pos[Turn][0]][pos[Turn][1]] != " ":
         print("You Can't Move!")
         continue
      table[pos[Turn][0]][pos[Turn][1]] = You
         
      for w in Win:
         for z in w:
            if table[pos[z][0]][pos[z][1]] != You:
               break
         else:
            print('{} Wins {}'.format(You, z))
            play = False
            break
      You = 'X' if You == 'O' else 'O'
      rounds += 1

TTT()






   