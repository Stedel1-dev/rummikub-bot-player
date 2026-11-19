# tile = ["colour", number]
# tile = ["black", 4]





# deck = {
#   "black": [1, 4, 4, 7],
#   "blue": [2, 5],
#   "orange": [3, 5, 5, 6, 11],
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
   deck[tile_colour].append(tile_num(tile))
   print(f"LOG: tile {tile} added to deck")



def remove_from_deck(tile, deck):
   deck[tile_colour].remove(tile_num(tile))
   print(f"LOG: tile {tile} removed from deck")

