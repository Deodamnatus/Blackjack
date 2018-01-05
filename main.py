from random import shuffle

# returns ordered deck
def generateDecks(numDeck):
    deck = []

    class Card:
        suit = ''
        value = 0

    for suit in ['Diamond', 'Heart', 'Spade', 'Club']:
        for value in range(1, 14):
            currCard = Card()
            currCard.suit = suit
            currCard.card = value
            if value >=10:
                currCard.value = 10
            else:
                currCard.value = value
            deck.append(currCard)

    if numDeck == 1:
        return deck
    return deck + generateDecks(numDeck-1)

def printCards(handlist):
    print('\n' * 100)
    print("You", end='\t\t')
    for player in range(2,len(handlist) + 1):def printCards(handlist):
    print('\n' * 100)
    print("You" end='\t\t')
    for player in range(2,len(handlist) + 1):
        print("Player ", player, end ='\t\t')
    print("Dealer")
    maxCardsToPrint= 0
    for player in range(0,len(handlist+1)):
        if len(handlist[player])>maxCardsToPrint:
            maxCardsToPrint = len(handlist[player])

    for card in range(0,maxCardsToPrint))
        for player in range(0,len(handlist)+1):
            if player == 0 and card >= 1:
                print("- -", end='\t\t')
            else:
                try:
                    currCard = handlist[player][card]
                    if currCard.card <= 10:
                        print(currCard.card, end =' ')
                    elif currCard.card == 11:
                        print("J", end=' ')
                    elif currCard.card == 12:
                        print("Q", end=' ')
                    elif currCard.card == 13:
                        print("K", end=' ')
                    spade = "♠"
                    heart = "♥"
                    diamond = "♦"
                    club = "♣"
                    if currCard.suit == "Spade":
                        print(spade, end = '\t\t')
                    elif currCard.suit == 'Heart':
                        print(heart, end = '\t\t')
                    elif currCard.suit == 'Diamond':
                        print(diamond, end = '\t\t')
                    elif currCard.suit == 'Club':
                        print(club, end = '\t\t')

                except IndexError:
                    print('\t\t')
        print("Player ", player, end ='\t\t')
    print("Dealer")
    maxCardsToPrint= 0
    for player in range(0,len(handlist+1)):
        if len(handlist[player])>maxCardsToPrint:
            maxCardsToPrint = len(handlist[player])

    for card in range(0,maxCardsToPrint):
        for player in range(0,len(handlist)+1):
            if player == 0 and card >= 1:
                print("- -", end='\t\t')
            else:
                try:
                    currCard = handlist[player][card]
                    if currCard.card <= 10:
                        print(currCard.card, end =' ')
                    elif currCard.card == 11:
                        print("J", end=' ')
                    elif currCard.card == 12:
                        print("Q", end=' ')
                    elif currCard.card == 13:
                        print("K", end=' ')
                    spade = "♠"
                    heart = "♥"
                    diamond = "♦"
                    club = "♣"
                    if currCard.suit == "Spade":
                        print(spade, end = '\t\t')
                    elif currCard.suit == 'Heart':
                        print(heart, end = '\t\t')
                    elif currCard.suit == 'Diamond':
                        print(diamond, end = '\t\t')
                    elif currCard.suit == 'Club':
                        print(club, end = '\t\t')

                except IndexError:
                    print('\t\t')



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
    numPlayers = ''
    while numPlayers not in [0,1,2,3]:
        numPlayers = int(input('How many AI players (0-3)?'))

    numDecks = 0
    while numDecks not in [1,2,3,4,5,6]:
        numDecks = int(input('How many decks (1-6)? '))

    #generate a deck with numDecks decks and shuffle it
    deck = generateDecks(numDecks)
    shuffle(deck)

    # deal initial cards
    # handlist is in format of [ [player0 card0, player0 card0], ...]
    handlist = []
    for player in range(0,numPlayers+2):
        handlist.append([deck[0],deck[1]])
        del deck[0:2]

    currplayer = 1
    won = None
    while won == None:

        hit = ''
        #if dealer's turn
        if currplayer == 0:
            totalpoints = 0
            for card in handlist[0]:
                totalpoints+=card.value
            hit = dealerChoice(totalpoints)
        #if players turn
        elif currplayer == 1:
            while hit not in [0,1]:
                printCards(handlist)
                hit = input("Hit or miss?")




