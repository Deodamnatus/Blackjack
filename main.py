from random import shuffle

# returns ordered deck
def generateDeck():
    deck = []

    class Card():
        suit = ''
        value = 0

    for suit in ['Diamond', 'Heart', 'Spade', 'Clover']:
        for value in range(1, 14):
            currCard = Card()
            currCard.suit = suit
            currCard.value = value
            deck.append(currCard)

    return deck


# shuffles deck
def shuffleDeck(deck):
    shuffle(deck)

# decide what to do as dealer

def dealerChoice(deck, playerpoints, ):
    #check for probability of drawing winning card

def PlayGame():
    #provide menu and get choice
    menuChoice == 0
    print("Welcome to Blackjack!\n\t1 - New Game\n\t2 - Tutorial\n\t3 - Strategy Tips")
    while menuChoice not in [1,2,3]:
        menuChoice = input(':')

    # new game
    if menuChoice == 1:
        deck = generateDeck()
        shuffleDeck(deck)
        numPlayers = input('How many players?')
        

    # Tutorial
    elif menuChoice ==1:


def takeTurn(deck, currPlayer, playerpoints):
    if currPlayer == 0:
        #dealer
    else:
        print("It is currently Player ", currPlayer, "'s turn. Would you like to fold (0), or hit (1)? ")
