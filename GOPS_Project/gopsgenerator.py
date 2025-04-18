import random

mutation_rate = 10

def new_hands(old_hands, population, pct, decksize):
    # Population of Children
    children = []
    new_hands = []
    # Keep the top percentile
    percentile = int(population*pct)
    best_hands = cut_bad(old_hands, percentile)
    best_kept = int(population*0.05)
    # Keep 5% best strategies
    for i in range(0,best_kept):
        new_hands.append(best_hands[i][0])
    # Take decksize / 2 (rounded down) elements from one hand
    mom_run = int(decksize / 2)

    # First take the mom's hand
    for mom in best_hands:
        # Then fill the rest in with dad's hand
        for dad in best_hands:
            hand = mom_add(mom[0], mom_run)
            hand = dad_add(dad, hand)
            # Find out if the child should have the gene
            gene = gene_check(mom[0],dad[0])
            hand.append(gene[0])
            hand.append(gene[1])
            # Add to the pool of hands
            children.append(hand)

    # Take only 100 of the children
    for i in range(0,population-best_kept):
        hand = random.choice(children)
        children.remove(hand)
        # Let Mutation occur
        while random.randint(1,100) <= mutation_rate:
            hand = mutate(hand)
        new_hands.append(hand)
    return new_hands

# Drop the bottom percentile
def cut_bad(old_hands, pct):
    sorted_hands = sorted(old_hands, key=lambda hand: hand[1], reverse=True)
    parents = sorted_hands[:pct]
    return parents

# Take the mom genes
def mom_add(mom, mom_run):
    hand = []
    # Pick a starting point from A-8
    mom_start = random.randint(0,mom_run+1)

    # Add a run of 6 elements starting at mom_start
    for i in range(0,13):
        if i < mom_start:
            hand.append(0)
        elif i >= mom_start+mom_run:
            hand.append(0)
        else:
            hand.append(mom[i])
    return hand

# Fill in the dad genes
def dad_add(dad, hand):
    # Need to add a temp dad
    stepdad = [x for x in dad[0] if x != 0]
    # Leave only what hasn't been added
    for card in hand:
        if card in stepdad:
            stepdad.remove(card)
    for i, card in enumerate(hand):
        if card == 0:
            hand[i] = stepdad.pop(0)
    return hand

# Mutations keep the population alive
def mutate(hand):
    option = 5
    match option:
        case 1:
            #return hand[1:] + hand[:1]
            return hand[1:13] + hand[:1] + hand[13:]
        case 2:
            #return hand[-1:] + hand[:-1]
            return hand[12:13] + hand[0:12] + hand[13:]
        case _:
            # 0-12 is for 13 card hand, Don't let indexes equal
            index_1 = -1
            index_2 = -1
            while index_1 == index_2:
                index_1 = random.randint(0,12)
                index_2 = random.randint(0,12)
            hand[index_1], hand[index_2] = hand[index_2], hand[index_1]
            return hand
        
# Gene Calculator
def gene_check(mom, dad):
    option = random.randint(1,4)
    match option:
        # M1, D1
        case 1:
            return [mom[13], dad[13]]
        # M1, D2
        case 2:
            return [mom[13],dad[14]]
        # M2, D1
        case 3:
            return [mom[14],dad[13]]
        # M2, D2
        case 4:
            return [mom[14],dad[14]]
'''
hand = [1,2,3,4,5,6,7,8,9,10,11,12,13,True,False]
hand_1 = [1,2,3,4,5,6,7,8,9,10,11,12,13]
gene = gene_check(hand, hand)
hand_1.append(gene[0])
hand_1.append(gene[1])
print(hand_1)


hand = [1,2,3,4,5,6,7,8,9,10,11,12,13]
while random.randint(1,100) <= mutation_rate:
    print("Mutated")
    hand = mutate(hand)
print(hand)
'''  