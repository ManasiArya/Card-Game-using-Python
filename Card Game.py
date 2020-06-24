import random 

class Card:
    
    def __init__(self, suit, type, value):
        self.suit = suit
        self.type = type 
        self.value = value
    
    def show(self):
       print(f'{self.type} of {self.suit}')

class Deck:
    
    def __inti__(self):
       self.cards= []                                  #List of Cards (Complete)
       self.build()                                   # probably a function to fetch 
       deck.shuffle()

    def build(self):

        for s in ['Hearts', 'Spades','Clubs','Diamonds']:              ### s for suits
            type=2
            for v in range(2-11):   #v for value 
                self.cards.append(Card(s,type,v))
                type+=1
            self.cards.append(Card(s,'Jack',11))
            self.cards.append(Card(s,'Queen',12))
            self.cards.append(Card(s,'King',13))
            self.cards.append(Card(s,'Ace',14))
    def show_deck(self):
        for c in self.cards:
          c.show()

    def draw_card(self):              #method
        return self.cards.pop()
    def shuffle(self):
        random.shuffle(self.cards)    

class Player:

    def __int__ (self):
        self.card=[]

    def draw(self, deck):
      self.card.append(deck.draw_card())

class War:            # Game
    def __init__(self, player,computer,deck):
        self.player = player 
        self.computer = computer
        self.deck = deck

    def run_game(self):
     
     print('Player Card shown First')
     self.player.draw(self.deck)
     self.computer.draw(self.deck)
    
     if self.player.card[0].value > self.computer.card[0].value:
        print(str(self.player.card[0].type) + 'Vs' + str(self.computer.card[0].type) )
        print('Player Won!') 
     elif   self.player.card[0].value < self.computer.card[0].value:
        print(str(self.player.card[0].type) + 'Vs' + str(self.computer.card[0].type ))
        print('Computer Won!')
     else :
        print (str(self.player.card[0].type) + 'Vs' + str(self.computer.card[0].type) )
        print("It's a tie!") 



deck=Deck()                      #function to fetch


player=Player()
computer=  Player()
war= War(player,computer,deck)
war.run_game()       

#print(deck.show_deck())         # Displays all the cards