deck = []
for i in range (4):
    if i == 0:
        k = 1
        for j in range (13):
            if k == 1:
                deck.append("A" + "♥")
            elif k == 11:
                deck.append("J" + "♥")
            elif k == 12:
                deck.append("Q" + "♥")
            elif k == 13:
                deck.append("K" + "♥")
            else:
                deck.append(str(k) + "♥")
            k += 1
    if i == 1:
        k = 1
        for j in range (13):
            if k == 1:
                deck.append("A" + "♦")
            elif k == 11:
                deck.append("J" + "♦")
            elif k == 12:
                deck.append("Q" + "♦")
            elif k == 13:
                deck.append("K" + "♦")
            else:
                deck.append(str(k) + "♦")
            k += 1
    if i == 2:
        k = 1
        for j in range (13):
            if k == 1:
                deck.append("A" + "♣")
            elif k == 11:
                deck.append("J" + "♣")
            elif k == 12:
                deck.append("Q" + "♣")
            elif k == 13:
                deck.append("K" + "♣")
            else:
                deck.append(str(k) + "♣")
            k += 1
    if i == 3:
        k = 1
        for j in range (13):
            if k == 1:
                deck.append("A" + "♠")
            elif k == 11:
                deck.append("J" + "♠")
            elif k == 12:
                deck.append("Q" + "♠")
            elif k == 13:
                deck.append("K" + "♠")
            else:
                deck.append(str(k) + "♠")
            k += 1
print(deck)