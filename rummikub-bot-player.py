import random






# tile = (colour, number, isJoker)




# tiles = {
#     "red": {
#         1: [2, 0],
#         2: [1, 0],
#         3: [1, 1]
#     }
# }








def init_pile():
   
   colours = ["black", "blue", "orange", "red"] # joker is also a colour, but isnt put here
   numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
   pile = {}
   
   
   for colour in colours:
      
      pile[colour] = {}
      
      for number in numbers:
         
         pile[colour][number] = [2, 0] # 2 fixed tiles, 0 jokers (representing the specific colour + number)
   
   
   pile["joker"] = {}
   
   pile["joker"][0] = [0, 2] # 2 jokers in this tile path 
   # pile = { "joker": {0: [0, 2]} }
   
   
   return pile
      




def init_deck(pile):
   
   deck = {}
   
   # initialises the deck's dict, all values set to 0
   colours = ["black", "blue", "orange", "red"] # joker is also a colour, but isnt put here
   numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
   
   for colour in colours:
         
         deck[colour] = {}
         
         for number in numbers:
            
            pile[colour][number] = [0, 0]
      
   deck["joker"] = {}
   
   deck["joker"][0] = [0, 0]
      
      
   # makes a list from the pile's dict so can choose a random tile
   pileList = []
   
   for _ in range(2):
      for colour, numbers in pile.items():
         for number, _ in numbers.items():
            pileList.append((colour, number))
   
   # chooses random tile
   for _ in range(14):
      tile = random.choice(pileList)
      pileList.remove(tile)
      
      colour, number = tile
      
      if number != 0: # if not joker
         deck[colour][number][0] += 1
         
      else: # if is joker
         deck[colour][number][1] += 1
      
      
   
   return deck, pile
      
      
      
      



# pack scanner algorithm:
# 
# conditions for a pack:
# 
# length >= 3
# 
# 
# 
#  - runs -> same colour, increment by 1 number from start, no max size (highest possible max 26, 2x13 tiles)
# 
#  - groups -> diff colour, same number, max size of 4
# 
# 
# 
#  search for runs optimisations:
#   - only search in the same colour key
#   - only search for +- 1 digit
#   - never start with joker
# 
#  search for groups optimisations:
#   - only search in different colour keys
#   - search for same digit
#   - never start with joker





def updateAvaliableTiles(deck, board):
   pass




def is_tile_in_path(colour, number, avaliableTiles):
   
   if avaliableTiles[colour][number] != [0, 0]:
      return True
   
   else:
      return False
   
   



COLOURS = ["black", "blue", "orange", "red"]
NUMBERS = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]



def find_run(avaliableTiles):
   
   global COLOURS, NUMBERS
   
   runLen = 0
   previousTile = (None, 0)
   
   
   # find a run
   for colour in COLOURS:
      
      
      for number in NUMBERS:
         
         currentTile = (colour, number)
         
         
         if is_tile_in_path(colour, number, avaliableTiles): # if tile is a member of the avaliable tiles
            
            if previousTile == (colour, number - 1): # tiles are in sequence
               runLen += 1
               
               
               
               
            
               
               
               
            
            
            
            
         previousTile = currentTile