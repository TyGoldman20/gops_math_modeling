import gamerunner as gr
import strategies as st

# Play each hand against random runs times
def single_iteration(hands, runs):
    averages = []
    
    for i, hand in enumerate(hands):
        strat1 = [hand, "Hand"]
        strat2 = [st.random, "Random"]
        score1 = 0
        score2 = 0

        for j in range(0,runs):
            score = gr.playgame(strat1, strat2, True)
            score1 += score[0]
            score2 += score[1]
        
        average = [hand, score1/runs, score2/runs]
        averages.append(average)

    return averages