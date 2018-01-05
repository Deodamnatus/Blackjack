from random import shuffle

# returns ordered deck
def generateDecks(numDeck):
    deck = []

    class Card():
        suit = ''
        value = 0

    for suit in ['Diamond', 'Heart', 'Spade', 'Clover']:
        for value in range(1, 14):
            currCard = Card()
            currCard.suit = suit
            currcard.card = value
            if value >=10:
                currCard.value = 10
            else:
                currCard.value = value
            deck.append(currCard)

    if numDeck == 1:
        return deck
    return deck + generateDecks(numDeck-1)

# decide what to do as dealer
def dealerChoice(dealerpoints):
    #check for probability of drawing winning card if you want we just did basic
    if dealerpoints < 16:
        return True
    else:
        return False

def PlayGame():
    deck = []
    #provide menu and get choice
    print("Welcome to Blackjack!")

    # new game
    numPlayers = int(input('How many players (excluding dealer)? '))
    numDecks = int(input('How many decks? '))

    #generate a deck with numDecks decks and shuffle it
    deck = generateDecks(numDecks)
    shuffle(deck)

    # deal initial cards
    # handlist is in format of [ [player0 card0, player0 card0], ...]
    handlist = []
    for player in range(0,numPlayers):
        handlist.append([deck[0],deck[1]])
        del deck[0:2]

    currplayer = 1
    playerwon = false
    while playerwon == false:
        hit = ''
        #if dealer's turn
        if currplayer == 0:
            totalpoints = 0
            for card in handlist[0]:
                totalpoints+=card.value
            hit = dealerChoice(totalpoints)

        elif currplayer == 1:
            while hit not in [0,1]:
                hit = input("Hit or miss?")

        

    # Tutorial
    elif menuChoice ==1:


def takeTurn(deck, currPlayer, playerpoints):
    if currPlayer == 0:
        #dealer
    else:
        print("It is currently Player ", currPlayer, "'s turn. Would you like to fold (0), or hit (1)? ")
