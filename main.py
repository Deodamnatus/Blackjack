from random import shuffle
import sys

def printTitle():
    print(
    '''
     ____  _            _     _            _    
    | __ )| | __ _  ___| | __(_) __ _  ___| | __
    |  _ \| |/ _` |/ __| |/ /| |/ _` |/ __| |/ /
    | |_) | | (_| | (__|   < | | (_| | (__|   < 
    |____/|_|\__,_|\___|_|\__/ |\__,_|\___|_|\_\
                           |__/             
    ''')


def totalPoints(handlist, playernumber):
    total = 0
    for card in handlist[playernumber]:
        total += card.value

    return total

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
            if value == 1:
                currCard.value = 11
            elif value >=10:
                currCard.value = 10
            else:
                currCard.value = value
            deck.append(currCard)

    if numDeck == 1:
        return deck
    return deck + generateDecks(numDeck-1)


def printCards(handlist):
    print('\n' * 100)
    print("You     ", end='\t\t')

    for player in range(2, len(handlist)):
        print("Player ", player, end='\t\t')
    print("Dealer  ")
    maxCardsToPrint = 0
    for player in range(0, len(handlist)):
        if len(handlist[player]) > maxCardsToPrint:
            maxCardsToPrint = len(handlist[player])

    for card in range(0, maxCardsToPrint):
        for player in range(0, len(handlist)):
            if player == len(handlist) - 1 and card >= 1:
                print("- -", end='\n')
            else:
                if player == len(handlist) - 1:
                    endvar = '\n'
                else:
                    endvar = '     \t\t'
                try:
                    currCard = handlist[player][card]
                    if currCard.card == 1:
                        print("A", end =' ')
                    elif currCard.card <= 10:
                        print(currCard.card, end=' ')
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
                        print(spade, end=endvar)
                    elif currCard.suit == 'Heart':
                        print(heart, end=endvar)
                    elif currCard.suit == 'Diamond':
                        print(diamond, end=endvar)
                    elif currCard.suit == 'Club':
                        print(club, end=endvar)

                except IndexError:
                    print('\t', end=endvar)
    print('')
    for player in range(0,len(handlist)):
        print("___     ", end = '\t\t')
    for player in range(0,len(handlist)):
        print(totalPoints(handlist,player), '      ', end = '\t\t')
    print("\n" * 10)

def getnextplayer(folded,currplayer):
    if currplayer + 1 == len(folded):
        if folded[0] == 0:
            return 0
        else:
            getnextplayer(folded,0)

    elif folded[currplayer + 1] == 0:
        return currplayer+1
    else:
        return getnextplayer(folded, currplayer + 1)

# decide what to do as dealer
def dealerChoice(handlist):
    #check for probability of drawing winning card if you want we just did basic
    dealerpoints =0
    for card in handlist[-1]:
        dealerpoints += card.value

    if dealerpoints < 16:
        return True
    else:
        return False

def PlayGame():
    print("Welcome to")
    printTitle()
    print("\n"*5)
    # new game
    numPlayers = ''
    while numPlayers not in [0,1,2,3]:
        numPlayers = int(input('How many AI players (0-3)?\n:'))

    numDecks = 0
    while numDecks not in [1,2,3,4,5,6]:
        numDecks = int(input('How many decks (1-6)?\n:'))

    #generate a deck with numDecks decks and shuffle it
    deck = generateDecks(numDecks)
    shuffle(deck)

    # deal initial cards
    # handlist is in format of [ [player0 card0, player0 card0], ...]
    handlist = []
    folded = {}
    for player in range(0,numPlayers+2):
        handlist.append([deck[0],deck[1]])
        del deck[0:2]
        if totalPoints(handlist, player) == 21:
            folded[player] = 1
        else:
            folded[player] = 0

    currplayer = 0
    while 0 in folded:

        hit = ''
        #if dealer's turn
        if currplayer == numPlayers+1:
            hit = dealerChoice(totalPoints(handlist,-1))
        #if players turn
        elif currplayer == 0:
            while hit not in [0,1]:
                printCards(handlist)
                hit = input("Hit or miss (0,1)?\n:")
        else:
            hit = dealerChoice(totalPoints(handlist,-1))
            # hit = AI hit function
        if hit == 1:
            handlist[currplayer].append(deck[0])
            del deck[0]
            if totalPoints(handlist,currplayer) == 21:
                folded[currplayer] = 1
            elif totalPoints(handlist, currplayer) > 21:
                for cardnumber in range(0,len(handlist[currplayer])):
                    Card = handlist[currplayer][cardnumber]
                    if Card.card == 1 and Card.value == 11:
                        Card.value = 1
                        break
                if totalPoints(handlist, currplayer)>21:
                    folded[currplayer] = 1
        else:
            folded[currplayer] = 1

        if 0 in folded:
            currplayer = getnextplayer(folded,currplayer)


    printCards(handlist)
    winner = 0
    for player in range(0,numPlayers+2):
        if totalPoints(handlist,player) == 21 and player == 0:
            print("You won!!!")
            winner = 1
        if totalPoints(handlist,player) == 21 and player == numPlayers+ 1:
            print("Dealer won!!!")
            winner = 1
        elif totalPoints(handlist, player) == 21:
            print("Player ",player, "won!!!")
            winner = 1
    if winner == 0:
        winner = ''
        for player







