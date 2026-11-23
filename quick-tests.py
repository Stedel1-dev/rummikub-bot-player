import random

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
   deck = {"black": [],
           "blue": [],
           "orange": [],
           "red": [],
           "joker": []
           }
   
   for _ in range(14):
      tile = random.choice(pile)
      pile.remove(tile)
      
      add_to_deck(tile, deck)
      
   return deck




def add_to_deck(tile, deck):
   print(tile)
   if tile_colour(tile) is not None:
      deck[tile_colour(tile)].append(tile_num(tile))
      
   else:
      deck["joker".append(None)]
      
   print(f"LOG: tile {tile} added to deck")
   
   
   
   
   
def tile_colour(tile):
   return tile[0]
   
   

def tile_num(tile):
   return tile[1]




pile = init_pile()

deck = init_deck(pile)

print(deck)