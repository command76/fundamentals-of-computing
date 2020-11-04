# Mini-project #6 - Blackjack

import simplegui
import random

# load card sprite - 936x384 - source: jfitz.com
CARD_SIZE = (72, 96)
CARD_CENTER = (36, 48)
card_images = simplegui.load_image("http://storage.googleapis.com/codeskulptor-assets/cards_jfitz.png")

CARD_BACK_SIZE = (72, 96)
CARD_BACK_CENTER = (36, 48)
card_back = simplegui.load_image("http://storage.googleapis.com/codeskulptor-assets/card_jfitz_back.png")    

# initialize some useful global variables
in_play = False
outcome = ""
score = 0

# define globals for cards
SUITS = ('C', 'S', 'H', 'D')
RANKS = ('A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K')
VALUES = {'A':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, 'T':10, 'J':10, 'Q':10, 'K':10}


# define card class
class Card:
    def __init__(self, suit, rank):
        if (suit in SUITS) and (rank in RANKS):
            self.suit = suit
            self.rank = rank
        else:
            self.suit = None
            self.rank = None
            print "Invalid card: ", suit, rank

    def __str__(self):
        return self.suit + self.rank

    def get_suit(self):
        return self.suit

    def get_rank(self):
        return self.rank

    def draw(self, canvas, pos, state):
        card_loc = (CARD_CENTER[0] + CARD_SIZE[0] * RANKS.index(self.rank), 
                    CARD_CENTER[1] + CARD_SIZE[1] * SUITS.index(self.suit))
        if in_play and state == 0:
            canvas.draw_image(card_back, (CARD_BACK_CENTER[0],CARD_BACK_CENTER[1]), CARD_BACK_SIZE, [pos[0] + CARD_BACK_CENTER[0], pos[1] + CARD_BACK_CENTER[1]], CARD_BACK_SIZE)
        else:
            canvas.draw_image(card_images, card_loc, CARD_SIZE, [pos[0] + CARD_CENTER[0], pos[1] + CARD_CENTER[1]], CARD_SIZE)


        
        
# define hand class
class Hand:
    def __init__(self, play_type):
        self.card = []
        self.play_type = play_type
        pass	# create Hand object

    def __str__(self):
        hand = ""
        for card in self.card:
            hand = hand + " " + card.get_suit() + card.get_rank()
        return "Hand contains " + hand
        pass	# return a string representation of a hand

    def add_card(self, card):
        self.card.append(card)
        pass	# add a card object to a hand

    def get_value(self):
        hand_value = 0
        i = 0
#        print len(self.card)
        while i < len(self.card):
            rank = self.card[i].get_rank()
            for key, value in VALUES.items():
                if rank == key:
                    hand_value += value
#                    print hand_value
                    if i == len(self.card) - 1:
                        if rank == 'A':
                            if hand_value + 10 < 21:
                                hand_value += 10
#                                print hand_value
                            elif hand_value + 10 > 21:
                                hand_value -= 10
            i += 1
        return hand_value
        
        # count aces as 1, if the hand has an ace, then add 10 to hand value if it doesn't bust
        pass	# compute the value of the hand, see Blackjack video


   
    def draw(self, canvas, pos):
        if self.play_type == "dealer":
            i = 0
            j = 0
            for card in self.card:
                if in_play and j == 0:
                    card.draw(canvas, (5 + i, 50), 0)
                    j += 1
                else:
                    card.draw(canvas, (5 + i, 50), 1)
                i += 72
        if self.play_type == "player":
            i = 0
            for card in self.card:
                card.draw(canvas, (5 + i, 195), 1)
                i += 72
        pass	# draw a hand
        
   
        
# define deck class 
class Deck:
    def __init__(self):
        self.deck = []
        for suit in SUITS:
            for rank in RANKS:
                self.deck.append(Card(suit, rank))
        pass	# create a Deck object        
            

    def shuffle(self):
        random.shuffle(self.deck)
        # shuffle the deck 
        pass    # use random.shuffle()

    def deal_card(self):
        return self.deck.pop()
        pass	# deal a card object from the deck
    
    def __str__(self):
        deck = ""
        for card in self.deck:
            deck = deck + " " + card.get_suit() + card.get_rank()
        return "Deck contains " + deck
        pass	# return a string representing the deck









#define event handlers for buttons
def deal():
    global outcome, in_play, player, dealer, deck, score
 

    # your code goes here
    deck = Deck()
    deck.shuffle()
    player = Hand("player")
    dealer = Hand("dealer")
    card = deck.deal_card()
    player.add_card(card)
    card = deck.deal_card()
    dealer.add_card(card)
    card = deck.deal_card()
    player.add_card(card)
    card = deck.deal_card()
    dealer.add_card(card)
    print dealer, player
    player.get_value()
    dealer.get_value()
    outcome = ""
    
    if in_play == True:
        score -= 1
        in_play = False
        deck = Deck()
        deck.shuffle()
        player = Hand("player")
        dealer = Hand("dealer")
        card = deck.deal_card()
        player.add_card(card)
        card = deck.deal_card()
        dealer.add_card(card)
        card = deck.deal_card()
        player.add_card(card)
        card = deck.deal_card()
        dealer.add_card(card)
        print dealer, player
        player.get_value()
        dealer.get_value()
        
        
        


    
    in_play = True
    
def hit():
    global player, deck, outcome, in_play, score
    if in_play == True:
        if player.get_value() <= 21:
            card = deck.deal_card()
            player.add_card(card)
            if player.get_value() > 21:
                print "You have busted"
                outcome = "You have busted"
                score -= 1
                in_play = False
    print outcome, player
        
    pass	# replace with your code below
 
    # if the hand is in play, hit the player
   
    # if busted, assign a message to outcome, update in_play and score
       
def stand():
    global dealer, deck, player, outcome, in_play, score
    if in_play == True:
        while dealer.get_value() < 17:
            card = deck.deal_card()
            dealer.add_card(card)
        if dealer.get_value() > 21:
            print "Dealer busted"
            if  player.get_value() <= 21:
                print "Player wins"
                outcome = "Dealer busted Player wins"
                score += 1
                in_play = False
            else:
                outcome = "Player and dealer busted"
                score -= 1
                in_play = False
        elif player.get_value() <= dealer.get_value():
            print "Dealer wins"
            score -= 1
            outcome = "Dealer wins"
            in_play = False
        else:
            print "Player wins"
            score += 1
            outcome = "Player wins"
            in_play = False
    print outcome, dealer
        
    pass	# replace with your code below
   
    # if hand is in play, repeatedly hit dealer until his hand has value 17 or more

    # assign a message to outcome, update in_play and score

# draw handler    
def draw(canvas):
    # test to make sure that card.draw works, replace with your code below
    global outcome, in_play
#    card = Card("S", "A")
#    card.draw(canvas, [300, 300])
    dealer.draw(canvas, [36, 48])
    player.draw(canvas, [36, 48])
    canvas.draw_text('Blackjack', (250, 25), 25, 'white', 'serif')
    canvas.draw_text('Player', (5, 185), 25, 'white', 'serif')
    canvas.draw_text('Dealer', (5, 40), 25, 'white', 'serif')
    canvas.draw_text(outcome, (150, 450), 25, 'white', 'serif')
    canvas.draw_text("Score = " + str(score), (150, 400), 25, 'white', 'serif')
    if in_play == True:
        canvas.draw_text("Hit of Stand?", (150, 350), 25, 'white', 'serif')
    else:
        canvas.draw_text("New Deal?", (150, 350), 25, 'white', 'serif')










# initialization frame
frame = simplegui.create_frame("Blackjack", 600, 600)
frame.set_canvas_background("Green")

#create buttons and canvas callback
frame.add_button("Deal", deal, 200)
frame.add_button("Hit",  hit, 200)
frame.add_button("Stand", stand, 200)
frame.set_draw_handler(draw)


# get things rolling
deal()
frame.start()


# remember to review the gradic rubric