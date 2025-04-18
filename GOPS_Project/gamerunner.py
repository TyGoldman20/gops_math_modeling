import random

# Run the a matchup between random and strat
def playgame(strat1, strat2, genetic):
    decksize = 13
    
    # Players
    p1 = [i for i in range(1, decksize + 1)]
    p2 = [i for i in range(1, decksize + 1)]
    # Prize Deck
    prizes = [i for i in range(1, decksize + 1)]
    # Initialize Point Things
    p1_score = 0
    p2_score = 0
    p1_last = -1
    p2_last = -1
    rollover = 0

    # Game Happens
    for i in range(1,decksize + 1): 
        prize = random.choice(prizes)
        prizes.remove(prize)

        if genetic:
            for i, card in enumerate(strat1[0]):
                if prize == i + 1:
                    p1_choice = card
            p2_choice = random.choice(p2)
            p2.remove(p2_choice)
        
        else:
            p1_choice = strat1[0](prize, p1, p2_last)
            p2_choice = strat2[0](prize, p2, p1_last)

        if p1_choice > p2_choice:
            p1_score += prize + rollover
            rollover = 0
        elif p1_choice < p2_choice:
            p2_score += prize + rollover
            rollover = 0
        else:
            rollover += prize

        p1_last = p1_choice
        p2_last = p2_choice

    # Print the score
    # print(f"{strat1[1]} vs {strat2[1]}: {p1_score} to {p2_score}")
    return (p1_score, p2_score) 