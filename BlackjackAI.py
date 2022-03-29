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
    del deck[0]
    del deck[0]

def begin():
    dealerStart()
    playerStart()

def copy(hand):
    evalHand = hand
    return evalHand


def convert(evalHand):
    evalHand = [s.strip("♥♦♣♠") for s in evalHand]
    evalHand = [s.replace('A', '11') for s in evalHand]
    evalHand = [s.replace('J', '10') for s in evalHand]
    evalHand = [s.replace('Q', '10') for s in evalHand]
    evalHand = [s.replace('K', '10') for s in evalHand]
    evalHand = list(map(int, evalHand))
    return evalHand

def hit(hand):
    deal(hand)
    evalHand = copy(hand)
    evalHand = convert(evalHand)
    return evalHand

def dealerLogic(hand, evalHand):
    while sum(evalHand) < 15:
        evalHand = hit(hand)
    return hand, evalHand

def playerLogic(hand, evalHand):
    flag = True
    while flag:
        if sum(evalHand) >= 17:
            flag = False
        elif sum(evalHand) >= 13 and evalDealerHand[1] < 7:
            flag = False
        elif sum(evalHand) >= 13 and evalDealerHand[1] >= 7:
            evalHand = hit(hand)
        elif sum(evalHand) == 12 and evalDealerHand[1] < 4:
            evalHand = hit(hand)
        elif sum(evalHand) == 12 and evalDealerHand[1] < 7:
            flag = False
        elif sum(evalHand) == 12:
            evalHand = hit(hand)
        else:
            evalHand = hit(hand)
    
    return hand, evalHand

def winner(player, dealer):
    global dealerWin
    global playerWin
    global tie

    if sum(dealer) == 21 and len(dealer) == 2:
        print("Blackjack! Dealer wins!")
        dealerWin += 1
    elif sum(player) == 21 and len(player) == 2:
        print("Blackjack! Player wins!")
        playerWin += 1
    elif sum(player) > 21:
        print("Player bust")
        dealerWin += 1
    elif sum(dealer) > 21:
        print("Dealer bust")
        playerWin += 1
    elif sum(player) == sum(dealer):
        print("Push")
        tie += 1
    elif sum(player) > sum(dealer):
        print("Player wins")
        playerWin += 1
    elif sum(player) < sum(dealer):
        print("Dealer wins")
        dealerWin +=1

def playGame():
    deck, playerHand, dealerHand, evalPlayerHand, evalDealerHand = []

    createDeck()
    shuffle()
    begin()
    evalPlayerHand = copy(playerHand)
    evalPlayerHand = convert(evalPlayerHand)
    evalDealerHand = copy(dealerHand)
    evalDealerHand = convert(evalDealerHand)
    playerHand = playerLogic(playerHand, evalPlayerHand)
    dealerHand = dealerLogic(dealerHand, evalDealerHand)

dealerWin = 0
playerWin = 0
tie = 0

times = int(input("How many games would you like the AI to play? "))
for i in range (times):

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

    print(dealerHand, "dealer beginning hand")
    print(playerHand, "player beginning hand")

    evalPlayerHand = copy(playerHand)
    evalPlayerHand = convert(evalPlayerHand)
    evalDealerHand = copy(dealerHand)
    evalDealerHand = convert(evalDealerHand)

    playerTuple = playerLogic(playerHand, evalPlayerHand)
    dealerTuple = dealerLogic(dealerHand, evalDealerHand)

    print(playerTuple[0],"final player hand", dealerTuple[0], "final dealer hand")
    print(sum(playerTuple[1]), "value of final player hand", sum(dealerTuple[1]), "value of final dealer hand")

    winner(playerTuple[1], dealerTuple[1])
    
print(dealerWin + playerWin + tie, " games were played.")
print("Of those...")
print(dealerWin, " times the dealer won.")
print(playerWin, " times the AI won.")
print(tie, " the game ended in a push.")
print("The AI won ", playerWin/(dealerWin + playerWin + tie) * 100, '%', " of the time.")
