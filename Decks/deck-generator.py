from random import shuffle
import os
# Using the card format for EDSAC
# Generates a sorted deck and a randomly shuffled deck

# Open / Create the file and write each card on its own line
def writeDeck(filename, deck):

    with open(filename, "wt") as file:
        for card in deck:
            file.write(f"{card}\n")

# Spaids, Clubs, Hearts, Diamonds
suites = ["P  ", "Q  ", "W  ", "E  "]
# Ace, 2, 3, 4, 5, 6, 7, 8, 9, 10, Jack, Queen, King
types = ["7 F", "1 F", "1 D", "2 F", "2 D", "3 F", "3 D", "4 F", "4 D", "5 F", "5 D", "6 F", "6 D"]

# Full deck (suites x types)
deck = []

# Cartesian product
for type in types:
    for suite in suites:
        deck.append(f"{suite}{type}")

# Sorted deck filename
filename = "sorted-deck.txt"

# Output the sorted deck if DNE
if not os.path.exists(filename):
    
    # Output sorted deck
    writeDeck(filename, deck)

# Shuffle the deck
shuffle(deck)

# Shuffled deck filename
filename = "shuffled-deck"
extension = ".txt"

# Check if shuffled deck file exists
if not os.path.exists(f'{filename}{extension}'):

    # Output shuffled deck
    writeDeck(f'{filename}{extension}', deck)
else:

    # Iterate until filename is not found
    iteration = 1
    while os.path.exists(f'{filename}({iteration}){extension}'):
        iteration += 1

    # Output shuffled deck
    writeDeck(f'{filename}({iteration}){extension}', deck)