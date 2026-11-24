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
   

   colours = ["black", "blue", "orange", "red"] # joker is also a colour, but isnt put here
   numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
   
   for colour in colours:
         
         deck[colour] = {}
         
         for number in numbers:
            
            pile[colour][number] = [0, 0]
      
   deck["joker"] = {}
   
   deck["joker"][0] = [0, 0]
      
      
      
   pileList = []
   # makes a list from the dict (pile)
   for _ in range(2):
      for colour, numbers in pile.items():
         for number, _ in numbers.items():
            pileList.append((colour, number))
   
   
   for _ in range(14):
      tile = random.choice(pileList)
      pileList.remove(tile)
      
      colour, number = tile
      
      deck[colour] = {}
      deck[colour][number] 
      
      
      
   
   
   
   return deck, pile
      
      
      
      






def dist_between_tiles():
   
   
   return distance



def add_to_deck():




def remove_from_deck():
   
