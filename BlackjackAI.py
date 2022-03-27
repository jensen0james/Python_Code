import random

def createDeck():
    deckCreator("♥")
    deckCreator("♦")
    deckCreator("♣")
    deckCreator("♠")

def deckCreator(symbol):
    deck.append("A" + symbol)
    for i in range (2,10):
        deck.append(str(i) + symbol)
    deck.append("J" + symbol)
    deck.append("Q" + symbol)
    deck.append("K" + symbol)

def shuffle():
    random.shuffle(deck)

def deal(hand):
    hand.append(deck[0])
    deck.remove[0]

def dealerStart():
    dealerHand.append(deck[0])
    dealerHand.append(deck[2])
    del deck[0]
    del deck[1]

def playerStart():
    playerHand.append(deck[0])
    playerHand.append(deck[1])
    del deck[0:1]

def begin():
    dealerStart()
    playerStart()

def copy(hand, evalHand):
    evalHand = hand
    print(evalHand)


def convert(evalHand):
    [s.strip("♥") for s in evalHand]
    [s.strip("♦") for s in evalHand]
    [s.strip("♣") for s in evalHand]
    [s.strip("♠") for s in evalHand]
    [s.replace('A', '11') for s in evalHand]
    [s.replace('J', '10') for s in evalHand]
    [s.replace('Q', '10') for s in evalHand]
    [s.replace('K', '10') for s in evalHand]
    evalHand = list(map(int, evalHand))
    print(evalHand)

def hit(hand, evalHand):
    deal(hand)
    copy(hand, evalHand)
    convert(evalHand)

def dealerLogic(hand, evalHand):
    while sum(evalHand) < 15:
        hit(hand, evalHand)

def playerLogic(hand, evalHand):
    flag = True
    while flag:
        if sum(evalHand) >= 17:
            flag = False
        elif sum(evalHand) >= 13 & evalDealerHand[0] < 7:
            flag = False
        elif sum(evalHand) >= 13 & evalDealerHand[0] >= 7:
            hit(hand, evalHand)
        elif sum(evalHand) == 12 & evalDealerHand[0] < 4:
            hit(hand, evalHand)
        elif sum(evalHand) == 12 & evalDealerHand[0] < 7:
            flag = False
        elif sum(evalHand) == 12:
            hit(hand, evalHand)
        else:
            hit(hand, evalHand)

deck = []

playerHand = []
evalPlayerHand = []

dealerHand = []
evalDealerHand = []

createDeck()

print(deck)

shuffle()

print(deck)

begin()

print(deck)

print(dealerHand)

print(playerHand)

copy(playerHand, evalPlayerHand)

convert(evalPlayerHand)

copy(dealerHand, evalDealerHand)

convert(evalDealerHand)

playerLogic(playerHand, evalPlayerHand)

dealerLogic(dealerHand, evalDealerHand)