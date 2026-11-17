
COLOURS = ["black", "blue", "orange", "red"]
NUMBERS = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]



# tile = ["black", 4]





# [ ["black", [tiles] ],["blue", [tiles] ],["orange", [tiles] ],["red", [tiles] ] ]



def tile_colour(tile):
   return tile[0]
   
   

def tile_num(tile):
   return tile[1]



def dist_between_tiles(tile1num, tile2num):
   loopSize = 13
      
   distance = abs((tile1num % loopSize) - (tile2num % loopSize))
   return distance



def colour_to_index(colour):
   if colour == "black":
      return 0
   
   elif colour == "blue":
      return 1
   
   elif colour == "orange":
      return 2
   
   elif colour == "red":
      return 3




def sort_deck(deck):
   for tile in deck:
      for colour in COLOURS:
         if tile_colour(tile) == colour:
            deck[colour_to_index(colour)][1].append(tile)