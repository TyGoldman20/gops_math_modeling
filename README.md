# gops_math_modeling
Using a genetic algorithm to find optimal strategies against random playing for the card game GOPS (Game of Pure Skill)

The main files are geneticgops.py and gops.py

gops.py:
This file runs the 7-8 preset strategies we came up with (initialized in strategies.py) and runs them against each other to show there is no best strategy.
Creates a .csv file with data

strategies.py:
Where all the fixed strategies are stored.
If you want to see how a strategy works look here.
If you want to add a strategy you could just add it here and then reference it in gops.py by st.function_name()

geneticgops.py:
This is the main file I was mentioning with the genetic algorithm.
Iterations is the number of generations.
Runs is the number of times a strategy plays the randomized strategy.
Percentile is how many strategies do you want your parent pool to be made up of.
During runtime, it will print what generation just completed and how many unique strategies are left.
This will also create a .csv file with some data.

gamerunner.py:
Nothing in here should need to be looked at. Just runs each game

gopsit.py:
IDK why I made this another file, but it also doesn't need to be looked at.
This really could just be in gamerunner.py
It runs each hand "runs" amount of times

gopsgenerator.py:
This is probably the most important file.
Creates the new generation.
Mutation Rate is 0-100.
Breeding strategies is done via a one-point crossover.
Mutations are left and right cycles, and pair swaps.
Currently also adds two True/False at the end of each hand. This is because I am currently trying to simulate a gene pair.
To remove the gene pair at the end comment out lines 26, 27, 28, 83, 86; and uncomment out lines 82 and 85.
You will also need to go to geneticgops.py and comment out lines 25-33


Excel File:
These are previous runs that I have ran. I believe my code is working here so it should be good
