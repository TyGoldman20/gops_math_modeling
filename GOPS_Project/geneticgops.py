import random
import gopsit as it
import gopsgenerator as gen

population = 100
decksize = 13
runs = 20
iterations = 100
percentile = .20
hands = []

# Clear Old data
with open("InClassModeling/geneaverages.csv", "w") as file:
    file.write(f"generation,hand,,,,,,,,,,,,,hand_score,rand_score\n")
# Generate the Population
for i in range(1,population+1):
    pdeck = [i for i in range(1,decksize+1)]
    hand = []
    for j in range(1,decksize+1):
        card = random.choice(pdeck)
        pdeck.remove(card)
        hand.append(card)
    # 100 means it doesn't have the gene, 101 means it has the gene. Recessive Trait
    # First Genome
    if random.randint(0,1) == 0:
        hand.append(True)
    else:
        hand.append(False)
    # Second Genome
    if random.randint(0,1) == 0:
        hand.append(True)
    else:
        hand.append(False)
    hands.append(hand)

# Check Uniqueness
unique_strategies = len(set(tuple(s) for s in hands))
print(f"Generation {0}: {unique_strategies} unique strategies")

for iteration in range(0,iterations):
    # Play each hand against random runs times
    averages = it.single_iteration(hands, runs)

    # Print all averages to the sheet
    with open("InClassModeling/geneaverages.csv", "a") as file:
        for stratScore in averages:
            file.write(f"Gen {iteration},{stratScore[0]},{stratScore[1]},{stratScore[2]}\n")

    # Generate New List through winners (Top 20th Percentile?)
    hands = gen.new_hands(averages, population, percentile, decksize)
    
    # Check on Convergence
    unique_strategies = len(set(tuple(s) for s in hands))
    print(f"Generation {iteration+1}: {unique_strategies} unique strategies")

# Print all children to the sheet
with open("InClassModeling/geneaverages.csv", "a") as file:
    for child in hands:
        file.write(f"Gen {iteration+1},{child},,\n")