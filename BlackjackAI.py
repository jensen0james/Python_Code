import random

def createDeck():
    deckCreator("♥")
    deckCreator("♦")
    deckCreator("♣")
    deckCreator("♠")

def deckCreator(symbol):
    deck.append("A" + symbol)
    for i in range (2,11):
        deck.append(str(i) + symbol)
    deck.append("J" + symbol)
    deck.append("Q" + symbol)
    deck.append("K" + symbol)

def shuffle():
    random.shuffle(deck)

def deal(hand):
    hand.append(deck[0])
    del deck[0]

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

def copy(hand):
    evalHand = hand
    print(evalHand, "copied hand")
    return evalHand


def convert(evalHand):
    evalHand = [s.strip("♥♦♣♠") for s in evalHand]
    print(evalHand)
    evalHand = [s.replace('A', '11') for s in evalHand]
    evalHand = [s.replace('J', '10') for s in evalHand]
    evalHand = [s.replace('Q', '10') for s in evalHand]
    evalHand = [s.replace('K', '10') for s in evalHand]
    evalHand = list(map(int, evalHand))
    print(evalHand)
    return evalHand

def hit(hand):
    deal(hand)
    evalHand = copy(hand)
    evalHand = convert(evalHand)
    return evalHand

def dealerLogic(hand, evalHand):
    while sum(evalHand) < 15:
        evalHand = hit(hand)
    return hand

def playerLogic(hand, evalHand):
    flag = True
    while flag:
        if sum(evalHand) >= 17:
            flag = False
        elif sum(evalHand) >= 13 & evalDealerHand[1] < 7:
            flag = False
        elif sum(evalHand) >= 13 & evalDealerHand[1] >= 7:
            evalHand = hit(hand)
        elif sum(evalHand) == 12 & evalDealerHand[1] < 4:
            evalHand = hit(hand)
        elif sum(evalHand) == 12 & evalDealerHand[1] < 7:
            flag = False
        elif sum(evalHand) == 12:
            evalHand = hit(hand)
        else:
            evalHand = hit(hand)
    return hand

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

print(dealerHand)

print(playerHand)

evalPlayerHand = copy(playerHand)

print(evalPlayerHand, "eval after copy")

evalPlayerHand = convert(evalPlayerHand)

evalDealerHand = copy(dealerHand)

evalDealerHand = convert(evalDealerHand)

print(evalDealerHand, evalPlayerHand)

playerHand = playerLogic(playerHand, evalPlayerHand)

dealerHand = dealerLogic(dealerHand, evalDealerHand)

print(playerHand,"final player hand", dealerHand, "final dealer hand")