from random import shuffle

# print game title
def printTitle():
    print(
        '''
         ____  _            _     _            _    
        | __ )| | __ _  ___| | __(_) __ _  ___| | __
        |  _ \| |/ _` |/ __| |/ /| |/ _` |/ __| |/ /
        | |_) | | (_| | (__|   < | | (_| | (__|   < 
        |____/|_|\__,_|\___|_|\__/ |\__,_|\___|_|\_\      
        ''', end='')
    print('                       |__/                               ')


# get total points for a certain player
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
            elif value >= 10:
                currCard.value = 10
            else:
                currCard.value = value
            deck.append(currCard)

    if numDeck == 1:
        return deck
    return deck + generateDecks(numDeck - 1)




# display cards of players based on handlist
def printCards(handlist, censored=True):
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
            if player == len(handlist) - 1 and card >= 1 and censored == True:
                print("- -", end='\n')
            else:
                if player == len(handlist) - 1:
                    endvar = '\n'
                else:
                    endvar = '     \t\t'

                try:
                    currCard = handlist[player][card]
                    sortdict = {1:'A',11:'J',12:'Q',13:'K', 'Spade':"♠", 'Heart':"♥", 'Diamond':"♦", 'Club':"♣"}
                    if currCard.card in sortdict:
                        print(sortdict[currCard.card], end = ' ')
                    print(sortdict[currCard.suit], end = endvar)

                except IndexError:
                    print('\t', end=endvar)
    # print('')
    for player in range(0, len(handlist)):
        print("___     ", end='\t\t')
    print('')
    for player in range(0, len(handlist)):
        if player == len(handlist) - 1 and censored == True:
            print('???     ')
        else:
            print(totalPoints(handlist, player), '      ', end='\t\t')
    print("\n" * 10)


# print function for printing winners after game over
def printWinners(handlist):

    winner = [[0], 0]
    for player in range(0, len(handlist)):
        if totalPoints(handlist, player) > winner[1] and totalPoints(handlist, player) < 21:
            winner[1] = totalPoints(handlist, player)
            winner[0] = [player]
        elif totalPoints(handlist, player) == winner[1]:
            winner[0] = [player] + winner[0]
    if len(handlist)-1 in winner[0]:
        print("Dealer won!!!")
    else:
        print("Player(s) ", end='')
        for player in winner[0]:
            print(player + 1, end=' ')
        print('won!!!')

# decide what to do as dealer
def dealerChoice(handlist):
    # check for probability of drawing winning card if you want we just did basic
    dealerpoints = 0
    for card in handlist[-1]:
        dealerpoints += card.value

    if dealerpoints < 16:
        return 1
    else:
        return 0


def PlayGame(handlist, folded, deck):
    currplayer = 0
    while 0 in folded.values():
        if folded[currplayer] == 0:
            print("Player ", currplayer, "'s turn")
            hit = ''
            # if dealer's turn
            if currplayer == numPlayers + 1:
                hit = dealerChoice(handlist)
            # if players turn
            elif currplayer == 0:
                while hit not in [0, 1]:
                    printCards(handlist)
                    hit = int(input("Hit or miss (1,0)?\n:"))
            else:
                hit = dealerChoice(handlist)
                # hit = AI hit function
            if hit == 1:
                handlist[currplayer].append(deck[0])
                del deck[0]
                if totalPoints(handlist, currplayer) == 21:
                    folded[currplayer] = 1
                elif totalPoints(handlist, currplayer) > 21:
                    for cardnumber in range(0, len(handlist[currplayer])):
                        Card = handlist[currplayer][cardnumber]
                        if Card.card == 1 and Card.value == 11:
                            Card.value = 1
                            break
                    if totalPoints(handlist, currplayer) > 21:
                        folded[currplayer] = 1
            else:
                folded[currplayer] = 1
        if currplayer == len(folded) - 1:
            currplayer = 0
        else:
            currplayer += 1


print("Welcome to")
printTitle()
print("\n" * 5)
# new game
numPlayers = ''
while numPlayers not in [0, 1, 2, 3]:
    numPlayers = int(input('How many AI players (0-3)?\n:'))

numDecks = 0
while numDecks not in [1, 2, 3, 4, 5, 6]:
    numDecks = int(input('How many decks (1-6)?\n:'))

# generate a deck with numDecks decks and shuffle it
deck = generateDecks(numDecks)
shuffle(deck)

# deal initial cards
# handlist is in format of [ [player0 card0, player0 card1], ...]
handlist = []
# folded is in the format of { player#:folded or not...} ex: {0:0} player 0 not folded
folded = {}
for player in range(0, numPlayers + 2):
    handlist.append([deck[0], deck[1]])
    del deck[0:2]
    if totalPoints(handlist, player) > 21:
        for cardnumber in range(0, len(handlist[player])):
            Card = handlist[player][cardnumber]
            if Card.card == 1 and Card.value == 11:
                Card.value = 1
                break

    if totalPoints(handlist, player) == 21:
        folded[player] = 1
    else:
        folded[player] = 0


PlayGame(handlist, folded, deck)

# prints uncensored version of game field
printCards(handlist, False)
printWinners(handlist)






