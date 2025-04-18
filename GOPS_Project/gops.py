import gamerunner as gr
import strategies as st

# Initialize Strategies (Should try to stick to non-random preset ideas)
strats = [(st.samecard, "Same Card"), (st.invertedcard, "Inverted Card"), (st.followcard, "Follow Card"), 
          (st.plus1card, "One Above Card"), (st.bottomnine, "Bottom 9"), (st.playforodds, "Play the Odds"), 
          (st.randomcard, "Random")]
averages = []
runs = 2000

for strat1 in strats:
    for strat2 in strats:
        # Initialize totals
        p1_total = 0
        p2_total = 0
        # Run game runs times
        for i in range(1,runs + 1):
            scores = gr.playgame(strat1, strat2, False)
            p1_total += scores[0]
            p2_total += scores[1]
        
        # Get the average
        p1_avg = p1_total / runs
        p2_avg = p2_total / runs
        # Add to the averages list
        averages.append([strat1[1], strat2[1], p1_avg, p2_avg])

        print(f"{strat1[1]} Average vs {strat2[1]} Average: {p1_avg} to {p2_avg}")

# Print all averages to the sheet
with open("InClassModeling/strataverages.csv", "w") as file:
    file.write(f"p1_strategy,p2_strategy,p1_score,p2_score\n")
    for stratScore in averages:
        file.write(f"{stratScore[0]},{stratScore[1]},{stratScore[2]},{stratScore[3]}\n")