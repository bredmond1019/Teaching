#####################################
### WELCOME TO YOUR OOP PROJECT #####
#####################################

# For this project you will be using OOP to create a card game. This card game will
# be the card game "War" for two players, you an the computer. If you don't know
# how to play "War" here are the basic rules:
#
# The deck is divided evenly, with each player receiving 26 cards, dealt one at a time,
# face down. Anyone may deal first. Each player places his stack of cards face down,
# in front of him.
#
# The Play:
#
# Each player turns up a card at the same time and the player with the higher card
# takes both cards and puts them, face down, on the bottom of his stack.
#
# If the cards are the same rank, it is War. Each player turns up three cards face
# down and one card face up. The player with the higher cards takes both piles
# (six cards). If the turned-up cards are again the same rank, each player places
# another card face down and turns another card face up. The player with the
# higher card takes all 10 cards, and so on.
#
# There are some more variations on this but we will keep it simple for now.
# Ignore "double" wars
#
# https://en.wikipedia.org/wiki/War_(card_game)

from random import shuffle

# Two useful variables for creating Cards.
SUITE = 'H D S C'.split()
RANKS = '2 3 4 5 6 7 8 9 10 J Q K A'.split()



class Deck:
    """
    This is the Deck Class. This object will create a deck of cards to initiate
    play. You can then use this Deck list of cards to split in half and give to
    the players.
    """





    def __init__(self):
        '''
        You should create a variable called 'allcards' that is a list of tuples containing each suit and rank. Forming a whole deck.
        For example: [(A,D), (2,D)...
                      (A,C), (2,C)...
                      (A,H), (2,H)...
                      (A,S), (2,S)...
                      ]
        You can either type out all the examples manually, or use a list comprehension and the lists created above SUITE and RANKS
        to help you out.
        '''







    def shuffle(self):
        '''
        From the random library, import the shuffle method, then shuffle the variable we created earlier: self.allcards
        you DO NOT need to use RETURN here
        '''








    def split_in_half(self):
        '''
        This should RETURN a list (or tuple) with exactly two item:
        - The first item should be a list itself, containting the first half of the deck
        - The second item should be another list, containing the second half of the deck
        '''
        









class Hand:
    '''
    This is the Hand class. Each player has a hand, and can add or remove
    cards from that hand.

    **I've done the __init__ and __str__ method for you already. You need to complete the methods: add, remove_card
    '''

    def __init__(self, cards):
        '''
        Takes a list of cards, assigns it to the variable 'cards'
        To be clear, the variable 'cards' is a LIST
        '''
        self.cards = cards



    def __str__(self):
        return "Contains {} cards".format(len(self.cards))


    # YOU CODE BELOW

    def add(self, added_cards):
        '''
        You should take the variable 'self.cards' from above and EXTEND the list to contain the newly added cards.
        To be clear, the variable 'added_cards' is also a LIST
        '''
        # Your code goes here





    def remove_card(self):
        '''
        You should take the list 'self.cards' and remove the last item from the list
        '''
        # Your code goes here









class Player:

    def __init__(self, name, hand):
        '''
        Please complete this method. Just a simple assignment

        Note:
        -name is a string
        -hand is a list -- which is an instance of the HAND class we created above
        '''
        # Your code goes here






    def play_card(self):
        '''
        This method should use a variable called 'drawn_card' which will take the hand and remove a card from it.
        It will RETURN the drawn_card
        '''
        drawn_card = self.hand.remove_card()
        print("{} has placed: {}".format(self.name, drawn_card))
        print('\n')
        return drawn_card




    def remove_war_cards(self):
        '''
        This method should create an empty list called 'war_cards'
        If the number of cards in the user's hand is less than 3, then just return the empty list
        Else, you should append to war_cards, the top three cards of the hand and remove those three cards from your hand.
        '''
        war_cards = []
        if len(self.hand.cards) < 3:
            return war_cards
        else:
            # Your code goes here





    def still_has_cards(self):
        """
        Returns True if player still has cards
        """
        return # Your code goes here







######################
#### GAME PLAY #######
######################
print("Welcome to War, let's begin...")

# Create New Deck and split in half
d = Deck()
d.shuffle()
half1, half2 = d.split_in_half()

# Create Both Players
comp = Player("computer", Hand(half1))
name = input("What is your name player? ")
user = Player(name, Hand(half2))

# Set Round Count
total_rounds = 0
war_count = 0

# Let's play
while user.still_has_cards() and comp.still_has_cards():
    total_rounds += 1
    print("It is time for a new round!")
    print("Here are the current standings: ")
    print(user.name+" count: "+str(len(user.hand.cards)))
    print(comp.name+" count: "+str(len(comp.hand.cards)))
    print("Both players play a card!")
    print('\n')

    # Cards on Table represented by list
    table_cards = []

    # Play cards


    # Add to table_cards


    # Check for War!


        # Play cards


        # Add to table_cards


        # Check to see who had higher rank







print("Great Game, it lasted: "+str(total_rounds))
print("A war occured "+str(war_count)+" times.")
