import random
from Settings import *
from Dealer import *
from NeuralDealer import *
import time

game_mode = GameModes.CLASSIC
suitsList = ['heart', 'diamond', 'spade', 'clubs']
valuesList = ['Ace', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'Jack', 'Queen', 'King']


def play_game(game_deck):
    # initialize the dealer, which also initializes the agent/player
    dealer = Dealer(game_deck, game_mode)
    AgentWins = 0
    for x in range(0, NUM_GAMES):
        dealer.deal()
        AgentWins += dealer.play()
        if SLOW_MODE:
            time.sleep(SLEEP_TIME)

    print("Agent Won %d Times" % AgentWins)
    # TODO Reward Agent with win/loss (+1/-1)

def play_neural_game(game_deck):
    dealer = NeuralDealer(game_deck)


class Card:
    def __init__(self, value, colour, decknum):
        self.value = value
        self.colour = colour
        self.decknum = decknum


def shuffle(s_deck):
    # Shuffles the deck a random number of times (between 1 and 5)
    num_shuffle = random.randint(1, 5)
    for i in range(0, num_shuffle):
        random.shuffle(s_deck)


deck = []
# initializes the deck(s) depending on the number of decks
for i in range(1, NUM_DECKS+1):
    deck += [Card(value, suit, i) for value in valuesList for suit in suitsList]
    # Shuffle the deck
    shuffle(deck)

if AI_MODE == 1:
    play_game(deck)

if AI_MODE == 2:
    play_neural_game(deck)
