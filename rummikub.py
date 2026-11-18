
COLOURS = ["black", "blue", "orange", "red"]
NUMBERS = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]


# tile = ["colour", number]
# tile = ["black", 4]





# deck = {
#   "black": [1, 4, 4, 7],
#   "blue": [2, 5],
#   "orannge": [3, 5, 5, 6, 11],
#   "red": []
# }
#




def tile_colour(tile):
   return tile[0]
   
   

def tile_num(tile):
   return tile[1]



def dist_between_tiles(tile1num, tile2num):
   loopSize = 13
      
   distance = abs((tile1num % loopSize) - (tile2num % loopSize))
   return distance



def add_to_deck(tile, deck):
   deck.update({tile_colour(tile): deck[tile_colour].append(tile_colour(tile))})
   print(f"LOG: tile {tile} added to deck")

def remove_from_deck(tile, deck):
   deck.update({tile_colour(tile): deck[tile_colour].remove(tile_colour(tile))})
   print(f"LOG: tile {tile} removed from deck")




def sort_deck(deck):
   for tile in deck:
      for colour in COLOURS:
         if tile_colour(tile) == colour:
            