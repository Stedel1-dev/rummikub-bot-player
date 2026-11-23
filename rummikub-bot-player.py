import random

# tile = ["colour", number]
# tile = ["black", 4]





# deck = {
#   "black": [ [1, False], [4, False], [4, False], [7, False] ],
#   "blue": [ [2, False], [5, False] ],
#   "orange": [ [3, False], [5, False], [5, False], [6, False], [11, False] ],
#   "red": []
#   "joker": [None, True]
# }
#



def init_pile():
   pile = []
   
   colours = ["black", "blue", "orange", "red"]
   numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
   
   for _ in range(2):
      for colour in colours:
         for number in numbers:
            pile.append([colour, number, False]) # [colour, number, isJoker]

      pile.append([None, None, True]) # joker tile
   
   return pile
      



def init_deck(pile):
   deck = {}
   
   for _ in range(14):
      tile = random.choice(pile)
      pile.remove(tile)
      
      add_to_deck(tile, deck)
      
   return deck
      
      
      
      
      
      


def tile_colour(tile):
   return tile[0]
   
   

def tile_num(tile):
   return tile[1]



def is_joker(tile):
   return tile[2]




def dist_between_tiles(tile1num, tile2num):
   loopSize = 13
      
   distance = abs((tile1num % loopSize) - (tile2num % loopSize))
   return distance



def add_to_deck(tile, deck):
   deck[tile_colour(tile)].append(tile_num(tile))
   print(f"LOG: tile {tile} added to deck")



def remove_from_deck(tile, deck):
   deck[tile_colour(tile)].remove(tile_num(tile))
   print(f"LOG: tile {tile} removed from deck")

