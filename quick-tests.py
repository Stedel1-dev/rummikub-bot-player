deck = {
   "black": [1, 4, 4, 7],
   "blue": [2, 5],
   "orange": [3, 5, 5, 6, 11],
   "red": []
}


tile = ["red", 1]


def tile_colour(tile):
   return tile[0]
   
   

def tile_num(tile):
   return tile[1]




def add_to_deck(tile, deck):
   deck[tile_colour(tile)].append(tile_num(tile))
   
   print(f"LOG: tile {tile} added to deck")
   


add_to_deck(tile, deck)

print(deck)