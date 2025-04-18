import random

# Basically the control deck
def randomcard(prize, pdeck, last):
    card = random.choice(pdeck)
    pdeck.remove(card)
    return card

# Always match the card
def samecard(prize, pdeck, last):
    # Find the same card in person's deck
    for card in pdeck:
        if card == prize:
            pdeck.remove(card)
            return card
    # If not there, tell for other purposes
    return 0

# Always match the card
def plus1card(prize, pdeck, last):
    # Throw the King
    if prize == 13:
        return pdeck.pop(0)
        
    # Find the same card in person's deck
    for card in pdeck:
        if card == prize + 1:
            pdeck.remove(card)
            return card
    # If not there, tell for other purposes
    return 0

# Play the inverted card
def invertedcard(prize, pdeck, last):
    # Find the inverted card in person's deck
    for card in pdeck:
        if 14 - card == prize:
            pdeck.remove(card)
            return card
    # If not there, tell for other purposes
    return 0

# Is basically just random!!!!!!!!!!
def followcard(prize, pdeck, last):
    # For the first card played
    if last == -1:
        return pdeck.pop(0)
    # Find the last card in your deck
    for card in pdeck:
        if card == last:
            pdeck.remove(card)
            return card
    # If not there, play smallest card
    card = pdeck.pop(0)
    return card

# Goal is to win the 9 worst cards which will give you 46
def bottomnine(prize, pdeck, last):
    # Find the 4 above card in person's deck
    for card in pdeck:
        if card == prize+4:
            pdeck.remove(card)
            return card
    # Then look for top 4
    for card in pdeck:
        if card == prize-9:
            pdeck.remove(card)
            return card
    # Something fucked up
    return 0

# Play one above every odd card and one below every even card
def playforodds(prize, pdeck, last):
    # Match the King
    if prize == 13:
        return samecard(prize, pdeck, last)
    # If Odd, play above
    elif prize % 2 == 1:
        for card in pdeck:
            if card == prize+1:
                pdeck.remove(card)
                return card
    # If Even, play below
    else:
        for card in pdeck:
            if card == prize-1:
                pdeck.remove(card)
                return card
    # Something fucked up
    return 0