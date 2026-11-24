
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




pile = init_pile()

for colour, numbers in pile.items():
   for number, _ in numbers.items():
      print(colour, number)


